# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveApRadioConfigRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        bcast_rate: int = None,
        beacon_int: int = None,
        channel: str = None,
        disabled: str = None,
        frag: int = None,
        htmode: str = None,
        hwmode: str = None,
        id: int = None,
        mcast_rate: int = None,
        mgmt_rate: int = None,
        minrate: int = None,
        noscan: str = None,
        probereq: str = None,
        require_mode: str = None,
        rts: int = None,
        shortgi: str = None,
        txpower: str = None,
        uapsd: int = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.bcast_rate = bcast_rate
        # This parameter is required.
        self.beacon_int = beacon_int
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.disabled = disabled
        # This parameter is required.
        self.frag = frag
        # This parameter is required.
        self.htmode = htmode
        # This parameter is required.
        self.hwmode = hwmode
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.mcast_rate = mcast_rate
        # This parameter is required.
        self.mgmt_rate = mgmt_rate
        # This parameter is required.
        self.minrate = minrate
        # This parameter is required.
        self.noscan = noscan
        # This parameter is required.
        self.probereq = probereq
        self.require_mode = require_mode
        # This parameter is required.
        self.rts = rts
        # This parameter is required.
        self.shortgi = shortgi
        # This parameter is required.
        self.txpower = txpower
        # This parameter is required.
        self.uapsd = uapsd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.bcast_rate is not None:
            result['BcastRate'] = self.bcast_rate

        if self.beacon_int is not None:
            result['BeaconInt'] = self.beacon_int

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.frag is not None:
            result['Frag'] = self.frag

        if self.htmode is not None:
            result['Htmode'] = self.htmode

        if self.hwmode is not None:
            result['Hwmode'] = self.hwmode

        if self.id is not None:
            result['Id'] = self.id

        if self.mcast_rate is not None:
            result['McastRate'] = self.mcast_rate

        if self.mgmt_rate is not None:
            result['MgmtRate'] = self.mgmt_rate

        if self.minrate is not None:
            result['Minrate'] = self.minrate

        if self.noscan is not None:
            result['Noscan'] = self.noscan

        if self.probereq is not None:
            result['Probereq'] = self.probereq

        if self.require_mode is not None:
            result['RequireMode'] = self.require_mode

        if self.rts is not None:
            result['Rts'] = self.rts

        if self.shortgi is not None:
            result['Shortgi'] = self.shortgi

        if self.txpower is not None:
            result['Txpower'] = self.txpower

        if self.uapsd is not None:
            result['Uapsd'] = self.uapsd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BcastRate') is not None:
            self.bcast_rate = m.get('BcastRate')

        if m.get('BeaconInt') is not None:
            self.beacon_int = m.get('BeaconInt')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Frag') is not None:
            self.frag = m.get('Frag')

        if m.get('Htmode') is not None:
            self.htmode = m.get('Htmode')

        if m.get('Hwmode') is not None:
            self.hwmode = m.get('Hwmode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('McastRate') is not None:
            self.mcast_rate = m.get('McastRate')

        if m.get('MgmtRate') is not None:
            self.mgmt_rate = m.get('MgmtRate')

        if m.get('Minrate') is not None:
            self.minrate = m.get('Minrate')

        if m.get('Noscan') is not None:
            self.noscan = m.get('Noscan')

        if m.get('Probereq') is not None:
            self.probereq = m.get('Probereq')

        if m.get('RequireMode') is not None:
            self.require_mode = m.get('RequireMode')

        if m.get('Rts') is not None:
            self.rts = m.get('Rts')

        if m.get('Shortgi') is not None:
            self.shortgi = m.get('Shortgi')

        if m.get('Txpower') is not None:
            self.txpower = m.get('Txpower')

        if m.get('Uapsd') is not None:
            self.uapsd = m.get('Uapsd')

        return self

