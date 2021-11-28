using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterBehaviour : MonoBehaviour {
    protected string firstName;
    protected string lastName;
    protected string[] aliases;

    [SerializeField] protected bool dirty;
    public Texture avatar;
    public int damage;

    [SerializeField] protected int powerIndex;
    [SerializeField] protected int conditionIndex;
    [SerializeField] protected Vector3Int[] statusHistory;
    [SerializeField] protected TechniqueView[] techniques;

    [SerializeField] protected Vector3Int maxConditionKnown;
    [SerializeField] protected Vector3Int maxPowersKnown;
    [SerializeField] protected Vector3Int powerModifier;

    public string FirstName { get { return firstName; } set { } }
    public string LastName { get { return lastName; } set { } }
    public string MainAlias { get { return aliases[0]; } set { } }

    public string FullName
    {
        get { return string.Format("{0} {1}", firstName, lastName); }
        set { }
    }

    public string[] AliasList { get { return aliases; } set { } }

    // Start is called before the first frame update
    void Start() {}

    // Update is called once per frame
    void Update() {
        if (dirty) {
            UpdateMaxParameters();
            dirty = false;
        }
    }

    protected virtual void UpdateMaxParameters() {
        for (int i = 0; i < statusHistory.Length; ++i) {
            maxPowersKnown = Vector3Int.Max(maxPowersKnown, statusHistory[i]);
            maxConditionKnown = Vector3Int.Max(maxConditionKnown, statusHistory[i]);
        }
    }

    public Vector3Int GetPowerStatus() { return statusHistory[powerIndex] + powerModifier; }
    public Vector3Int GetHealthStatus() { return statusHistory[conditionIndex]; }

    public Vector3Int GetMaxPowersKnown() { return maxPowersKnown; }
    public Vector3Int GetMaxConditionKnown() { return maxConditionKnown; }

    public void TakeHit(float strike) {
        Vector3Int cPower = GetPowerStatus();
        strike = strike / cPower.z + ((float)damage) / statusHistory[powerIndex].z;
        int dmg = (int)strike;

        // TODO: calculate damage to physical conditioning

        powerIndex -= dmg;
        if (powerIndex < 0) powerIndex = 0;

        damage = (int)(statusHistory[powerIndex].z * (strike - dmg));
    }
}
