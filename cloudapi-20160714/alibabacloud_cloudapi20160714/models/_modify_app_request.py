# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class ModifyAppRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        disabled: bool = None,
        extend: str = None,
        security_token: str = None,
        tag: List[main_models.ModifyAppRequestTag] = None,
    ):
        # The ID of the app.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The value must be 4 to 26 characters in length and can contain letters, digits, and underscores (_). It must start with a letter.
        # 
        # This parameter is required only when you want to modify the value.
        self.app_name = app_name
        # The description of the app. The description can contain a maximum of 180 characters in length.
        # 
        # This parameter is required only when you want to modify the value.
        self.description = description
        self.disabled = disabled
        # 扩展信息
        self.extend = extend
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ModifyAppRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ModifyAppRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The value of the tag.
        # 
        # N can be an integer from 1 to 20.``
        # 
        # This parameter is required.
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

