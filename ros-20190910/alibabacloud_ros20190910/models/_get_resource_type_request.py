# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceTypeRequest(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        version_id: str = None,
    ):
        # The ID of the request.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The version ID. If you want to query a specific version of the resource type, you must specify this parameter. If you do not specify this parameter, only the resource type is queried.
        # 
        # > This parameter is supported only for modules.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

