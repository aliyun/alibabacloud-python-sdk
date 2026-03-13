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
        # The operation that you want to perform.
        self.api_name = api_name
        # The version number of the API.
        # 
        # >  You can call the [DescribeGroupProductions](~~DescribeGroupProductions~~) operation to query the version number.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The POP code of the Alibaba Cloud service.
        # 
        # This parameter is required.
        self.pop_code = pop_code
        # The ID of the user who switches from the current view to the destination view by using the management account.
        self.role_for = role_for
        # The type of the view. Default value: 0. Valid values:
        # 
        # *   0: the view of the current Alibaba Cloud account.
        # *   1: the view of all accounts for the enterprise.
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

