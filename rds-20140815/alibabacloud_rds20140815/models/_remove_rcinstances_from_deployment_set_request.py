# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveRCInstancesFromDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        rcinstance_ids: str = None,
        region_id: str = None,
    ):
        # The deployment set ID.
        # 
        # This parameter is required.
        self.deployment_set_id = deployment_set_id
        # The instance ID.
        # 
        # This parameter is required.
        self.rcinstance_ids = rcinstance_ids
        # The region ID. You can call DescribeRegions to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.rcinstance_ids is not None:
            result['RCInstanceIds'] = self.rcinstance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('RCInstanceIds') is not None:
            self.rcinstance_ids = m.get('RCInstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

