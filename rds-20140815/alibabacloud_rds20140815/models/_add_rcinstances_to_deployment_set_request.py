# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRCInstancesToDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        deployment_set_group_no: str = None,
        deployment_set_id: str = None,
        force: bool = None,
        rcinstance_ids: str = None,
        region_id: str = None,
    ):
        # The group number of the instance in the deployment set. This parameter is valid only when the deployment set strategy of the ECS instance to be added or adjusted is AvailabilityGroup. Valid values: 1 to 7.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        # 
        # This parameter is required.
        self.deployment_set_id = deployment_set_id
        # Specifies whether to forcibly release the running instance. Valid values:
        # * **true**: yes.
        # * **false** (default): no.
        self.force = force
        # The instance IDs.
        # 
        # This parameter is required.
        self.rcinstance_ids = rcinstance_ids
        # The region ID. You can call the DescribeRegions operation to query the region ID.
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
        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.force is not None:
            result['Force'] = self.force

        if self.rcinstance_ids is not None:
            result['RCInstanceIds'] = self.rcinstance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RCInstanceIds') is not None:
            self.rcinstance_ids = m.get('RCInstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

