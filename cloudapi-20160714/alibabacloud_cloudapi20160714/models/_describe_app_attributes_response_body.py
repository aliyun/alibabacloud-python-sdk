# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAppAttributesResponseBody(DaraModel):
    def __init__(
        self,
        apps: main_models.DescribeAppAttributesResponseBodyApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned app information. It is an array that consists of AppAttribute data.
        self.apps = apps
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apps') is not None:
            temp_model = main_models.DescribeAppAttributesResponseBodyApps()
            self.apps = temp_model.from_map(m.get('Apps'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAppAttributesResponseBodyApps(DaraModel):
    def __init__(
        self,
        app_attribute: List[main_models.DescribeAppAttributesResponseBodyAppsAppAttribute] = None,
    ):
        self.app_attribute = app_attribute

    def validate(self):
        if self.app_attribute:
            for v1 in self.app_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppAttribute'] = []
        if self.app_attribute is not None:
            for k1 in self.app_attribute:
                result['AppAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_attribute = []
        if m.get('AppAttribute') is not None:
            for k1 in m.get('AppAttribute'):
                temp_model = main_models.DescribeAppAttributesResponseBodyAppsAppAttribute()
                self.app_attribute.append(temp_model.from_map(k1))

        return self

class DescribeAppAttributesResponseBodyAppsAppAttribute(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        created_time: str = None,
        description: str = None,
        disabled: bool = None,
        extend: str = None,
        modified_time: str = None,
        tags: main_models.DescribeAppAttributesResponseBodyAppsAppAttributeTags = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The name of the app.
        self.app_name = app_name
        # The creation time (UTC) of the app.
        self.created_time = created_time
        # The description of the app.
        self.description = description
        self.disabled = disabled
        # 扩展信息
        self.extend = extend
        # The modification time (UTC) of the app.
        self.modified_time = modified_time
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAppAttributesResponseBodyAppsAppAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeAppAttributesResponseBodyAppsAppAttributeTags(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for v1 in self.tag_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k1 in self.tag_info:
                result['TagInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k1 in m.get('TagInfo'):
                temp_model = main_models.DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

