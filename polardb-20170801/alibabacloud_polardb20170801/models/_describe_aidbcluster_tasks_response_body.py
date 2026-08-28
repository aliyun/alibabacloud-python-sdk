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
        page_number: int = None,
        page_record_count: str = None,
        page_size: str = None,
        relative_dbcluster_id: str = None,
        request_id: str = None,
        task_type: str = None,
        total_record_count: str = None,
    ):
        # The cluster engine.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The cluster endpoint details.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The total number of records on the current page.
        self.page_record_count = page_record_count
        # The number of records per page.
        self.page_size = page_size
        # The ID of the PolarDB cluster.
        self.relative_dbcluster_id = relative_dbcluster_id
        # Id of the request
        self.request_id = request_id
        # The task type.
        self.task_type = task_type
        # The total number of records.
        self.total_record_count = total_record_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

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
        tune_arch: str = None,
    ):
        # The task completion time.
        self.completed_time = completed_time
        # The creation time.
        self.creation_time = creation_time
        # The node description.
        self.dbnode_description = dbnode_description
        # The template operator instance ID.
        self.dbnode_id = dbnode_id
        # The instance status. This parameter may not be returned.
        self.dbnode_status = dbnode_status
        # The instance status.
        self.dbnode_status_desc = dbnode_status_desc
        # The zone.
        self.data_zone_id = data_zone_id
        # The cluster engine.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The model name.
        self.model_name = model_name
        # The path.
        self.model_path = model_path
        # The model source.
        self.model_source = model_source
        # The running parameters.
        self.running_times = running_times
        # The task start time.
        self.start_time = start_time
        # The mode.
        self.train_mode = train_mode
        # The type.
        self.train_type = train_type
        # The tuning framework.
        self.tune_arch = tune_arch

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

        if self.tune_arch is not None:
            result['TuneArch'] = self.tune_arch

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

        if m.get('TuneArch') is not None:
            self.tune_arch = m.get('TuneArch')

        return self

