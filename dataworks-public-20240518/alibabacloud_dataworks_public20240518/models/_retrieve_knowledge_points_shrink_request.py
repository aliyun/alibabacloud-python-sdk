# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveKnowledgePointsShrinkRequest(DaraModel):
    def __init__(
        self,
        focus_objects_shrink: str = None,
        knowledge_base_ids_shrink: str = None,
        max_results: int = None,
        query: str = None,
    ):
        # The graph objects to focus the search on. You can specify up to 2 unique objects. The objects must be within the current authorized search scope and do not expand permissions.
        self.focus_objects_shrink = focus_objects_shrink
        # A list of 1 to 50 unique knowledge base IDs that restricts the search. If you omit this parameter, the operation discovers knowledge bases within the caller’s authorized scope. If you provide IDs, the operation checks access to each knowledge base and the entire request fails if the caller lacks access to any of them.
        self.knowledge_base_ids_shrink = knowledge_base_ids_shrink
        # The maximum number of hits across all knowledge bases. Default value: 10. Valid values: 1 to 50. This parameter does not specify the quota for each knowledge base or the page size.
        self.max_results = max_results
        # The natural language question. The length cannot exceed 256 Unicode code points after leading and trailing whitespaces are removed.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.focus_objects_shrink is not None:
            result['FocusObjects'] = self.focus_objects_shrink

        if self.knowledge_base_ids_shrink is not None:
            result['KnowledgeBaseIds'] = self.knowledge_base_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FocusObjects') is not None:
            self.focus_objects_shrink = m.get('FocusObjects')

        if m.get('KnowledgeBaseIds') is not None:
            self.knowledge_base_ids_shrink = m.get('KnowledgeBaseIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

