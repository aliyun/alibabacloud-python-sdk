# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePopApiRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        pop_code: str = None,
    ):
        # The operation name of the Alibaba Cloud service.
        # 
        # This parameter is required.
        self.api_name = api_name
        # The version number of the API.
        # 
        # >  You can call the [DescribePopApiVersionList](~~DescribePopApiVersionList~~) operation to query the version number.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The POP code of the Alibaba Cloud service.
        # 
        # >  You can call the [DescribeApiList](~~DescribeApiList~~) operation to query the POP code.
        # 
        # This parameter is required.
        self.pop_code = pop_code

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

        if self.pop_code is not None:
            result['PopCode'] = self.pop_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')

        return self

