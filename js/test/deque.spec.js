'use strict';

const DEQUE = require('../deque')
const CHAI = require('chai')
const expect = CHAI.expect

describe('deque.js tests', function(){
    it('append adds a value', function(){
        let deq =  new DEQUE()
        deq.append('lul')
        expect(deq.size()).to.equal(1);
    });

    it('append adds multiple values', function(){
        let deq =  new DEQUE()
        deq.append('nah')
        deq.append('bruh')
        expect(deq.size()).to.equal(2);
    });

    it('popleft removes first node added', function(){
        let deq =  new DEQUE()
        deq.append('first')
        deq.append('second')
        expect(deq.popleft()).to.be.string('first');
    });

    it('popleft throws error on empty deque', function(){
        let deq =  new DEQUE()
        expect(deq.popleft).to.throw(Error);
    });

    it('peek returns next node to be dequed', function(){
        let deq =  new DEQUE()
        deq.appendleft('peek me')
        expect(deq.peek()).to.be.string('peek me');
    });

    it('peek returns null on empty deque', function(){
        let deq =  new DEQUE()
        expect(deq.peek()).to.be.null;
    });

    it('size returns zero on empty deque', function(){
        let deq =  new DEQUE()
        expect(deq.size()).to.equal(0);
    });

    it('appendleft adds node to front', function(){
        let deq =  new DEQUE()
        deq.appendleft('leftshark')
        expect(deq._dll.head.data).to.be.string('leftshark');
    });

    it('appendleft adds multiple nodes', function(){
        let deq =  new DEQUE()
        deq.appendleft('one')
        deq.appendleft('two')
        expect(deq.size()).to.equal(2);
    });

    it('pop removes node', function(){
        let deq =  new DEQUE()
        deq.append('notme')
        deq.append('me')
        expect(deq.pop()).to.be.string('me');
    });

    it('pop throws error on empty deque', function(){
        let deq =  new DEQUE()
        expect(deq.pop).to.throw(Error);
    });

    it('peekleft show head node value', function(){
        let deq =  new DEQUE()
        deq.append('do not look at me')
        deq.appendleft('look at me!')
        expect(deq.peekleft()).to.be.string('look at me!');
    });

    it('peekleft returns null on empty deque', function(){
        let deq =  new DEQUE()
        expect(deq.peekleft()).to.be.null;
    });
});