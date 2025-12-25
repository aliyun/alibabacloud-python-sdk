# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRCDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        region_id: str = None,
    ):
        # The deployment set ID.
        # 
        # This parameter is required.
        self.deployment_set_id = deployment_set_id
        # The region ID.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

