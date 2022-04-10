using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CharacterBattleView : MonoBehaviour
{
    public CharacterBehaviour pchar;
    public bool dirty;

    public RawImage avatar;
    public Slider[] powerBars;
    public Slider[] conditionBars;

    // Start is called before the first frame update
    void Start() {}

    // Update is called once per frame
    void Update() {
        if (dirty) {
            UpdateView();
            dirty = false;
        }
    }

    void UpdateView() {
        avatar.texture = pchar.avatar;
        UpdateBars(powerBars, pchar.GetMaxPowersKnown(), pchar.GetPowerStatus());
        UpdateBars(conditionBars, pchar.GetMaxConditionKnown(), pchar.GetHealthStatus());
    }

    void UpdateBars(Slider[] bars, Vector3Int maxStat, Vector3Int curStat) {
        Vector3Int v3iMax = maxStat;
        int mAux = (v3iMax.x + v3iMax.y + v3iMax.z) / 3;

        Vector3Int v3i = curStat;
        int aux = (v3i.x + v3i.y + v3i.z) / 3;

        for (int i = 0; i < 4; ++i) {
            bars[i].maxValue = (i==0) ? mAux : v3iMax[i-1];
            bars[i].value = (i==0) ? aux : v3i[i-1];
        }
    }

    public void SelectChar(CharacterBehaviour updtChar) {
        pchar = updtChar;
        dirty = true;
    }
}
