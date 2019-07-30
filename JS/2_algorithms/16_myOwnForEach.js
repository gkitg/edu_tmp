Array.prototype.myForEach = function(func) {
    for (var i = 0; i < this.length; i++) {
        func(this[i]);
    }
};

[1, 2, 3, 45].myForEach(i => {
    console.log(i);
});
 