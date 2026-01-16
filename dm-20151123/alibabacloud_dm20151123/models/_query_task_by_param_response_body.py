# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryTaskByParamResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryTaskByParamResponseBodyData = None,
    ):
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Returned results
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryTaskByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryTaskByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        task: List[main_models.QueryTaskByParamResponseBodyDataTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('task') is not None:
            for k1 in m.get('task'):
                temp_model = main_models.QueryTaskByParamResponseBodyDataTask()
                self.task.append(temp_model.from_map(k1))

        return self

class QueryTaskByParamResponseBodyDataTask(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        config_set_id: str = None,
        config_set_name: str = None,
        create_time: str = None,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
        receivers_name: str = None,
        request_count: str = None,
        tag_name: str = None,
        task_id: str = None,
        task_status: str = None,
        template_name: str = None,
        utc_create_time: int = None,
    ):
        # Address type, sending address: 1; random address: 0;
        self.address_type = address_type
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Creation time
        self.create_time = create_time
        # dedicated IP pool ID.
        self.ip_pool_id = ip_pool_id
        # dedicated IP pool name.
        self.ip_pool_name = ip_pool_name
        # Receiver\\"s name
        self.receivers_name = receivers_name
        # Request count
        self.request_count = request_count
        # Tag
        self.tag_name = tag_name
        # Task ID
        self.task_id = task_id
        # Task status, sent successfully: 1
        self.task_status = task_status
        # Template name
        self.template_name = template_name
        # Creation time in UTC format
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id

        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')

        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')

        return self

