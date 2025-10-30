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
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.deploy_mode = deploy_mode
        self.standby_vswitch_id = standby_vswitch_id
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

