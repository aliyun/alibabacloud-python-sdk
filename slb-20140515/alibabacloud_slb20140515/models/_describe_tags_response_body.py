# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_sets: main_models.DescribeTagsResponseBodyTagSets = None,
        total_count: int = None,
    ):
        # The number of the returned page. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Default value: 50. Maximum value: 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The tags that are queried.
        self.tag_sets = tag_sets
        # The number of instances returned.
        self.total_count = total_count

    def validate(self):
        if self.tag_sets:
            self.tag_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_sets is not None:
            result['TagSets'] = self.tag_sets.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagSets') is not None:
            temp_model = main_models.DescribeTagsResponseBodyTagSets()
            self.tag_sets = temp_model.from_map(m.get('TagSets'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTagsResponseBodyTagSets(DaraModel):
    def __init__(
        self,
        tag_set: List[main_models.DescribeTagsResponseBodyTagSetsTagSet] = None,
    ):
        self.tag_set = tag_set

    def validate(self):
        if self.tag_set:
            for v1 in self.tag_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagSet'] = []
        if self.tag_set is not None:
            for k1 in self.tag_set:
                result['TagSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_set = []
        if m.get('TagSet') is not None:
            for k1 in m.get('TagSet'):
                temp_model = main_models.DescribeTagsResponseBodyTagSetsTagSet()
                self.tag_set.append(temp_model.from_map(k1))

        return self

class DescribeTagsResponseBodyTagSetsTagSet(DaraModel):
    def __init__(
        self,
        instance_count: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The number of instances to which the tag is added.
        self.instance_count = instance_count
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
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

