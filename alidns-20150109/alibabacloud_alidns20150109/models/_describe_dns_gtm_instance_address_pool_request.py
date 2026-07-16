# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmInstanceAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        lang: str = None,
    ):
        # The ID of the address pool.<props="china">You can call the [DescribeDnsGtmInstanceAddressPools](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspools?spm=a2c4g.11186623.help-menu-29697.d_0_5_1_3_9_7.1cee430dbd1I3y) operation to obtain the ID.
        # <props="intl">You can call the [DescribeDnsGtmInstanceAddressPools](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspools?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the ID.
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The language of the response. Default value: en. Valid values: en, zh, and ja.
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

