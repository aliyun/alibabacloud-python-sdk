# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmAlertLogsRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        end_timestamp: int = None,
        entity_type: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
    ):
        # Alert type:
        # - ALERT
        # - RESUME
        self.action_type = action_type
        # The end time of the query (timestamp).
        # 
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # Alarm object types:
        # - GTM_ADDRESS: Address
        # - GTM_ADDRESS_POOL: Address Pool
        # - GTM_INSTANCE: Instance
        # - GTM_MONITOR_TEMPLATE: Health Check Template
        self.entity_type = entity_type
        # Search keyword, usually an address ID, address pool ID, domain information, etc.
        self.keyword = keyword
        # Language type of the returned information:
        # - zh-CN: Chinese
        # - en-US: English
        self.lang = lang
        # Current page number, starting from **1**, default is **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of 100 and a default of 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The start time of the query (timestamp).
        # 
        # This parameter is required.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

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

        return self

