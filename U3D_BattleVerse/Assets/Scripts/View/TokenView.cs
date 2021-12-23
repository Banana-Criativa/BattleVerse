using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems; // IDragHandler

[RequireComponent(typeof(RectTransform))]
public class TokenView : MonoBehaviour, IDragHandler {
    [SerializeField] protected RectTransform me;

    [SerializeField] protected Image background;
    [SerializeField] protected Color bgTint;

    [SerializeField] protected Text text;
    [SerializeField] protected string content;
    [SerializeField] protected TextAnchor align;
    [SerializeField] protected Color textColor;

    // Start is called before the first frame update
    void Start() {
        me = GetComponent<RectTransform>();
        UpdateView();
    }

    // Update is called once per frame
    // void Update() {}

    public void UpdateView() {
        background.color = bgTint;
        text.alignment = align;
        text.color = textColor;
        text.text = content;
    }

    public void OnDrag(PointerEventData eventData) {
        Vector3 screenPosition = eventData.pointerCurrentRaycast.screenPosition;
        Vector3 screenOffset = new Vector2(Screen.width, Screen.height) / 2;

        Debug.Log("Coords: " + screenPosition.ToString());
        me.anchoredPosition = screenPosition - screenOffset;
    }
}
