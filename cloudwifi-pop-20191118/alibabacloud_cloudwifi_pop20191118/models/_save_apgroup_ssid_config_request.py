# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveApgroupSsidConfigRequest(DaraModel):
    def __init__(
        self,
        acct_port: int = None,
        acct_secret: str = None,
        acct_server: str = None,
        apgroup_id: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_cache: str = None,
        auth_port: int = None,
        auth_secret: str = None,
        auth_server: str = None,
        binding: str = None,
        cir: int = None,
        dae_client: str = None,
        dae_port: int = None,
        dae_secret: str = None,
        disabled: str = None,
        disassoc_low_ack: str = None,
        disassoc_weak_rssi: int = None,
        dynamic_vlan: int = None,
        effect: bool = None,
        enc_key: str = None,
        encryption: str = None,
        hidden: str = None,
        id: int = None,
        ieee_80211w: str = None,
        ignore_weak_probe: int = None,
        isolate: str = None,
        lite_effect: bool = None,
        max_inactivity: int = None,
        maxassoc: str = None,
        multicast_forward: int = None,
        nasid: str = None,
        network: int = None,
        new_ssid: str = None,
        ownip: str = None,
        secondary_acct_port: int = None,
        secondary_acct_secret: str = None,
        secondary_acct_server: str = None,
        secondary_auth_port: int = None,
        secondary_auth_secret: str = None,
        secondary_auth_server: str = None,
        short_preamble: str = None,
        ssid: str = None,
        ssid_lb: int = None,
        type: int = None,
        vlan_dhcp: int = None,
        wmm: str = None,
    ):
        self.acct_port = acct_port
        self.acct_secret = acct_secret
        self.acct_server = acct_server
        # This parameter is required.
        self.apgroup_id = apgroup_id
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.auth_cache = auth_cache
        self.auth_port = auth_port
        self.auth_secret = auth_secret
        self.auth_server = auth_server
        # This parameter is required.
        self.binding = binding
        self.cir = cir
        self.dae_client = dae_client
        self.dae_port = dae_port
        self.dae_secret = dae_secret
        self.disabled = disabled
        self.disassoc_low_ack = disassoc_low_ack
        self.disassoc_weak_rssi = disassoc_weak_rssi
        self.dynamic_vlan = dynamic_vlan
        self.effect = effect
        self.enc_key = enc_key
        # This parameter is required.
        self.encryption = encryption
        self.hidden = hidden
        self.id = id
        self.ieee_80211w = ieee_80211w
        self.ignore_weak_probe = ignore_weak_probe
        self.isolate = isolate
        self.lite_effect = lite_effect
        self.max_inactivity = max_inactivity
        self.maxassoc = maxassoc
        self.multicast_forward = multicast_forward
        self.nasid = nasid
        # This parameter is required.
        self.network = network
        # This parameter is required.
        self.new_ssid = new_ssid
        self.ownip = ownip
        self.secondary_acct_port = secondary_acct_port
        self.secondary_acct_secret = secondary_acct_secret
        self.secondary_acct_server = secondary_acct_server
        self.secondary_auth_port = secondary_auth_port
        self.secondary_auth_secret = secondary_auth_secret
        self.secondary_auth_server = secondary_auth_server
        self.short_preamble = short_preamble
        # This parameter is required.
        self.ssid = ssid
        self.ssid_lb = ssid_lb
        self.type = type
        self.vlan_dhcp = vlan_dhcp
        self.wmm = wmm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acct_port is not None:
            result['AcctPort'] = self.acct_port

        if self.acct_secret is not None:
            result['AcctSecret'] = self.acct_secret

        if self.acct_server is not None:
            result['AcctServer'] = self.acct_server

        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache

        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port

        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret

        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server

        if self.binding is not None:
            result['Binding'] = self.binding

        if self.cir is not None:
            result['Cir'] = self.cir

        if self.dae_client is not None:
            result['DaeClient'] = self.dae_client

        if self.dae_port is not None:
            result['DaePort'] = self.dae_port

        if self.dae_secret is not None:
            result['DaeSecret'] = self.dae_secret

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.disassoc_low_ack is not None:
            result['DisassocLowAck'] = self.disassoc_low_ack

        if self.disassoc_weak_rssi is not None:
            result['DisassocWeakRssi'] = self.disassoc_weak_rssi

        if self.dynamic_vlan is not None:
            result['DynamicVlan'] = self.dynamic_vlan

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.enc_key is not None:
            result['EncKey'] = self.enc_key

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.hidden is not None:
            result['Hidden'] = self.hidden

        if self.id is not None:
            result['Id'] = self.id

        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w

        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe

        if self.isolate is not None:
            result['Isolate'] = self.isolate

        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect

        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity

        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc

        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward

        if self.nasid is not None:
            result['Nasid'] = self.nasid

        if self.network is not None:
            result['Network'] = self.network

        if self.new_ssid is not None:
            result['NewSsid'] = self.new_ssid

        if self.ownip is not None:
            result['Ownip'] = self.ownip

        if self.secondary_acct_port is not None:
            result['SecondaryAcctPort'] = self.secondary_acct_port

        if self.secondary_acct_secret is not None:
            result['SecondaryAcctSecret'] = self.secondary_acct_secret

        if self.secondary_acct_server is not None:
            result['SecondaryAcctServer'] = self.secondary_acct_server

        if self.secondary_auth_port is not None:
            result['SecondaryAuthPort'] = self.secondary_auth_port

        if self.secondary_auth_secret is not None:
            result['SecondaryAuthSecret'] = self.secondary_auth_secret

        if self.secondary_auth_server is not None:
            result['SecondaryAuthServer'] = self.secondary_auth_server

        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble

        if self.ssid is not None:
            result['Ssid'] = self.ssid

        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb

        if self.type is not None:
            result['Type'] = self.type

        if self.vlan_dhcp is not None:
            result['VlanDhcp'] = self.vlan_dhcp

        if self.wmm is not None:
            result['Wmm'] = self.wmm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcctPort') is not None:
            self.acct_port = m.get('AcctPort')

        if m.get('AcctSecret') is not None:
            self.acct_secret = m.get('AcctSecret')

        if m.get('AcctServer') is not None:
            self.acct_server = m.get('AcctServer')

        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')

        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')

        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')

        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')

        if m.get('Binding') is not None:
            self.binding = m.get('Binding')

        if m.get('Cir') is not None:
            self.cir = m.get('Cir')

        if m.get('DaeClient') is not None:
            self.dae_client = m.get('DaeClient')

        if m.get('DaePort') is not None:
            self.dae_port = m.get('DaePort')

        if m.get('DaeSecret') is not None:
            self.dae_secret = m.get('DaeSecret')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DisassocLowAck') is not None:
            self.disassoc_low_ack = m.get('DisassocLowAck')

        if m.get('DisassocWeakRssi') is not None:
            self.disassoc_weak_rssi = m.get('DisassocWeakRssi')

        if m.get('DynamicVlan') is not None:
            self.dynamic_vlan = m.get('DynamicVlan')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')

        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')

        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')

        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')

        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')

        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')

        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')

        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NewSsid') is not None:
            self.new_ssid = m.get('NewSsid')

        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')

        if m.get('SecondaryAcctPort') is not None:
            self.secondary_acct_port = m.get('SecondaryAcctPort')

        if m.get('SecondaryAcctSecret') is not None:
            self.secondary_acct_secret = m.get('SecondaryAcctSecret')

        if m.get('SecondaryAcctServer') is not None:
            self.secondary_acct_server = m.get('SecondaryAcctServer')

        if m.get('SecondaryAuthPort') is not None:
            self.secondary_auth_port = m.get('SecondaryAuthPort')

        if m.get('SecondaryAuthSecret') is not None:
            self.secondary_auth_secret = m.get('SecondaryAuthSecret')

        if m.get('SecondaryAuthServer') is not None:
            self.secondary_auth_server = m.get('SecondaryAuthServer')

        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')

        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')

        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')

        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')

        return self

