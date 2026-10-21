# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.GetTaskResponseBodyTask = None,
    ):
        # The ID of a request.
        self.request_id = request_id
        # The information about the task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task is not None:
            result['task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('task') is not None:
            temp_model = main_models.GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('task'))

        return self

class GetTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error: main_models.GetTaskResponseBodyTaskError = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_path: str = None,
        resource_type: str = None,
        status: str = None,
        task_action: str = None,
        task_id: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The error returned for the task.
        self.error = error
        # The code of the service.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The path of the resources. The relative resource ID. The resource path contains the complete resource location (parent resource/child resource).
        self.resource_path = resource_path
        # The resource type.
        self.resource_type = resource_type
        # The task state.
        # 
        # Pending
        # 
        # Running
        # 
        # Succeeded
        # 
        # Failed
        # 
        # Cancelling
        # 
        # Cancelled.
        self.status = status
        # The type of the task operation. Valid values: Create, Update, and Delete.
        self.task_action = task_action
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.product is not None:
            result['product'] = self.product

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        if self.task_action is not None:
            result['taskAction'] = self.task_action

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('error') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class GetTaskResponseBodyTaskError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

