# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        end_user_id: str = None,
        require_extra_attributes: List[str] = None,
    ):
        self.business_channel = business_channel
        self.end_user_id = end_user_id
        self.require_extra_attributes = require_extra_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.require_extra_attributes is not None:
            result['RequireExtraAttributes'] = self.require_extra_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RequireExtraAttributes') is not None:
            self.require_extra_attributes = m.get('RequireExtraAttributes')

        return self

