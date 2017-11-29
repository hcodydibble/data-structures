"use strict";

const linkedList = require("./linked-list");

class Stack {
    constructor(iterable=null){
        this.linked = new linkedList.LinkedList();
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