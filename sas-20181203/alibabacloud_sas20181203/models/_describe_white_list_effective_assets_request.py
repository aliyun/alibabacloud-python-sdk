# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListEffectiveAssetsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        need_statistics: int = None,
        page_size: int = None,
        remark: str = None,
        source_ip: str = None,
        strategy_id: int = None,
    ):
        # The page number. Default value: **1**. Pages start from page 1.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to return the number of **untrusted programs**. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.need_statistics = need_statistics
        # The number of entries per page. Maximum value: **1000**. Default value: 20. If you leave this parameter empty, 20 data entries are returned per page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The condition that is used to query assets. You can enter an IP address, a public IP address, an private IP address, or an asset name for fuzzy match.
        self.remark = remark
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to obtain the ID.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.need_statistics is not None:
            result['NeedStatistics'] = self.need_statistics

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NeedStatistics') is not None:
            self.need_statistics = m.get('NeedStatistics')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

