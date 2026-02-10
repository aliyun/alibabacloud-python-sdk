# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHoneypotEventsRequest(DaraModel):
    def __init__(
        self,
        agent_id_list: List[str] = None,
        alarm_event_id: int = None,
        current_page: int = None,
        dealed: str = None,
        honeypot_id_list: List[str] = None,
        lang: str = None,
        page_size: int = None,
        portrait_id: str = None,
        request_id: str = None,
        risk_level_list: List[str] = None,
        src_ip: str = None,
    ):
        # The probe IDs.
        self.agent_id_list = agent_id_list
        # The ID of the alert.
        self.alarm_event_id = alarm_event_id
        # The page number.
        self.current_page = current_page
        # The status of the event. Valid values:
        # 
        # *   **y**: handled
        # *   **n**: unhandled
        # *   **a**: all statuses
        self.dealed = dealed
        # The honeypot IDs.
        self.honeypot_id_list = honeypot_id_list
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the attacker profile.
        self.portrait_id = portrait_id
        # The request ID.
        self.request_id = request_id
        # The risk levels.
        self.risk_level_list = risk_level_list
        # The source IP address of the attack.
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id_list is not None:
            result['AgentIdList'] = self.agent_id_list

        if self.alarm_event_id is not None:
            result['AlarmEventId'] = self.alarm_event_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.honeypot_id_list is not None:
            result['HoneypotIdList'] = self.honeypot_id_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.portrait_id is not None:
            result['PortraitId'] = self.portrait_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIdList') is not None:
            self.agent_id_list = m.get('AgentIdList')

        if m.get('AlarmEventId') is not None:
            self.alarm_event_id = m.get('AlarmEventId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('HoneypotIdList') is not None:
            self.honeypot_id_list = m.get('HoneypotIdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PortraitId') is not None:
            self.portrait_id = m.get('PortraitId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

