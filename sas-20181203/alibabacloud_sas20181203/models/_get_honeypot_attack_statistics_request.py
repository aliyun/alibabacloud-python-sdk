# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetHoneypotAttackStatisticsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time_stamp: int = None,
        lang: str = None,
        page_size: int = None,
        risk_level_list: List[str] = None,
        src_ip: str = None,
        start_time_stamp: int = None,
        statistics_type: str = None,
    ):
        # The page number of the returned page. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The end time in the timestamp format.
        self.end_time_stamp = end_time_stamp
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of entries to return on each page in a paging query. Default value: 20. If this parameter is left empty, 20 entries are returned by default. Do not leave this parameter empty.
        self.page_size = page_size
        # The list of risk levels.
        self.risk_level_list = risk_level_list
        # The IP address of the attack source.
        # 
        # This parameter is required.
        self.src_ip = src_ip
        # The start time in the timestamp format.
        self.start_time_stamp = start_time_stamp
        # The type of statistics for the attack source. Valid values:
        # 
        # - **TOP_ATTACKED_AGENT**: The top 5 probes that are attacked most frequently.
        # - **TOP_ATTACKED_IP**: The top 5 IP addresses that are attacked most frequently.
        # - **ATTACK_EVENT_TYPE**: The intrusion event type.
        # - **ATTACK_HONEYPOT_TYPE**: The type of the attacked honeypot.
        # 
        # This parameter is required.
        self.statistics_type = statistics_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp

        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')

        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')

        return self

