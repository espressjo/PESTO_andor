How to use python_andor.py
=================================

Getting Started
---------------

**Getting the window comupter ready**

First, connect to the window desktop that is installed on the telescope with anydesk

.. figure:: anydesk.png

	Anydesk icon.

Then enter the number: 432 587 514. The password is Cinnamon&Nutmeg. Then, launch Audela.

.. figure:: audela.png

	Audela icon.

In the console (see image), start the server script

.. highlight:: tcl

::

	source server.tcl


.. highlight:: none



.. figure:: console.png

	Audela consol. 

** On the Linux machine (probably Lyra)**

First open a terminal (ctrl+alt+t in Ubuntu) and open a python console (i.e., >>> python). Then enter:

.. highlight:: python

::

	from python_andor import command as com

	com = com() 

.. highlight:: none

The camera should now be initialized and ready to be used.

Practical example
-----------------

** To launch a live feed of the camera**

In the same python console where the command class has been initialized, enter:

.. highlight:: python

::
	
	com.video()

.. highlight:: none

You will be prompt to enter the exposure time. Do it, and a live stream should start after (exposure time)+2 seconds.

** To launch a script **

In the same python console, enter:

.. highlight:: python

::

	com.script()

.. highlight:: none

You will then be prompted to enter the type of exposure [Target,flat,video or dark], the exposure time and the name of the object. Do it, and a live stream should start after (exposure time)+2 seconds.



