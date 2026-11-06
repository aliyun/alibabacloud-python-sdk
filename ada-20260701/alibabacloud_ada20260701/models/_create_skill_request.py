# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateSkillRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        metadata: Any = None,
        name: str = None,
        visibility: str = None,
    ):
        # The description of the skill.
        # 
        # This parameter is required.
        self.description = description
        # The metadata of the skill, in JSON object format. You must and can only provide one content source. For specific fields, refer to the supplementary description of request parameters.
        # 
        # This parameter is required.
        self.metadata = metadata
        # The unique identifier of the skill. Only English letters, digits, underscores, and hyphens are supported. The length cannot exceed 64 characters.
        # 
        # This parameter is required.
        self.name = name
        # The visibility of the skill. Valid values: user and tenant. Default value: user.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.name is not None:
            result['Name'] = self.name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

