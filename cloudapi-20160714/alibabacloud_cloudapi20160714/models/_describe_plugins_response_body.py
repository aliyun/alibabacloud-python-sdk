# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePluginsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugins: main_models.DescribePluginsResponseBodyPlugins = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The returned information about the plug-in. It is an array consisting of PluginAttribute data.
        self.plugins = plugins
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.plugins:
            self.plugins.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plugins is not None:
            result['Plugins'] = self.plugins.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Plugins') is not None:
            temp_model = main_models.DescribePluginsResponseBodyPlugins()
            self.plugins = temp_model.from_map(m.get('Plugins'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePluginsResponseBodyPlugins(DaraModel):
    def __init__(
        self,
        plugin_attribute: List[main_models.DescribePluginsResponseBodyPluginsPluginAttribute] = None,
    ):
        self.plugin_attribute = plugin_attribute

    def validate(self):
        if self.plugin_attribute:
            for v1 in self.plugin_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PluginAttribute'] = []
        if self.plugin_attribute is not None:
            for k1 in self.plugin_attribute:
                result['PluginAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_attribute = []
        if m.get('PluginAttribute') is not None:
            for k1 in m.get('PluginAttribute'):
                temp_model = main_models.DescribePluginsResponseBodyPluginsPluginAttribute()
                self.plugin_attribute.append(temp_model.from_map(k1))

        return self

class DescribePluginsResponseBodyPluginsPluginAttribute(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        plugin_data: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        region_id: str = None,
        tags: main_models.DescribePluginsResponseBodyPluginsPluginAttributeTags = None,
    ):
        # The creation time (UTC) of the plug-in.
        self.created_time = created_time
        # The plug-in description.
        self.description = description
        # The last modification time (UTC) of the plug-in.
        self.modified_time = modified_time
        # The definition statement of the plug-in.
        self.plugin_data = plugin_data
        # The ID of the plug-in.
        self.plugin_id = plugin_id
        # The name of the plug-in.
        self.plugin_name = plugin_name
        # The type of the plug-in.
        self.plugin_type = plugin_type
        # The region where the plug-in is located.
        self.region_id = region_id
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
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribePluginsResponseBodyPluginsPluginAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribePluginsResponseBodyPluginsPluginAttributeTags(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo] = None,
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
                temp_model = main_models.DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo(DaraModel):
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

