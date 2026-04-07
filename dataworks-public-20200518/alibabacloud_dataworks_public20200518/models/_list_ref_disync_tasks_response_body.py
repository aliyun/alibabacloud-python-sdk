# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListRefDISyncTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListRefDISyncTasksResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        self.data = data
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListRefDISyncTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRefDISyncTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        disync_tasks: List[main_models.ListRefDISyncTasksResponseBodyDataDISyncTasks] = None,
    ):
        # The details of the synchronization tasks. In most cases, a data source is used by multiple synchronization tasks. Therefore, the value of this parameter is an array. The following parameters are the elements in the array. The sample values of these parameters show the details of a synchronization task.
        self.disync_tasks = disync_tasks

    def validate(self):
        if self.disync_tasks:
            for v1 in self.disync_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DISyncTasks'] = []
        if self.disync_tasks is not None:
            for k1 in self.disync_tasks:
                result['DISyncTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disync_tasks = []
        if m.get('DISyncTasks') is not None:
            for k1 in m.get('DISyncTasks'):
                temp_model = main_models.ListRefDISyncTasksResponseBodyDataDISyncTasks()
                self.disync_tasks.append(temp_model.from_map(k1))

        return self

class ListRefDISyncTasksResponseBodyDataDISyncTasks(DaraModel):
    def __init__(
        self,
        di_destination_datasource: str = None,
        di_source_datasource: str = None,
        node_id: int = None,
        node_name: str = None,
        task_type: str = None,
    ):
        # The destination of the synchronization task. If the synchronization task has multiple destinations, the return value is a JSON array, such as \\\\"odps_writer\\\\", \\\\"mysql\\\\". If the RefType parameter is set to to, the synchronization tasks that use the specified data source as the destination are returned. In this case, the value of this parameter indicates the specified data source.
        self.di_destination_datasource = di_destination_datasource
        # The source of the synchronization task. If the synchronization task has multiple sources, the return value is a JSON array, such as \\\\"odps_writer\\\\", \\\\"mysql\\\\". If the RefType parameter is set to from, the synchronization tasks that use the specified data source as the source are returned. In this case, the value of this parameter indicates the specified data source.
        self.di_source_datasource = di_source_datasource
        # The ID of the synchronization task.
        self.node_id = node_id
        # The name of the synchronization task.
        self.node_name = node_name
        # The type of the synchronization task. Valid values:
        # 
        # *   DI_OFFLINE: batch synchronization task
        # *   DI_REALTIME: real-time synchronization task
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.di_destination_datasource is not None:
            result['DiDestinationDatasource'] = self.di_destination_datasource

        if self.di_source_datasource is not None:
            result['DiSourceDatasource'] = self.di_source_datasource

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiDestinationDatasource') is not None:
            self.di_destination_datasource = m.get('DiDestinationDatasource')

        if m.get('DiSourceDatasource') is not None:
            self.di_source_datasource = m.get('DiSourceDatasource')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

