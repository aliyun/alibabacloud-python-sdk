# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteKBSyncLinkRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        link_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # This parameter is required.
        self.link_id = link_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

