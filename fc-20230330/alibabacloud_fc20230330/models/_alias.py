# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class Alias(DaraModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        self.additional_version_weight = additional_version_weight
        self.alias_name = alias_name
        self.created_time = created_time
        self.description = description
        self.last_modified_time = last_modified_time
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

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')

        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

