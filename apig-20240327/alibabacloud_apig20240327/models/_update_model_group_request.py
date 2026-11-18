# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateModelGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        expected_version: int = None,
        model_card_ids: List[str] = None,
        name: str = None,
    ):
        # The nullable description. The maximum length is 1024 UTF-16 code units.
        self.description = description
        # The group version obtained from the most recent Get operation. A stale version returns Conflict.ModelGroupChanged. Submitting the same expectedVersion, name, description, and modelCardIds retries the Failed or PartiallyFailed configuration for the same version, reuses the operationId, and does not increment the group version. Pending, Running, or Succeeded states are not forcibly reset.
        # 
        # This parameter is required.
        self.expected_version = expected_version
        # The actual or logical model identities within the same instance. The list can be null and must not contain duplicates. Model groups are not accepted as members.
        # 
        # This parameter is required.
        self.model_card_ids = model_card_ids
        # The unique name within the instance. The length is 1 to 128 UTF-8 bytes after trimming.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.expected_version is not None:
            result['expectedVersion'] = self.expected_version

        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expectedVersion') is not None:
            self.expected_version = m.get('expectedVersion')

        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

