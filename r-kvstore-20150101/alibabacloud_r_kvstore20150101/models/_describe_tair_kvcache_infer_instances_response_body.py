# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeTairKVCacheInferInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeTairKVCacheInferInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned records.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeTairKVCacheInferInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTairKVCacheInferInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        tair_infer_instance_dto: List[main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTO] = None,
    ):
        self.tair_infer_instance_dto = tair_infer_instance_dto

    def validate(self):
        if self.tair_infer_instance_dto:
            for v1 in self.tair_infer_instance_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TairInferInstanceDTO'] = []
        if self.tair_infer_instance_dto is not None:
            for k1 in self.tair_infer_instance_dto:
                result['TairInferInstanceDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tair_infer_instance_dto = []
        if m.get('TairInferInstanceDTO') is not None:
            for k1 in m.get('TairInferInstanceDTO'):
                temp_model = main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTO()
                self.tair_infer_instance_dto.append(temp_model.from_map(k1))

        return self

class DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTO(DaraModel):
    def __init__(
        self,
        ack_id: str = None,
        capacity: int = None,
        charge_type: str = None,
        compute_unit_num: int = None,
        create_time: str = None,
        destroy_time: str = None,
        elastic_vnode_count: int = None,
        end_time: str = None,
        fixed_vnode_count: int = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        model: str = None,
        model_service_num: int = None,
        network_type: str = None,
        private_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTags = None,
        vnode_count: int = None,
        vnode_name: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.ack_id = ack_id
        self.capacity = capacity
        self.charge_type = charge_type
        self.compute_unit_num = compute_unit_num
        self.create_time = create_time
        self.destroy_time = destroy_time
        self.elastic_vnode_count = elastic_vnode_count
        self.end_time = end_time
        self.fixed_vnode_count = fixed_vnode_count
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.model = model
        self.model_service_num = model_service_num
        self.network_type = network_type
        self.private_ip = private_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.vnode_count = vnode_count
        self.vnode_name = vnode_name
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_id is not None:
            result['AckId'] = self.ack_id

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.compute_unit_num is not None:
            result['ComputeUnitNum'] = self.compute_unit_num

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time

        if self.elastic_vnode_count is not None:
            result['ElasticVNodeCount'] = self.elastic_vnode_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fixed_vnode_count is not None:
            result['FixedVNodeCount'] = self.fixed_vnode_count

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.model is not None:
            result['Model'] = self.model

        if self.model_service_num is not None:
            result['ModelServiceNum'] = self.model_service_num

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vnode_count is not None:
            result['VNodeCount'] = self.vnode_count

        if self.vnode_name is not None:
            result['VNodeName'] = self.vnode_name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckId') is not None:
            self.ack_id = m.get('AckId')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ComputeUnitNum') is not None:
            self.compute_unit_num = m.get('ComputeUnitNum')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')

        if m.get('ElasticVNodeCount') is not None:
            self.elastic_vnode_count = m.get('ElasticVNodeCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FixedVNodeCount') is not None:
            self.fixed_vnode_count = m.get('FixedVNodeCount')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelServiceNum') is not None:
            self.model_service_num = m.get('ModelServiceNum')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VNodeCount') is not None:
            self.vnode_count = m.get('VNodeCount')

        if m.get('VNodeName') is not None:
            self.vnode_name = m.get('VNodeName')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeTairKVCacheInferInstancesResponseBodyInstancesTairInferInstanceDTOTagsTag(DaraModel):
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

