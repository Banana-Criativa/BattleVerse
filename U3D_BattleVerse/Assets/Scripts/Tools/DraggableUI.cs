using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems; // IDragHandler

[RequireComponent(typeof(RectTransform))]
public class DraggableUI : MonoBehaviour, IDragHandler {
    [SerializeField] protected RectTransform me;

    // Start is called before the first frame update
    protected virtual void Start() {
        me = GetComponent<RectTransform>();
    }

    // Update is called once per frame
    // void Update() {}

    public virtual void OnDrag(PointerEventData eventData) {
        Vector3 screenPosition = eventData.pointerCurrentRaycast.screenPosition;
        Vector3 screenOffset = new Vector2(Screen.width, Screen.height) / 2;

        //Debug.Log("Coords: " + screenPosition.ToString());
        me.anchoredPosition = screenPosition - screenOffset;
    }
}
