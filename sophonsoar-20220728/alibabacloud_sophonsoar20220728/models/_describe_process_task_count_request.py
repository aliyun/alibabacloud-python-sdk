# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeProcessTaskCountRequest(DaraModel):
    def __init__(
        self,
        entity_uuid_list: List[str] = None,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # Collection of entity UUIDs.
        # 
        # This parameter is required.
        self.entity_uuid_list = entity_uuid_list
        # Language type for request and response messages. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # User ID for administrators to switch to other member\\"s perspective.
        self.role_for = role_for
        # View type.
        # 
        # - **0**: Current Alibaba Cloud account view.
        # - **1**: View for all accounts under the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_uuid_list is not None:
            result['EntityUuidList'] = self.entity_uuid_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityUuidList') is not None:
            self.entity_uuid_list = m.get('EntityUuidList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

