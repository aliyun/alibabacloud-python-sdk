# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetComputeEngineJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        configs: Dict[str, Any] = None,
        create_time: str = None,
        endpoint: str = None,
        extra_info: Dict[str, Any] = None,
        finish_time: str = None,
        job_id: str = None,
        job_name: str = None,
        job_type: str = None,
        last_error_code: str = None,
        last_error_info: str = None,
        request_id: str = None,
        state: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.configs = configs
        self.create_time = create_time
        self.endpoint = endpoint
        self.extra_info = extra_info
        self.finish_time = finish_time
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.last_error_code = last_error_code
        self.last_error_info = last_error_info
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.configs is not None:
            result['Configs'] = self.configs

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code

        if self.last_error_info is not None:
            result['LastErrorInfo'] = self.last_error_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')

        if m.get('LastErrorInfo') is not None:
            self.last_error_info = m.get('LastErrorInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

