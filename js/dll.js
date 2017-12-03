'use strict';

class Node{
    constructor(data, nxt=null, prev=null){
        this.data = data
        this.nxt = nxt;
        this.prev = prev
    }
}

class DLL{
    constructor(){
        this.head = null
        this.tail = null
        this._counter = 0
    }

    push(val){
        let oldHead = this.head;
        this.head = new Node(val, this.nxt=this.head);
        this._counter ++;
        if(oldHead){
            oldHead.prev = this.head
        }else{
            this.tail = this.head
        }
    }

    append(val){
        let oldTail = this.tail
        this.tail = new Node(val, this.prev=this.tail)
        this._counter ++
        if(oldTail){
            oldTail.nxt = this.tail
        }else{
            this.head = this.tail
        }
    }

    pop(){
        if(this._counter === 0){
            this.head = null
            this.tail = null
        }
        let message = {failure: 'Failure: No such Node in the list.'}
        if(!this.head){
            throw new Error(message.failure);
        }
        let output = this.head.data
        this.head = this.head.nxt
        if(this.head){
            this.head.prev = null
        }else{
            this.tail = null
        }
        this._counter --
        return output;
    }

    shift(){
        if(this._counter === 0){
            this.head = null
            this.tail = null
        }
        let message = {failure: 'Failure: No such Node in the list.'}
        if(!this.tail){
            throw new Error(message.failure);
        }
        let output = this.tail.data
        this.tail = this.tail.prev
        if(this.tail){
            this.tail.nxt = null
        }else{
            this.head = null
        }
        this._counter --
        return output;
    }

    remove(val){
        if(!this.head){
            return 'Nothing in the list to remove.';
        }
        if(this.head.data === val){
            this.pop()
            return;
        }
        let curr = this.head
        while(curr.nxt){
            if(curr.data === val){
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                this._counter --
                return;
            }
            curr = curr.nxt
        }
        if(val === this.tail.data){
            this.shift()
            return;
        }
        return 'No such Node in the list.';
    }
}

module.exports = DLL;