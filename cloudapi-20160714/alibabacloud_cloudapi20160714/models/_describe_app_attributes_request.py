# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAppAttributesRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: int = None,
        app_key: str = None,
        app_name: str = None,
        enable_tag_auth: bool = None,
        extend: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        sort: str = None,
        tag: List[main_models.DescribeAppAttributesRequestTag] = None,
    ):
        # The AppCode of the app.
        self.app_code = app_code
        # The ID of the app.
        self.app_id = app_id
        # The app key that is used to make an API call.
        self.app_key = app_key
        # The name of the app.
        self.app_name = app_name
        # Specifies whether to enable tag verification.
        self.enable_tag_auth = enable_tag_auth
        # 扩展信息
        self.extend = extend
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token
        # The order. Valid values: asc and desc. Default value: desc.
        # 
        # *   asc: The apps are displayed in ascending order of modification time.
        # *   desc: The apps are displayed in descending order of modification time.
        self.sort = sort
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

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sort is not None:
            result['Sort'] = self.sort

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAppAttributesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAppAttributesRequestTag(DaraModel):
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
        # The key of the tag.
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

