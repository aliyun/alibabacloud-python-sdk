# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccountSafetyIncidentRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        case_code: str = None,
        current: str = None,
        event_id: str = None,
        page_size: str = None,
        punish_end_time: str = None,
        punish_start_time: str = None,
        resource_id: str = None,
        status: str = None,
    ):
        # The language. Default value: zh.
        # 
        # - **zh**: Chinese.
        # - **en**: English.
        self.aliyun_lang = aliyun_lang
        # The event name code.
        self.case_code = case_code
        # The current page number. The value must be greater than 0.
        self.current = current
        # The event ID.
        self.event_id = event_id
        # The number of records per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The end time of the control action.
        # 
        # > Format: yyyy-MM-dd HH:mm:ss
        self.punish_end_time = punish_end_time
        # The start time of the control action.
        # 
        # > Format: yyyy-MM-dd HH:mm:ss
        self.punish_start_time = punish_start_time
        # The resource ID.
        self.resource_id = resource_id
        # The event status. Valid values:
        # 
        # - **Executing**: In progress.
        # - **Removed**: Removed.
        # - **Alerting**: Alerting.
        # - **Ended**: Ended.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.case_code is not None:
            result['CaseCode'] = self.case_code

        if self.current is not None:
            result['Current'] = self.current

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.punish_end_time is not None:
            result['PunishEndTime'] = self.punish_end_time

        if self.punish_start_time is not None:
            result['PunishStartTime'] = self.punish_start_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('CaseCode') is not None:
            self.case_code = m.get('CaseCode')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PunishEndTime') is not None:
            self.punish_end_time = m.get('PunishEndTime')

        if m.get('PunishStartTime') is not None:
            self.punish_start_time = m.get('PunishStartTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

