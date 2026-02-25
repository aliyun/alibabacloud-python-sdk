# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListMediaWorkflowExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        media_workflow_execution_list: main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionList = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        self.media_workflow_execution_list = media_workflow_execution_list
        # The returned value of NextPageToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_workflow_execution_list:
            self.media_workflow_execution_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_workflow_execution_list is not None:
            result['MediaWorkflowExecutionList'] = self.media_workflow_execution_list.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaWorkflowExecutionList') is not None:
            temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionList()
            self.media_workflow_execution_list = temp_model.from_map(m.get('MediaWorkflowExecutionList'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionList(DaraModel):
    def __init__(
        self,
        media_workflow_execution: List[main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecution] = None,
    ):
        self.media_workflow_execution = media_workflow_execution

    def validate(self):
        if self.media_workflow_execution:
            for v1 in self.media_workflow_execution:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaWorkflowExecution'] = []
        if self.media_workflow_execution is not None:
            for k1 in self.media_workflow_execution:
                result['MediaWorkflowExecution'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_workflow_execution = []
        if m.get('MediaWorkflowExecution') is not None:
            for k1 in m.get('MediaWorkflowExecution'):
                temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecution()
                self.media_workflow_execution.append(temp_model.from_map(k1))

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecution(DaraModel):
    def __init__(
        self,
        activity_list: main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityList = None,
        creation_time: str = None,
        input: main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInput = None,
        media_id: str = None,
        media_workflow_id: str = None,
        name: str = None,
        run_id: str = None,
        state: str = None,
    ):
        self.activity_list = activity_list
        self.creation_time = creation_time
        self.input = input
        self.media_id = media_id
        self.media_workflow_id = media_workflow_id
        self.name = name
        self.run_id = run_id
        self.state = state

    def validate(self):
        if self.activity_list:
            self.activity_list.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_list is not None:
            result['ActivityList'] = self.activity_list.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.name is not None:
            result['Name'] = self.name

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityList') is not None:
            temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityList()
            self.activity_list = temp_model.from_map(m.get('ActivityList'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Input') is not None:
            temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInput(DaraModel):
    def __init__(
        self,
        input_file: main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInputInputFile = None,
        user_data: str = None,
    ):
        self.input_file = input_file
        self.user_data = user_data

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInputInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionInputInputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityList(DaraModel):
    def __init__(
        self,
        activity: List[main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivity] = None,
    ):
        self.activity = activity

    def validate(self):
        if self.activity:
            for v1 in self.activity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Activity'] = []
        if self.activity is not None:
            for k1 in self.activity:
                result['Activity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity = []
        if m.get('Activity') is not None:
            for k1 in m.get('Activity'):
                temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivity()
                self.activity.append(temp_model.from_map(k1))

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivity(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        job_id: str = None,
        mnsmessage_result: main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivityMNSMessageResult = None,
        message: str = None,
        name: str = None,
        start_time: str = None,
        state: str = None,
        type: str = None,
    ):
        self.code = code
        self.end_time = end_time
        self.job_id = job_id
        self.mnsmessage_result = mnsmessage_result
        self.message = message
        self.name = name
        self.start_time = start_time
        self.state = state
        self.type = type

    def validate(self):
        if self.mnsmessage_result:
            self.mnsmessage_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.mnsmessage_result is not None:
            result['MNSMessageResult'] = self.mnsmessage_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivityMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListMediaWorkflowExecutionsResponseBodyMediaWorkflowExecutionListMediaWorkflowExecutionActivityListActivityMNSMessageResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        message_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

