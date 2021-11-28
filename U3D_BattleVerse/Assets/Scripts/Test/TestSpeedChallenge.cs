using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TestSpeedChallenge : MonoBehaviour {
    public bool trigger;
    public bool animating;

    public float dt;
    public float totalTime = 0;
    public float fullAnimationTime = 5;
    public float animationTime = 0;

    public Slider[] progressViews;
    public int[] speeds;
    public float[] progress;
    public float[] previous;

    // Start is called before the first frame update
    protected virtual void Start() {
        // allocate auxiliary memory once
        progress = new float[speeds.Length];
        previous = new float[speeds.Length];

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

    protected virtual int UpdateProgress() {
        float[] time = new float[progress.Length];
        float diff, minTime = float.MaxValue;
        int i, ret = -1;

        for (i = 0; i < progress.Length; ++i) {
            if (progress[i] >= 1) progress[i] = 0;

            diff = (float)(1.0f - progress[i]);
            time[i] = diff / speeds[i];
            if (time[i] < minTime) {
                ret = i; // whoose turn it is now
                minTime = time[i];
                // how much to move by how fast to cover it
                animationTime = diff * (fullAnimationTime / speeds[i]);
            }
        }

        for (i = 0; i < speeds.Length; ++i) {
            previous[i] = progress[i];
            progress[i] += minTime * speeds[i];
        }

        return ret;
    }

    protected virtual void UpdateView(float delta) {
        for (int i = 0; i < progressViews.Length; ++i) {
            progressViews[i].value = Mathf.Lerp(previous[i], progress[i], delta);
        }
    }
}
