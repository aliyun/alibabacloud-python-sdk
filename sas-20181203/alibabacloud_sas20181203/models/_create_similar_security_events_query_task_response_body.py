# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateSimilarSecurityEventsQueryTaskResponseBody(DaraModel):
    def __init__(
        self,
        create_similar_security_events_query_task_response: main_models.CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse = None,
        request_id: str = None,
    ):
        # The information about the task that queries alert events of the same alert type.
        self.create_similar_security_events_query_task_response = create_similar_security_events_query_task_response
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.create_similar_security_events_query_task_response:
            self.create_similar_security_events_query_task_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_similar_security_events_query_task_response is not None:
            result['CreateSimilarSecurityEventsQueryTaskResponse'] = self.create_similar_security_events_query_task_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSimilarSecurityEventsQueryTaskResponse') is not None:
            temp_model = main_models.CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse()
            self.create_similar_security_events_query_task_response = temp_model.from_map(m.get('CreateSimilarSecurityEventsQueryTaskResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateSimilarSecurityEventsQueryTaskResponseBodyCreateSimilarSecurityEventsQueryTaskResponse(DaraModel):
    def __init__(
        self,
        status: str = None,
        task_id: int = None,
    ):
        # The status of the task. Valid values:
        # 
        # *   **New**: The task is created.
        # *   **RetrievingData**: Data is being retrieved.
        # *   **DataRetrieved**: Data is retrieved.
        # *   **Processing**: The task is running.
        # *   **Success**: The task is successful.
        # *   **Failed**: The task failed.
        # *   **PartialFailed**: The task partially failed.
        self.status = status
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

