# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListCloudGtmAlertLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: main_models.ListCloudGtmAlertLogsResponseBodyLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The alert logs.
        self.logs = logs
        # Current page number, starting from 1, default is 1.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of 100 and a default of 20.
        self.page_size = page_size
        # Unique request identification code.
        self.request_id = request_id
        # Total number of alarm log entries.
        self.total_items = total_items
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            temp_model = main_models.ListCloudGtmAlertLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m.get('Logs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListCloudGtmAlertLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        log: List[main_models.ListCloudGtmAlertLogsResponseBodyLogsLog] = None,
    ):
        self.log = log

    def validate(self):
        if self.log:
            for v1 in self.log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Log'] = []
        if self.log is not None:
            for k1 in self.log:
                result['Log'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k1 in m.get('Log'):
                temp_model = main_models.ListCloudGtmAlertLogsResponseBodyLogsLog()
                self.log.append(temp_model.from_map(k1))

        return self

class ListCloudGtmAlertLogsResponseBodyLogsLog(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        content: str = None,
        entity_type: str = None,
        timestamp: int = None,
    ):
        # Alert type:
        # - ALERT
        # - RESUME
        self.action_type = action_type
        # The alert content.
        self.content = content
        # Alarm object types:
        # - GTM_ADDRESS: Address
        # - GTM_ADDRESS_POOL: Address Pool
        # - GTM_INSTANCE: Instance
        # - GTM_MONITOR_TEMPLATE: Health Check Template
        self.entity_type = entity_type
        # Alert log time (timestamp).
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.content is not None:
            result['Content'] = self.content

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

