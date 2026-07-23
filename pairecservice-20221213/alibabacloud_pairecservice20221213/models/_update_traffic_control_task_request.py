# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateTrafficControlTaskRequest(DaraModel):
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
        statis_baeavior_condition_array: str = None,
        statis_behavior_condition_array: str = None,
        statis_behavior_condition_express: str = None,
        statis_behavior_condition_type: str = None,
        traffic_control_targets: List[main_models.UpdateTrafficControlTaskRequestTrafficControlTargets] = None,
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
        # The description of the traffic control plan.
        self.description = description
        # A list of effective scene IDs.
        self.effective_scene_ids = effective_scene_ids
        # The end time.
        self.end_time = end_time
        # The execution time. Valid values: `Permanent` (runs indefinitely) and `TimeRange` (runs within a specified period). If you select `TimeRange`, you must also specify `StartTime` and `EndTime`.
        self.execution_time = execution_time
        # The Flink resource ID.
        self.flink_resource_id = flink_resource_id
        # The instance ID.
        self.instance_id = instance_id
        # The item conditions, specified in an array format.
        self.item_condition_array = item_condition_array
        # The item conditions, specified as an expression.
        self.item_condition_express = item_condition_express
        # The item condition type.
        self.item_condition_type = item_condition_type
        # The item table ID.
        self.item_table_meta_id = item_table_meta_id
        # The name of the traffic control plan.
        self.name = name
        # A comma-separated list of pre-release experiment IDs.
        self.pre_experiment_ids = pre_experiment_ids
        # A comma-separated list of production experiment IDs.
        self.prod_experiment_ids = prod_experiment_ids
        # The scene ID.
        self.scene_id = scene_id
        # The engine service ID.
        self.service_id = service_id
        # A list of associated engine service IDs.
        self.service_ids = service_ids
        # The start time.
        self.start_time = start_time
        # The conditions for behavior statistics, specified in an array format.
        self.statis_baeavior_condition_array = statis_baeavior_condition_array
        # The conditions for behavior statistics, specified in an array format.
        self.statis_behavior_condition_array = statis_behavior_condition_array
        # The conditions for behavior statistics, specified as an expression.
        self.statis_behavior_condition_express = statis_behavior_condition_express
        # The condition type for behavior statistics.
        self.statis_behavior_condition_type = statis_behavior_condition_type
        # A list of traffic control targets.
        self.traffic_control_targets = traffic_control_targets
        # The conditions for the target user group, specified in an array format.
        self.user_condition_array = user_condition_array
        # The conditions for the target user group, specified as an expression.
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

        if self.statis_baeavior_condition_array is not None:
            result['StatisBaeaviorConditionArray'] = self.statis_baeavior_condition_array

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

        if m.get('StatisBaeaviorConditionArray') is not None:
            self.statis_baeavior_condition_array = m.get('StatisBaeaviorConditionArray')

        if m.get('StatisBehaviorConditionArray') is not None:
            self.statis_behavior_condition_array = m.get('StatisBehaviorConditionArray')

        if m.get('StatisBehaviorConditionExpress') is not None:
            self.statis_behavior_condition_express = m.get('StatisBehaviorConditionExpress')

        if m.get('StatisBehaviorConditionType') is not None:
            self.statis_behavior_condition_type = m.get('StatisBehaviorConditionType')

        self.traffic_control_targets = []
        if m.get('TrafficControlTargets') is not None:
            for k1 in m.get('TrafficControlTargets'):
                temp_model = main_models.UpdateTrafficControlTaskRequestTrafficControlTargets()
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

class UpdateTrafficControlTaskRequestTrafficControlTargets(DaraModel):
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
        # The end time of the traffic control target.
        self.end_time = end_time
        # The event for the traffic control target.
        self.event = event
        # The item conditions, specified in an array format.
        self.item_condition_array = item_condition_array
        # The item conditions, specified as an expression.
        self.item_condition_express = item_condition_express
        # The item condition type.
        self.item_condition_type = item_condition_type
        # The name of the traffic control target.
        self.name = name
        # Indicates whether this is a new item recall.
        self.new_product_regulation = new_product_regulation
        # The recall policy name.
        self.recall_name = recall_name
        # The start time of the traffic control target.
        self.start_time = start_time
        # The statistical period.
        self.statis_period = statis_period
        # The status.
        self.status = status
        # The tolerance range for the traffic control target.
        self.tolerance_value = tolerance_value
        # The value of the traffic control target.
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

