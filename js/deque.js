'use strict';

const DLL = require('./dll')

class Deque{
    constructor(){
        this._dll = new DLL()
    }

    append(val){
        this._dll.append(val)
    }

    appendleft(val){
        this._dll.push(val)
    }

    pop(){
        try{
        return this._dll.shift();
        }catch(e){
            throw new Error('Nothing in the Deque');
        }
    }

    popleft(){
        try{
            return this._dll.pop();
        }catch(e){
            throw new Error('Nothing in the Deque');
        }
    }

    peek(){
        if(this._dll._counter === 0){
            return null;
        }
        return this._dll.tail.data;
    }

    peekleft(){
        if(this._dll._counter === 0){
            return null;
        }
        return this._dll.head.data; 
    }

    size(){
        return this._dll._counter
    }
}

module.exports = Deque