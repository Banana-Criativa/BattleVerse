using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpeedChallengeInt : SpeedChallenge {
    public bool updateMeasures;

    // Start is called before the first frame update
    protected override void Start() {
        // exclusive to integer versions like TestSpeedChallengeInt
        ResetMeasurements();

        // standard start routine
        base.Start();
    }

    // Update is called once per frame
    protected override void Update() {
        base.Update(); // run base first
        if (animating || trigger) return; // early return

        if (updateMeasures) UpdateMeasurements();
    }

    protected override void ConfigProgressViews() {
        for (int i = 0; i < progressViews.Length; ++i) {
            progressViews[i].wholeNumbers = true;
            progressViews[i].minValue = 0;
            progressViews[i].maxValue = maxSliderLength;
        }
    }

    protected override float UpdateProgress() {
        float minTime = base.UpdateProgress();

        if (Mathf.Floor(minTime) < minTime)
            Debug.LogError("Failed to stratify turn length");

        return minTime;
    }

    protected virtual void ResetMeasurements() {
        int i;

        for(i=0; i<speeds.Length; ++i) {
            if (i == 0) maxSliderLength = speeds[i];
            else maxSliderLength = Tools.LCM(maxSliderLength, speeds[i]);
        }
    }

    public virtual void UpdateMeasurements() {
        System.Int64 tmp;
        int i;

        for(i=0;i<progress.Length; ++i) {
            tmp = Tools.GCD((System.Int64)(maxSliderLength - progress[i]), speeds[i]);
            if (speeds[i] > tmp) {
                ScaleMeasurements(speeds[i] / tmp);
                ConfigProgressViews();
            }
        }
    }

    protected virtual void ScaleMeasurements(System.Int64 delta) {
        maxSliderLength *= delta;
        for (int i = 0; i < progress.Length; ++i) { progress[i] *= delta; }
    }
}
