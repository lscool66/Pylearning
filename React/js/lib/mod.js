//缺省导出
export default class A {
    constructor(x) {
        this.x = x;
    }
    show() {
        console.log(this.x);
    }
}

export function foo() {
    console.log('foo function');
}