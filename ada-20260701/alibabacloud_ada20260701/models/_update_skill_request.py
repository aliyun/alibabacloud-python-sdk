# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class UpdateSkillRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        expected_version: int = None,
        metadata: Any = None,
        name: str = None,
        visibility: str = None,
    ):
        # The updated description of the skill.
        self.description = description
        # The expected version number.
        self.expected_version = expected_version
        # The updated metadata of the skill. The JSON object is replaced as a whole. The content supports one of the following: Transit ID, bundleUrl, or skillMd.
        self.metadata = metadata
        # The name of the skill to be updated. This parameter is only used to locate the skill and cannot be used to modify the name.
        # 
        # This parameter is required.
        self.name = name
        # The updated visibility. Valid values: `user` and `tenant`.
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

        if self.expected_version is not None:
            result['ExpectedVersion'] = self.expected_version

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

        if m.get('ExpectedVersion') is not None:
            self.expected_version = m.get('ExpectedVersion')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

