

function foo(name) {
    this.name = name;
}
// 原型
foo.prototype = {
    'sayName':function () {
        console.log(this.name);
    }
}

// 创建了一个类 
// 类的方法区
// 