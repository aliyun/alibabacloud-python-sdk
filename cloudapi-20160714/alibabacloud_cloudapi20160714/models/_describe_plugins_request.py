# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePluginsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        security_token: str = None,
        tag: List[main_models.DescribePluginsRequestTag] = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The ID of the plug-in.
        self.plugin_id = plugin_id
        # The name of the plug-in.
        self.plugin_name = plugin_name
        # The business type of the plug-in.
        self.plugin_type = plugin_type
        self.security_token = security_token
        # The tag of objects that match the lifecycle rule. You can specify multiple tags.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribePluginsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribePluginsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # N can be an integer from 1 to 20.``
        self.key = key
        # The value of the tag.
        # 
        # N can be an integer from 1 to 20.``
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

