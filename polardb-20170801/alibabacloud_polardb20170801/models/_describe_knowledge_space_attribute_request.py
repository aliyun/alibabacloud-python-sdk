# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKnowledgeSpaceAttributeRequest(DaraModel):
    def __init__(
        self,
        knowledge_space_id: str = None,
        region_id: str = None,
    ):
        # The unique identifier of the knowledge space.
        # 
        # This parameter is required.
        self.knowledge_space_id = knowledge_space_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

