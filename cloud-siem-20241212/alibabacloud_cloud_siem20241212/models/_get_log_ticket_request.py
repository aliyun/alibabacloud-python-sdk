# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogTicketRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response messages. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The user ID for data access.
        self.log_user_id = log_user_id
        # The region of the Data Management hub for threat analysis. Select the region based on the location of your asset. Valid values:
        # 
        # - cn-hangzhou: The asset is in the Chinese mainland.
        # 
        # - ap-southeast-1: The asset is in a region outside China.
        self.region_id = region_id
        # The user ID of a member. This parameter lets an administrator switch to the perspective of the member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

