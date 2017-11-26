"use strict";

class Node {
    constructor(data, next=null){
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor(iterable=null) {
        this.head = null;
        this._counter = 0;
        if(Array.isArray(iterable)){
            iterable.map(x => this.push(x));
        }
    }

    push(val){
        let newHead = new Node(val, this.head);
        this.head = newHead;
        this._counter ++;
    }

    pop(){
        if(this.head === null){
            throw 'IndexError: Nothing to pop.';
        }
        let output = this.head;
        this.head = this.head.next;
        this._counter --;
        return output.data;
    }

    search(val){
        let searchThrough = this.head;
        try{
            while(this.head){
                if(val === searchThrough.data){
                    return searchThrough.data;
                }else{
                    searchThrough = searchThrough.next;
                }
            }
        }catch(e){
            return 'No such Node';
        }
    }

    remove(val){
        let currentNode = this.head;
        let previousNode = null;
        let found = false;
        if(currentNode === null){
            throw 'IndexError: Nothing in the list.';
        }
        try{
            while(currentNode && found === false){
                if(val === currentNode.data){
                    found = true;
                }else{
                    previousNode = currentNode;
                    currentNode = currentNode.next;
                }
            }
            if(previousNode === null){
                this.pop();
            }else if(currentNode.next === null){
                previousNode.next = null;
            }else{
                previousNode.next = currentNode.next;
            }
        }catch(e){
            throw 'ValueError: No such Node.';
        }
        this._counter --;
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

    size(){
        return this._counter;
    }
}

if(require.main === module){
    var list = new LinkedList([1, 2, 3, 4, 5]);
    console.log(list.display());
    console.log(list.size());
}