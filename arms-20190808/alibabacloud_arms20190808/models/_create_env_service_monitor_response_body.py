# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateEnvServiceMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateEnvServiceMonitorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateEnvServiceMonitorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateEnvServiceMonitorResponseBodyData(DaraModel):
    def __init__(
        self,
        matched_msg: str = None,
        matched_target_count: int = None,
        namespace: str = None,
        service_monitor_name: str = None,
    ):
        # Indicates whether targets are matched.
        self.matched_msg = matched_msg
        # The number of matched targets.
        self.matched_target_count = matched_target_count
        # The namespace.
        self.namespace = namespace
        # The name of the created ServiceMonitor.
        self.service_monitor_name = service_monitor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.matched_msg is not None:
            result['MatchedMsg'] = self.matched_msg

        if self.matched_target_count is not None:
            result['MatchedTargetCount'] = self.matched_target_count

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.service_monitor_name is not None:
            result['ServiceMonitorName'] = self.service_monitor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchedMsg') is not None:
            self.matched_msg = m.get('MatchedMsg')

        if m.get('MatchedTargetCount') is not None:
            self.matched_target_count = m.get('MatchedTargetCount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ServiceMonitorName') is not None:
            self.service_monitor_name = m.get('ServiceMonitorName')

        return self

