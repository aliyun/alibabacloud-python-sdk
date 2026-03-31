# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeployRevisionRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_resource_type: str = None,
        description: str = None,
        hooks: str = None,
        location: str = None,
        revision_type: str = None,
    ):
        # This parameter is required.
        self.application_name = application_name
        self.deploy_resource_type = deploy_resource_type
        self.description = description
        self.hooks = hooks
        self.location = location
        self.revision_type = revision_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.deploy_resource_type is not None:
            result['DeployResourceType'] = self.deploy_resource_type

        if self.description is not None:
            result['Description'] = self.description

        if self.hooks is not None:
            result['Hooks'] = self.hooks

        if self.location is not None:
            result['Location'] = self.location

        if self.revision_type is not None:
            result['RevisionType'] = self.revision_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('DeployResourceType') is not None:
            self.deploy_resource_type = m.get('DeployResourceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hooks') is not None:
            self.hooks = m.get('Hooks')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('RevisionType') is not None:
            self.revision_type = m.get('RevisionType')

        return self

