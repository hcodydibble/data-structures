(function () {'use strict';}());

class PriorityQueue{
    constructor(){
        this._priorityDict = {};
    }

    insert(value, priority=0){
        if(this._priorityDict[priority] !== undefined){
            this._priorityDict[priority].push(value)
        }else{
            this._priorityDict[priority] = priority
            this._priorityDict[priority] = []
            this._priorityDict[priority].push(value)
        }
    }

    pop(){
        if(isEmptyObject(this._priorityDict)){
            throw new Error('There is nothing to pop')
        }
        let highestPriority = Math.max.apply(Math, Object.keys(this._priorityDict).map(Number))
        let popped = this._priorityDict[highestPriority].shift()
        if(isEmptyObject(this._priorityDict[highestPriority])){
            delete this._priorityDict[highestPriority]
        }
        return popped
    }

    peek(){
        if(isEmptyObject(this._priorityDict)){
            return undefined
        }
        let highestPriority = Math.max.apply(Math, Object.keys(this._priorityDict).map(Number))
        return this._priorityDict[highestPriority][0]
    }
}

function isEmptyObject( obj ) {
    for ( var name in obj ) {
        return false;
    }
    return true;
}

module.exports = PriorityQueue;
