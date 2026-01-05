# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateTaskInstancesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        task_instances: List[main_models.UpdateTaskInstancesRequestTaskInstances] = None,
    ):
        # The remarks.
        self.comment = comment
        # The instances.
        self.task_instances = task_instances

    def validate(self):
        if self.task_instances:
            for v1 in self.task_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        result['TaskInstances'] = []
        if self.task_instances is not None:
            for k1 in self.task_instances:
                result['TaskInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        self.task_instances = []
        if m.get('TaskInstances') is not None:
            for k1 in m.get('TaskInstances'):
                temp_model = main_models.UpdateTaskInstancesRequestTaskInstances()
                self.task_instances.append(temp_model.from_map(k1))

        return self

class UpdateTaskInstancesRequestTaskInstances(DaraModel):
    def __init__(
        self,
        data_source: main_models.UpdateTaskInstancesRequestTaskInstancesDataSource = None,
        id: int = None,
        priority: int = None,
        runtime_resource: str = None,
    ):
        # The information about the associated data source.
        self.data_source = data_source
        # The instance ID.
        # 
        # This parameter is required.
        self.id = id
        # The priority of the instance. Valid values: 1, 3, 5, 7, and 8.
        # 
        # A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The resource group information. Set this parameter to the ID of a resource group for scheduling.
        self.runtime_resource = runtime_resource

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            temp_model = main_models.UpdateTaskInstancesRequestTaskInstancesDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource = m.get('RuntimeResource')

        return self

class UpdateTaskInstancesRequestTaskInstancesDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the data source.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

