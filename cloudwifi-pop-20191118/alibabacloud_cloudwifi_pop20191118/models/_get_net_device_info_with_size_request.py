# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetDeviceInfoWithSizeRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        host_name: str = None,
        id: int = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        page_size: int = None,
        password: str = None,
        request_id: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.host_name = host_name
        self.id = id
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.page_size = page_size
        self.password = password
        # This parameter is required.
        self.request_id = request_id
        self.role = role
        self.service_tag = service_tag
        self.username = username

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

        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.id is not None:
            result['Id'] = self.id

        if self.idc is not None:
            result['Idc'] = self.idc

        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod

        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer

        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip

        if self.model is not None:
            result['Model'] = self.model

        if self.net_pod is not None:
            result['NetPod'] = self.net_pod

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.password is not None:
            result['Password'] = self.password

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role

        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Idc') is not None:
            self.idc = m.get('Idc')

        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')

        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')

        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

