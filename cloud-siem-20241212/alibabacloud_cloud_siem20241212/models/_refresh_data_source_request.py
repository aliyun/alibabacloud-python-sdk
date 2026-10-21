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
        # The data source ID. This parameter is required in actual API calls. If it is not provided, the service returns a 400 error.
        self.data_source_id = data_source_id
        # The language of the received messages. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        # 
        # Note: This parameter is required in actual API calls. If it is not provided, the service returns a 400 error: "The specified Lang can not be empty." Pass the language code explicitly.
        self.lang = lang
        # The region where the data management center for threat analysis is located. Select the management center region based on the region where your assets reside. Valid values:
        # - cn-hangzhou: assets in the Chinese mainland and Hong Kong (China)
        # - ap-southeast-1: assets in regions outside China
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the view of another member.
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

