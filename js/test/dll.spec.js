'use strict';

let DLL = require('../dll');
let chai = require("chai");
let expect = chai.expect;

describe('dll.js tests', function() {
    it("dll have empty head on creation", function(){
        let dll = new DLL()
        expect(dll.head).to.be.null
    });

    it('push adds new node', function(){
        let dll = new DLL()
        dll.push('val')
        expect(dll.head.data).to.be.string('val')
    });

    it('push moves head along', function(){
        let dll = new DLL()
        dll.push(1)
        dll.push(2)
        expect(dll.head.data).to.equal(2)
    });

    it('old head points to new head', function(){
        let dll = new DLL()
        dll.push('val')
        dll.push('lul')
        expect(dll.head.nxt.prev.data).to.be.string('lul')
    });

    it('pop removes head', function(){
        let dll = new DLL()
        dll.push('val')
        let ayy = dll.pop()
        expect(ayy.data).to.be.string('val')
    });

    it('pop moves head along', function(){
        let dll = new DLL()
        dll.push('val')
        dll.push('lul')
        dll.pop()
        expect(dll.head.data).to.equal('val')
    });

    it('pop returns undefined on empty list', function(){
        let dll = new DLL()
        expect(dll.pop()).to.be.undefined
    });

    it('append adds tail', function(){
        let dll = new DLL()
        dll.append('backend')
        expect(dll.tail.data).to.be.string('backend')
    });

    it('append moves tail along appropriately', function(){
        let dll = new DLL()
        dll.append('ayy')
        dll.append('bae')
        dll.append('see')
        expect(dll.tail.data).to.be.string('see')
    });
});