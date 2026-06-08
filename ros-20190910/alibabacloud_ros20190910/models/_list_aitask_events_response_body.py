# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListAITaskEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        events: List[main_models.ListAITaskEventsResponseBodyEvents] = None,
        http_status_code: int = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The error code.
        self.code = code
        # The events.
        self.events = events
        # The HTTP status code.
        self.http_status_code = http_status_code
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The ID of the AI task.
        self.task_id = task_id
        # The state of the AI task.
        # 
        # *   PENDING
        # *   WAITING
        # *   RUNNING
        # *   SUCCESS
        # *   FAILURE
        self.task_status = task_status
        # The type of the AI task.
        # 
        # *   GenerateTemplate: The AI task is used to generate a template.
        # *   FixTemplate: The AI task is used to fix a template.
        self.task_type = task_type

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.ListAITaskEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class ListAITaskEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        create_time: str = None,
        estimated_processing_time: str = None,
        event_data: str = None,
        handler_process_status: str = None,
        handler_type: str = None,
    ):
        # The type of the agent that is used to execute the AI task.
        # 
        # Valid values:
        # 
        # *   GenerateTemplateAgent
        # *   FixUserTemplateAgent
        self.agent_type = agent_type
        # The time when the event was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The estimated execution time of the handler. Unit: seconds.
        self.estimated_processing_time = estimated_processing_time
        # The details of the event.
        self.event_data = event_data
        # The execution state of the handler that process the AI task.
        # 
        # Valid values:
        # 
        # *   SUCCESS
        # *   RUNNING
        # *   FAILURE
        self.handler_process_status = handler_process_status
        # The type of the handler that is used to execute the task.
        # 
        # Valid values:
        # 
        # *   TerraformTemplateGenerator
        # *   TemplateGenerator
        # *   ROSTemplateModifier
        # *   TerraformTemplateStaticFixer
        # *   TerraformTemplateDynamicFixer
        # *   DocumentTemplateGenerator
        # *   TerraformTemplateModifier
        # *   TemplateModifier
        # *   FixTemplateInputPreprocessor
        # *   TemplateStaticFixer
        # *   GenerateTemplateInputPreprocessor
        # *   ROSTemplateGenerator
        # *   TemplateDynamicFixer
        # *   BaseDynamicFixer
        # *   ROSTemplateStaticFixer
        # *   ROSTemplateDynamicFixer
        self.handler_type = handler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.estimated_processing_time is not None:
            result['EstimatedProcessingTime'] = self.estimated_processing_time

        if self.event_data is not None:
            result['EventData'] = self.event_data

        if self.handler_process_status is not None:
            result['HandlerProcessStatus'] = self.handler_process_status

        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EstimatedProcessingTime') is not None:
            self.estimated_processing_time = m.get('EstimatedProcessingTime')

        if m.get('EventData') is not None:
            self.event_data = m.get('EventData')

        if m.get('HandlerProcessStatus') is not None:
            self.handler_process_status = m.get('HandlerProcessStatus')

        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')

        return self

