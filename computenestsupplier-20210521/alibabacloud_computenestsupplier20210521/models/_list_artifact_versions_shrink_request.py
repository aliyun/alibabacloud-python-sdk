# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListArtifactVersionsShrinkRequest(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        filters_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The artifact ID.
        # 
        # To obtain the artifact ID, call the [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) operation.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The filter.
        self.filters_shrink = filters_shrink
        # The number of entries to return on each page. The maximum value is 100. The default value is 20.
        self.max_results = max_results
        # The token to retrieve the next page of results. Set this to the NextToken value from the previous call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.filters_shrink is not None:
            result['Filters'] = self.filters_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('Filters') is not None:
            self.filters_shrink = m.get('Filters')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

