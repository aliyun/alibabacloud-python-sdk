# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHoneypotAlarmEventsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        dst_ip: str = None,
        page_size: int = None,
        risk_level_list: List[str] = None,
        src_ip: str = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The status of the alert event. Default value: **a**. Valid values:
        # 
        # *   **a**: all states
        # *   **y**: handled
        # *   **n**: unhandled
        self.dealed = dealed
        # The destination IP address.
        self.dst_ip = dst_ip
        # The number of entries per page. Default value: 100. If you leave this parameter empty, 100 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty. We recommend that you set the value to a value no greater than 100.
        self.page_size = page_size
        # The risk levels.
        self.risk_level_list = risk_level_list
        # The source IP address.
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

