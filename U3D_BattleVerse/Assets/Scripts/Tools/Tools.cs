using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class Tools {
    public static System.Int64 GCD (System.Int64 a, System.Int64 b) {
        System.Int64 tmp;

        while (b != 0) {
            tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

    public static System.Int64 LCM (System.Int64 a, System.Int64 b) {
        return (a / GCD(a, b)) * b;
    }
}
