# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListSynchronizationJobsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: int = None,
        filters: List[main_models.ListSynchronizationJobsRequestFilters] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        status: str = None,
        target_ids: List[str] = None,
        target_type: str = None,
    ):
        # 同步方向[ingress,egress]
        self.direction = direction
        # 同步结束时间
        self.end_time = end_time
        self.filters = filters
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 分页查询时每页行数。默认值为20，最大值为100。
        self.max_results = max_results
        # 查询凭证（Token），取值为上一次API调用返回的NextToken参数值。
        self.next_token = next_token
        # 当前查询的列表页码，默认为1。
        self.page_number = page_number
        # 当前查询的列表页码，默认为20。
        self.page_size = page_size
        # 同步开始时间
        self.start_time = start_time
        # 同步状态[pending,running,suspending,failed,partial_success,success]
        self.status = status
        # 同步目标ID
        self.target_ids = target_ids
        # 同步目标类型[identity_provider,organizational_unit,application,user]
        self.target_type = target_type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListSynchronizationJobsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class ListSynchronizationJobsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

