# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateAppRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_key: str = None,
        app_name: str = None,
        app_secret: str = None,
        description: str = None,
        extend: str = None,
        security_token: str = None,
        tag: List[main_models.CreateAppRequestTag] = None,
    ):
        # The AppCode of the application.
        self.app_code = app_code
        # The key of the application that is used to make an API call.
        self.app_key = app_key
        # The name of the application. The name must be 4 to 26 characters in length. The name can contain letters, digits, and underscores (_), and must start with a letter.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The password of the application.
        self.app_secret = app_secret
        # The description of the application. The description can be up to 180 characters in length.
        self.description = description
        # The extended information.
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
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.description is not None:
            result['Description'] = self.description

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
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAppRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateAppRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # Valid values of n: `[1, 20]`.
        self.key = key
        # The value of the tag.
        # 
        # Valid values of n: `[1, 20]`. If the parameter has a value, you must specify a value for the tag key with the same N as tag.N.Key. Otherwise, an error is reported.
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

