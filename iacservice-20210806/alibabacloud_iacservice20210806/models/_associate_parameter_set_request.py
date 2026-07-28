# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateParameterSetRequest(DaraModel):
    def __init__(
        self,
        parameter_set_ids: List[str] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The list of parameter set IDs to associate with the resource. Maximum length: 5.
        # 
        # This parameter is required.
        self.parameter_set_ids = parameter_set_ids
        # The resource ID. When the resource type is ModuleVersion, the value is a concatenation of <moduleId>-<moduleversion>, such as mod-34535345df123fr-v3.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - Module: template
        # - ModuleVersion: template version
        # - Task: node
        # - Stack: resource stack.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

