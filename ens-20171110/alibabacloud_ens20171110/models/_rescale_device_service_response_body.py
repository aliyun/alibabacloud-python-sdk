# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class RescaleDeviceServiceResponseBody(DaraModel):
    def __init__(
        self,
        device_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
        resource_detail_infos: List[main_models.RescaleDeviceServiceResponseBodyResourceDetailInfos] = None,
    ):
        # The IDs of the devices.
        self.device_ids = device_ids
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The key properties of the device.
        self.resource_detail_infos = resource_detail_infos

    def validate(self):
        if self.resource_detail_infos:
            for v1 in self.resource_detail_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceDetailInfos'] = []
        if self.resource_detail_infos is not None:
            for k1 in self.resource_detail_infos:
                result['ResourceDetailInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_detail_infos = []
        if m.get('ResourceDetailInfos') is not None:
            for k1 in m.get('ResourceDetailInfos'):
                temp_model = main_models.RescaleDeviceServiceResponseBodyResourceDetailInfos()
                self.resource_detail_infos.append(temp_model.from_map(k1))

        return self

class RescaleDeviceServiceResponseBodyResourceDetailInfos(DaraModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        isp: str = None,
        mac: str = None,
        region_id: str = None,
        server: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the device.
        self.id = id
        # The IP address of the device.
        self.ip = ip
        # The Internet service provider (ISP) to which the device belongs.
        self.isp = isp
        # The media access control (MAC) address of the device.
        self.mac = mac
        # The ID of the edge node to which the device belongs.
        self.region_id = region_id
        # The name of the server on which the device is deployed.
        self.server = server
        # The status of the device.
        self.status = status
        # The type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['ID'] = self.id

        if self.ip is not None:
            result['IP'] = self.ip

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.server is not None:
            result['Server'] = self.server

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

