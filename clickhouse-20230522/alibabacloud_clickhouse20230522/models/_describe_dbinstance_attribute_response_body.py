# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceAttributeResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceAttributeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceAttributeResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        bid: str = None,
        category: str = None,
        charge_type: str = None,
        click_observe_service_status: str = None,
        create_time: str = None,
        dbinstance_id: str = None,
        deletion_protection: bool = None,
        deploy_schema: str = None,
        description: str = None,
        disabled_ports: str = None,
        engine: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        latest_engine_minor_version: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        multi_zones: List[main_models.DescribeDBInstanceAttributeResponseBodyDataMultiZones] = None,
        node_count: str = None,
        node_scale_max: str = None,
        node_scale_min: str = None,
        nodes: List[main_models.DescribeDBInstanceAttributeResponseBodyDataNodes] = None,
        object_store_size: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        status: str = None,
        storage_quota: str = None,
        storage_size: int = None,
        storage_type: str = None,
        tags: List[main_models.DescribeDBInstanceAttributeResponseBodyDataTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The channel ID.
        self.bid = bid
        self.category = category
        # The billing method. Enterprise Edition clusters use the pay-as-you-go billing method.
        self.charge_type = charge_type
        self.click_observe_service_status = click_observe_service_status
        # The time when the cluster was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether the release protection feature is enabled for the cluster.
        self.deletion_protection = deletion_protection
        # The deployment mode of the cluster. Valid values: single_az and multi_az.
        # 
        # *   single_az: indicates that the server nodes are deployed in the primary zone. The ID of the primary zone is specified by the ZoneID parameter.
        # *   multi_az: indicates that the server nodes are deployed in multiple zones. The information about the zones is specified by the MultiZones parameter.
        # 
        # The keeper nodes are deployed in multiple zones.
        self.deploy_schema = deploy_schema
        # The cluster description.
        self.description = description
        # The disabled database ports. Multiple database ports are separated by commas (,).
        self.disabled_ports = disabled_ports
        # The engine type.
        self.engine = engine
        # The minor engine version of the cluster.
        self.engine_minor_version = engine_minor_version
        # The engine version.
        self.engine_version = engine_version
        # The time when the cluster expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # >  Pay-as-you-go clusters never expire. If the cluster is a pay-as-you-go cluster, an empty string is returned for this parameter.
        self.expire_time = expire_time
        # The latest minor engine version.
        self.latest_engine_minor_version = latest_engine_minor_version
        # The lock mode of the cluster.
        self.lock_mode = lock_mode
        # The reason why the cluster was locked.
        self.lock_reason = lock_reason
        # The end time of the maintenance window.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        self.maintain_start_time = maintain_start_time
        # The information about the zones.
        self.multi_zones = multi_zones
        self.node_count = node_count
        self.node_scale_max = node_scale_max
        self.node_scale_min = node_scale_min
        # The nodes.
        self.nodes = nodes
        # The size of the object storage space.
        self.object_store_size = object_store_size
        # The region ID.
        self.region_id = region_id
        # The resource ID.
        self.resource_group_id = resource_group_id
        # The maximum capacity for elastic scaling.
        self.scale_max = scale_max
        # The minimum capacity for elastic scaling.
        self.scale_min = scale_min
        # The cluster status.
        self.status = status
        self.storage_quota = storage_quota
        # The size of the storage space. Unit: GB.
        self.storage_size = storage_size
        # The storage type.
        self.storage_type = storage_type
        # The details of the tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.multi_zones:
            for v1 in self.multi_zones:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.category is not None:
            result['Category'] = self.category

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.click_observe_service_status is not None:
            result['ClickObserveServiceStatus'] = self.click_observe_service_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deploy_schema is not None:
            result['DeploySchema'] = self.deploy_schema

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled_ports is not None:
            result['DisabledPorts'] = self.disabled_ports

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.latest_engine_minor_version is not None:
            result['LatestEngineMinorVersion'] = self.latest_engine_minor_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        result['MultiZones'] = []
        if self.multi_zones is not None:
            for k1 in self.multi_zones:
                result['MultiZones'].append(k1.to_map() if k1 else None)

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max

        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClickObserveServiceStatus') is not None:
            self.click_observe_service_status = m.get('ClickObserveServiceStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploySchema') is not None:
            self.deploy_schema = m.get('DeploySchema')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisabledPorts') is not None:
            self.disabled_ports = m.get('DisabledPorts')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('LatestEngineMinorVersion') is not None:
            self.latest_engine_minor_version = m.get('LatestEngineMinorVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        self.multi_zones = []
        if m.get('MultiZones') is not None:
            for k1 in m.get('MultiZones'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDataMultiZones()
                self.multi_zones.append(temp_model.from_map(k1))

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')

        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDBInstanceAttributeResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

class DescribeDBInstanceAttributeResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        node_status: str = None,
        zone_id: str = None,
    ):
        # The node status.
        self.node_status = node_status
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBInstanceAttributeResponseBodyDataMultiZones(DaraModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

