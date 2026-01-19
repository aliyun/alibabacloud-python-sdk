# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        add_vpcips: str = None,
        cache_size: int = None,
        charge_type: str = None,
        client_token: str = None,
        cluster_node_count: int = None,
        cluster_node_type: str = None,
        config_pattern_type: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        deploy_scheme: str = None,
        engine: str = None,
        engine_version: str = None,
        multi_zone: List[main_models.CreateDBInstanceRequestMultiZone] = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        scale_max: float = None,
        scale_min: float = None,
        security_iplist: str = None,
        tag: List[main_models.CreateDBInstanceRequestTag] = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to add the virtual private cloud (VPC) CIDR block to the IP address whitelist. Valid values:
        # 
        # *   1: yes.
        # *   0: no.
        self.add_vpcips = add_vpcips
        # The reserved cache size.
        # 
        # This parameter is required.
        self.cache_size = cache_size
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.cluster_node_count = cluster_node_count
        self.cluster_node_type = cluster_node_type
        self.config_pattern_type = config_pattern_type
        # The instance endpoint.
        self.connection_string = connection_string
        # The instance type. You can call the [DescribeAllDBInstanceClass](https://help.aliyun.com/document_detail/2853363.html) operation to query instance types.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The instance description.
        self.dbinstance_description = dbinstance_description
        # The deployment method of the instance.
        self.deploy_scheme = deploy_scheme
        # The database engine of the instance. Default value: **selectdb**.
        self.engine = engine
        # The database engine version of the instance. Default value: **3.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The configurations of multi-zone deployment.
        # 
        # > 
        # 
        # *   This parameter takes effect and is required only when DeployScheme is set to multi_az.
        self.multi_zone = multi_zone
        # The unit of the subscription duration of the cluster. Valid values:
        # 
        # *   **Year**: subscription on a yearly basis.
        # *   **Month**: subscription on a monthly basis.
        # 
        # >  This parameter takes effect and is required only when **ChargeType** is set to **Prepaid**.
        self.period = period
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.scale_max = scale_max
        self.scale_min = scale_min
        # The IP addresses in the whitelist of the instance. Separate multiple IP addresses with commas (,).
        self.security_iplist = security_iplist
        # The instance tags.
        self.tag = tag
        # The subscription duration of the instance. Valid values:
        # 
        # *   If Period is set to Year, valid values of UsedTime are 1, 2, 3, 4, and 5.
        # *   If Period is set to Month, valid values of UsedTime are 1 to 12.
        # 
        # >  This parameter takes effect and is required only when **ChargeType** is set to **Prepaid**.
        self.used_time = used_time
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.multi_zone:
            for v1 in self.multi_zone:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_vpcips is not None:
            result['AddVPCIPs'] = self.add_vpcips

        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_node_count is not None:
            result['ClusterNodeCount'] = self.cluster_node_count

        if self.cluster_node_type is not None:
            result['ClusterNodeType'] = self.cluster_node_type

        if self.config_pattern_type is not None:
            result['ConfigPatternType'] = self.config_pattern_type

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.deploy_scheme is not None:
            result['DeployScheme'] = self.deploy_scheme

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['MultiZone'] = []
        if self.multi_zone is not None:
            for k1 in self.multi_zone:
                result['MultiZone'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVPCIPs') is not None:
            self.add_vpcips = m.get('AddVPCIPs')

        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterNodeCount') is not None:
            self.cluster_node_count = m.get('ClusterNodeCount')

        if m.get('ClusterNodeType') is not None:
            self.cluster_node_type = m.get('ClusterNodeType')

        if m.get('ConfigPatternType') is not None:
            self.config_pattern_type = m.get('ConfigPatternType')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DeployScheme') is not None:
            self.deploy_scheme = m.get('DeployScheme')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.multi_zone = []
        if m.get('MultiZone') is not None:
            for k1 in m.get('MultiZone'):
                temp_model = main_models.CreateDBInstanceRequestMultiZone()
                self.multi_zone.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class CreateDBInstanceRequestMultiZone(DaraModel):
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

