# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetResourceTypeRequest(DaraModel):
    def __init__(
        self,
        default_version_id: str = None,
        description: str = None,
        resource_type: str = None,
        version_id: str = None,
    ):
        # The ID of the default version. You can use this parameter to specify the default version of the resource type.
        # 
        # > You can specify only one of the VersionId and DefaultVersionId parameters.
        self.default_version_id = default_version_id
        # The description of the resource type or resource type version. The description can be up to 512 characters in length.
        self.description = description
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The version ID. If you want to modify a version of the resource type, you must specify this parameter. If you do not specify this parameter, only the resource type is modified.
        # 
        # > You can specify only one of the VersionId and DefaultVersionId parameters.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id

        if self.description is not None:
            result['Description'] = self.description

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

