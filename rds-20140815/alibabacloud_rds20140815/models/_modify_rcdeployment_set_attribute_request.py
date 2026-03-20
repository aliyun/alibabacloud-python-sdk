# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCDeploymentSetAttributeRequest(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        deployment_set_name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.deployment_set_id = deployment_set_id
        self.deployment_set_name = deployment_set_name
        self.description = description
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

        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

