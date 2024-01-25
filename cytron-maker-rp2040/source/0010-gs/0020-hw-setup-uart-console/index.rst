.. _gs-setup-uart-console:

UART Console am PC
##################

.. sidebar:: Ziel

   Dein Terminalemulator arbeitet mit der UART des MCU-Board.

.. topic:: Übersicht

   Über den *Raspberry Pi – Debug Probe* wird eine Null-Modem Verbindung zwischen
   deinem Host-PC und der ersten UART0 der MCU (RP2040) hergestellt. Mit Hilfe
   einer vorinstallierten Applikation in der MCU wird die Verbindung überprüft.

   Dazu benötigst du auf deinem Host-PC einen Terminalemulator deiner Wahl.
   Gängige Programme wären hier: `Minicom`_, `Picocom`_, `GNU Screen`_,
   `Kermit`_, `goSerial`_, `Tabby`_, `PuTTY`_, `Tera Term`_,
   `PySerial (miniterm)`_, oder `web-serial-terminal`_. Fast alle sind für
   Linux, MacOS und auch Windows verfügbar. Letzterer arbeitet innerhalb
   eines *Google Chrome* oder *Microsoft Edge* WEB Browser mit aktiver
   *Serial Web API*.

   .. attention::

      Eventuell ist auf deinem Host-PC eine Rechteerweiterung (z.B.
      :program:`udev` Regeln unter Linux) oder sogar die Installation
      spezieller Treiber (Windows) notwendig, um als normaler Benutzer
      auf die neuen seriellen Schnittstellen aus dem Terminalemulator
      heraus zugreifen zu können.

      **Bei Schwierigkeiten mit dem Setup helfen dir unsere Mentoren gerne
      weiter!** *Bitte scheue dich nicht, uns anzusprechen.*

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. include:: yourspace.rsti

.. admonition:: Nur für Mentoren
   :class: red-border bug
   :collapsible:

   Das MCU-Board muss mit folgender Firmware zurückgesetzt sein:
   :download:`MP-RPI_PICO-20240125-v1.23.0-preview.66.g307ecc570.dirty.uf2
   </_assets/MP-RPI_PICO-20240125-v1.23.0-preview.66.g307ecc570.dirty.uf2>`

   Eventuell muss der Flash zuvor mit :download:`flash_nuke.uf2
   </_assets/flash_nuke.uf2>` komplett geleert werden.

.. target-notes::

.. _`Minicom`:
   https://salsa.debian.org/minicom-team/minicom/-/releases

.. _`Minicom@SDO`:
   https://salsa.debian.org/minicom-team/minicom

.. _`Picocom`:
   https://github.com/npat-efault/picocom/releases

.. _`Picocom@GH`:
   https://github.com/npat-efault/picocom

.. _`GNU Screen`:
   https://www.gnu.org/software/screen

.. _`GNU Screen@SGO`:
   https://savannah.gnu.org/projects/screen

.. _`Kermit`:
   https://www.kermitproject.org/

.. _`Kermit@GH`:
   https://github.com/KermitProject

.. _`goSerial`:
   https://www.furrysoft.de/?page=goserial

.. _`Tabby`:
   https://tabby.sh/

.. _`Tabby@GH`:
   https://github.com/eugeny/tabby

.. _`PuTTY`:
   https://www.chiark.greenend.org.uk/~sgtatham/putty

.. _`PuTTY@Git`:
   https://git.tartarus.org/?p=simon/putty.git

.. _`Tera Term`:
   https://github.com/TeraTermProject/teraterm/releases

.. _`Tera Term@GH`:
   https://github.com/TeraTermProject/teraterm

.. _`PySerial (miniterm)`:
   https://pypi.org/project/pyserial

.. _`PySerial@GH`:
   https://github.com/pyserial/pyserial

.. _`web-serial-terminal`:
   https://bipes.net.br/aroca/web-serial-terminal

.. _`web-serial-terminal@GH`:
   https://github.com/rafaelaroca/web-serial-terminal
