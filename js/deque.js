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
        this._dll.shift()
        }catch(e){
            throw new Error()
        }
    }
}

let d = new Deque
console.log(d.pop())