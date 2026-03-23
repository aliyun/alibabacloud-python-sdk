# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveApBasicConfigRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        country: str = None,
        dai: str = None,
        description: str = None,
        echo_int: int = None,
        failover: int = None,
        id: int = None,
        insecure_allowed: int = None,
        lan_ip: str = None,
        lan_mask: str = None,
        lan_status: int = None,
        log_ip: str = None,
        log_level: int = None,
        name: str = None,
        passwd: str = None,
        protocol: str = None,
        route: str = None,
        scan: int = None,
        token_server: str = None,
        vpn: str = None,
        work_mode: int = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.country = country
        self.dai = dai
        self.description = description
        # This parameter is required.
        self.echo_int = echo_int
        self.failover = failover
        # This parameter is required.
        self.id = id
        self.insecure_allowed = insecure_allowed
        self.lan_ip = lan_ip
        self.lan_mask = lan_mask
        self.lan_status = lan_status
        self.log_ip = log_ip
        self.log_level = log_level
        # This parameter is required.
        self.name = name
        self.passwd = passwd
        self.protocol = protocol
        self.route = route
        self.scan = scan
        self.token_server = token_server
        self.vpn = vpn
        self.work_mode = work_mode

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

        if self.country is not None:
            result['Country'] = self.country

        if self.dai is not None:
            result['Dai'] = self.dai

        if self.description is not None:
            result['Description'] = self.description

        if self.echo_int is not None:
            result['EchoInt'] = self.echo_int

        if self.failover is not None:
            result['Failover'] = self.failover

        if self.id is not None:
            result['Id'] = self.id

        if self.insecure_allowed is not None:
            result['InsecureAllowed'] = self.insecure_allowed

        if self.lan_ip is not None:
            result['LanIp'] = self.lan_ip

        if self.lan_mask is not None:
            result['LanMask'] = self.lan_mask

        if self.lan_status is not None:
            result['LanStatus'] = self.lan_status

        if self.log_ip is not None:
            result['LogIp'] = self.log_ip

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.name is not None:
            result['Name'] = self.name

        if self.passwd is not None:
            result['Passwd'] = self.passwd

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.route is not None:
            result['Route'] = self.route

        if self.scan is not None:
            result['Scan'] = self.scan

        if self.token_server is not None:
            result['TokenServer'] = self.token_server

        if self.vpn is not None:
            result['Vpn'] = self.vpn

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Dai') is not None:
            self.dai = m.get('Dai')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EchoInt') is not None:
            self.echo_int = m.get('EchoInt')

        if m.get('Failover') is not None:
            self.failover = m.get('Failover')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InsecureAllowed') is not None:
            self.insecure_allowed = m.get('InsecureAllowed')

        if m.get('LanIp') is not None:
            self.lan_ip = m.get('LanIp')

        if m.get('LanMask') is not None:
            self.lan_mask = m.get('LanMask')

        if m.get('LanStatus') is not None:
            self.lan_status = m.get('LanStatus')

        if m.get('LogIp') is not None:
            self.log_ip = m.get('LogIp')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Route') is not None:
            self.route = m.get('Route')

        if m.get('Scan') is not None:
            self.scan = m.get('Scan')

        if m.get('TokenServer') is not None:
            self.token_server = m.get('TokenServer')

        if m.get('Vpn') is not None:
            self.vpn = m.get('Vpn')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

