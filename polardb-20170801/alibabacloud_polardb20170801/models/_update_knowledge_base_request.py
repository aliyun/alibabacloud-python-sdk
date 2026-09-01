# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        region_id: str = None,
        search_mode: str = None,
    ):
        # The description of the knowledge base.
        self.description = description
        # The unique ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The name of the knowledge base.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The search mode. Valid values:
        # 
        # * balanced (default): balanced mode.
        # * precise: precise mode.
        # * semantic: semantic mode.
        # * knn: KNN mode.
        # * rrf: reciprocal rank fusion (RRF) mode.
        self.search_mode = search_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        return self

