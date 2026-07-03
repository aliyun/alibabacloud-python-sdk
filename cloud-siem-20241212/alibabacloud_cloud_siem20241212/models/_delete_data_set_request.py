# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataSetRequest(DaraModel):
    def __init__(
        self,
        data_set_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The ID of the dataset.
        # 
        # This parameter is required.
        self.data_set_id = data_set_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The region of the Data Management center for threat analysis. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: for assets in the Chinese mainland.
        # 
        # - ap-southeast-1: for assets outside the Chinese mainland.
        self.region_id = region_id
        # The user ID that an administrator uses to switch to the perspective of a member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

