# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeTairKVCacheInferInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstances = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTairKVCacheInferInstanceAttributeResponseBodyInstances(DaraModel):
    def __init__(
        self,
        dbinstance_attribute: List[main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttribute] = None,
    ):
        self.dbinstance_attribute = dbinstance_attribute

    def validate(self):
        if self.dbinstance_attribute:
            for v1 in self.dbinstance_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k1 in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k1 in m.get('DBInstanceAttribute'):
                temp_model = main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttribute(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        charge_type: str = None,
        compute_unit_num: int = None,
        connection_string: str = None,
        create_time: str = None,
        end_time: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        is_delete: int = None,
        is_order_completed: str = None,
        model: str = None,
        model_service_num: int = None,
        network_type: str = None,
        private_ip: str = None,
        region_id: str = None,
        replica_num: str = None,
        resource_group_id: str = None,
        storage: int = None,
        tags: main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        zone_type: str = None,
    ):
        self.architecture_type = architecture_type
        self.charge_type = charge_type
        self.compute_unit_num = compute_unit_num
        self.connection_string = connection_string
        self.create_time = create_time
        self.end_time = end_time
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.is_delete = is_delete
        self.is_order_completed = is_order_completed
        self.model = model
        self.model_service_num = model_service_num
        self.network_type = network_type
        self.private_ip = private_ip
        self.region_id = region_id
        self.replica_num = replica_num
        self.resource_group_id = resource_group_id
        self.storage = storage
        self.tags = tags
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id
        self.zone_type = zone_type

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.compute_unit_num is not None:
            result['ComputeUnitNum'] = self.compute_unit_num

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.is_order_completed is not None:
            result['IsOrderCompleted'] = self.is_order_completed

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

        if self.replica_num is not None:
            result['ReplicaNum'] = self.replica_num

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ComputeUnitNum') is not None:
            self.compute_unit_num = m.get('ComputeUnitNum')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('IsOrderCompleted') is not None:
            self.is_order_completed = m.get('IsOrderCompleted')

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

        if m.get('ReplicaNum') is not None:
            self.replica_num = m.get('ReplicaNum')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag] = None,
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
                temp_model = main_models.DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeTairKVCacheInferInstanceAttributeResponseBodyInstancesDBInstanceAttributeTagsTag(DaraModel):
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

