# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudwifi_pop20191118 import models as main_models
from darabonba.model import DaraModel

class UpdateNetDeviceInfoRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        devices: List[main_models.UpdateNetDeviceInfoRequestDevices] = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        # This parameter is required.
        self.devices = devices
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for v1 in self.devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['Devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['Devices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.UpdateNetDeviceInfoRequestDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateNetDeviceInfoRequestDevices(DaraModel):
    def __init__(
        self,
        host_name: str = None,
        id: int = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        password: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.host_name = host_name
        # This parameter is required.
        self.id = id
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        # This parameter is required.
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.password = password
        self.role = role
        # This parameter is required.
        self.service_tag = service_tag
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.password is not None:
            result['Password'] = self.password

        if self.role is not None:
            result['Role'] = self.role

        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

