var Gv = {
    HF: function (a) {
        a.reverse()
    },
    A2: function (a, b) {
        a.splice(0, b)
    },
    ch: function (a, b) {
        var c = a[0];
        a[0] = a[b % a.length];
        a[b % a.length] = c
    }
};

Hv = function (a) {
    a = a.split("");
    Gv.A2(a, 1);
    Gv.ch(a, 39);
    Gv.A2(a, 3);
    return a.join("")
};

s = 'ccOqAOq0QJ8wRQIgBuNfgiPAG1So8sHkvynM2zI_Al-_RcmY0dUoFSZh3mICIQCpqaaY08hzym7HTEEy_Kd4eBUoIZzWrlAJvWpkl-NatA%3D%3D'
a = Hv(s)

var g = {
    i: function ()
}
