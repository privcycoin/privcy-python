****************************
  Introduction
****************************

The goal of this library is to make it easier for:

- Payment gateways to support privcy
- Merchant sites to integrate privcy payments directly
- Other services that require (micro-)payments to use privcy

In this initial release it implements a thin wrapper around the 
privcy JSON-RPC API. Using this API from Python directly is conceptually very simple, 
here is the example from the API 
documentation page:

::

    from jsonrpc import ServiceProxy
    
    access = ServiceProxy("http://user:password@127.0.0.1:20103")
    access.getinfo()
    access.listreceivedbyaddress(6)
    access.sendtoaddress("11yEmxiMso2RsFVfBcCa616npBvGgxiBX", 10)

However, this approach has some disadvantages, one thing is that error handling is complex, as it
requires manually checking the contents of :const:`JSONException` objects.

``privcy-python`` attempts to create an even more friendly interface by wrapping the JSON-RPC API. The major advantages
compared to a raw ``jsonrpc`` based approach are:

- Better exception handling. Exceptions are converted to subclasses of :class:`~privcyrpc.exceptions.privcyException`.

- Automatic privcy configuration loading. In case the ``privcy -server`` or ``privcyd`` program runs on the same 
  machine as the client script, and as the same user, the configuration file can automatically be parsed. This
  makes it unneccesary to explicitly specify a *username* and *password*. Of course, this is still possible.

- Documentation in Pythonish format. You are reading this right now.

- The functions 
  :func:`~privcyrpc.connection.privcyConnection.getinfo`, :func:`~privcyrpc.connection.privcyConnection.listreceivedbyaccount`,
  :func:`~privcyrpc.connection.privcyConnection.listreceivedbyaddress`, 
  :func:`~privcyrpc.connection.privcyConnection.listtransactions` and more return actual Python objects, instead of simply
  dictionaries. This makes for cleaner code, as the fields can simply be addressed with ``x.foo`` instead of 
  ``x['foo']``.

The plan for future releases is to add a more high-level interface on top of this.

