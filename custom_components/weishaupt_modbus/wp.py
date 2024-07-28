"""Platform for sensor integration."""

from pymodbus.client import ModbusTcpClient as ModbusClient

# import logging

# hp_ip = "10.10.1.225"
# hp_port = 502

# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
APPID_offset = 100


class heat_pump:
    """Test."""

    def __init__(self, hp_ip, hp_port) -> None:
        """Test."""
        self._ip = hp_ip
        self._port = hp_port
        self.WWP = None

    def connect(self):
        """Test."""
        try:
            self.WWP = ModbusClient(host=self._ip, port=self._port)
            return self.WWP.connected
        except:
            return None

    ##############################################################################################################################
    # Modbus Register List:                                                                                                      #
    # https://docs.google.com/spreadsheets/d/1EZ3QgyB41xaXo4B5CfZe0Pi8KPwzIGzK/edit?gid=1730751621#gid=1730751621                #
    ##############################################################################################################################

    #####################
    #   System          #
    #####################
    @property
    def Sys_Aussentemperatur1(self):
        """Outer Temperature1."""
        try:
            return self.WWP.read_input_registers(30001, slave=1).registers[0] / 10
        except:
            return None

    @property
    def Sys_Aussentemperatur2(self):
        """Outer Temperature2."""
        try:
            return self.WWP.read_input_registers(30002, slave=1).registers[0] / 10
        except:
            return None

    @property
    def Sys_Fehler(self):
        """Outer Temperature2."""
        try:
            val = self.WWP.read_input_registers(30004, slave=1).registers[0]
            if val == 65535:
                return "kein Fehler"
            return "Fehler: " + val
        except:
            return None

    @property
    def Sys_Warnung(self):
        """Outer Temperature2."""
        try:
            val = self.WWP.read_input_registers(30004, slave=1).registers[0]
            if val == 65535:
                return "kein Fehler"
            return "Fehler: " + val
        except:
            return None

    @property
    def Sys_Fehlerfrei(self):
        """Outer Temperature2."""
        try:
            val = self.WWP.read_input_registers(30005, slave=1).registers[0]
            if val == 0:
                return "Fehler aktiv"
            return "Störungsfreier Betrieb"
        except:
            return None

    @property
    def Sys_Betriebsanzeige(self):  # noqa: C901
        """Energy used today."""
        try:
            val = self.WWP.read_input_registers(30006, slave=1).registers[0]
            match val:
                case 0:
                    return "Undefiniert"
                case 1:
                    return "Relaistest"
                case 2:
                    return "Notaus"
                case 3:
                    return "Diagnose"
                case 4:
                    return "Handbetrieb"
                case 5:
                    return "Handbetrieb Heizen"
                case 6:
                    return "Handbetrieb Kühlen"
                case 7:
                    return "Manueller Abtaubetrieb"
                case 8:
                    return "Abtauen"
                case 9:
                    return "WEZ2"
                case 10:
                    return "EVU_SPERRE"
                case 11:
                    return "SG Tarif"
                case 12:
                    return "SG Maximal"
                case 13:
                    return "Tarifladung"
                case 14:
                    return "Erhöhter Betrieb"
                case 15:
                    return "Standzeit"
                case 16:
                    return "Standbybetrieb"
                case 17:
                    return "Spülbetrieb"
                case 18:
                    return "Frostschutz"
                case 19:
                    return "Heizbetrieb"
                case 20:
                    return "Warmwasserbetrieb"
                case 21:
                    return "Legionellenschutz"
                case 22:
                    return "Umschaltung HZ KU"
                case 23:
                    return "Kühlbetrieb"
                case 24:
                    return "Passive Kühlung"
                case 25:
                    return "Sommerbetrieb"
                case 26:
                    return "Schwimmbad"
                case 27:
                    return "Urlaub"
                case 28:
                    return "Estrich"
                case 29:
                    return "Gesperrt"
                case 30:
                    return "Sperre AT"
                case 31:
                    return "Sperre Sommer"
                case 32:
                    return "Sperre Winter"
                case 33:
                    return "Einsatzgrenze"
                case 34:
                    return "HK Sperre"
                case 35:
                    return "Absenk"
        except:
            return None

    @property
    def Sys_Betriebsart(self):
        """Energy used today."""
        val = self.WWP.read_holding_registers(40001, slave=1).registers[0]
        match val:
            case 0:
                return "AUTOMATIK"
            case 1:
                return "HEIZEN"
            case 2:
                return "KÜHLEN"
            case 3:
                return "SOMMER"
            case 4:
                return "STANDBY"
            case 5:
                return "2.WEZ"

    #####################
    #   Heizkreis       #
    #####################
    @property
    def HK_Raumsolltemperatur(self):
        """Raumsolltemperatur."""
        return self.WWP.read_input_registers(31101, slave=1).registers[0] / 10

    @property
    def HK_Raumtemperatur(self):
        """Raumtemperatur."""
        val = self.WWP.read_input_registers(31102, slave=1).registers[0]
        if val == 32768:
            return None
        return val / 10

    @property
    def HK_Raumfeuchte(self):
        """Raumtemperatur."""
        val = self.WWP.read_input_registers(31103, slave=1).registers[0]
        if val == 65535:
            return None
        return val

    @property
    def HK_Vorlaufsolltemperatur(self):
        """HK_Vorlaufsolltemperatur."""
        return self.WWP.read_input_registers(31104, slave=1).registers[0] / 10

    @property
    def HK_Vorlauftemperatur(self):
        """HK_Vorlauftemperatur."""
        val = self.WWP.read_input_registers(31105, slave=1).registers[0]
        if val == 32768:
            return None
        return val / 10

    @property
    def HK_Konfiguration(self):
        """Energy used today."""
        val = self.WWP.read_holding_registers(41101, slave=1).registers[0]
        match val:
            case 0:
                return "AUS"
            case 1:
                return "PUMPENKREIS"
            case 2:
                return "MISCHKREIS"
            case 3:
                return "SOLLWERT (PUMPE M1)"

    @property
    def HK_AnforderungTyp(self):
        """Energy used today."""
        val = self.WWP.read_holding_registers(41102, slave=1).registers[0]
        match val:
            case 0:
                return "AUS"
            case 1:
                return "WITTERUNGSGEFÜHRT"
            case 2:
                return "KONSTANT"

    @property
    def HK_Betriebsart(self):
        """Energy used today."""
        val = self.WWP.read_holding_registers(41103, slave=1).registers[0]

        match val:
            case 0:
                return "AUTOMATIK"
            case 1:
                return "KOMFORT"
            case 2:
                return "NORMAL"
            case 3:
                return "ABSENKBETRIEB"
            case 5:
                return "STANDBY"

    @property
    def HK_Pause_Party(self):
        """Energy used today."""
        val = self.WWP.read_holding_registers(41104, slave=1).registers[0]
        if val == 25:
            return "Automatik"
        if val < 25:
            time = (25 - val) * 0.5
            return "Pausenzeit " + time + "h"
        if val > 25:
            time = (val - 25) * 0.5
            return "Partyzeit " + val * 0.5 + "h"

    #####################
    #   Warm Water      #
    #####################
    @property
    def WW_Soll(self):
        """Test."""
        return self.WWP.read_holding_registers(42103, slave=1).registers[0] / 10

    @WW_Soll.setter
    def WW_Soll(self, value):
        self.WWP.write_register(42103, value * 10, slave=1)

    @property
    def WW_Ist(self):
        """Temperature of warm-water."""
        return self.WWP.read_input_registers(32102, slave=1).registers[0] / 10

    @property
    def WW_Soll_info(self):
        """Temperature of warm-water."""
        return self.WWP.read_input_registers(32101, slave=1).registers[0] / 10

    #####################
    #   Heatpump        #
    #####################
    @property
    def Hp_Betrieb(self):  # noqa: C901
        """Energy used today."""
        val = self.WWP.read_input_registers(33101, slave=1).registers[0]
        match val:
            case 0:
                return "Undefiniert"
            case 1:
                return "Relaistest"
            case 2:
                return "Notaus"
            case 3:
                return "Diagnose"
            case 4:
                return "Handbetrieb"
            case 5:
                return "Handbetrieb Heizen"
            case 6:
                return "Handbetrieb Kühlen"
            case 7:
                return "Manueller Abtaubetrieb"
            case 8:
                return "Abtauen"
            case 9:
                return "WEZ2"
            case 10:
                return "EVU_SPERRE"
            case 11:
                return "SG Tarif"
            case 12:
                return "SG Maximal"
            case 13:
                return "Tarifladung"
            case 14:
                return "Erhöhter Betrieb"
            case 15:
                return "Standzeit"
            case 16:
                return "Standbybetrieb"
            case 17:
                return "Spülbetrieb"
            case 18:
                return "Frostschutz"
            case 19:
                return "Heizbetrieb"
            case 20:
                return "Warmwasserbetrieb"
            case 21:
                return "Legionellenschutz"
            case 22:
                return "Umschaltung HZ KU"
            case 23:
                return "Kühlbetrieb"
            case 24:
                return "Passive Kühlung"
            case 25:
                return "Sommerbetrieb"
            case 26:
                return "Schwimmbad"
            case 27:
                return "Urlaub"
            case 28:
                return "Estrich"
            case 29:
                return "Gesperrt"
            case 30:
                return "Sperre AT"
            case 31:
                return "Sperre Sommer"
            case 32:
                return "Sperre Winter"
            case 33:
                return "Einsatzgrenze"
            case 34:
                return "HK Sperre"
            case 35:
                return "Absenk"

    @property
    def Hp_Stoermeldung(self):
        """Energy used today."""
        val = self.WWP.read_input_registers(33102, slave=1).registers[0]
        match val:
            case 0:
                return "Störung"
            case 1:
                return "Störungsfrei"

    @property
    def Hp_Leistungsanforderung(self):
        """Energy used today."""
        return self.WWP.read_input_registers(33103, slave=1).registers[0]

    @property
    def Hp_Vorlauftemperatur(self):
        """Energy used today."""
        return self.WWP.read_input_registers(33104, slave=1).registers[0] / 10

    @property
    def Hp_Ruecklauftemperatur(self):
        """Energy used today."""
        return self.WWP.read_input_registers(33105, slave=1).registers[0] / 10

    #####################
    #   Statistics      #
    #####################
    @property
    def Energy_total_today(self):
        """Energy used today."""
        return self.WWP.read_input_registers(36101, slave=1).registers[0]

    @property
    def Energy_total_yesterday(self):
        """Energy used yesterday."""
        return self.WWP.read_input_registers(36102, slave=1).registers[0]

    @property
    def Energy_total_month(self):
        """Energy used month."""
        return self.WWP.read_input_registers(36103, slave=1).registers[0]

    @property
    def Energy_total_year(self):
        """Energy used year."""
        return self.WWP.read_input_registers(36104, slave=1).registers[0]

    @property
    def Heating_total_today(self):
        """Energy used for heating today."""
        return self.WWP.read_input_registers(36201, slave=1).registers[0]

    @property
    def Heating_total_yesterday(self):
        """Energy used for heating yesterday."""
        return self.WWP.read_input_registers(36202, slave=1).registers[0]

    @property
    def Heating_total_month(self):
        """Energy used for heating month."""
        return self.WWP.read_input_registers(36203, slave=1).registers[0]

    @property
    def Heating_total_year(self):
        """Energy used for heating year."""
        return self.WWP.read_input_registers(36204, slave=1).registers[0]

    @property
    def Water_total_today(self):
        """Energy used for heating water today."""
        return self.WWP.read_input_registers(36301, slave=1).registers[0]

    @property
    def Water_total_yesterday(self):
        """Energy used for heating water yesterday."""
        return self.WWP.read_input_registers(36302, slave=1).registers[0]

    @property
    def Water_total_month(self):
        """Energy used for heating water month."""
        return self.WWP.read_input_registers(36303, slave=1).registers[0]

    @property
    def Water_total_year(self):
        """Energy used for heating water year."""
        return self.WWP.read_input_registers(36304, slave=1).registers[0]

    @property
    def Cooling_total_today(self):
        """Energy used for cooling."""
        return self.WWP.read_input_registers(36401, slave=1).registers[0]

    @property
    def Cooling_total_yesterday(self):
        """Energy used for cooling."""
        return self.WWP.read_input_registers(36402, slave=1).registers[0]

    @property
    def Cooling_total_month(self):
        """Energy used for cooling."""
        return self.WWP.read_input_registers(36403, slave=1).registers[0]

    @property
    def Cooling_total_year(self):
        """Energy used for cooling."""
        return self.WWP.read_input_registers(36404, slave=1).registers[0]


# whp = heat_pump(hp_ip, hp_port)
# whp.connect()
# print(whp.WW_Soll)
# whp.WW_Soll = 44
# print(whp.WW_Soll)
# whp.WW_Soll = 45
# print(whp.WW_Soll)

# print(whp.WW_Ist)
