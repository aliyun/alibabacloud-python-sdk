# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetTicketResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTicketResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTicketResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTicketResponseBodyData(DaraModel):
    def __init__(
        self,
        assignee: str = None,
        assignee_name: str = None,
        category_id: str = None,
        category_name: str = None,
        close_code: str = None,
        comment: str = None,
        context: str = None,
        created_time: int = None,
        creator: str = None,
        creator_name: str = None,
        current_task_id: str = None,
        current_task_name: str = None,
        current_task_start_time: int = None,
        customer_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        source: str = None,
        start_time: int = None,
        state: str = None,
        template_id: str = None,
        template_version: str = None,
        ticket_id: str = None,
        title: str = None,
        updated_time: int = None,
    ):
        self.assignee = assignee
        self.assignee_name = assignee_name
        self.category_id = category_id
        self.category_name = category_name
        self.close_code = close_code
        self.comment = comment
        self.context = context
        self.created_time = created_time
        self.creator = creator
        self.creator_name = creator_name
        self.current_task_id = current_task_id
        self.current_task_name = current_task_name
        self.current_task_start_time = current_task_start_time
        self.customer_id = customer_id
        self.end_time = end_time
        self.instance_id = instance_id
        self.job_id = job_id
        self.source = source
        self.start_time = start_time
        self.state = state
        self.template_id = template_id
        self.template_version = template_version
        self.ticket_id = ticket_id
        self.title = title
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee is not None:
            result['Assignee'] = self.assignee

        if self.assignee_name is not None:
            result['AssigneeName'] = self.assignee_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.close_code is not None:
            result['CloseCode'] = self.close_code

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.context is not None:
            result['Context'] = self.context

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.current_task_id is not None:
            result['CurrentTaskId'] = self.current_task_id

        if self.current_task_name is not None:
            result['CurrentTaskName'] = self.current_task_name

        if self.current_task_start_time is not None:
            result['CurrentTaskStartTime'] = self.current_task_start_time

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.title is not None:
            result['Title'] = self.title

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Assignee') is not None:
            self.assignee = m.get('Assignee')

        if m.get('AssigneeName') is not None:
            self.assignee_name = m.get('AssigneeName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CloseCode') is not None:
            self.close_code = m.get('CloseCode')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CurrentTaskId') is not None:
            self.current_task_id = m.get('CurrentTaskId')

        if m.get('CurrentTaskName') is not None:
            self.current_task_name = m.get('CurrentTaskName')

        if m.get('CurrentTaskStartTime') is not None:
            self.current_task_start_time = m.get('CurrentTaskStartTime')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

