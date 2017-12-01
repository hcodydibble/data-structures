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
        this._dll.shift()
    }
}

let d = new Deque
console.log(d.pop())