# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListTicketTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListTicketTasksResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTicketTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTicketTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        assignee: str = None,
        assignee_name: str = None,
        comment: str = None,
        end_time: int = None,
        file_keys: List[str] = None,
        file_urls: List[str] = None,
        instance_id: str = None,
        start_time: int = None,
        task_definition_node_id: str = None,
        task_definition_node_type: str = None,
        task_id: str = None,
        task_name: str = None,
        ticket_id: str = None,
    ):
        self.action = action
        self.assignee = assignee
        self.assignee_name = assignee_name
        self.comment = comment
        self.end_time = end_time
        self.file_keys = file_keys
        self.file_urls = file_urls
        self.instance_id = instance_id
        self.start_time = start_time
        self.task_definition_node_id = task_definition_node_id
        self.task_definition_node_type = task_definition_node_type
        self.task_id = task_id
        self.task_name = task_name
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.assignee is not None:
            result['Assignee'] = self.assignee

        if self.assignee_name is not None:
            result['AssigneeName'] = self.assignee_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_keys is not None:
            result['FileKeys'] = self.file_keys

        if self.file_urls is not None:
            result['FileUrls'] = self.file_urls

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_definition_node_id is not None:
            result['TaskDefinitionNodeId'] = self.task_definition_node_id

        if self.task_definition_node_type is not None:
            result['TaskDefinitionNodeType'] = self.task_definition_node_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Assignee') is not None:
            self.assignee = m.get('Assignee')

        if m.get('AssigneeName') is not None:
            self.assignee_name = m.get('AssigneeName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileKeys') is not None:
            self.file_keys = m.get('FileKeys')

        if m.get('FileUrls') is not None:
            self.file_urls = m.get('FileUrls')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskDefinitionNodeId') is not None:
            self.task_definition_node_id = m.get('TaskDefinitionNodeId')

        if m.get('TaskDefinitionNodeType') is not None:
            self.task_definition_node_type = m.get('TaskDefinitionNodeType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        return self

