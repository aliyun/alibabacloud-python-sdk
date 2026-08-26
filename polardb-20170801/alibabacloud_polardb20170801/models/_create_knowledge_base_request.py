# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        knowledge_base_type: str = None,
        knowledge_space_id: str = None,
        name: str = None,
        region_id: str = None,
        search_mode: str = None,
    ):
        # The description of the knowledge base.
        self.description = description
        # The type of the knowledge base: PERSONAL or PUBLIC.
        self.knowledge_base_type = knowledge_base_type
        # The unique identifier of the knowledge space.
        # 
        # This parameter is required.
        self.knowledge_space_id = knowledge_space_id
        # The name of the knowledge base.
        # 
        # This parameter is required.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The search mode. Valid values:
        # 
        # * balanced (default): balanced mode
        # * precise: precise mode
        # * semantic: semantic mode
        # * knn: KNN mode
        # * rrf: reciprocal rank fusion
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

        if self.knowledge_base_type is not None:
            result['KnowledgeBaseType'] = self.knowledge_base_type

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

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

        if m.get('KnowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('KnowledgeBaseType')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        return self

