# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListTagsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tags: List[main_models.ListTagsResponseBodyTags] = None,
    ):
        # The maximum number of results to return when using NextToken-based pagination. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If a next query is available, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The entity tags. The value is a JSON array string in the following format:
        # 
        # `"[{"tagKey1":"tagValue1"},{"tagKey2":"tagValue2"}]"`
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        count: int = None,
        tag: str = None,
    ):
        # The number of quick queries returned on the current page.
        self.count = count
        # The key of the tag to query. You can specify multiple keys. N is a positive integer.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

