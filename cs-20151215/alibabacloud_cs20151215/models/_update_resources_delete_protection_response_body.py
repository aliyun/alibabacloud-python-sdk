# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateResourcesDeleteProtectionResponseBody(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        protection: str = None,
        request_id: str = None,
        resource_type: str = None,
        resources: List[str] = None,
    ):
        # The namespace of the resource.
        self.namespace = namespace
        # The deletion protection status of the resource.
        self.protection = protection
        # The request ID.
        self.request_id = request_id
        # The resource type.
        self.resource_type = resource_type
        # The list of resources for which the deletion protection status is updated.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.protection is not None:
            result['protection'] = self.protection

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.resources is not None:
            result['resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('protection') is not None:
            self.protection = m.get('protection')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        return self

