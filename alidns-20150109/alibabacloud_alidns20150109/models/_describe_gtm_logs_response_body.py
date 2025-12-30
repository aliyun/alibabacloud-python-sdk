# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: main_models.DescribeGtmLogsResponseBodyLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The list of logs returned.
        self.logs = logs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned on all pages.
        self.total_items = total_items
        # The total number of pages returned.
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
            temp_model = main_models.DescribeGtmLogsResponseBodyLogs()
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

class DescribeGtmLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        log: List[main_models.DescribeGtmLogsResponseBodyLogsLog] = None,
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
                temp_model = main_models.DescribeGtmLogsResponseBodyLogsLog()
                self.log.append(temp_model.from_map(k1))

        return self

class DescribeGtmLogsResponseBodyLogsLog(DaraModel):
    def __init__(
        self,
        content: str = None,
        entity_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
        id: int = None,
        oper_action: str = None,
        oper_ip: str = None,
        oper_time: str = None,
        oper_timestamp: int = None,
    ):
        # The formatted message content.
        self.content = content
        # The ID of the object that was operated on.
        self.entity_id = entity_id
        # The name of the object that was operated on.
        self.entity_name = entity_name
        # The type of the object that was operated on.
        self.entity_type = entity_type
        # The ID of the log record.
        self.id = id
        # The operation performed.
        self.oper_action = oper_action
        # The IP address subject to the operation.
        self.oper_ip = oper_ip
        # The time when the operation was performed.
        self.oper_time = oper_time
        # A timestamp that indicates the time when the operation was performed.
        self.oper_timestamp = oper_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.id is not None:
            result['Id'] = self.id

        if self.oper_action is not None:
            result['OperAction'] = self.oper_action

        if self.oper_ip is not None:
            result['OperIp'] = self.oper_ip

        if self.oper_time is not None:
            result['OperTime'] = self.oper_time

        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')

        if m.get('OperIp') is not None:
            self.oper_ip = m.get('OperIp')

        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')

        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')

        return self

