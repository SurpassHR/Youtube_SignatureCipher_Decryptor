Gv = function (a) {
    a = a.split("");
    Fv.Hm(a, 30);
    Fv.i7(a, 69);
    Fv.Hm(a, 3);
    Fv.i7(a, 20);
    Fv.Hm(a, 52);
    Fv.i7(a, 32);
    Fv.D3(a, 3);
    return a.join("")
};


var Fv = {
    i7: function (a, b) {
        var c = a[0];
        a[0] = a[b % a.length];
        a[b % a.length] = c
    },
    D3: function (a, b) {
        a.splice(0, b)
    },
    Hm: function (a) {
        a.reverse()
    }
};
