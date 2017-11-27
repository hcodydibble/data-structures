"use strict";

const LL = require("./linked-list");

class Stack {
    constructor(iterable=null){
        this.linked = new LL();
        if(Array.isArray(iterable)){
            iterable.map(x => this.push(x));
        }
    }

    push(val){
        this.linked.push(val);
    }

    pop(){
        return this.linked.pop();
    }

    size(){
        return this.linked.size();
    }
}

module.exports = Stack;