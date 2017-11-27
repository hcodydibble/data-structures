"use strict";

class Node{
    constructor(data, next=null, previous=null){
        this.data = data;
        this.next = next;
        this.previous = previous;
    }
}

class DLL{
    constructor(){
        this.head = null;
        this.tail = null;
        this._counter = 0;
    }

    push(val){
        let newHead = new Node(val, this.head);
        if(this.head){
            this.head.previous = newHead;
        }
        if(this.tail === null){
            this.tail = newHead;
        }
        this.head = newHead;
        this._counter ++;
    }

    append(val){
        let newTail = new Node(val, this.tail);
        if(this.tail){
            this.tail.next = newTail;
        }else{
            this.head = newTail;
        }
        this.tail = newTail;
        this._counter ++;
    }

    pop(){
        if(this._counter === 0){
            this.head = null;
            this.tail = null;
        }
        if(this.head === null){
            throw new new Error("IndexError: Empty list, unable to pop.");
        }
        let output = this.head.data;
        this.head = this.head.next;
        this.head.next = null;
        this._counter --;
        return output;
    }

    shift(){
        if(this._counter === 0){
            this.head = null;
            this.tail = null;
        }
        if(this.tail === null){
            throw new new Error("IndexError: Empty list, unable to shift.");
        }
        let output = this.tail.data;
        this.tail = this.tail.previous;
        this._counter --;
        return output;
    }

    display(){
        let node = this.head;
        let displayThis = [];
        while(node){
            displayThis.push(node.data);
            node = node.next;
        }
        return displayThis;
    }
}

module.exports = DLL;

var d = new DLL();
d.append(3);
d.append(4);
d.shift();
