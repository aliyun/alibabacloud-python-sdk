# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class CreateSqlLogTaskRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filters: List[main_models.CreateSqlLogTaskRequestFilters] = None,
        instance_id: str = None,
        name: str = None,
        node_id: str = None,
        role: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # The end of the time range to query. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time
        # The filter conditions.
        self.filters = filters
        # The ID of the database instance.
        self.instance_id = instance_id
        # The name of the task.
        self.name = name
        # The node ID.
        # 
        # >  This parameter is available only for instances that run in a cluster architecture. You can specify this parameter to query the offline tasks of a specific node. By default, if this parameter is not specified, the information about the offline tasks of the primary node is returned.
        self.node_id = node_id
        # The role of the node of the PolarDB-X 2.0 database instance. Valid values:
        # 
        # *   **polarx_cn**: compute node
        # *   **polarx_dn**: data node
        self.role = role
        # The beginning of the time range to query. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time
        # The type of the task. Valid values:
        # 
        # *   **Export**
        # *   **Query**
        # *   **Insight**
        self.type = type

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

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.role is not None:
            result['Role'] = self.role

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.CreateSqlLogTaskRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateSqlLogTaskRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter parameter.
        # 
        # >  For more information about the supported filter parameters and their valid values, see the following **supplement about the Key parameter**.
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

