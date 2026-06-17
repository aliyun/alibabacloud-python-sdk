# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInvadeEventListRequest(DaraModel):
    def __init__(
        self,
        assets_ip: str = None,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        current_page: str = None,
        end_time: str = None,
        event_key: str = None,
        event_name: str = None,
        event_uuid: str = None,
        is_ignore: str = None,
        lang: str = None,
        member_uid: int = None,
        page_size: str = None,
        process_status_list: List[int] = None,
        risk_level: List[int] = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The IP address of the affected asset.
        self.assets_ip = assets_ip
        # The ID of the affected instance.
        self.assets_instance_id = assets_instance_id
        # The name of the affected instance.
        self.assets_instance_name = assets_instance_name
        # The number of the page to return.
        # 
        # Default: 1.
        self.current_page = current_page
        # The end of the time range to query. This must be a UNIX timestamp in seconds. If you omit this parameter, the query defaults to the current time.
        self.end_time = end_time
        # A unique identifier for the breach awareness event.
        self.event_key = event_key
        # The name of the breach awareness event.
        self.event_name = event_name
        # The universally unique identifier (UUID) of the breach awareness event.
        self.event_uuid = event_uuid
        # Specifies whether to query for ignored breach awareness events. Valid values:
        # 
        # - **true**: Ignored.
        # 
        # - **false**: Not ignored.
        self.is_ignore = is_ignore
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member account.
        self.member_uid = member_uid
        # The number of entries to return per page.
        # 
        # Default: 6. Maximum: 10.
        self.page_size = page_size
        # An array of processing statuses to filter events by. Only events with a status specified in this array are returned.
        self.process_status_list = process_status_list
        # An array of risk levels to filter events by. Only events with a risk level specified in this array are returned.
        self.risk_level = risk_level
        # The source IP address that initiated the event.
        self.source_ip = source_ip
        # The start of the time range to query. This must be a UNIX timestamp in seconds. If you omit this parameter, the query defaults to the last 30 days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_ip is not None:
            result['AssetsIP'] = self.assets_ip

        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_status_list is not None:
            result['ProcessStatusList'] = self.process_status_list

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsIP') is not None:
            self.assets_ip = m.get('AssetsIP')

        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessStatusList') is not None:
            self.process_status_list = m.get('ProcessStatusList')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

