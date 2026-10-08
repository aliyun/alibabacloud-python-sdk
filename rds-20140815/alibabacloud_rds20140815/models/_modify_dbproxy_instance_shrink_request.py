# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBProxyInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_num: str = None,
        dbproxy_instance_type: str = None,
        dbproxy_nodes_shrink: str = None,
        effective_specific_time: str = None,
        effective_time: str = None,
        migrate_azshrink: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_ids: str = None,
    ):
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A deprecated parameter. You do not need to configure this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The number of proxy instances. If this parameter is set to 0, the proxy service of this type is disabled for the instance. Valid values: **1** to **16**.
        # > More proxy instances can handle more requests. You can check the load of proxy instances based on monitoring data and then specify an appropriate number of proxy instances.
        # 
        # This parameter is required.
        self.dbproxy_instance_num = dbproxy_instance_num
        # The type of the database proxy instance. Valid values:
        # - **common**: general-purpose database proxy
        # - **exclusive**: dedicated database proxy (default)
        # 
        # This parameter is required.
        self.dbproxy_instance_type = dbproxy_instance_type
        # The list of proxy nodes.
        # > This parameter is required when the current proxy instance uses multi-active zone deployment.
        self.dbproxy_nodes_shrink = dbproxy_nodes_shrink
        # The specified time for the modification to take effect. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > This parameter is required when **EffectiveTime** is set to **SpecificTime**.
        self.effective_specific_time = effective_specific_time
        # The effective period. Valid values:
        # 
        # * **Immediate**: The modification takes effect immediately.
        # * **MaintainTime**: The modification takes effect during the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # * **SpecificTime**: The modification takes effect at a specified time.
        # 
        # Default value: **MaintainTime**.
        self.effective_time = effective_time
        # The list of active zones for proxy migration.
        # > Currently, only ApsaraDB RDS for MySQL proxy instances with cloud disks support active zone migration.
        self.migrate_azshrink = migrate_azshrink
        self.owner_id = owner_id
        # The region ID. You can call DescribeRegions to obtain the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A deprecated parameter. You do not need to configure this parameter.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_instance_num is not None:
            result['DBProxyInstanceNum'] = self.dbproxy_instance_num

        if self.dbproxy_instance_type is not None:
            result['DBProxyInstanceType'] = self.dbproxy_instance_type

        if self.dbproxy_nodes_shrink is not None:
            result['DBProxyNodes'] = self.dbproxy_nodes_shrink

        if self.effective_specific_time is not None:
            result['EffectiveSpecificTime'] = self.effective_specific_time

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.migrate_azshrink is not None:
            result['MigrateAZ'] = self.migrate_azshrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyInstanceNum') is not None:
            self.dbproxy_instance_num = m.get('DBProxyInstanceNum')

        if m.get('DBProxyInstanceType') is not None:
            self.dbproxy_instance_type = m.get('DBProxyInstanceType')

        if m.get('DBProxyNodes') is not None:
            self.dbproxy_nodes_shrink = m.get('DBProxyNodes')

        if m.get('EffectiveSpecificTime') is not None:
            self.effective_specific_time = m.get('EffectiveSpecificTime')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('MigrateAZ') is not None:
            self.migrate_azshrink = m.get('MigrateAZ')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

