using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HitRollController : MonoBehaviour {
    [SerializeField] Vector3 strategicPositions = Vector3.one;
    [SerializeField] uint die = 20;
    [SerializeField] bool leftToRight = true;

    public InputField inputLHS, inputRHS;
    public Text totalPositions, textLHS, textTie, textRHS, textProbLHS, textProbRHS;
    public Slider probabilitySlider;
    
    // Start is called before the first frame update
    void Start() {}

    // Update is called once per frame
    void Update() {}

    public void SetLeftToRight(bool value) {
        leftToRight = value;
        UpdateView();
    }

    public void UpdateData() {
        strategicPositions = new Vector3Int(int.Parse(inputLHS.text), int.Parse(inputRHS.text), 0);
        strategicPositions.z = strategicPositions.x + strategicPositions.y;
        UpdateView();
    }

    void UpdateView() {
        float probLHS = strategicPositions.x / strategicPositions.z;
        float probRHS = strategicPositions.y / strategicPositions.z;

        textProbLHS.text = (100*probLHS).ToString("0.00") + "%";
        textProbRHS.text = (100*probRHS).ToString("0.00") + "%";
        probabilitySlider.value = probLHS;
        totalPositions.text = strategicPositions.z.ToString();

        if(leftToRight) {
            Vector2Int tmp = new Vector2Int(Mathf.CeilToInt(die + 1 - die * probLHS), Mathf.FloorToInt(die * probRHS));
            textLHS.text = ">=" + tmp.x.ToString();
            textTie.text = tmp.x - tmp.y > 1 ? (tmp.x - 1).ToString() : "---";
            textRHS.text = "<=" + tmp.y.ToString();
        }
        else {
            Vector2Int tmp = new Vector2Int(Mathf.FloorToInt(die * probLHS), Mathf.CeilToInt(die + 1 - die * probRHS));
            textLHS.text = "<=" + tmp.x.ToString();
            textTie.text = tmp.y - tmp.x > 1 ? (tmp.y - 1).ToString() : "---";
            textRHS.text = ">=" + tmp.y.ToString();
        }
    }
}
