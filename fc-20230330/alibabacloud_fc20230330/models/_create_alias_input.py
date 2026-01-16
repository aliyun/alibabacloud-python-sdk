# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateAliasInput(DaraModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        description: str = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        # This parameter is required.
        self.alias_name = alias_name
        self.description = description
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight

        if self.alias_name is not None:
            result['aliasName'] = self.alias_name

        if self.description is not None:
            result['description'] = self.description

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')

        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

