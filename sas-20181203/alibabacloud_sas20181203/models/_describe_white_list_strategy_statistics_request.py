# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListStrategyStatisticsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        source_ip: str = None,
        strategy_ids: str = None,
    ):
        # The page number. Default value: **1**. Pages start from page 1.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Maximum value: 1000. Default value: 20. If you leave this parameter empty, 20 data entries are returned per page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to obtain the ID.
        self.strategy_ids = strategy_ids

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_ids is not None:
            result['StrategyIds'] = self.strategy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')

        return self

