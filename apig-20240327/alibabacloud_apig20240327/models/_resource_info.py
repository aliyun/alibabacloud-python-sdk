# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceInfo(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        resource_version: str = None,
    ):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.resource_version = resource_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')

        return self

