# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeEventLevelCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        event_levels: main_models.DescribeEventLevelCountResponseBodyEventLevels = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The statistics of alerts by risk level.
        self.event_levels = event_levels
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.event_levels:
            self.event_levels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.event_levels is not None:
            result['EventLevels'] = self.event_levels.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EventLevels') is not None:
            temp_model = main_models.DescribeEventLevelCountResponseBodyEventLevels()
            self.event_levels = temp_model.from_map(m.get('EventLevels'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEventLevelCountResponseBodyEventLevels(DaraModel):
    def __init__(
        self,
        remind: int = None,
        serious: int = None,
        suspicious: int = None,
    ):
        # The number of alerts whose Emergency level is Reminder.
        self.remind = remind
        # The number of alerts whose Emergency level is Urgent.
        self.serious = serious
        # The number of alerts whose Emergency level is Suspicious.
        self.suspicious = suspicious

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remind is not None:
            result['Remind'] = self.remind

        if self.serious is not None:
            result['Serious'] = self.serious

        if self.suspicious is not None:
            result['Suspicious'] = self.suspicious

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remind') is not None:
            self.remind = m.get('Remind')

        if m.get('Serious') is not None:
            self.serious = m.get('Serious')

        if m.get('Suspicious') is not None:
            self.suspicious = m.get('Suspicious')

        return self

