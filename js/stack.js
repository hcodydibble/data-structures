"use strict";

const LL = require("./linked-list");

class Stack {
    constructor(){
        this.linked = new LL();
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