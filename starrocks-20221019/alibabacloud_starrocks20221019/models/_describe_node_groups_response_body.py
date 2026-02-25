# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.DescribeNodeGroupsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeNodeGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeNodeGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        architecture: str = None,
        begin_time: int = None,
        billing_instance_id: str = None,
        commodity_code: str = None,
        component_type: str = None,
        cu: int = None,
        default_group: bool = None,
        description: str = None,
        disk_number: int = None,
        elastic_node_number: int = None,
        enable_public_network: bool = None,
        endpoint: str = None,
        expire_time: int = None,
        http_port: int = None,
        instance_id: str = None,
        local_storage_instance_type: str = None,
        memory_cpu_ratio: int = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_info: List[main_models.DescribeNodeGroupsResponseBodyDataNodeInfo] = None,
        pay_type: str = None,
        public_address: str = None,
        region_id: str = None,
        resident_node_number: int = None,
        running_time: int = None,
        spec_type: str = None,
        status: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
        tags: List[main_models.DescribeNodeGroupsResponseBodyDataTags] = None,
        target_elastic_node_number: int = None,
        zone_id: str = None,
    ):
        self.account_status = account_status
        self.architecture = architecture
        self.begin_time = begin_time
        self.billing_instance_id = billing_instance_id
        self.commodity_code = commodity_code
        self.component_type = component_type
        self.cu = cu
        self.default_group = default_group
        self.description = description
        self.disk_number = disk_number
        self.elastic_node_number = elastic_node_number
        self.enable_public_network = enable_public_network
        self.endpoint = endpoint
        self.expire_time = expire_time
        self.http_port = http_port
        self.instance_id = instance_id
        self.local_storage_instance_type = local_storage_instance_type
        self.memory_cpu_ratio = memory_cpu_ratio
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_info = node_info
        self.pay_type = pay_type
        self.public_address = public_address
        self.region_id = region_id
        self.resident_node_number = resident_node_number
        self.running_time = running_time
        self.spec_type = spec_type
        self.status = status
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size
        self.tags = tags
        self.target_elastic_node_number = target_elastic_node_number
        self.zone_id = zone_id

    def validate(self):
        if self.node_info:
            for v1 in self.node_info:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.default_group is not None:
            result['DefaultGroup'] = self.default_group

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_number is not None:
            result['DiskNumber'] = self.disk_number

        if self.elastic_node_number is not None:
            result['ElasticNodeNumber'] = self.elastic_node_number

        if self.enable_public_network is not None:
            result['EnablePublicNetwork'] = self.enable_public_network

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.local_storage_instance_type is not None:
            result['LocalStorageInstanceType'] = self.local_storage_instance_type

        if self.memory_cpu_ratio is not None:
            result['MemoryCpuRatio'] = self.memory_cpu_ratio

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        result['NodeInfo'] = []
        if self.node_info is not None:
            for k1 in self.node_info:
                result['NodeInfo'].append(k1.to_map() if k1 else None)

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.public_address is not None:
            result['PublicAddress'] = self.public_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resident_node_number is not None:
            result['ResidentNodeNumber'] = self.resident_node_number

        if self.running_time is not None:
            result['RunningTime'] = self.running_time

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_performance_level is not None:
            result['StoragePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.target_elastic_node_number is not None:
            result['TargetElasticNodeNumber'] = self.target_elastic_node_number

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('DefaultGroup') is not None:
            self.default_group = m.get('DefaultGroup')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskNumber') is not None:
            self.disk_number = m.get('DiskNumber')

        if m.get('ElasticNodeNumber') is not None:
            self.elastic_node_number = m.get('ElasticNodeNumber')

        if m.get('EnablePublicNetwork') is not None:
            self.enable_public_network = m.get('EnablePublicNetwork')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LocalStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('LocalStorageInstanceType')

        if m.get('MemoryCpuRatio') is not None:
            self.memory_cpu_ratio = m.get('MemoryCpuRatio')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k1 in m.get('NodeInfo'):
                temp_model = main_models.DescribeNodeGroupsResponseBodyDataNodeInfo()
                self.node_info.append(temp_model.from_map(k1))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PublicAddress') is not None:
            self.public_address = m.get('PublicAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResidentNodeNumber') is not None:
            self.resident_node_number = m.get('ResidentNodeNumber')

        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoragePerformanceLevel') is not None:
            self.storage_performance_level = m.get('StoragePerformanceLevel')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeNodeGroupsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TargetElasticNodeNumber') is not None:
            self.target_elastic_node_number = m.get('TargetElasticNodeNumber')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNodeGroupsResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeNodeGroupsResponseBodyDataNodeInfo(DaraModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

