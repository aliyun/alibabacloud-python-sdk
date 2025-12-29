# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployApplicationGroupRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_parameters: str = None,
        name: str = None,
        region_id: str = None,
        revision_id: str = None,
    ):
        # The name of the application.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The deployment information about the application group.
        # 
        # This parameter is required.
        self.deploy_parameters = deploy_parameters
        # The name of the application group.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region in which you want to deploy the application group.
        self.region_id = region_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')

        return self

