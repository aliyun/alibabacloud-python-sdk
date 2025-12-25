# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizationResourceInfo(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        parent_resource_id: str = None,
        resource_id: str = None,
    ):
        self.environment_id = environment_id
        self.parent_resource_id = parent_resource_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.parent_resource_id is not None:
            result['parentResourceId'] = self.parent_resource_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('parentResourceId') is not None:
            self.parent_resource_id = m.get('parentResourceId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        return self

