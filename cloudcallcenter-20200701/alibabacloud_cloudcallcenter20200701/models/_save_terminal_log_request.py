# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveTerminalLogRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        call_id: str = None,
        content: str = None,
        data_type: int = None,
        instance_id: str = None,
        job_id: str = None,
        method_name: str = None,
        status: str = None,
        unique_request_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.call_id = call_id
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_id = job_id
        self.method_name = method_name
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.unique_request_id = unique_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.content is not None:
            result['Content'] = self.content

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.status is not None:
            result['Status'] = self.status

        if self.unique_request_id is not None:
            result['UniqueRequestId'] = self.unique_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UniqueRequestId') is not None:
            self.unique_request_id = m.get('UniqueRequestId')

        return self

