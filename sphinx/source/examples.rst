****************************
  Examples
****************************

A basic program that uses ``python-privcy`` looks like this:

First, import the library and exceptions.

::

    import privcyrpc
    from privcyrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``privcy`` instance of the current user on the local machine
with one call to
:func:`~privcyrpc.connect_to_local`. This returns a :class:`~privcyrpc.connection.privcyConnection` objects:

::

    conn = privcyrpc.connect_to_local()

Try to move one privcy from account ``testaccount`` to account ``testaccount2`` using 
:func:`~privcyrpc.connection.privcyConnection.move`. Catch the :class:`~privcyrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~privcyrpc.connection.privcyConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

