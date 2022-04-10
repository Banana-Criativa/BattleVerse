using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TokenView : DraggableUI {
    [SerializeField] protected Image background;
    [SerializeField] protected Sprite sprite;
    [SerializeField] protected Color bgTint;

    [SerializeField] protected Text text;
    [SerializeField] protected string content;
    [SerializeField] protected TextAnchor align;
    [SerializeField] protected Color textColor;

    // Start is called before the first frame update
    protected override void Start() {
        base.Start();
        UpdateView();
    }

    // Update is called once per frame
    // void Update() {}

    public void UpdateView() {
        if(background != null) {
            background.sprite = sprite;
            background.color = bgTint;
        }

        if(text != null) {
            text.alignment = align;
            text.color = textColor;
            text.text = content;
        }
    }
}
