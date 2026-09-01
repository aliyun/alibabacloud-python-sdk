# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOpenApiListRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        lang: str = None,
        pop_code: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # The API name.
        self.api_name = api_name
        # The API version number.
        # 
        # > Call the [DescribeGroupProductions](~~DescribeGroupProductions~~) API to get this parameter.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The language type for requests and responses. The default value is **zh**. Values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The POP CODE of the Alibaba Cloud product API.
        # 
        # This parameter is required.
        self.pop_code = pop_code
        # The user ID of the member whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. The default is 0. Values:
        # 
        # - 0: Current Alibaba Cloud account view.
        # 
        # - 1: View of all accounts under the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.pop_code is not None:
            result['PopCode'] = self.pop_code

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

