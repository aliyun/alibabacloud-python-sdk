# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListTrafficControlTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        traffic_control_tasks: List[main_models.ListTrafficControlTasksResponseBodyTrafficControlTasks] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of traffic control tasks.
        self.total_count = total_count
        # The list of traffic control tasks.
        self.traffic_control_tasks = traffic_control_tasks

    def validate(self):
        if self.traffic_control_tasks:
            for v1 in self.traffic_control_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficControlTasks'] = []
        if self.traffic_control_tasks is not None:
            for k1 in self.traffic_control_tasks:
                result['TrafficControlTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_control_tasks = []
        if m.get('TrafficControlTasks') is not None:
            for k1 in m.get('TrafficControlTasks'):
                temp_model = main_models.ListTrafficControlTasksResponseBodyTrafficControlTasks()
                self.traffic_control_tasks.append(temp_model.from_map(k1))

        return self

class ListTrafficControlTasksResponseBodyTrafficControlTasks(DaraModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        effective_scene_ids: List[int] = None,
        effective_scene_name_list: List[str] = None,
        effective_scene_names: List[int] = None,
        end_time: str = None,
        ever_published: bool = None,
        execution_time: str = None,
        flink_resource_id: str = None,
        flink_resource_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        pre_experiment_ids: str = None,
        prepub_status: str = None,
        prod_experiment_ids: str = None,
        product_status: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_id: str = None,
        service_id_list: List[int] = None,
        service_ids: List[str] = None,
        start_time: str = None,
        statis_bahavior_condition_express: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[main_models.ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets] = None,
        traffic_control_task_id: str = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        # The behavior table ID.
        self.behavior_table_meta_id = behavior_table_meta_id
        # The control granularity.
        self.control_granularity = control_granularity
        # The control logic.
        self.control_logic = control_logic
        # The control type.
        self.control_type = control_type
        # The description of the traffic control task.
        self.description = description
        # The list of effective scene IDs.
        self.effective_scene_ids = effective_scene_ids
        # The list of effective scene names.
        self.effective_scene_name_list = effective_scene_name_list
        # The list of effective scene names.
        self.effective_scene_names = effective_scene_names
        # The end time.
        self.end_time = end_time
        # Indicates whether the task has ever been published.
        self.ever_published = ever_published
        # The execution schedule for the task. Valid values:
        # 
        # - `Permanent`: The task runs indefinitely.
        # 
        # - `TimeRange`: The task runs within a specified time range. If you set this parameter to this value, you must also specify the `StartTime` and `EndTime` parameters.
        self.execution_time = execution_time
        # The Flink resource ID.
        self.flink_resource_id = flink_resource_id
        # The name of the Flink resource.
        self.flink_resource_name = flink_resource_name
        # The creation time of the task.
        self.gmt_create_time = gmt_create_time
        # The last update time of the task.
        self.gmt_modified_time = gmt_modified_time
        # The item condition, in an array format.
        self.item_condition_array = item_condition_array
        # The item condition, in an expression format.
        self.item_condition_express = item_condition_express
        # The item condition type.
        self.item_condition_type = item_condition_type
        # The item table ID.
        self.item_table_meta_id = item_table_meta_id
        # The name of the traffic control task.
        self.name = name
        # A comma-separated list of staging experiment IDs.
        self.pre_experiment_ids = pre_experiment_ids
        # The staging environment status.
        self.prepub_status = prepub_status
        # A comma-separated list of production experiment IDs.
        self.prod_experiment_ids = prod_experiment_ids
        # The production environment status.
        self.product_status = product_status
        # The scene ID. You can obtain this ID by calling the `ListScenes` operation.
        self.scene_id = scene_id
        # The name of the scene.
        self.scene_name = scene_name
        # The service ID.
        self.service_id = service_id
        # The list of service IDs.
        self.service_id_list = service_id_list
        # The list of bound engine service IDs.
        self.service_ids = service_ids
        # The start time.
        self.start_time = start_time
        # The behavior statistics expression.
        self.statis_bahavior_condition_express = statis_bahavior_condition_express
        # The behavior statistics condition, in an array format.
        self.statis_behavior_condition_array = statis_behavior_condition_array
        # The behavior statistics expression.
        self.statis_behavior_condition_express = statis_behavior_condition_express
        # The condition type for behavior statistics.
        self.statis_behavior_condition_type = statis_behavior_condition_type
        # The list of traffic control targets.
        self.traffic_control_targets = traffic_control_targets
        # The traffic control task ID.
        self.traffic_control_task_id = traffic_control_task_id
        # The condition for the target user group, in an array format.
        self.user_condition_array = user_condition_array
        # The condition for the target user group, in an expression format.
        self.user_condition_express = user_condition_express
        # The condition type for the target user group.
        self.user_condition_type = user_condition_type
        # The user table ID.
        self.user_table_meta_id = user_table_meta_id

    def validate(self):
        if self.traffic_control_targets:
            for v1 in self.traffic_control_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior_table_meta_id is not None:
            result['BehaviorTableMetaId'] = self.behavior_table_meta_id

        if self.control_granularity is not None:
            result['ControlGranularity'] = self.control_granularity

        if self.control_logic is not None:
            result['ControlLogic'] = self.control_logic

        if self.control_type is not None:
            result['ControlType'] = self.control_type

        if self.description is not None:
            result['Description'] = self.description

        if self.effective_scene_ids is not None:
            result['EffectiveSceneIds'] = self.effective_scene_ids

        if self.effective_scene_name_list is not None:
            result['EffectiveSceneNameList'] = self.effective_scene_name_list

        if self.effective_scene_names is not None:
            result['EffectiveSceneNames'] = self.effective_scene_names

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ever_published is not None:
            result['EverPublished'] = self.ever_published

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.flink_resource_id is not None:
            result['FlinkResourceId'] = self.flink_resource_id

        if self.flink_resource_name is not None:
            result['FlinkResourceName'] = self.flink_resource_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array

        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express

        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type

        if self.item_table_meta_id is not None:
            result['ItemTableMetaId'] = self.item_table_meta_id

        if self.name is not None:
            result['Name'] = self.name

        if self.pre_experiment_ids is not None:
            result['PreExperimentIds'] = self.pre_experiment_ids

        if self.prepub_status is not None:
            result['PrepubStatus'] = self.prepub_status

        if self.prod_experiment_ids is not None:
            result['ProdExperimentIds'] = self.prod_experiment_ids

        if self.product_status is not None:
            result['ProductStatus'] = self.product_status

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_id_list is not None:
            result['ServiceIdList'] = self.service_id_list

        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statis_bahavior_condition_express is not None:
            result['StatisBahaviorConditionExpress'] = self.statis_bahavior_condition_express

        if self.statis_behavior_condition_array is not None:
            result['StatisBehaviorConditionArray'] = self.statis_behavior_condition_array

        if self.statis_behavior_condition_express is not None:
            result['StatisBehaviorConditionExpress'] = self.statis_behavior_condition_express

        if self.statis_behavior_condition_type is not None:
            result['StatisBehaviorConditionType'] = self.statis_behavior_condition_type

        result['TrafficControlTargets'] = []
        if self.traffic_control_targets is not None:
            for k1 in self.traffic_control_targets:
                result['TrafficControlTargets'].append(k1.to_map() if k1 else None)

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        if self.user_condition_array is not None:
            result['UserConditionArray'] = self.user_condition_array

        if self.user_condition_express is not None:
            result['UserConditionExpress'] = self.user_condition_express

        if self.user_condition_type is not None:
            result['UserConditionType'] = self.user_condition_type

        if self.user_table_meta_id is not None:
            result['UserTableMetaId'] = self.user_table_meta_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorTableMetaId') is not None:
            self.behavior_table_meta_id = m.get('BehaviorTableMetaId')

        if m.get('ControlGranularity') is not None:
            self.control_granularity = m.get('ControlGranularity')

        if m.get('ControlLogic') is not None:
            self.control_logic = m.get('ControlLogic')

        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveSceneIds') is not None:
            self.effective_scene_ids = m.get('EffectiveSceneIds')

        if m.get('EffectiveSceneNameList') is not None:
            self.effective_scene_name_list = m.get('EffectiveSceneNameList')

        if m.get('EffectiveSceneNames') is not None:
            self.effective_scene_names = m.get('EffectiveSceneNames')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EverPublished') is not None:
            self.ever_published = m.get('EverPublished')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('FlinkResourceId') is not None:
            self.flink_resource_id = m.get('FlinkResourceId')

        if m.get('FlinkResourceName') is not None:
            self.flink_resource_name = m.get('FlinkResourceName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')

        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')

        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')

        if m.get('ItemTableMetaId') is not None:
            self.item_table_meta_id = m.get('ItemTableMetaId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreExperimentIds') is not None:
            self.pre_experiment_ids = m.get('PreExperimentIds')

        if m.get('PrepubStatus') is not None:
            self.prepub_status = m.get('PrepubStatus')

        if m.get('ProdExperimentIds') is not None:
            self.prod_experiment_ids = m.get('ProdExperimentIds')

        if m.get('ProductStatus') is not None:
            self.product_status = m.get('ProductStatus')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceIdList') is not None:
            self.service_id_list = m.get('ServiceIdList')

        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisBahaviorConditionExpress') is not None:
            self.statis_bahavior_condition_express = m.get('StatisBahaviorConditionExpress')

        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')

        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')

        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')

        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k1 in m.get('TrafficControlTargets'):
                temp_model = main_models.ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k1))

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')

        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')

        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')

        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')

        return self

class ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargets(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        split_parts: main_models.ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_target_id: str = None,
        traffic_control_task_id: str = None,
        value: float = None,
    ):
        # The end time.
        self.end_time = end_time
        # The event for the traffic control target.
        self.event = event
        # The creation time of the target.
        self.gmt_create_time = gmt_create_time
        # The last update time of the target.
        self.gmt_modified_time = gmt_modified_time
        # The item condition, in an array format.
        self.item_condition_array = item_condition_array
        # The item condition, in an expression format.
        self.item_condition_express = item_condition_express
        # The item condition type.
        self.item_condition_type = item_condition_type
        # The name of the traffic control target.
        self.name = name
        # Indicates whether the traffic control target is for a new product recall.
        self.new_product_regulation = new_product_regulation
        # The name of the recall strategy.
        self.recall_name = recall_name
        # The details of the split points.
        self.split_parts = split_parts
        # The start time.
        self.start_time = start_time
        # The statistics period.
        self.statis_period = statis_period
        # The status of the traffic control target.
        self.status = status
        # The tolerance value for the traffic control target.
        self.tolerance_value = tolerance_value
        # The traffic control target ID.
        self.traffic_control_target_id = traffic_control_target_id
        # The traffic control task ID.
        self.traffic_control_task_id = traffic_control_task_id
        # The value of the traffic control target.
        self.value = value

    def validate(self):
        if self.split_parts:
            self.split_parts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event is not None:
            result['Event'] = self.event

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array

        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express

        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type

        if self.name is not None:
            result['Name'] = self.name

        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation

        if self.recall_name is not None:
            result['RecallName'] = self.recall_name

        if self.split_parts is not None:
            result['SplitParts'] = self.split_parts.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period

        if self.status is not None:
            result['Status'] = self.status

        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value

        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')

        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')

        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')

        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')

        if m.get('SplitParts') is not None:
            temp_model = main_models.ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts()
            self.split_parts = temp_model.from_map(m.get('SplitParts'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')

        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListTrafficControlTasksResponseBodyTrafficControlTasksTrafficControlTargetsSplitParts(DaraModel):
    def __init__(
        self,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        # The list of value-based split points for the target.
        self.set_values = set_values
        # The list of time-based split points.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.set_values is not None:
            result['SetValues'] = self.set_values

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

