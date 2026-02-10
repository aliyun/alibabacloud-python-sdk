# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteListProcessRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        desc: int = None,
        lang: str = None,
        order_by: int = None,
        page_size: int = None,
        process_name: str = None,
        process_type: int = None,
        source_ip: str = None,
        strategy_id: int = None,
    ):
        # The page number. Default value: **1**. Pages start from page 1.
        self.current_page = current_page
        # The sort order. Default value: descending order. Valid values:
        # 
        # *   **1**: ascending order
        # *   **2**: descending order
        self.desc = desc
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The item based on which you want to sort the returned results. Default value: **process type**. Valid values:
        # 
        # *   **1**: process type
        # *   **2**: degree of trustability
        self.order_by = order_by
        # The number of entries per page. Maximum value: 1000. Default value: 20. If you leave this parameter empty, 20 data entries are returned per page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The name of the process.
        self.process_name = process_name
        # The type of the process. Valid values:
        # 
        # *   **1**: trusted
        # *   **2**: suspicious
        # *   **3**: malicious
        self.process_type = process_type
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip
        # The ID of the policy.
        # 
        # >  You can call the [DescribeWhiteListStrategyList](~~DescribeWhiteListStrategyList~~) operation to obtain the ID.
        # 
        # This parameter is required.
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

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

