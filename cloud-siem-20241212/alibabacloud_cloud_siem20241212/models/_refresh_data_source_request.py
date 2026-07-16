# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The ID of the data source.
        self.data_source_id = data_source_id
        # The language of the messages. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The region where the Data Management Center for threat analysis is located. Select the region of the Data Management Center based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can use this parameter to switch to the perspective of the specified member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

