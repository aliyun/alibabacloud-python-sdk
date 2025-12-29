# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tags: List[main_models.DescribeTagsResponseBodyTags] = None,
    ):
        # The token used to start the next query.
        # 
        # >  If not all results are returned in the first query, this parameter is returned. You can pass in the value of this parameter in the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Details about the tags.
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The values of the tags.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

