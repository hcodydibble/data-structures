"use strict";

class Node {
    constructor(data, next=null){
        this.data = data
        this.next = next
    }
}

class LinkedList {
    constructor(iterable=null) {
        this.head = null;
        this._counter = 0;
        if(Array.isArray(iterable)){
            iterable.forEach(x => this.push(x));
        }
    }

    push(val){
        this.head = new Node(val, this.head);
        this._counter ++;
    }

    pop(){
        if(this.head === null){
            return undefined;
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
                    return searchThrough;
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
            throw new Error('IndexError: Nothing in the list.');
        }
        try{
            while(currentNode && !found){
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
            throw new Error('ValueError: No such Node.');
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
        return displayThis.join(", ");
    }

    size(){
        return this._counter;
    }
}

module.exports = {LinkedList,
                  Node};

if(require.main === module){
    var list = new LinkedList([1, 2, 3, 4]);
    console.log(list.display());
    console.log(list.size());
}