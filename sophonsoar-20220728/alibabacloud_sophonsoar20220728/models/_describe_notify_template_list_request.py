# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNotifyTemplateListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese.
        # *   **en**: English.
        self.lang = lang
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

