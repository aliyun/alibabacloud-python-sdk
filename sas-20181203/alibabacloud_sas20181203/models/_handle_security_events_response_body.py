# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class HandleSecurityEventsResponseBody(DaraModel):
    def __init__(
        self,
        handle_security_events_response: main_models.HandleSecurityEventsResponseBodyHandleSecurityEventsResponse = None,
        request_id: str = None,
    ):
        # The handling result of the alert events.
        self.handle_security_events_response = handle_security_events_response
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.handle_security_events_response:
            self.handle_security_events_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handle_security_events_response is not None:
            result['HandleSecurityEventsResponse'] = self.handle_security_events_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandleSecurityEventsResponse') is not None:
            temp_model = main_models.HandleSecurityEventsResponseBodyHandleSecurityEventsResponse()
            self.handle_security_events_response = temp_model.from_map(m.get('HandleSecurityEventsResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class HandleSecurityEventsResponseBodyHandleSecurityEventsResponse(DaraModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        # The ID of the task to handle the alert events.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

