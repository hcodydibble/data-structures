'use strict';

let Priority = require("../priorityQ");
let chai = require("chai");
let expect = chai.expect;

describe("priorityQ.js tests", function(){
    it("pop removes highest priority", function(){
        let pque = new Priority()
        for(var i = 0; i < 3; i++){
            pque.insert(i)
        }
        pque.insert(8, 2)
        pque.insert(10, 2)
        expect(pque.pop()).to.equal(8);
    });

    it("pop raises error on new priority queue", function(){
        let pque = new Priority()
        expect(pque.pop).to.throw(Error);
    });

    it("peek shows highest priority", function(){
        let pque = new Priority()
        for(var i = 0; i < 3; i++){
            pque.insert(i)
        }
        pque.insert(8, 2)
        pque.insert(10, 2)
        pque.insert(0, 33)
        expect(pque.peek()).to.equal(0);
    });

    it("peek returns undefined if priority queue is empty", function(){
        let pque = new Priority()
        expect(pque.peek()).to.be.undefined;
    });
});