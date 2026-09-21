# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogTasksRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filters: List[main_models.DescribeSqlLogTasksRequestFilters] = None,
        instance_id: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The end time of the query. Specify a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The list of query filter conditions.
        self.filters = filters
        # The database instance ID.
        self.instance_id = instance_id
        # The node ID.
        # >This parameter is applicable only to Cluster Edition instances. You can specify a node to query its batch tasks. If you do not specify this parameter, the batch tasks of the primary node are returned by default.
        self.node_id = node_id
        # The page number for the paging query. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The maximum number of records per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The start time of the query. Specify a UNIX timestamp in milliseconds.
        self.start_time = start_time

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeSqlLogTasksRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSqlLogTasksRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter parameter.
        # 
        # > For supported filter parameters and their values, refer to **Supplementary description of request parameters**.
        self.key = key
        # The value of the filter parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

