# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterTaskAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_info: str = None,
        cluster_network_type: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbcluster_status_desc: str = None,
        dbtype: str = None,
        dbversion: str = None,
        data_sets: List[main_models.DescribeAIDBClusterTaskAttributeResponseBodyDataSets] = None,
        extra_info: List[Dict[str, Any]] = None,
        kind_code: int = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        model_path: str = None,
        request_id: str = None,
        task_info: List[main_models.DescribeAIDBClusterTaskAttributeResponseBodyTaskInfo] = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The access information for the model in a test deployment.
        self.access_info = access_info
        # The cluster network type.
        self.cluster_network_type = cluster_network_type
        # The task creation time.
        self.create_time = create_time
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The training status. Valid values:
        # 
        # - **ACTIVATION**: Training in progress.
        # 
        # - **COMPLETED**: Training successful.
        # 
        # - **FAILED**: Training failed.
        self.dbcluster_status = dbcluster_status
        # The training status description. Valid values:
        # 
        # - **ACTIVATION**: Training in progress.
        # 
        # - **COMPLETED**: Training successful.
        # 
        # - **FAILED**: Training failed.
        self.dbcluster_status_desc = dbcluster_status_desc
        # The engine type.
        self.dbtype = dbtype
        # The version. Valid value:
        # 
        # - **3.1**: Model operator tuning.
        self.dbversion = dbversion
        # The datasets used for the task.
        self.data_sets = data_sets
        # A list of objects containing additional information about the task.
        self.extra_info = extra_info
        # The instance type. Valid value:
        # 
        # - **18**.
        self.kind_code = kind_code
        # The lock mode. Valid values:
        # 
        # - **0**: Locked.
        # 
        # - **1**: Unlocked.
        self.lock_mode = lock_mode
        # The maintenance end time.
        self.maintain_end_time = maintain_end_time
        # The maintenance start time.
        self.maintain_start_time = maintain_start_time
        # A comma-separated list of output model paths from the model fine-tuning task.
        self.model_path = model_path
        # The ID of the request.
        self.request_id = request_id
        # A list of objects containing information about each training task.
        self.task_info = task_info
        # The VPC ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_sets:
            for v1 in self.data_sets:
                 if v1:
                    v1.validate()
        if self.task_info:
            for v1 in self.task_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_info is not None:
            result['AccessInfo'] = self.access_info

        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbcluster_status_desc is not None:
            result['DBClusterStatusDesc'] = self.dbcluster_status_desc

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        result['DataSets'] = []
        if self.data_sets is not None:
            for k1 in self.data_sets:
                result['DataSets'].append(k1.to_map() if k1 else None)

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.kind_code is not None:
            result['KindCode'] = self.kind_code

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.model_path is not None:
            result['ModelPath'] = self.model_path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskInfo'] = []
        if self.task_info is not None:
            for k1 in self.task_info:
                result['TaskInfo'].append(k1.to_map() if k1 else None)

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInfo') is not None:
            self.access_info = m.get('AccessInfo')

        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBClusterStatusDesc') is not None:
            self.dbcluster_status_desc = m.get('DBClusterStatusDesc')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        self.data_sets = []
        if m.get('DataSets') is not None:
            for k1 in m.get('DataSets'):
                temp_model = main_models.DescribeAIDBClusterTaskAttributeResponseBodyDataSets()
                self.data_sets.append(temp_model.from_map(k1))

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k1 in m.get('TaskInfo'):
                temp_model = main_models.DescribeAIDBClusterTaskAttributeResponseBodyTaskInfo()
                self.task_info.append(temp_model.from_map(k1))

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeAIDBClusterTaskAttributeResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        completed_time: str = None,
        model_name: str = None,
        model_path: str = None,
        model_source: str = None,
        running_times: str = None,
        start_time: str = None,
        train_mode: str = None,
        train_type: str = None,
    ):
        # The task completion time.
        self.completed_time = completed_time
        # The base model.
        self.model_name = model_name
        # The path to the custom model.
        self.model_path = model_path
        # The source of the model. Valid values:
        # 
        # - **public**: A pre-built model.
        # 
        # - **custom**: A custom model.
        self.model_source = model_source
        # The runtime parameters.
        self.running_times = running_times
        # The task start time.
        self.start_time = start_time
        # The task type. Valid values:
        # 
        # - **sft**: Supervised Fine-tuning.
        # 
        # - **grpo**: Reinforcement learning.
        self.train_mode = train_mode
        # The training method. Valid values:
        # 
        # - **lora**: Low-Rank Adaptation (LoRA) training.
        # 
        # - **full**: Full training.
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

class DescribeAIDBClusterTaskAttributeResponseBodyDataSets(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        path: str = None,
        split_dataset_ratio: str = None,
        type: str = None,
    ):
        # The dataset name.
        self.dataset_name = dataset_name
        # The dataset path.
        self.path = path
        # The proportion of the training set reserved for validation.
        self.split_dataset_ratio = split_dataset_ratio
        # The type of the dataset. Valid values:
        # 
        # - **train**: The training set.
        # 
        # - **eval**: The validation set.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.path is not None:
            result['Path'] = self.path

        if self.split_dataset_ratio is not None:
            result['SplitDatasetRatio'] = self.split_dataset_ratio

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('SplitDatasetRatio') is not None:
            self.split_dataset_ratio = m.get('SplitDatasetRatio')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

