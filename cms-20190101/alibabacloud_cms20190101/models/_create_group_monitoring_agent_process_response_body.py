# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateGroupMonitoringAgentProcessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        resource: main_models.CreateGroupMonitoringAgentProcessResponseBodyResource = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the call is successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The group process information.
        self.resource = resource
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resource') is not None:
            temp_model = main_models.CreateGroupMonitoringAgentProcessResponseBodyResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateGroupMonitoringAgentProcessResponseBodyResource(DaraModel):
    def __init__(
        self,
        group_process_id: str = None,
    ):
        # The ID of the group process.
        self.group_process_id = group_process_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_process_id is not None:
            result['GroupProcessId'] = self.group_process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupProcessId') is not None:
            self.group_process_id = m.get('GroupProcessId')

        return self

