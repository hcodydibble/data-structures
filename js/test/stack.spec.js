"use strict";

let Stack = require("../stack");
let chai = require("chai");
let expect = chai.expect;

describe("stack.js tests", function(){
    it("push adds new value", function(){
        let s = new Stack();
        s.push(2);
        expect(s.linked.head.data).to.equal(2);
    });

    it("push moves head along appropriately", function(){
        let s = new Stack();
        s.push(1);
        s.push(2);
        expect(s.linked.head.data).to.equal(2);
    });

    it("push moves old head to next of new head", function(){
        let s = new Stack(); 
        s.push(1);
        s.push(2);
        expect(s.linked.head.next.data).to.equal(1);
    });

    it("pop returns head value", function(){
       let s = new Stack();
       s.push("lul") ;
       expect(s.pop()).to.have.string("lul");
    });

    it("pop shifts head", function(){
        let s = new Stack();
        s.push("word");
        s.push(1);
        s.pop();
        expect(s.linked.head.data).to.have.string("word");
    });

    it("size returns Stack length", function(){
        let s = new Stack();
        expect(s.size()).to.equal(0);
    });

    it("stack takes an iterable", function(){
       let s = new Stack([1, 2, 3, 4]); 
       expect(s.size()).to.equal(4);
    });
});