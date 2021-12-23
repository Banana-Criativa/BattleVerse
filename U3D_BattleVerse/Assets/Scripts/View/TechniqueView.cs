using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TechniqueView : MonoBehaviour {
    public string techniqueName;
    public int[] costs;
    public Vector3Int[] yields;

    // Start is called before the first frame update
    void Start() {}

    // Update is called once per frame
    void Update() {}

    public Vector3Int useIt(int costId, int yieldId) {
        return yields[yieldId] * costs[costId];
    }
}
