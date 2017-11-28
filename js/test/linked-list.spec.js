'use strict';

let linkedList = require("../linked-list");
let chai = require("chai");
let expect = chai.expect;

describe("linked-list.js tests", function(){
    it("push adds new value", function(){
        let aList = new linkedList.LinkedList();
        aList.push(2);
        expect(aList.head.data).to.equal(2);
    });

    it("push moves head along appropriately", function(){
        let aList = new linkedList.LinkedList();
        aList.push(1);
        aList.push(2);
        expect(aList.head.data).to.equal(2);
    });

    it("push moves old head to next of new head", function(){
        let aList = new linkedList.LinkedList(); 
        aList.push(1);
        aList.push(2);
        expect(aList.head.next.data).to.equal(1);
    });

    it("pop returns head value", function(){
       let aList = new linkedList.LinkedList();
       aList.push("lul") ;
       expect(aList.pop()).to.have.string("lul");
    });

    it("pop shifts head", function(){
        let aList = new linkedList.LinkedList();
        aList.push("word");
        aList.push(1);
        aList.pop();
        expect(aList.head.data).to.have.string("word");
    });

    it("empty list returns undefined", function(){
        let aList = new linkedList.LinkedList();
        expect(aList.pop()).to.be.undefined;
    });

    it("size returns list length", function(){
        let aList = new linkedList.LinkedList();
        expect(aList.size()).to.equal(0);
    });

    it("search returns no node if not there", function(){
       let aList = new linkedList.LinkedList();
       aList.push(1);
       expect(aList.search(2)).to.have.string("No such Node");
    });

    it("search returns Node", function(){
        let aList = new linkedList.LinkedList();
        aList.push(1);
        aList.push(2);
        expect(aList.search(1)).to.be.an.instanceof(linkedList.Node).and.to.have.property('data').to.equal(1);
    });

    it("remove removes a single node", function(){
        let aList = new linkedList.LinkedList();
        aList.push(1);
        aList.remove(1);
        expect(aList.head).to.be.null;
    });

    it("remove works as expected", function(){
        let aList = new linkedList.LinkedList();
        aList.push(2);
        aList.push(3);
        aList.push(4);
        aList.remove(3);
        expect(aList.head.next.data).to.equal(2);
    });

    it("display displays correctly", function(){
        let aList = new linkedList.LinkedList();
        for (var i = 0; i < 5; i++) {
            aList.push(i);
        }
        expect(aList.display()).to.be.string('4, 3, 2, 1, 0');
    });

    it("linked list iterable works", function(){
        let aList = new linkedList.LinkedList([1, 2, 3, 4]);
       expect(aList.size()).to.equal(4); 
    });

    it("remove on empty list throws error", function(){
        let aList = new linkedList.LinkedList();
        expect(aList.remove).to.throw();
    });
});