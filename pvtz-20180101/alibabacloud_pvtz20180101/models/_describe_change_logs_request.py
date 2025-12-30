# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChangeLogsRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        entity_type: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The end of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_timestamp = end_timestamp
        # The type of operation logs. Valid values:
        # 
        # *   **PV_ZONE**: the logs that record the operations on built-in authoritative zones
        # *   **PV_RECORD**: the logs that record the operations on DNS records
        # *   **RESOLVER_RULE**: the logs that record the operations on forwarding rules
        # *   **CUSTOM_LINE**: the logs that record the operations on user-defined lines
        # *   **RESOLVER_ENDPOINT**: the logs that record the operations on outbound endpoints
        # *   **INBOUND_ENDPOINT**: the logs that record the operations on inbound endpoints
        # *   **CACHE_RESERVE_DOMAIN**: the logs that record the operations on cache retention domain names
        # 
        # >  If you set EntityType to other values, all types of logs are queried.
        self.entity_type = entity_type
        # The keyword of the operation or the operation content. Fuzzy search is supported. The value is not case-sensitive.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The beginning of the time range to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_timestamp = start_timestamp
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. Valid values:
        # 
        # *   If you set ZoneId to a zone ID, the logs that record the operations on the DNS records of the specified zone are queried.\\
        # 
        # *   If you leave ZoneId empty, the logs that record the operations on all zones and the DNS records of these zones that belong to the current Alibaba Cloud account are queried.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

