# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProcessStatisticsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        process_action_end: int = None,
        process_action_start: int = None,
        role_for: str = None,
        role_type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The end time of the query for response tasks. The value is a 13-digit UNIX timestamp.
        self.process_action_end = process_action_end
        # The start time of the query for response tasks. The value is a 13-digit UNIX timestamp.
        self.process_action_start = process_action_start
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0 (default): the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.process_action_end is not None:
            result['ProcessActionEnd'] = self.process_action_end

        if self.process_action_start is not None:
            result['ProcessActionStart'] = self.process_action_start

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProcessActionEnd') is not None:
            self.process_action_end = m.get('ProcessActionEnd')

        if m.get('ProcessActionStart') is not None:
            self.process_action_start = m.get('ProcessActionStart')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

