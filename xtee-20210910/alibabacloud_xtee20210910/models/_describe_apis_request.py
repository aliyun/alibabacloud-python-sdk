# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        api_group_id: str = None,
        api_region_id: str = None,
        api_type: str = None,
        reg_id: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # API group ID.
        # 
        # This parameter is required.
        self.api_group_id = api_group_id
        # Region ID.
        # 
        # This parameter is required.
        self.api_region_id = api_region_id
        # API type.
        # 
        # This parameter is required.
        self.api_type = api_type
        # Region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.api_group_id is not None:
            result['apiGroupId'] = self.api_group_id

        if self.api_region_id is not None:
            result['apiRegionId'] = self.api_region_id

        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('apiGroupId') is not None:
            self.api_group_id = m.get('apiGroupId')

        if m.get('apiRegionId') is not None:
            self.api_region_id = m.get('apiRegionId')

        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

