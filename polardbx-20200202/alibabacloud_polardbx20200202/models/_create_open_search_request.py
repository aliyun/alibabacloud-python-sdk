# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOpenSearchRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        client_token: str = None,
        dbinstance_description: str = None,
        dbnode_class: str = None,
        engine_version: str = None,
        instance_spec: str = None,
        node_count: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_space: int = None,
        storage_type: str = None,
        topology_type: str = None,
        used_time: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_2: str = None,
        zone_3: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. Default value: true.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.auto_renew = auto_renew
        # The client token used to ensure the idempotence of the request. Use a different value for each creation request.
        self.client_token = client_token
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The node specifications code of PolarDBX Search data nodes. Available specifications depend on the region and sales configuration. Use a PolarDBX Search specification code that is available for purchase in the current region.
        # 
        # This parameter is required.
        self.dbnode_class = dbnode_class
        # The PolarDBX Search DPI engine version. The value is fixed to 3.0. If this parameter is not specified, the default value 3.0 is used.
        self.engine_version = engine_version
        # A compatible parameter that does not take effect. Use DBNodeClass to specify the PolarDBX Search data node specifications.
        self.instance_spec = instance_spec
        # The number of PolarDBX Search data nodes. The value must be a positive integer and a multiple of the number of selected zones.
        # 
        # This parameter is required.
        self.node_count = node_count
        # The billing method of the instance.
        # 
        # - **PREPAY**: subscription.
        # - **POSTPAY**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle. Valid values for subscription: Year and Month. Default value for pay-as-you-go: Hour.
        self.period = period
        # The region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. This parameter can be left empty. This parameter is not supported.
        self.resource_group_id = resource_group_id
        # The storage space per node, in GB. The value must be a positive integer.
        self.storage_space = storage_space
        # The storage type. Default value: cloud_auto.
        self.storage_type = storage_type
        # The topology type. Valid values:
        # 
        # - **1azone**: single active zone.
        # - **3azones**: three active zones.
        self.topology_type = topology_type
        # The subscription duration. Specify the number of months or years for prepaid instances.
        # 
        # > When Period is set to Year, valid values for this parameter are 1, 2, and 3.
        self.used_time = used_time
        # VPC ID。
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The second zone. This parameter is required when TopologyType is set to 3azones. The value cannot be the same as other zones.
        self.zone_2 = zone_2
        # The third zone. This parameter is required when TopologyType is set to 3azones. The value cannot be the same as other zones.
        self.zone_3 = zone_3
        # The zone of the instance.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_2 is not None:
            result['Zone2'] = self.zone_2

        if self.zone_3 is not None:
            result['Zone3'] = self.zone_3

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Zone2') is not None:
            self.zone_2 = m.get('Zone2')

        if m.get('Zone3') is not None:
            self.zone_3 = m.get('Zone3')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

