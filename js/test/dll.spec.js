'use strict';

let DLL = require('../dll');
let chai = require("chai");
let expect = chai.expect;;

describe('dll.js tests', function() {
    it("dll have empty head on creation", function(){
        let dll = new DLL()
        expect(dll.head).to.be.null;
    });

    it('push adds new node', function(){
        let dll = new DLL()
        dll.push('val')
        expect(dll.head.data).to.be.string('val');
    });

    it('push moves head along', function(){
        let dll = new DLL()
        dll.push(1)
        dll.push(2)
        expect(dll.head.data).to.equal(2);
    });

    it('old head points to new head', function(){
        let dll = new DLL()
        dll.push('val')
        dll.push('lul')
        expect(dll.head.nxt.prev.data).to.be.string('lul');
    });

    it('pop removes head', function(){
        let dll = new DLL()
        dll.push('val')
        let ayy = dll.pop()
        expect(ayy).to.be.string('val');
    });

    it('pop moves head along', function(){
        let dll = new DLL()
        dll.push('val')
        dll.push('lul')
        dll.pop()
        expect(dll.head.data).to.equal('val');
    });

    it('pop throws error on empty list', function(){
        let dll = new DLL()
        expect(dll.pop).to.throw(Error);
    });

    it('append adds tail', function(){
        let dll = new DLL()
        dll.append('backend')
        expect(dll.tail.data).to.be.string('backend');
    });

    it('append moves tail along appropriately', function(){
        let dll = new DLL()
        dll.append('ayy')
        dll.append('bae')
        dll.append('see')
        expect(dll.tail.data).to.be.string('see');
    });

    it('shift removes tail node', function(){
        let dll = new DLL()
        dll.append('lul')
        dll.push('idk')
        dll.shift()
        expect(dll.tail.data).to.be.string('idk');
    });

    it('shift throws error on empty list', function(){
        let dll = new DLL()
        expect(dll.shift).to.throw(Error);
    })

    it('empty list remove returns string', function(){
        let dll = new DLL()
        expect(dll.remove()).to.be.string('Nothing in the list to remove.');
    });

    it('remove returns string if node not in', function(){
        let dll = new DLL()
        dll.push('val!')
        expect(dll.remove('lul')).to.be.string('No such Node in the list.');
    });

    it('remove pops head', function(){
        let dll = new DLL()
        dll.push('val!')
        expect(dll.remove('val!')).to.be.undefined;
    });

    it('remove shifts tail', function(){
        let dll = new DLL()
        dll.append('tail!')
        expect(dll.remove('tail!')).to.be.undefined;
    });
});