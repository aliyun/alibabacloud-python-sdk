# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZoneRecordsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        tag: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The keyword of the hostname. The value is not case-sensitive. You can set SearchMode to LIKE or EXACT. The default value of SearchMode is EXACT.
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
        # The search mode. Valid values:
        # 
        # *   **LIKE**: fuzzy search
        # *   **EXACT** (default): exact search
        # 
        # The value of Keyword is the search scope.
        self.search_mode = search_mode
        # The tag added to the DNS record. Valid values:
        # 
        # *   ecs: If you set Tag to ecs, the DNS records added to the hostnames of Elastic Compute Service (ECS) instances in the zone are queried.
        # *   If Tag is left empty, the DNS records in the zone are queried.
        self.tag = tag
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

