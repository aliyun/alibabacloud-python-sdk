# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertLogCountResponseBody(DaraModel):
    def __init__(
        self,
        alert_log_count: List[main_models.DescribeAlertLogCountResponseBodyAlertLogCount] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The statistics of alert logs.
        self.alert_log_count = alert_log_count
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.alert_log_count:
            for v1 in self.alert_log_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertLogCount'] = []
        if self.alert_log_count is not None:
            for k1 in self.alert_log_count:
                result['AlertLogCount'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_log_count = []
        if m.get('AlertLogCount') is not None:
            for k1 in m.get('AlertLogCount'):
                temp_model = main_models.DescribeAlertLogCountResponseBodyAlertLogCount()
                self.alert_log_count.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertLogCountResponseBodyAlertLogCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        logs: List[main_models.DescribeAlertLogCountResponseBodyAlertLogCountLogs] = None,
    ):
        # The number of alert logs.
        self.count = count
        # The details about alert logs.
        self.logs = logs

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribeAlertLogCountResponseBodyAlertLogCountLogs()
                self.logs.append(temp_model.from_map(k1))

        return self

class DescribeAlertLogCountResponseBodyAlertLogCountLogs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the dimension field based on which alert logs are aggregated.
        self.name = name
        # The value of the dimension field based on which alert logs are aggregated.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

