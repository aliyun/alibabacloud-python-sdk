# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigLayer7BlackWhiteListRequest(DaraModel):
    def __init__(
        self,
        black_list: List[str] = None,
        domain: str = None,
        resource_group_id: str = None,
        white_list: List[str] = None,
    ):
        self.black_list = black_list
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list is not None:
            result['BlackList'] = self.black_list

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

