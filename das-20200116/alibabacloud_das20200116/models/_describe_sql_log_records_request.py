# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogRecordsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filters: List[main_models.DescribeSqlLogRecordsRequestFilters] = None,
        instance_id: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. This value is a UNIX timestamp. Unit: millisecond.
        self.end_time = end_time
        # The filter conditions.
        self.filters = filters
        # The database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # *   For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this parameter is valid only for instances of the Cluster Edition. If you do not specify this parameter, the log details of the primary node is queried by default.
        # *   For PolarDB-X 2.0 instances, set this parameter to **polarx_cn** if the node is a compute node, or **polarx_dn** if the node is a data node.
        self.node_id = node_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The role of the node of the PolarDB-X 2.0 instance. Valid values:
        # 
        # *   \\*\\*polarx_cn\\*\\*: compute node
        # *   \\*\\*polarx_dn\\*\\*: data node
        self.role = role
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: millisecond.
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

        if self.role is not None:
            result['Role'] = self.role

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
                temp_model = main_models.DescribeSqlLogRecordsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSqlLogRecordsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter parameter.
        # 
        # >  For more information about the supported filter parameters and their valid values, see the **Supported parameters and values for Key** section of this topic.
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

