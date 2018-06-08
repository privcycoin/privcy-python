=================
 Usage
=================

See also the `main privcy documentation`_ for details and background on setting up and
using privcyd remotely.

Setting up privcy for remote control
-------------------------------------

If you run privcy with the ``-server`` argument, or if you run ``privcyd``, it can be controlled 
either by sending it HTTP-JSON-RPC commands.

However, beginning with privcy 0.3.3 you must create a ``privcy.conf`` file in the privcy data directory 
(default ``$HOME/.bitconf``) and set an RPC password:

::

  rpcuser=anything
  rpcpassword=anything

Once that is done, the easiest way to check whether privcy accepts remote commands is by running 
privcy again, with the command (and any parameters) as arguments. For example:

::

  $ privcyd getinfo

Connecting to the wallet from Python
-------------------------------------

There are two functions for this:

*Connecting to local privcy instance*
  Use the function :func:`~privcyrpc.connect_to_local`. This automagically
  sorts out the connection to a privcy process running on the current machine,
  for the current user.
  
  ::
  
    conn = privcyrpc.connect_to_local()

*Connecting to a remote privcy instance*
  Use the function :func:`~privcyrpc.connect_to_remote`. For this function
  it is neccesary to explicitly specify a hostname and port to connect to, and
  to provide user credentials for logging in.

  ::
  
    conn = privcyrpc.connect_to_remote('foo', 'bar', host='payments.yoyodyne.com', port=20103)


How to use the API
-------------------------------------

For basic sending and receiving of payments, the four most important methods are 

*Getting the current balance*
  Use the method :func:`~privcyrpc.connection.privcyConnection.getbalance` to get the current server balance.
  
  ::
  
    print "Your balance is %f" % (conn.getbalance(),)

*Check a customer address for validity and get information about it*
  This can be done with the method :func:`~privcyrpc.connection.privcyConnection.validateaddress`.

  ::

      rv = conn.validateaddress(foo)
      if rv.isvalid:
          print "The address that you provided is valid"
      else:
          print "The address that you provided is invalid, please correct"

*Sending payments*
  The method :func:`~privcyrpc.connection.privcyConnection.sendtoaddress` sends a specified
  amount of coins to a specified address.

  ::

      conn.sendtoaddress("msTGAm1ApjEJfsWfAaRVaZHRm26mv5GL73", 20.0)

*Get a new address for accepting payments*
  To accept payments, use the method :func:`~privcyrpc.connection.privcyConnection.getnewaddress`
  to generate a new address. Give this address to the customer and store it in a safe place, to be able to check
  when the payment to this address has been made.

  ::
  
      pay_to = conn.getnewaddress()
      print "We will ship the pirate sandwidth after payment of 200 coins to ", pay_to

*Check how much has been received at a certain address*
  The method :func:`~privcyrpc.connection.privcyConnection.getreceivedbyaddress` 
  returns how many privcys have been received at a certain address. Together with the
  previous function, this can be used to check whether a payment has been made
  by the customer.

  ::

      amount = conn.getreceivedbyaddress(pay_to)
      if amount > 200.0:
          print "Thanks, your sandwidth will be prepared and shipped."



      
The account API
-------------------------------------
More advanced usage of privcy allows multiple accounts within one wallet. This
can be useful if you are writing software for a bank, or 
simply want to have a clear separation between customers payments.

For this, see the `Account API`_ documentation.

.. _main privcy documentation: https://en.privcy.it/wiki/Main_Page
.. _account API: https://en.privcy.it/wiki/Accounts_explained


