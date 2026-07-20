# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryResourceControlEventsRequest(DaraModel):
    def __init__(
        self,
        action_code: str = None,
        action_codes: List[str] = None,
        aliyun_lang: str = None,
        business_code: str = None,
        case_codes_prefix: List[str] = None,
        current: int = None,
        domain: str = None,
        event_code: str = None,
        event_codes: List[str] = None,
        event_id: str = None,
        event_id_list: List[str] = None,
        exclude_action_codes: List[str] = None,
        exclude_event_codes: List[str] = None,
        exclude_reasons: List[str] = None,
        include_reasons: List[str] = None,
        instance_id: str = None,
        ip: str = None,
        page_size: int = None,
        punish_end_time: str = None,
        punish_start_time: str = None,
        reason: str = None,
        source_codes: List[str] = None,
        status: str = None,
        status_list: List[str] = None,
        url: str = None,
    ):
        self.action_code = action_code
        self.action_codes = action_codes
        self.aliyun_lang = aliyun_lang
        self.business_code = business_code
        self.case_codes_prefix = case_codes_prefix
        self.current = current
        self.domain = domain
        self.event_code = event_code
        self.event_codes = event_codes
        self.event_id = event_id
        self.event_id_list = event_id_list
        self.exclude_action_codes = exclude_action_codes
        self.exclude_event_codes = exclude_event_codes
        self.exclude_reasons = exclude_reasons
        self.include_reasons = include_reasons
        self.instance_id = instance_id
        self.ip = ip
        self.page_size = page_size
        self.punish_end_time = punish_end_time
        self.punish_start_time = punish_start_time
        self.reason = reason
        self.source_codes = source_codes
        self.status = status
        self.status_list = status_list
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_code is not None:
            result['ActionCode'] = self.action_code

        if self.action_codes is not None:
            result['ActionCodes'] = self.action_codes

        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.business_code is not None:
            result['BusinessCode'] = self.business_code

        if self.case_codes_prefix is not None:
            result['CaseCodesPrefix'] = self.case_codes_prefix

        if self.current is not None:
            result['Current'] = self.current

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_codes is not None:
            result['EventCodes'] = self.event_codes

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        if self.exclude_action_codes is not None:
            result['ExcludeActionCodes'] = self.exclude_action_codes

        if self.exclude_event_codes is not None:
            result['ExcludeEventCodes'] = self.exclude_event_codes

        if self.exclude_reasons is not None:
            result['ExcludeReasons'] = self.exclude_reasons

        if self.include_reasons is not None:
            result['IncludeReasons'] = self.include_reasons

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.punish_end_time is not None:
            result['PunishEndTime'] = self.punish_end_time

        if self.punish_start_time is not None:
            result['PunishStartTime'] = self.punish_start_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source_codes is not None:
            result['SourceCodes'] = self.source_codes

        if self.status is not None:
            result['Status'] = self.status

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')

        if m.get('ActionCodes') is not None:
            self.action_codes = m.get('ActionCodes')

        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')

        if m.get('CaseCodesPrefix') is not None:
            self.case_codes_prefix = m.get('CaseCodesPrefix')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventCodes') is not None:
            self.event_codes = m.get('EventCodes')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        if m.get('ExcludeActionCodes') is not None:
            self.exclude_action_codes = m.get('ExcludeActionCodes')

        if m.get('ExcludeEventCodes') is not None:
            self.exclude_event_codes = m.get('ExcludeEventCodes')

        if m.get('ExcludeReasons') is not None:
            self.exclude_reasons = m.get('ExcludeReasons')

        if m.get('IncludeReasons') is not None:
            self.include_reasons = m.get('IncludeReasons')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PunishEndTime') is not None:
            self.punish_end_time = m.get('PunishEndTime')

        if m.get('PunishStartTime') is not None:
            self.punish_start_time = m.get('PunishStartTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SourceCodes') is not None:
            self.source_codes = m.get('SourceCodes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

