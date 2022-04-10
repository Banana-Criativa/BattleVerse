using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SpeedChallenge : MonoBehaviour {
    public bool trigger;
    public bool animating;
    // used for aggregating sppeds, ideally with LCM of speeds
    [SerializeField] protected System.Int64 maxSliderLength = 1;

    public float dt;
    public float totalTime = 0;
    public float prevTime = 0;
    public float fullAnimationTime = 5;
    public float animationTime = 0;

    public Slider roundView;
    public Slider[] progressViews;
    public int[] speeds;
    public float[] progress;
    public float[] previous;

    // Start is called before the first frame update
    protected virtual void Start() {
        // allocate auxiliary memory once
        progress = new float[speeds.Length];
        previous = new float[speeds.Length];

        roundView.wholeNumbers = false;
        roundView.minValue = 0.0f;
        roundView.maxValue = 1.0f;
        roundView.value = 0.0f;

        ConfigProgressViews();
    }

    // Update is called once per frame
    protected virtual void Update() {
        if (animating) {
            dt = Mathf.Clamp01(dt + Time.deltaTime / animationTime);
            UpdateView(dt);
            if (dt == 1) {
                dt = 0;
                animating = false;
            }
        }
        else if(trigger) {
            UpdateProgress();
            UpdateView(0);
            trigger = false;
            animating = true;
        }
    }

    public void TriggerTurn() { trigger = true; }

    protected virtual void ConfigProgressViews() {
        for (int i = 0; i < progressViews.Length; ++i) {
            progressViews[i].wholeNumbers = false;
            progressViews[i].minValue = 0.0f;
            progressViews[i].maxValue = 1.0f;
        }
    }

    protected virtual float UpdateProgress() {
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

        for (i = 0; i < speeds.Length; ++i) {
            previous[i] = progress[i];
            progress[i] += minTime * speeds[i];
        }

        prevTime = (Mathf.Floor(totalTime) == totalTime) ? 0.0f : roundView.value;
        totalTime += minTime / maxSliderLength;
        return minTime;
    }

    protected virtual void UpdateView(float delta) {
        float tmp = (totalTime == Mathf.Floor(totalTime)) ? 1.0f : totalTime - Mathf.Floor(totalTime);
        roundView.value = Mathf.Lerp(prevTime, tmp, delta);
        for (int i = 0; i < progressViews.Length; ++i) {
            progressViews[i].value = Mathf.Lerp(previous[i], progress[i], delta);
        }
    }
}
