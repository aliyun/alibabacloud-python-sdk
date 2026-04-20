# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterTasksResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        items: List[main_models.DescribeAIDBClusterTasksResponseBodyItems] = None,
        relative_dbcluster_id: str = None,
        request_id: str = None,
        task_type: str = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.items = items
        self.relative_dbcluster_id = relative_dbcluster_id
        # Id of the request
        self.request_id = request_id
        self.task_type = task_type

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAIDBClusterTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class DescribeAIDBClusterTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        completed_time: str = None,
        creation_time: str = None,
        dbnode_description: str = None,
        dbnode_id: str = None,
        dbnode_status: str = None,
        dbnode_status_desc: str = None,
        data_zone_id: str = None,
        engine: str = None,
        engine_version: str = None,
        model_name: str = None,
        model_path: str = None,
        model_source: str = None,
        running_times: str = None,
        start_time: str = None,
        train_mode: str = None,
        train_type: str = None,
    ):
        self.completed_time = completed_time
        self.creation_time = creation_time
        self.dbnode_description = dbnode_description
        self.dbnode_id = dbnode_id
        self.dbnode_status = dbnode_status
        self.dbnode_status_desc = dbnode_status_desc
        self.data_zone_id = data_zone_id
        self.engine = engine
        self.engine_version = engine_version
        self.model_name = model_name
        self.model_path = model_path
        self.model_source = model_source
        self.running_times = running_times
        self.start_time = start_time
        self.train_mode = train_mode
        self.train_type = train_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbnode_description is not None:
            result['DBNodeDescription'] = self.dbnode_description

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status

        if self.dbnode_status_desc is not None:
            result['DBNodeStatusDesc'] = self.dbnode_status_desc

        if self.data_zone_id is not None:
            result['DataZoneId'] = self.data_zone_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_path is not None:
            result['ModelPath'] = self.model_path

        if self.model_source is not None:
            result['ModelSource'] = self.model_source

        if self.running_times is not None:
            result['RunningTimes'] = self.running_times

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode

        if self.train_type is not None:
            result['TrainType'] = self.train_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBNodeDescription') is not None:
            self.dbnode_description = m.get('DBNodeDescription')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')

        if m.get('DBNodeStatusDesc') is not None:
            self.dbnode_status_desc = m.get('DBNodeStatusDesc')

        if m.get('DataZoneId') is not None:
            self.data_zone_id = m.get('DataZoneId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')

        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')

        if m.get('RunningTimes') is not None:
            self.running_times = m.get('RunningTimes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')

        if m.get('TrainType') is not None:
            self.train_type = m.get('TrainType')

        return self

