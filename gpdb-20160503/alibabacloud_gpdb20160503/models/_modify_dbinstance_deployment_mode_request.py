# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceDeploymentModeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        deploy_mode: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in the specified region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The deployment mode. Valid values:
        # 
        # *   multiple: Multi-zone development.
        # *   single: Single-zone deployment.
        # 
        # This parameter is required.
        self.deploy_mode = deploy_mode
        # The vSwitch ID of the secondary zone.
        # 
        # > 
        # 
        # *   This parameter must be specified only when DeployMode is set to multiple.
        # 
        # *   The vSwitch must be deployed in the zone that is specified by the StandbyZoneId parameter.
        self.standby_vswitch_id = standby_vswitch_id
        # The ID of the secondary zone.
        # 
        # > 
        # 
        # *   This parameter must be specified only when DeployMode is set to multiple.
        # 
        # *   You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the available zone list.
        # 
        # *   The ID of the secondary zone must be different from the ID of the primary zone.
        self.standby_zone_id = standby_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        return self

