// classical merge algo
Array.prototype.mergesort = function() {
    console.log(this) 
    if(this.length == 1) {
        return this;
    }
    var merge = function(left, right){
       var sorted = [];
       var l = r = 0;
        while(l < left.length && r < right.length){
            if(left[l] < right[r]) {
                sorted.push(left[l])
                l+=1
            } else {
                sorted.push(right[r])
                r+=1
            }
        }
        return sorted.concat(left.slice(l) , right.slice(r));
    }
    
    var arr1 = this.slice(0, this.length/2).mergesort();
    var arr2 = this.slice(this.length/2).mergesort();
    return merge(arr1, arr2);
};
 
console.log([1,10,55,33,45,189,33].mergesort());
 
 
// slicker merge using 'splice'
Array.prototype.mergesort = function() {
    console.log(this) 
    if(this.length == 1) {
        return this;
    }
    var merge = function(left, right){
       var sorted = [];
    while (left && left.length > 0 && right && right.length > 0){
        var b = left[0] <= right[0];
        sorted.push(b? left[0]: right[0]);
        b? left.splice(0, 1): right.splice(0, 1);
    }
    return sorted.concat(left, right);
    }
    
    var arr1 = this.slice(0, this.length/2).mergesort();
    var arr2 = this.slice(this.length/2).mergesort();
    return merge(arr1, arr2);
};
 
console.log([1,10,55,33,45,189,33].mergesort());
