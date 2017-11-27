'use strict';

let List = require("../linked-list");
let chai = require("chai");
let expect = chai.expect;

describe("linked-list.js tests", function(){
    it("push adds new value", function(){
        let list = new List();
        list.push(2);
        expect(list.head.data).to.equal(2);
    });

    it("push moves head along appropriately", function(){
        let list = new List();
        list.push(1);
        list.push(2);
        expect(list.head.data).to.equal(2);
    });

    it("push moves old head to next of new head", function(){
        let list = new List(); 
        list.push(1);
        list.push(2);
        expect(list.head.next.data).to.equal(1);
    });

    it("pop returns head value", function(){
       let list = new List();
       list.push("lul") ;
       expect(list.pop()).to.have.string("lul");
    });

    it("pop shifts head", function(){
        let list = new List();
        list.push("word");
        list.push(1);
        list.pop();
        expect(list.head.data).to.have.string("word");
    });

    it("size returns list length", function(){
        let list = new List();
        expect(list.size()).to.equal(0);
    });

    it("linked list takes an iterable", function(){
       let s = new List([1, 2, 3, 4]); 
       expect(s.size()).to.equal(4);
    });

    it("search returns no node if not there", function(){
       let list = new List();
       list.push(1);
       expect(list.search(2)).to.have.string("No such Node");
    });

    it("search returns Node's data", function(){
        let list = new List();
        list.push(1);
        list.push(2);
        expect(list.search(1)).to.equal(1);
    });

    it("remove removes a sinlge node", function(){
        let list = new List();
        list.push(1);
        list.remove(1);
        expect(list.head).to.be.null;
    });

    it("remove works as expected", function(){
        let list = new List();
        list.push(2);
        list.push(3);
        list.push(4);
        list.remove(3);
        expect(list.head.next.data).to.equal(2);
    });

    it("display displays correctly", function(){
        let list = new List();
        for (var i = 0; i < 5; i++) {
            list.push(i);
        }
        expect(list.display()).to.be.an("array").and.to.include.ordered.members([4, 3, 2, 1, 0]);
    });

    it("linked list iterable works", function(){
        let list = new List([1, 2, 3, 4]);
       expect(list.size()).to.equal(4); 
    });

    it("remove on empty list throws error", function(){
        let list = new List();
        expect(list.remove).to.throw();
    });

    it("pop on empty list throws error", function(){
        let list = new List();
        expect(list.pop).to.throw();
    });
});