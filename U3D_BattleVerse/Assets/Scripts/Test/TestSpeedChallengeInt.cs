using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TestSpeedChallengeInt : TestSpeedChallenge {
    // used for aggregating sppeds, ideally with LCM of speeds
    public System.Int64 maxSliderLength = 0;

    // Start is called before the first frame update
    protected override void Start() {
        // exclusive to integer versions like TestSpeedChallengeInt
        ResetMeasurements();

        // standard start routine
        base.Start();
    }

    // Update is called once per frame
    // void Update() {}

    protected override void ConfigProgressViews() {
        for (int i = 0; i < progressViews.Length; ++i) {
            progressViews[i].wholeNumbers = true;
            progressViews[i].minValue = 0;
            progressViews[i].maxValue = maxSliderLength;
        }
    }

    protected override int UpdateProgress() {
        float[] time = new float[progress.Length];
        float diff, minTime = float.MaxValue;
        int i, ret = -1;

        for (i = 0; i < progress.Length; ++i) {
            if (progress[i] >= maxSliderLength) progress[i] -= maxSliderLength;

            diff = (float)(maxSliderLength - progress[i]);
            time[i] = diff / speeds[i];
            if (time[i] < minTime) {
                ret = i; // whoose turn it is now
                minTime = time[i];
                // how much to move by how fast to cover it
                animationTime = (diff / maxSliderLength) * (fullAnimationTime / speeds[i]);
            }
        }

        if (Mathf.Floor(minTime) < minTime) Debug.LogError("Failed to stratify turn length");

        for (i = 0; i < speeds.Length; ++i) {
            previous[i] = progress[i];
            progress[i] += minTime * speeds[i];
        }

        totalTime += minTime / maxSliderLength;
        return ret;
    }

    protected virtual void ResetMeasurements() {
        int i;

        for(i=0; i<speeds.Length; ++i) {
            if (i == 0) maxSliderLength = speeds[i];
            else maxSliderLength *= speeds[i];
        }
    }
}
