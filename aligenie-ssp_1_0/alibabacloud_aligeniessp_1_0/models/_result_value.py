# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ResultValue(DaraModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[main_models.ResultValueDeviceUnionIds] = None,
        name: str = None,
        firmware_version: str = None,
        mac: str = None,
        sn: str = None,
    ):
        # The openId corresponding to the device.
        self.device_open_id = device_open_id
        # The organization ID and UnionId information corresponding to the device.
        self.device_union_ids = device_union_ids
        # The name of the device.
        self.name = name
        # The firmware version of the device.
        self.firmware_version = firmware_version
        # The MAC address of the device.
        self.mac = mac
        # The SN information of the device.
        self.sn = sn

    def validate(self):
        if self.device_union_ids:
            for v1 in self.device_union_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k1 in self.device_union_ids:
                result['DeviceUnionIds'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k1 in m.get('DeviceUnionIds'):
                temp_model = main_models.ResultValueDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self



class ResultValueDeviceUnionIds(DaraModel):
    def __init__(
        self,
        organization_id: str = None,
        device_union_id: str = None,
    ):
        # The organization ID.
        self.organization_id = organization_id
        # The UnionId of the device.
        self.device_union_id = device_union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')

        return self

