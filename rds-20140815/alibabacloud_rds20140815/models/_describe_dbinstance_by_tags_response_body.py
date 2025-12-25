# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceByTagsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstanceByTagsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details about the instance.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstanceByTagsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstanceByTagsResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_tag: List[main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTag] = None,
    ):
        self.dbinstance_tag = dbinstance_tag

    def validate(self):
        if self.dbinstance_tag:
            for v1 in self.dbinstance_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceTag'] = []
        if self.dbinstance_tag is not None:
            for k1 in self.dbinstance_tag:
                result['DBInstanceTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_tag = []
        if m.get('DBInstanceTag') is not None:
            for k1 in m.get('DBInstanceTag'):
                temp_model = main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTag()
                self.dbinstance_tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTag(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        tags: main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTags = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The details about the tag.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceByTagsResponseBodyItemsDBInstanceTagTagsTag(DaraModel):
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

