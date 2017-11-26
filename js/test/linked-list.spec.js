'use strict';

let List = require("../linked-list");
let chai = require("chai");
let expect = chai.expect;

describe("linked-list.js tests", function(){
    it("push adds new value", function(){
        let aList = new List();
        let pushed = aList.push(2);
        expect(aList.head.data).to.equal(2);
    });
});