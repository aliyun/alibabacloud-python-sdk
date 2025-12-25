# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudSdkServersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_servers: List[main_models.DescribeHybridCloudSdkServersResponseBodySdkServers] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sdk_servers = sdk_servers
        self.total_count = total_count

    def validate(self):
        if self.sdk_servers:
            for v1 in self.sdk_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SdkServers'] = []
        if self.sdk_servers is not None:
            for k1 in self.sdk_servers:
                result['SdkServers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sdk_servers = []
        if m.get('SdkServers') is not None:
            for k1 in m.get('SdkServers'):
                temp_model = main_models.DescribeHybridCloudSdkServersResponseBodySdkServers()
                self.sdk_servers.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudSdkServersResponseBodySdkServers(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        create_time: int = None,
        host_name: str = None,
        ip: str = None,
        mid: str = None,
        protection_group_address: str = None,
        pullin_status: str = None,
        resource_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.host_name = host_name
        self.ip = ip
        # SDKID。
        self.mid = mid
        self.protection_group_address = protection_group_address
        self.pullin_status = pullin_status
        self.resource_id = resource_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mid is not None:
            result['Mid'] = self.mid

        if self.protection_group_address is not None:
            result['ProtectionGroupAddress'] = self.protection_group_address

        if self.pullin_status is not None:
            result['PullinStatus'] = self.pullin_status

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        if m.get('ProtectionGroupAddress') is not None:
            self.protection_group_address = m.get('ProtectionGroupAddress')

        if m.get('PullinStatus') is not None:
            self.pullin_status = m.get('PullinStatus')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

