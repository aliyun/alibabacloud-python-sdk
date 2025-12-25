# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudUnassignedMachinesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        unassigned_machines: List[main_models.DescribeHybridCloudUnassignedMachinesResponseBodyUnassignedMachines] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The servers that are not assigned to the hybrid cloud cluster.
        self.unassigned_machines = unassigned_machines

    def validate(self):
        if self.unassigned_machines:
            for v1 in self.unassigned_machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UnassignedMachines'] = []
        if self.unassigned_machines is not None:
            for k1 in self.unassigned_machines:
                result['UnassignedMachines'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.unassigned_machines = []
        if m.get('UnassignedMachines') is not None:
            for k1 in m.get('UnassignedMachines'):
                temp_model = main_models.DescribeHybridCloudUnassignedMachinesResponseBodyUnassignedMachines()
                self.unassigned_machines.append(temp_model.from_map(k1))

        return self

class DescribeHybridCloudUnassignedMachinesResponseBodyUnassignedMachines(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        custom_name: str = None,
        host_name: str = None,
        ip: str = None,
        mac: str = None,
        memory: int = None,
        mid: str = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The name of the node.
        self.custom_name = custom_name
        # The host name.
        self.host_name = host_name
        # The IP address of the server.
        self.ip = ip
        # The media access control (MAC) address of the device.
        self.mac = mac
        # The memory size. Unit: KB. A conversion factor of 1,000 is used.
        self.memory = memory
        # The ID of the node.
        self.mid = mid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_name is not None:
            result['CustomName'] = self.custom_name

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.mid is not None:
            result['Mid'] = self.mid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        return self

