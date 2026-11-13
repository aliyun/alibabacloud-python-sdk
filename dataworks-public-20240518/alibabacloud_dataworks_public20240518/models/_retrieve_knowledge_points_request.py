# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class RetrieveKnowledgePointsRequest(DaraModel):
    def __init__(
        self,
        focus_objects: List[main_models.RetrieveKnowledgePointsRequestFocusObjects] = None,
        knowledge_base_ids: List[str] = None,
        max_results: int = None,
        query: str = None,
    ):
        # The graph objects to focus the search on. You can specify up to 2 unique objects. The objects must be within the current authorized search scope and do not expand permissions.
        self.focus_objects = focus_objects
        # A list of 1 to 50 unique knowledge base IDs that restricts the search. If you omit this parameter, the operation discovers knowledge bases within the caller’s authorized scope. If you provide IDs, the operation checks access to each knowledge base and the entire request fails if the caller lacks access to any of them.
        self.knowledge_base_ids = knowledge_base_ids
        # The maximum number of hits across all knowledge bases. Default value: 10. Valid values: 1 to 50. This parameter does not specify the quota for each knowledge base or the page size.
        self.max_results = max_results
        # The natural language question. The length cannot exceed 256 Unicode code points after leading and trailing whitespaces are removed.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.focus_objects:
            for v1 in self.focus_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FocusObjects'] = []
        if self.focus_objects is not None:
            for k1 in self.focus_objects:
                result['FocusObjects'].append(k1.to_map() if k1 else None)

        if self.knowledge_base_ids is not None:
            result['KnowledgeBaseIds'] = self.knowledge_base_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.focus_objects = []
        if m.get('FocusObjects') is not None:
            for k1 in m.get('FocusObjects'):
                temp_model = main_models.RetrieveKnowledgePointsRequestFocusObjects()
                self.focus_objects.append(temp_model.from_map(k1))

        if m.get('KnowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('KnowledgeBaseIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class RetrieveKnowledgePointsRequestFocusObjects(DaraModel):
    def __init__(
        self,
        id: str = None,
        knowledge_base_id: str = None,
        type: str = None,
    ):
        # The location ID of the knowledge point. Copy this value exactly as it appears in the search results and use it together with the corresponding KnowledgeBaseId and Type. Do not parse or convert this value.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the knowledge base to which the knowledge point belongs. This parameter is used together with Type and Id to locate the knowledge point.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The read category of the knowledge point. Use GRAPH for the current focus objects and graph nodes.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

