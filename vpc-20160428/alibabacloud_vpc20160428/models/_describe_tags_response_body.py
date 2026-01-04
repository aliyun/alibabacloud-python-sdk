# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: main_models.DescribeTagsResponseBodyTagResources = None,
    ):
        # The token that is used for the next query. Valid values:
        # 
        # *   If the value of **NextToken** is not returned, it indicates that no next query is to be sent.
        # *   If a value of **NextToken** is returned, the value is the token that is used for the subsequent query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of tags that meet the filter conditions.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagResources') is not None:
            temp_model = main_models.DescribeTagsResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m.get('TagResources'))

        return self

class DescribeTagsResponseBodyTagResources(DaraModel):
    def __init__(
        self,
        tag_resource: List[main_models.DescribeTagsResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for v1 in self.tag_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k1 in self.tag_resource:
                result['TagResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k1 in m.get('TagResource'):
                temp_model = main_models.DescribeTagsResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k1))

        return self

class DescribeTagsResponseBodyTagResourcesTagResource(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

