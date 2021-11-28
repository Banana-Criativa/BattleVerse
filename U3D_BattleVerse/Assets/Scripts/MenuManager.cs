using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum OptionMode {
    SELECTION,
    TARGET
}

public class MenuManager : MonoBehaviour {
    public KeyCode charSelectKey = KeyCode.Alpha0;
    public KeyCode turnDeciderKey = KeyCode.T;
    public KeyCode[] charViewKeys = { KeyCode.Alpha1, KeyCode.Alpha2, KeyCode.Alpha3, KeyCode.Alpha4 };
    public CharacterBehaviour[] players;

    public GameObject charMenu;
    private GameObject charViewGo;
    public GameObject turnView;

    public CharacterBattleView charView;

    private OptionMode mode = OptionMode.SELECTION;

    // Start is called before the first frame update
    void Start() {
        charViewGo = charView.gameObject;
    }

    // Update is called once per frame
    void Update() {
        int charSlct = -1;

        if (Input.GetKeyDown(charSelectKey))
            TargetSelection();
        else if (Input.GetKeyDown(turnDeciderKey))
            ActivateTurnView();
        else {
            for (int i = 0; i < charViewKeys.Length; ++i) {
                if (Input.GetKeyDown(charViewKeys[i])) charSlct = i;
            }

            if (charSlct >= 0) SelectCharacter(charSlct);
        }
    }

    public void TargetSelection() {
        charViewGo.SetActive(false);
        turnView.SetActive(false);
        charMenu.SetActive(true);
    }

    public void SelectCharacter(int id) {
        charMenu.SetActive(false);
        turnView.SetActive(false);

        charViewGo.SetActive(true);
        charView.SelectChar(players[id]);
    }

    public void ActivateTurnView() {
        charViewGo.SetActive(false);
        charMenu.SetActive(false);
        turnView.SetActive(true);
    }

    public void SelectOption(int id) {
        if (mode == OptionMode.SELECTION)
            SelectCharacter(id);
        else if (mode == OptionMode.TARGET)
            SelectCharacter(id); // TODO: build attack system
    }
}
