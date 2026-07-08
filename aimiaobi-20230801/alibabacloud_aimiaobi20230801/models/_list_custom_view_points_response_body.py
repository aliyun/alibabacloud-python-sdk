# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListCustomViewPointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCustomViewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of results returned.
        self.max_results = max_results
        # The error description.
        self.message = message
        # The token for the next page of results.
        self.next_token = next_token
        # The unique identifier of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. \\`true\\`: The request was successful. \\`false\\`: The request failed.
        self.success = success
        # The total number of entries.
        self.total_count = total_count

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCustomViewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomViewPointsResponseBodyData(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        attitude: str = None,
        create_time: str = None,
        create_user: str = None,
        id: str = None,
        status: str = None,
        task_error_message: str = None,
        task_status: int = None,
        view_points: List[main_models.ListCustomViewPointsResponseBodyDataViewPoints] = None,
    ):
        # The ID of the asynchronous task that analyzes the custom viewpoint.
        self.async_task_id = async_task_id
        # The viewpoint.
        self.attitude = attitude
        # The time when the viewpoint was created.
        self.create_time = create_time
        # The ID of the user who created the viewpoint.
        self.create_user = create_user
        # The ID of the custom viewpoint.
        self.id = id
        # The task execution status. Valid values: PENDING, RUNNING, SUCCEEDED, SUSPENDED, FAILED, and CANCELED.
        self.status = status
        # The error message for the task execution.
        self.task_error_message = task_error_message
        # The task execution status. 0: PENDING, 1: RUNNING, 2: SUCCEEDED, 3: PAUSED, 4: FAILED (retriable), 5: FAILED (non-retriable), 6: CANCELED.
        self.task_status = task_status
        # A list of topic selection viewpoints.
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.ListCustomViewPointsResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class ListCustomViewPointsResponseBodyDataViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.ListCustomViewPointsResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        # The outline.
        self.outlines = outlines
        # The generated viewpoint.
        self.point = point
        # The summary.
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.ListCustomViewPointsResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class ListCustomViewPointsResponseBodyDataViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        # The outline.
        self.outline = outline
        # The summary of the outline.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

