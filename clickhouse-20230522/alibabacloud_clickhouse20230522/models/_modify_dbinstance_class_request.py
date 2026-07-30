# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class ModifyDBInstanceClassRequest(DaraModel):
    def __init__(
        self,
        auto_scale_config: main_models.ModifyDBInstanceClassRequestAutoScaleConfig = None,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        node_count: int = None,
        node_scale_max: int = None,
        node_scale_min: int = None,
        region_id: str = None,
        scale_max: int = None,
        scale_min: int = None,
        storage_quota: int = None,
        storage_type: str = None,
    ):
        # The autoscaling configuration for the compute group.
        self.auto_scale_config = auto_scale_config
        # The compute group ID.
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The number of nodes. Valid values: 2 to 16.
        self.node_count = node_count
        # The maximum capacity per node for serverless autoscaling. Valid values: 4 to 32. This value must be greater than the minimum value.
        self.node_scale_max = node_scale_max
        # The minimum capacity per node for serverless autoscaling. Valid values: 4 to 32.
        self.node_scale_min = node_scale_min
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The maximum capacity for serverless autoscaling.
        self.scale_max = scale_max
        # The minimum capacity for serverless autoscaling.
        self.scale_min = scale_min
        # The pre-purchased storage capacity in GB.
        self.storage_quota = storage_quota
        # The storage type.
        self.storage_type = storage_type

    def validate(self):
        if self.auto_scale_config:
            self.auto_scale_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scale_config is not None:
            result['AutoScaleConfig'] = self.auto_scale_config.to_map()

        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_scale_max is not None:
            result['NodeScaleMax'] = self.node_scale_max

        if self.node_scale_min is not None:
            result['NodeScaleMin'] = self.node_scale_min

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.storage_quota is not None:
            result['StorageQuota'] = self.storage_quota

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScaleConfig') is not None:
            temp_model = main_models.ModifyDBInstanceClassRequestAutoScaleConfig()
            self.auto_scale_config = temp_model.from_map(m.get('AutoScaleConfig'))

        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeScaleMax') is not None:
            self.node_scale_max = m.get('NodeScaleMax')

        if m.get('NodeScaleMin') is not None:
            self.node_scale_min = m.get('NodeScaleMin')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('StorageQuota') is not None:
            self.storage_quota = m.get('StorageQuota')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class ModifyDBInstanceClassRequestAutoScaleConfig(DaraModel):
    def __init__(
        self,
        burst_num: int = None,
        status: str = None,
        v_switch_infos: List[main_models.ModifyDBInstanceClassRequestAutoScaleConfigVSwitchInfos] = None,
    ):
        # The number of burstable nodes for autoscaling.
        self.burst_num = burst_num
        # Specifies whether to enable or disable autoscaling. Valid values: `enable` and `disable`.
        self.status = status
        # Information about the VSwitches.
        self.v_switch_infos = v_switch_infos

    def validate(self):
        if self.v_switch_infos:
            for v1 in self.v_switch_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.burst_num is not None:
            result['BurstNum'] = self.burst_num

        if self.status is not None:
            result['Status'] = self.status

        result['VSwitchInfos'] = []
        if self.v_switch_infos is not None:
            for k1 in self.v_switch_infos:
                result['VSwitchInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstNum') is not None:
            self.burst_num = m.get('BurstNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.v_switch_infos = []
        if m.get('VSwitchInfos') is not None:
            for k1 in m.get('VSwitchInfos'):
                temp_model = main_models.ModifyDBInstanceClassRequestAutoScaleConfigVSwitchInfos()
                self.v_switch_infos.append(temp_model.from_map(k1))

        return self

class ModifyDBInstanceClassRequestAutoScaleConfigVSwitchInfos(DaraModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The VSwitch IDs.
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

