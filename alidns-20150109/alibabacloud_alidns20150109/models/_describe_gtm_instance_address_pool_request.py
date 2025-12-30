# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmInstanceAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        lang: str = None,
    ):
        # The ID of the address pool that you want to query.
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The language used by the user.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

