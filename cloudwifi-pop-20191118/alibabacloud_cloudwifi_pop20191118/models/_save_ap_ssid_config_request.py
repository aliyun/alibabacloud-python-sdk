# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveApSsidConfigRequest(DaraModel):
    def __init__(
        self,
        acct_port: int = None,
        acct_secret: str = None,
        acct_server: str = None,
        acct_status_server_work: int = None,
        ap_asset_id: int = None,
        app_code: str = None,
        app_name: str = None,
        arp_proxy_enable: int = None,
        auth_cache: str = None,
        auth_port: int = None,
        auth_secret: str = None,
        auth_server: str = None,
        auth_status_server_work: int = None,
        cir: int = None,
        cir_step: int = None,
        cir_type: int = None,
        cir_ul: int = None,
        dae_client: str = None,
        dae_port: int = None,
        dae_secret: str = None,
        disabled: str = None,
        disassoc_low_ack: str = None,
        disassoc_weak_rssi: int = None,
        dynamic_vlan: int = None,
        enc_key: str = None,
        encryption: str = None,
        fourth_auth_port: int = None,
        fourth_auth_secret: str = None,
        fourth_auth_server: str = None,
        ft_over_ds: int = None,
        hidden: str = None,
        id: int = None,
        ieee_80211r: int = None,
        ieee_80211w: str = None,
        ignore_weak_probe: int = None,
        isolate: str = None,
        lite_effect: bool = None,
        mac: str = None,
        max_inactivity: int = None,
        maxassoc: int = None,
        mobility_domain: str = None,
        multicast_forward: int = None,
        nasid: str = None,
        nd_proxy_work: int = None,
        network: int = None,
        ownip: str = None,
        radio_index: str = None,
        secondary_acct_port: int = None,
        secondary_acct_secret: str = None,
        secondary_acct_server: str = None,
        secondary_auth_port: int = None,
        secondary_auth_secret: str = None,
        secondary_auth_server: str = None,
        send_config_to_ap: bool = None,
        short_preamble: str = None,
        ssid: str = None,
        ssid_lb: int = None,
        third_auth_port: int = None,
        third_auth_secret: str = None,
        third_auth_server: str = None,
        type: int = None,
        vlan_dhcp: int = None,
        wmm: str = None,
    ):
        self.acct_port = acct_port
        self.acct_secret = acct_secret
        self.acct_server = acct_server
        self.acct_status_server_work = acct_status_server_work
        self.ap_asset_id = ap_asset_id
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.arp_proxy_enable = arp_proxy_enable
        # This parameter is required.
        self.auth_cache = auth_cache
        self.auth_port = auth_port
        self.auth_secret = auth_secret
        self.auth_server = auth_server
        self.auth_status_server_work = auth_status_server_work
        self.cir = cir
        self.cir_step = cir_step
        self.cir_type = cir_type
        self.cir_ul = cir_ul
        self.dae_client = dae_client
        self.dae_port = dae_port
        self.dae_secret = dae_secret
        # This parameter is required.
        self.disabled = disabled
        # This parameter is required.
        self.disassoc_low_ack = disassoc_low_ack
        # This parameter is required.
        self.disassoc_weak_rssi = disassoc_weak_rssi
        # This parameter is required.
        self.dynamic_vlan = dynamic_vlan
        self.enc_key = enc_key
        # This parameter is required.
        self.encryption = encryption
        self.fourth_auth_port = fourth_auth_port
        self.fourth_auth_secret = fourth_auth_secret
        self.fourth_auth_server = fourth_auth_server
        self.ft_over_ds = ft_over_ds
        # This parameter is required.
        self.hidden = hidden
        self.id = id
        self.ieee_80211r = ieee_80211r
        # This parameter is required.
        self.ieee_80211w = ieee_80211w
        self.ignore_weak_probe = ignore_weak_probe
        # This parameter is required.
        self.isolate = isolate
        self.lite_effect = lite_effect
        # This parameter is required.
        self.mac = mac
        # This parameter is required.
        self.max_inactivity = max_inactivity
        # This parameter is required.
        self.maxassoc = maxassoc
        self.mobility_domain = mobility_domain
        self.multicast_forward = multicast_forward
        self.nasid = nasid
        self.nd_proxy_work = nd_proxy_work
        # This parameter is required.
        self.network = network
        self.ownip = ownip
        # This parameter is required.
        self.radio_index = radio_index
        self.secondary_acct_port = secondary_acct_port
        self.secondary_acct_secret = secondary_acct_secret
        self.secondary_acct_server = secondary_acct_server
        self.secondary_auth_port = secondary_auth_port
        self.secondary_auth_secret = secondary_auth_secret
        self.secondary_auth_server = secondary_auth_server
        self.send_config_to_ap = send_config_to_ap
        # This parameter is required.
        self.short_preamble = short_preamble
        # This parameter is required.
        self.ssid = ssid
        # This parameter is required.
        self.ssid_lb = ssid_lb
        self.third_auth_port = third_auth_port
        self.third_auth_secret = third_auth_secret
        self.third_auth_server = third_auth_server
        self.type = type
        # This parameter is required.
        self.vlan_dhcp = vlan_dhcp
        # This parameter is required.
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

        if self.acct_status_server_work is not None:
            result['AcctStatusServerWork'] = self.acct_status_server_work

        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.arp_proxy_enable is not None:
            result['ArpProxyEnable'] = self.arp_proxy_enable

        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache

        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port

        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret

        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server

        if self.auth_status_server_work is not None:
            result['AuthStatusServerWork'] = self.auth_status_server_work

        if self.cir is not None:
            result['Cir'] = self.cir

        if self.cir_step is not None:
            result['CirStep'] = self.cir_step

        if self.cir_type is not None:
            result['CirType'] = self.cir_type

        if self.cir_ul is not None:
            result['CirUl'] = self.cir_ul

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

        if self.enc_key is not None:
            result['EncKey'] = self.enc_key

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.fourth_auth_port is not None:
            result['FourthAuthPort'] = self.fourth_auth_port

        if self.fourth_auth_secret is not None:
            result['FourthAuthSecret'] = self.fourth_auth_secret

        if self.fourth_auth_server is not None:
            result['FourthAuthServer'] = self.fourth_auth_server

        if self.ft_over_ds is not None:
            result['FtOverDs'] = self.ft_over_ds

        if self.hidden is not None:
            result['Hidden'] = self.hidden

        if self.id is not None:
            result['Id'] = self.id

        if self.ieee_80211r is not None:
            result['Ieee80211r'] = self.ieee_80211r

        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w

        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe

        if self.isolate is not None:
            result['Isolate'] = self.isolate

        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity

        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc

        if self.mobility_domain is not None:
            result['MobilityDomain'] = self.mobility_domain

        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward

        if self.nasid is not None:
            result['Nasid'] = self.nasid

        if self.nd_proxy_work is not None:
            result['NdProxyWork'] = self.nd_proxy_work

        if self.network is not None:
            result['Network'] = self.network

        if self.ownip is not None:
            result['Ownip'] = self.ownip

        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index

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

        if self.send_config_to_ap is not None:
            result['SendConfigToAp'] = self.send_config_to_ap

        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble

        if self.ssid is not None:
            result['Ssid'] = self.ssid

        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb

        if self.third_auth_port is not None:
            result['ThirdAuthPort'] = self.third_auth_port

        if self.third_auth_secret is not None:
            result['ThirdAuthSecret'] = self.third_auth_secret

        if self.third_auth_server is not None:
            result['ThirdAuthServer'] = self.third_auth_server

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

        if m.get('AcctStatusServerWork') is not None:
            self.acct_status_server_work = m.get('AcctStatusServerWork')

        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ArpProxyEnable') is not None:
            self.arp_proxy_enable = m.get('ArpProxyEnable')

        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')

        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')

        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')

        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')

        if m.get('AuthStatusServerWork') is not None:
            self.auth_status_server_work = m.get('AuthStatusServerWork')

        if m.get('Cir') is not None:
            self.cir = m.get('Cir')

        if m.get('CirStep') is not None:
            self.cir_step = m.get('CirStep')

        if m.get('CirType') is not None:
            self.cir_type = m.get('CirType')

        if m.get('CirUl') is not None:
            self.cir_ul = m.get('CirUl')

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

        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('FourthAuthPort') is not None:
            self.fourth_auth_port = m.get('FourthAuthPort')

        if m.get('FourthAuthSecret') is not None:
            self.fourth_auth_secret = m.get('FourthAuthSecret')

        if m.get('FourthAuthServer') is not None:
            self.fourth_auth_server = m.get('FourthAuthServer')

        if m.get('FtOverDs') is not None:
            self.ft_over_ds = m.get('FtOverDs')

        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ieee80211r') is not None:
            self.ieee_80211r = m.get('Ieee80211r')

        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')

        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')

        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')

        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')

        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')

        if m.get('MobilityDomain') is not None:
            self.mobility_domain = m.get('MobilityDomain')

        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')

        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')

        if m.get('NdProxyWork') is not None:
            self.nd_proxy_work = m.get('NdProxyWork')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')

        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')

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

        if m.get('SendConfigToAp') is not None:
            self.send_config_to_ap = m.get('SendConfigToAp')

        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')

        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')

        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')

        if m.get('ThirdAuthPort') is not None:
            self.third_auth_port = m.get('ThirdAuthPort')

        if m.get('ThirdAuthSecret') is not None:
            self.third_auth_secret = m.get('ThirdAuthSecret')

        if m.get('ThirdAuthServer') is not None:
            self.third_auth_server = m.get('ThirdAuthServer')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')

        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')

        return self

