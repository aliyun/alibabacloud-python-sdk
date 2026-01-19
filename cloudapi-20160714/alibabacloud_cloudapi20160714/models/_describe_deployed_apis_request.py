# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeDeployedApisRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_method: str = None,
        api_name: str = None,
        api_path: str = None,
        enable_tag_auth: bool = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
        tag: List[main_models.DescribeDeployedApisRequestTag] = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The HTTP method of the API request.
        self.api_method = api_method
        # The name of the API. The name is used for fuzzy match.
        self.api_name = api_name
        # The request path of the API.
        self.api_path = api_path
        # Specifies whether to enable tag verification.
        self.enable_tag_auth = enable_tag_auth
        # The ID of the API group.
        self.group_id = group_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name
        # The tags.
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_method is not None:
            result['ApiMethod'] = self.api_method

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_path is not None:
            result['ApiPath'] = self.api_path

        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiMethod') is not None:
            self.api_method = m.get('ApiMethod')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')

        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDeployedApisRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDeployedApisRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

