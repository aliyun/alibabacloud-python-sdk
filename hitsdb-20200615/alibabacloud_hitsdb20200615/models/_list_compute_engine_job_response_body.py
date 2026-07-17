# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ListComputeEngineJobResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        job_list: List[main_models.ListComputeEngineJobResponseBodyJobList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.job_list = job_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.ListComputeEngineJobResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListComputeEngineJobResponseBodyJobList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: int = None,
        endpoint: str = None,
        extra_info: Dict[str, Any] = None,
        finish_time: int = None,
        job_id: str = None,
        message: str = None,
        reason: str = None,
        started_at: str = None,
        state: str = None,
    ):
        self.app_name = app_name
        self.create_time = create_time
        self.endpoint = endpoint
        self.extra_info = extra_info
        self.finish_time = finish_time
        self.job_id = job_id
        self.message = message
        self.reason = reason
        self.started_at = started_at
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

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

        if self.message is not None:
            result['Message'] = self.message

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.started_at is not None:
            result['StartedAt'] = self.started_at

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

