# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreatePluginRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        plugin_data: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        security_token: str = None,
        tag: List[main_models.CreatePluginRequestTag] = None,
    ):
        # The description of the plug-in. The description can contain a maximum of 200 characters in length.
        self.description = description
        # The plug-in definition. Supported formats: JSON and YAML.
        # 
        # This parameter is required.
        self.plugin_data = plugin_data
        # The name of the plug-in. The name must be 4 to 50 characters in length and can contain letters, digits, and underscores (_). However, it cannot start with an underscore.
        # 
        # This parameter is required.
        self.plugin_name = plugin_name
        # The type of the plug-in. Valid values:
        # 
        # *   **ipControl: IP address-based access control**
        # *   **trafficControl: throttling**
        # *   **backendSignature: backend signature**
        # *   **jwtAuth** :JWT (OpenId Connect) authentication
        # *   **cors** :cross-origin resource sharing (CORS)
        # *   **caching**
        # 
        # This parameter is required.
        self.plugin_type = plugin_type
        self.security_token = security_token
        # The tag of objects that match the rule. You can specify multiple tags.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data

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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePluginRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePluginRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # N can be an integer from 1 to 20.``
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag.
        # 
        # N can be an integer from 1 to 20.``
        # 
        # This parameter is required.
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

