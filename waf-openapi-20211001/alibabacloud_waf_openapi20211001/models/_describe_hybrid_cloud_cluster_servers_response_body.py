# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudClusterServersResponseBody(DaraModel):
    def __init__(
        self,
        cluster_servers: List[main_models.DescribeHybridCloudClusterServersResponseBodyClusterServers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The result list.
        self.cluster_servers = cluster_servers
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cluster_servers:
            for v1 in self.cluster_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterServers'] = []
        if self.cluster_servers is not None:
            for k1 in self.cluster_servers:
                result['ClusterServers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_servers = []
        if m.get('ClusterServers') is not None:
            for k1 in m.get('ClusterServers'):
                temp_model = main_models.DescribeHybridCloudClusterServersResponseBodyClusterServers()
                self.cluster_servers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudClusterServersResponseBodyClusterServers(DaraModel):
    def __init__(
        self,
        continents: str = None,
        continents_value: int = None,
        cpu: int = None,
        create_timestamp: int = None,
        custom_name: str = None,
        group_id: int = None,
        group_name: str = None,
        group_type: str = None,
        host_name: str = None,
        ip: str = None,
        job_status: str = None,
        mac: str = None,
        memory: int = None,
        mid: str = None,
        operator: str = None,
        operator_value: int = None,
        region_code: str = None,
        region_code_value: int = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        # The continent.
        self.continents = continents
        # The continent code of the protection cluster.
        # 
        # > For the list of code values, see the supplementary description of response parameters.
        self.continents_value = continents_value
        # The number of CPU cores.
        self.cpu = cpu
        # The creation timestamp, in milliseconds.
        self.create_timestamp = create_timestamp
        # The node name.
        self.custom_name = custom_name
        # The node group ID.
        self.group_id = group_id
        # The name of the node group.
        self.group_name = group_name
        # The type of the hybrid cloud node group. Valid values:
        # 
        # - **protect**: protection.
        # 
        # - **control**: management.
        # 
        # - **storage**: storage.
        # 
        # - **controlStorage**: management and storage.
        self.group_type = group_type
        # The hostname.
        self.host_name = host_name
        # The IP address.
        self.ip = ip
        # The running status of the machine.
        self.job_status = job_status
        # The MAC address.
        self.mac = mac
        # The memory data.
        self.memory = memory
        # The machine identifier (MID).
        self.mid = mid
        # The cloud service provider.
        self.operator = operator
        # The operator value.
        self.operator_value = operator_value
        # The region name.
        self.region_code = region_code
        # The region code.
        self.region_code_value = region_code_value
        # The machine status.
        self.status = status
        # The last update timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continents is not None:
            result['Continents'] = self.continents

        if self.continents_value is not None:
            result['ContinentsValue'] = self.continents_value

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.custom_name is not None:
            result['CustomName'] = self.custom_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.mid is not None:
            result['Mid'] = self.mid

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_value is not None:
            result['OperatorValue'] = self.operator_value

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_code_value is not None:
            result['RegionCodeValue'] = self.region_code_value

        if self.status is not None:
            result['Status'] = self.status

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Continents') is not None:
            self.continents = m.get('Continents')

        if m.get('ContinentsValue') is not None:
            self.continents_value = m.get('ContinentsValue')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorValue') is not None:
            self.operator_value = m.get('OperatorValue')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionCodeValue') is not None:
            self.region_code_value = m.get('RegionCodeValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

