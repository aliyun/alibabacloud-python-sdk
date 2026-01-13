# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficControlTaskRequest(DaraModel):
    def __init__(
        self,
        behavior_table_meta_id: str = None,
        control_granularity: str = None,
        control_logic: str = None,
        control_type: str = None,
        description: str = None,
        effective_scene_ids: List[int] = None,
        end_time: str = None,
        execution_time: str = None,
        flink_resource_id: str = None,
        instance_id: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        item_table_meta_id: str = None,
        name: str = None,
        pre_experiment_ids: str = None,
        prod_experiment_ids: str = None,
        scene_id: str = None,
        service_id: str = None,
        service_ids: List[int] = None,
        start_time: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[main_models.CreateTrafficControlTaskRequestTrafficControlTargets] = None,
        user_condition_array: str = None,
        user_condition_express: str = None,
        user_condition_type: str = None,
        user_table_meta_id: str = None,
    ):
        self.behavior_table_meta_id = behavior_table_meta_id
        self.control_granularity = control_granularity
        self.control_logic = control_logic
        self.control_type = control_type
        self.description = description
        self.effective_scene_ids = effective_scene_ids
        self.end_time = end_time
        self.execution_time = execution_time
        self.flink_resource_id = flink_resource_id
        self.instance_id = instance_id
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.item_table_meta_id = item_table_meta_id
        self.name = name
        self.pre_experiment_ids = pre_experiment_ids
        self.prod_experiment_ids = prod_experiment_ids
        self.scene_id = scene_id
        # This parameter is required.
        self.service_id = service_id
        self.service_ids = service_ids
        self.start_time = start_time
        self.statis_behavior_condition_array = statis_behavior_condition_array
        self.statis_behavior_condition_express = statis_behavior_condition_express
        self.statis_behavior_condition_type = statis_behavior_condition_type
        self.traffic_control_targets = traffic_control_targets
        self.user_condition_array = user_condition_array
        self.user_condition_express = user_condition_express
        self.user_condition_type = user_condition_type
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.flink_resource_id is not None:
            result['FlinkResourceId'] = self.flink_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.prod_experiment_ids is not None:
            result['ProdExperimentIds'] = self.prod_experiment_ids

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('FlinkResourceId') is not None:
            self.flink_resource_id = m.get('FlinkResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('ProdExperimentIds') is not None:
            self.prod_experiment_ids = m.get('ProdExperimentIds')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')

        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')

        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')

        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k1 in m.get('TrafficControlTargets'):
                temp_model = main_models.CreateTrafficControlTaskRequestTrafficControlTargets()
                self.traffic_control_targets.append(temp_model.from_map(k1))

        if m.get('UserConditionArray') is not None:
            self.user_condition_array = m.get('UserConditionArray')

        if m.get('UserConditionExpress') is not None:
            self.user_condition_express = m.get('UserConditionExpress')

        if m.get('UserConditionType') is not None:
            self.user_condition_type = m.get('UserConditionType')

        if m.get('UserTableMetaId') is not None:
            self.user_table_meta_id = m.get('UserTableMetaId')

        return self

class CreateTrafficControlTaskRequestTrafficControlTargets(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event is not None:
            result['Event'] = self.event

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period

        if self.status is not None:
            result['Status'] = self.status

        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Event') is not None:
            self.event = m.get('Event')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

