# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetJobResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetJobResourceUsageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetJobResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetJobResourceUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        job_resource_usage_list: List[main_models.GetJobResourceUsageResponseBodyDataJobResourceUsageList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.job_resource_usage_list = job_resource_usage_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.job_resource_usage_list:
            for v1 in self.job_resource_usage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobResourceUsageList'] = []
        if self.job_resource_usage_list is not None:
            for k1 in self.job_resource_usage_list:
                result['jobResourceUsageList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_resource_usage_list = []
        if m.get('jobResourceUsageList') is not None:
            for k1 in m.get('jobResourceUsageList'):
                temp_model = main_models.GetJobResourceUsageResponseBodyDataJobResourceUsageList()
                self.job_resource_usage_list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetJobResourceUsageResponseBodyDataJobResourceUsageList(DaraModel):
    def __init__(
        self,
        cu_usage: int = None,
        date: str = None,
        job_owner: str = None,
        memory_usage: int = None,
        quota_nickname: str = None,
    ):
        self.cu_usage = cu_usage
        self.date = date
        self.job_owner = job_owner
        self.memory_usage = memory_usage
        self.quota_nickname = quota_nickname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage

        if self.date is not None:
            result['date'] = self.date

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        return self

