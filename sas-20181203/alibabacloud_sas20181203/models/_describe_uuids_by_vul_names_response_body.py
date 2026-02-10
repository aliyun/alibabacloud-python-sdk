# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUuidsByVulNamesResponseBody(DaraModel):
    def __init__(
        self,
        machine_info_statistics: List[main_models.DescribeUuidsByVulNamesResponseBodyMachineInfoStatistics] = None,
        request_id: str = None,
        vul_count: int = None,
    ):
        # The statistics about the servers.
        self.machine_info_statistics = machine_info_statistics
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of vulnerabilities on the server.
        self.vul_count = vul_count

    def validate(self):
        if self.machine_info_statistics:
            for v1 in self.machine_info_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineInfoStatistics'] = []
        if self.machine_info_statistics is not None:
            for k1 in self.machine_info_statistics:
                result['MachineInfoStatistics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_info_statistics = []
        if m.get('MachineInfoStatistics') is not None:
            for k1 in m.get('MachineInfoStatistics'):
                temp_model = main_models.DescribeUuidsByVulNamesResponseBodyMachineInfoStatistics()
                self.machine_info_statistics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

class DescribeUuidsByVulNamesResponseBodyMachineInfoStatistics(DaraModel):
    def __init__(
        self,
        internet_ip: str = None,
        intranet_ip: str = None,
        machine_instance_id: str = None,
        machine_ip: str = None,
        machine_name: str = None,
        os: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # The public IP address of the server on which the exception was detected.
        self.internet_ip = internet_ip
        # The private IP address of the server on which the exception was detected.
        self.intranet_ip = intranet_ip
        # The instance ID of the server.
        self.machine_instance_id = machine_instance_id
        # The IP address of the server.
        self.machine_ip = machine_ip
        # The name of the server.
        self.machine_name = machine_name
        # The operating system that the server runs.
        self.os = os
        # The region ID of the server.
        self.region_id = region_id
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.machine_instance_id is not None:
            result['MachineInstanceId'] = self.machine_instance_id

        if self.machine_ip is not None:
            result['MachineIp'] = self.machine_ip

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.os is not None:
            result['Os'] = self.os

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MachineInstanceId') is not None:
            self.machine_instance_id = m.get('MachineInstanceId')

        if m.get('MachineIp') is not None:
            self.machine_ip = m.get('MachineIp')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

