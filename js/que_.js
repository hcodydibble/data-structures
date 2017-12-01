'use strict';

let DLL = require('./dll')

class Queue{
    constructor(){
        this.dll = new DLL()
    }

    enqueue(val){
        this.dll.push(val)
    }

    dequeue(){
        try{
            return this.dll.shift();
        }catch(e){
            return undefined;
        }
    }

    peek(){
        if(this.dll._counter === 0){
            return undefined
        }
        return this.dll.tail.data;
    }

    size(){
        return this.dll._counter;
    }
}

module.exports = Queue;