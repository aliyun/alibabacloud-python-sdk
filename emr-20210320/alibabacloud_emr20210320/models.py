# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AckNodeNodeSelectorLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AckNodeNodeSelectorTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodeNodeSelector(TeaModel):
    def __init__(
        self,
        labels: List[AckNodeNodeSelectorLabels] = None,
        taints: List[AckNodeNodeSelectorTaints] = None,
    ):
        self.labels = labels
        self.taints = taints

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodeNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodeNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class AckNode(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        node_selector: AckNodeNodeSelector = None,
    ):
        self.node_id = node_id
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeSelector') is not None:
            temp_model = AckNodeNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class AckNodePoolNodeSelectorLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AckNodePoolNodeSelectorTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodePoolNodeSelector(TeaModel):
    def __init__(
        self,
        labels: List[AckNodePoolNodeSelectorLabels] = None,
        taints: List[AckNodePoolNodeSelectorTaints] = None,
    ):
        self.labels = labels
        self.taints = taints

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodePoolNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodePoolNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class AckNodePool(TeaModel):
    def __init__(
        self,
        node_pool_id: str = None,
        node_selector: AckNodePoolNodeSelector = None,
    ):
        self.node_pool_id = node_pool_id
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeSelector') is not None:
            temp_model = AckNodePoolNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class AckNodeSelectorLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AckNodeSelectorTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AckNodeSelector(TeaModel):
    def __init__(
        self,
        labels: List[AckNodeSelectorLabels] = None,
        taints: List[AckNodeSelectorTaints] = None,
    ):
        self.labels = labels
        self.taints = taints

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['Taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AckNodeSelectorLabels()
                self.labels.append(temp_model.from_map(k))
        self.taints = []
        if m.get('Taints') is not None:
            for k in m.get('Taints'):
                temp_model = AckNodeSelectorTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class Application(TeaModel):
    def __init__(
        self,
        application_name: str = None,
    ):
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        return self


class ApplicationConfig(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        config_scope: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
    ):
        self.application_name = application_name
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value
        self.config_scope = config_scope
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        return self


class ApplicationConfigParam(TeaModel):
    def __init__(
        self,
        config_action: str = None,
        config_file_name: str = None,
        config_item_description: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        config_scope: str = None,
        effective_actions: str = None,
        effective_type: str = None,
        node_group_id: str = None,
        node_id: str = None,
    ):
        self.config_action = config_action
        self.config_file_name = config_file_name
        self.config_item_description = config_item_description
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value
        self.config_scope = config_scope
        self.effective_actions = effective_actions
        self.effective_type = effective_type
        self.node_group_id = node_group_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_action is not None:
            result['ConfigAction'] = self.config_action
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_description is not None:
            result['ConfigItemDescription'] = self.config_item_description
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.effective_actions is not None:
            result['EffectiveActions'] = self.effective_actions
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemDescription') is not None:
            self.config_item_description = m.get('ConfigItemDescription')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('EffectiveActions') is not None:
            self.effective_actions = m.get('EffectiveActions')
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class AutoRenewInstance(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        instance_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AutoRenewInstanceParam(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_duration: str = None,
        auto_renew_duration_unit: str = None,
        instance_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ByLoadScalingRule(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        cool_down_interval: int = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.cool_down_interval = cool_down_interval
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.statistics = statistics
        self.threshold = threshold
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ByLoadScalingRuleSpec(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.statistics = statistics
        self.threshold = threshold
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ByTimeScalingRule(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        launch_expiration_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        self.end_time = end_time
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ByTimeScalingRuleSpec(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        self.end_time = end_time
        self.launch_time = launch_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ClickhouseConf(TeaModel):
    def __init__(
        self,
        initial_replica: int = None,
        initial_shard: int = None,
        new_node_count: int = None,
        resize_type: str = None,
    ):
        self.initial_replica = initial_replica
        self.initial_shard = initial_shard
        self.new_node_count = new_node_count
        self.resize_type = resize_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_replica is not None:
            result['InitialReplica'] = self.initial_replica
        if self.initial_shard is not None:
            result['InitialShard'] = self.initial_shard
        if self.new_node_count is not None:
            result['NewNodeCount'] = self.new_node_count
        if self.resize_type is not None:
            result['ResizeType'] = self.resize_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialReplica') is not None:
            self.initial_replica = m.get('InitialReplica')
        if m.get('InitialShard') is not None:
            self.initial_shard = m.get('InitialShard')
        if m.get('NewNodeCount') is not None:
            self.new_node_count = m.get('NewNodeCount')
        if m.get('ResizeType') is not None:
            self.resize_type = m.get('ResizeType')
        return self


class NodeAttributes(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        ram_role: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.ram_role = ram_role
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ClusterStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubscriptionConfig(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        return self


class Tag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class Cluster(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        create_time: int = None,
        deploy_mode: str = None,
        emr_default_role: str = None,
        end_time: int = None,
        expire_time: int = None,
        node_attributes: NodeAttributes = None,
        payment_type: str = None,
        ready_time: int = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        security_mode: str = None,
        state_change_reason: ClusterStateChangeReason = None,
        subscription_config: SubscriptionConfig = None,
        tags: List[Tag] = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_state = cluster_state
        self.cluster_type = cluster_type
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.emr_default_role = emr_default_role
        self.end_time = end_time
        self.expire_time = expire_time
        self.node_attributes = node_attributes
        self.payment_type = payment_type
        self.ready_time = ready_time
        self.region_id = region_id
        self.release_version = release_version
        self.resource_group_id = resource_group_id
        self.security_mode = security_mode
        self.state_change_reason = state_change_reason
        self.subscription_config = subscription_config
        self.tags = tags

    def validate(self):
        if self.node_attributes:
            self.node_attributes.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NodeAttributes') is not None:
            temp_model = NodeAttributes()
            self.node_attributes = temp_model.from_map(m['NodeAttributes'])
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        if m.get('StateChangeReason') is not None:
            temp_model = ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class NodeSelector(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        node_group_name: str = None,
        node_group_types: List[str] = None,
        node_names: List[str] = None,
        node_select_type: str = None,
    ):
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_group_types = node_group_types
        self.node_names = node_names
        self.node_select_type = node_select_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')
        return self


class ClusterScript(TeaModel):
    def __init__(
        self,
        execution_fail_strategy: str = None,
        execution_moment: str = None,
        node_select: NodeSelector = None,
        priority: int = None,
        script_args: str = None,
        script_name: str = None,
        script_path: str = None,
    ):
        self.execution_fail_strategy = execution_fail_strategy
        self.execution_moment = execution_moment
        self.node_select = node_select
        self.priority = priority
        self.script_args = script_args
        self.script_name = script_name
        self.script_path = script_path

    def validate(self):
        if self.node_select:
            self.node_select.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy
        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment
        if self.node_select is not None:
            result['NodeSelect'] = self.node_select.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_path is not None:
            result['ScriptPath'] = self.script_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')
        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')
        if m.get('NodeSelect') is not None:
            temp_model = NodeSelector()
            self.node_select = temp_model.from_map(m['NodeSelect'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')
        return self


class ClusterSummary(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        create_time: int = None,
        emr_default_role: str = None,
        end_time: int = None,
        expire_time: int = None,
        payment_type: str = None,
        ready_time: int = None,
        release_version: str = None,
        resource_group_id: str = None,
        state_change_reason: ClusterStateChangeReason = None,
        tags: List[Tag] = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_state = cluster_state
        self.cluster_type = cluster_type
        self.create_time = create_time
        self.emr_default_role = emr_default_role
        self.end_time = end_time
        self.expire_time = expire_time
        self.payment_type = payment_type
        self.ready_time = ready_time
        self.release_version = release_version
        self.resource_group_id = resource_group_id
        self.state_change_reason = state_change_reason
        self.tags = tags

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateChangeReason') is not None:
            temp_model = ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ComponentInstanceSelectorComponentInstances(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_id: str = None,
    ):
        self.application_name = application_name
        self.component_name = component_name
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ComponentInstanceSelectorComponents(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
    ):
        self.application_name = application_name
        self.component_name = component_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        return self


class ComponentInstanceSelector(TeaModel):
    def __init__(
        self,
        action_scope: str = None,
        application_names: List[str] = None,
        component_instances: List[ComponentInstanceSelectorComponentInstances] = None,
        components: List[ComponentInstanceSelectorComponents] = None,
        node_group_ids: List[str] = None,
        node_ids: List[str] = None,
        run_action_scope: str = None,
    ):
        self.action_scope = action_scope
        self.application_names = application_names
        self.component_instances = component_instances
        self.components = components
        self.node_group_ids = node_group_ids
        self.node_ids = node_ids
        self.run_action_scope = run_action_scope

    def validate(self):
        if self.component_instances:
            for k in self.component_instances:
                if k:
                    k.validate()
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_scope is not None:
            result['ActionScope'] = self.action_scope
        if self.application_names is not None:
            result['ApplicationNames'] = self.application_names
        result['ComponentInstances'] = []
        if self.component_instances is not None:
            for k in self.component_instances:
                result['ComponentInstances'].append(k.to_map() if k else None)
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.run_action_scope is not None:
            result['RunActionScope'] = self.run_action_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionScope') is not None:
            self.action_scope = m.get('ActionScope')
        if m.get('ApplicationNames') is not None:
            self.application_names = m.get('ApplicationNames')
        self.component_instances = []
        if m.get('ComponentInstances') is not None:
            for k in m.get('ComponentInstances'):
                temp_model = ComponentInstanceSelectorComponentInstances()
                self.component_instances.append(temp_model.from_map(k))
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ComponentInstanceSelectorComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RunActionScope') is not None:
            self.run_action_scope = m.get('RunActionScope')
        return self


class ComponentLayoutNodeSelector(TeaModel):
    def __init__(
        self,
        node_end_index: int = None,
        node_group_id: str = None,
        node_group_index: int = None,
        node_group_name: str = None,
        node_group_types: List[str] = None,
        node_names: List[str] = None,
        node_select_type: str = None,
        node_start_index: int = None,
    ):
        self.node_end_index = node_end_index
        self.node_group_id = node_group_id
        self.node_group_index = node_group_index
        self.node_group_name = node_group_name
        self.node_group_types = node_group_types
        self.node_names = node_names
        self.node_select_type = node_select_type
        self.node_start_index = node_start_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_end_index is not None:
            result['NodeEndIndex'] = self.node_end_index
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_index is not None:
            result['NodeGroupIndex'] = self.node_group_index
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_select_type is not None:
            result['NodeSelectType'] = self.node_select_type
        if self.node_start_index is not None:
            result['NodeStartIndex'] = self.node_start_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeEndIndex') is not None:
            self.node_end_index = m.get('NodeEndIndex')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupIndex') is not None:
            self.node_group_index = m.get('NodeGroupIndex')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeSelectType') is not None:
            self.node_select_type = m.get('NodeSelectType')
        if m.get('NodeStartIndex') is not None:
            self.node_start_index = m.get('NodeStartIndex')
        return self


class ComponentLayout(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_selector: ComponentLayoutNodeSelector = None,
    ):
        self.application_name = application_name
        self.component_name = component_name
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeSelector') is not None:
            temp_model = ComponentLayoutNodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class ConvertNodeGroup(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
    ):
        self.node_group_id = node_group_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class ConvertNodeGroupParam(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
    ):
        self.node_group_id = node_group_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class CostOptimizedConfig(TeaModel):
    def __init__(
        self,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        spot_instance_pools: int = None,
    ):
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.spot_instance_pools = spot_instance_pools

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        return self


class DiskInfo(TeaModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.count = count
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class SystemDiskParam(TeaModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateNodeGroupParam(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        data_disks: List[DiskInfo] = None,
        instance_types: List[str] = None,
        node_count: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        node_key_pair_name: str = None,
        node_ram_role: str = None,
        node_root_password: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        system_disk: SystemDiskParam = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.data_disks = data_disks
        self.instance_types = instance_types
        self.node_count = node_count
        self.node_group_name = node_group_name
        self.node_group_type = node_group_type
        self.node_key_pair_name = node_key_pair_name
        self.node_ram_role = node_ram_role
        self.node_root_password = node_root_password
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.security_group_id = security_group_id
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk
        self.v_switch_ids = v_switch_ids
        self.with_public_ip = with_public_ip
        self.zone_id = zone_id

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_key_pair_name is not None:
            result['NodeKeyPairName'] = self.node_key_pair_name
        if self.node_ram_role is not None:
            result['NodeRamRole'] = self.node_ram_role
        if self.node_root_password is not None:
            result['NodeRootPassword'] = self.node_root_password
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DiskInfo()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeKeyPairName') is not None:
            self.node_key_pair_name = m.get('NodeKeyPairName')
        if m.get('NodeRamRole') is not None:
            self.node_ram_role = m.get('NodeRamRole')
        if m.get('NodeRootPassword') is not None:
            self.node_root_password = m.get('NodeRootPassword')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDisk') is not None:
            temp_model = SystemDiskParam()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.count = count
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DecreaseNodeGroupParam(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        release_instance_ids: List[str] = None,
    ):
        self.node_group_id = node_group_id
        self.release_instance_ids = release_instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.release_instance_ids is not None:
            result['ReleaseInstanceIds'] = self.release_instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('ReleaseInstanceIds') is not None:
            self.release_instance_ids = m.get('ReleaseInstanceIds')
        return self


class DeploymentLayout(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_selector: NodeSelector = None,
    ):
        self.application_name = application_name
        self.component_name = component_name
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeSelector') is not None:
            temp_model = NodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        return self


class Disk(TeaModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.count = count
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DiskSize(TeaModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class FailedReason(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        error_msg: str = None,
        request_id: str = None,
        service: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.error_msg = error_msg
        self.request_id = request_id
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class HealthSummary(TeaModel):
    def __init__(
        self,
        bad_count: int = None,
        good_count: int = None,
        none_count: int = None,
        stopped_count: int = None,
        total_count: int = None,
        unknown_count: int = None,
        warning_count: int = None,
    ):
        self.bad_count = bad_count
        self.good_count = good_count
        self.none_count = none_count
        self.stopped_count = stopped_count
        self.total_count = total_count
        self.unknown_count = unknown_count
        self.warning_count = warning_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bad_count is not None:
            result['BadCount'] = self.bad_count
        if self.good_count is not None:
            result['GoodCount'] = self.good_count
        if self.none_count is not None:
            result['NoneCount'] = self.none_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.unknown_count is not None:
            result['UnknownCount'] = self.unknown_count
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BadCount') is not None:
            self.bad_count = m.get('BadCount')
        if m.get('GoodCount') is not None:
            self.good_count = m.get('GoodCount')
        if m.get('NoneCount') is not None:
            self.none_count = m.get('NoneCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UnknownCount') is not None:
            self.unknown_count = m.get('UnknownCount')
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class IncreaseNodeGroup(TeaModel):
    def __init__(
        self,
        description: str = None,
        node_count: int = None,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        v_switch_id: str = None,
    ):
        self.description = description
        self.node_count = node_count
        self.node_group_id = node_group_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class IncreaseNodeGroupParam(TeaModel):
    def __init__(
        self,
        node_count: int = None,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        v_switch_id: str = None,
    ):
        self.node_count = node_count
        self.node_group_id = node_group_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class KeyValue(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class MetaStoreConf(TeaModel):
    def __init__(
        self,
        db_password: str = None,
        db_url: str = None,
        db_user_name: str = None,
    ):
        self.db_password = db_password
        self.db_url = db_url
        self.db_user_name = db_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_url is not None:
            result['DbUrl'] = self.db_url
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbUrl') is not None:
            self.db_url = m.get('DbUrl')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        return self


class MetricsTrigger(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        cool_down_interval: int = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.cool_down_interval = cool_down_interval
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.statistics = statistics
        self.threshold = threshold
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class Node(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        expire_time: int = None,
        instance_type: str = None,
        maintenance_status: str = None,
        node_group_id: str = None,
        node_group_type: str = None,
        node_id: str = None,
        node_name: str = None,
        node_state: str = None,
        private_ip: str = None,
        public_ip: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.expire_time = expire_time
        self.instance_type = instance_type
        self.maintenance_status = maintenance_status
        self.node_group_id = node_group_id
        self.node_group_type = node_group_type
        self.node_id = node_id
        self.node_name = node_name
        self.node_state = node_state
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.maintenance_status is not None:
            result['MaintenanceStatus'] = self.maintenance_status
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_state is not None:
            result['NodeState'] = self.node_state
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaintenanceStatus') is not None:
            self.maintenance_status = m.get('MaintenanceStatus')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeState') is not None:
            self.node_state = m.get('NodeState')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeCountConstraint(TeaModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        type: str = None,
        values: List[int] = None,
    ):
        self.max = max
        self.min = min
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SpotBidPrice(TeaModel):
    def __init__(
        self,
        bid_price: float = None,
        instance_type: str = None,
    ):
        self.bid_price = bid_price
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid_price is not None:
            result['BidPrice'] = self.bid_price
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BidPrice') is not None:
            self.bid_price = m.get('BidPrice')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class NodeGroupStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.category = category
        self.count = count
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.count is not None:
            result['Count'] = self.count
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class NodeGroup(TeaModel):
    def __init__(
        self,
        additional_security_group_ids: List[str] = None,
        cost_optimized_config: CostOptimizedConfig = None,
        data_disks: List[DataDisk] = None,
        deployment_set_strategy: str = None,
        graceful_shutdown: bool = None,
        instance_types: List[str] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_group_state: str = None,
        node_group_type: str = None,
        node_resize_strategy: str = None,
        payment_type: str = None,
        running_node_count: int = None,
        spot_bid_prices: List[SpotBidPrice] = None,
        spot_instance_remedy: bool = None,
        spot_strategy: str = None,
        state_change_reason: NodeGroupStateChangeReason = None,
        system_disk: SystemDisk = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
        zone_id: str = None,
    ):
        self.additional_security_group_ids = additional_security_group_ids
        self.cost_optimized_config = cost_optimized_config
        self.data_disks = data_disks
        self.deployment_set_strategy = deployment_set_strategy
        self.graceful_shutdown = graceful_shutdown
        self.instance_types = instance_types
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_group_state = node_group_state
        self.node_group_type = node_group_type
        self.node_resize_strategy = node_resize_strategy
        self.payment_type = payment_type
        self.running_node_count = running_node_count
        self.spot_bid_prices = spot_bid_prices
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_strategy = spot_strategy
        self.state_change_reason = state_change_reason
        self.system_disk = system_disk
        self.v_switch_ids = v_switch_ids
        self.with_public_ip = with_public_ip
        self.zone_id = zone_id

    def validate(self):
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_bid_prices:
            for k in self.spot_bid_prices:
                if k:
                    k.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids
        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy
        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_state is not None:
            result['NodeGroupState'] = self.node_group_state
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.running_node_count is not None:
            result['RunningNodeCount'] = self.running_node_count
        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k in self.spot_bid_prices:
                result['SpotBidPrices'].append(k.to_map() if k else None)
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')
        if m.get('CostOptimizedConfig') is not None:
            temp_model = CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m['CostOptimizedConfig'])
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')
        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupState') is not None:
            self.node_group_state = m.get('NodeGroupState')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RunningNodeCount') is not None:
            self.running_node_count = m.get('RunningNodeCount')
        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k in m.get('SpotBidPrices'):
                temp_model = SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k))
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('StateChangeReason') is not None:
            temp_model = NodeGroupStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        if m.get('SystemDisk') is not None:
            temp_model = SystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class NodeGroupConfig(TeaModel):
    def __init__(
        self,
        additional_security_group_ids: List[str] = None,
        cost_optimized_config: CostOptimizedConfig = None,
        data_disks: List[DataDisk] = None,
        deployment_set_strategy: str = None,
        graceful_shutdown: bool = None,
        instance_types: List[str] = None,
        node_count: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        node_resize_strategy: str = None,
        payment_type: str = None,
        spot_bid_prices: List[SpotBidPrice] = None,
        spot_instance_remedy: bool = None,
        spot_strategy: str = None,
        subscription_config: SubscriptionConfig = None,
        system_disk: SystemDisk = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
    ):
        self.additional_security_group_ids = additional_security_group_ids
        self.cost_optimized_config = cost_optimized_config
        self.data_disks = data_disks
        self.deployment_set_strategy = deployment_set_strategy
        self.graceful_shutdown = graceful_shutdown
        self.instance_types = instance_types
        self.node_count = node_count
        self.node_group_name = node_group_name
        self.node_group_type = node_group_type
        self.node_resize_strategy = node_resize_strategy
        self.payment_type = payment_type
        self.spot_bid_prices = spot_bid_prices
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_strategy = spot_strategy
        self.subscription_config = subscription_config
        self.system_disk = system_disk
        self.v_switch_ids = v_switch_ids
        self.with_public_ip = with_public_ip

    def validate(self):
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_bid_prices:
            for k in self.spot_bid_prices:
                if k:
                    k.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids
        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy
        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k in self.spot_bid_prices:
                result['SpotBidPrices'].append(k.to_map() if k else None)
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')
        if m.get('CostOptimizedConfig') is not None:
            temp_model = CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m['CostOptimizedConfig'])
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')
        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k in m.get('SpotBidPrices'):
                temp_model = SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k))
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        if m.get('SystemDisk') is not None:
            temp_model = SystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')
        return self


class NodeGroupParam(TeaModel):
    def __init__(
        self,
        auto_pay_order: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        data_disks: List[DiskInfo] = None,
        description: str = None,
        instance_types: List[str] = None,
        node_count: int = None,
        node_group_index: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        system_disk: SystemDiskParam = None,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        self.auto_pay_order = auto_pay_order
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.data_disks = data_disks
        self.description = description
        self.instance_types = instance_types
        self.node_count = node_count
        self.node_group_index = node_group_index
        self.node_group_name = node_group_name
        self.node_group_type = node_group_type
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.system_disk = system_disk
        self.v_switch_ids = v_switch_ids
        self.zone_id = zone_id

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_index is not None:
            result['NodeGroupIndex'] = self.node_group_index
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DiskInfo()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupIndex') is not None:
            self.node_group_index = m.get('NodeGroupIndex')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('SystemDisk') is not None:
            temp_model = SystemDiskParam()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class OSUser(TeaModel):
    def __init__(
        self,
        group: str = None,
        password: str = None,
        user: str = None,
    ):
        self.group = group
        self.password = password
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class OnKubeClusterResource(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class OperationStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class Operation(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: int = None,
        description: str = None,
        end_time: int = None,
        operation_id: str = None,
        operation_state: str = None,
        operation_type: str = None,
        start_time: int = None,
        state_change_reason: OperationStateChangeReason = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.description = description
        self.end_time = end_time
        self.operation_id = operation_id
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.start_time = start_time
        self.state_change_reason = state_change_reason

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_state is not None:
            result['OperationState'] = self.operation_state
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationState') is not None:
            self.operation_state = m.get('OperationState')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StateChangeReason') is not None:
            temp_model = OperationStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['StateChangeReason'])
        return self


class Order(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        order_id: str = None,
    ):
        self.create_time = create_time
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class Page(TeaModel):
    def __init__(
        self,
        items: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class Pod(TeaModel):
    def __init__(
        self,
        message: str = None,
        pod_name: str = None,
        pod_status: str = None,
        reason: str = None,
    ):
        self.message = message
        self.pod_name = pod_name
        self.pod_status = pod_status
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class PromotionInfo(TeaModel):
    def __init__(
        self,
        can_prom_fee: str = None,
        is_selected: str = None,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.is_selected = is_selected
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class PriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        pay_type: str = None,
        promotion_results: List[PromotionInfo] = None,
        resource_type: str = None,
        spot_instance_type_original_price: str = None,
        spot_instance_type_price: str = None,
        spot_original_price: str = None,
        spot_price: str = None,
        tax_price: str = None,
        trade_price: str = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.pay_type = pay_type
        self.promotion_results = promotion_results
        self.resource_type = resource_type
        self.spot_instance_type_original_price = spot_instance_type_original_price
        self.spot_instance_type_price = spot_instance_type_price
        self.spot_original_price = spot_original_price
        self.spot_price = spot_price
        self.tax_price = tax_price
        self.trade_price = trade_price

    def validate(self):
        if self.promotion_results:
            for k in self.promotion_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        result['PromotionResults'] = []
        if self.promotion_results is not None:
            for k in self.promotion_results:
                result['PromotionResults'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_instance_type_original_price is not None:
            result['SpotInstanceTypeOriginalPrice'] = self.spot_instance_type_original_price
        if self.spot_instance_type_price is not None:
            result['SpotInstanceTypePrice'] = self.spot_instance_type_price
        if self.spot_original_price is not None:
            result['SpotOriginalPrice'] = self.spot_original_price
        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price
        if self.tax_price is not None:
            result['TaxPrice'] = self.tax_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        self.promotion_results = []
        if m.get('PromotionResults') is not None:
            for k in m.get('PromotionResults'):
                temp_model = PromotionInfo()
                self.promotion_results.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotInstanceTypeOriginalPrice') is not None:
            self.spot_instance_type_original_price = m.get('SpotInstanceTypeOriginalPrice')
        if m.get('SpotInstanceTypePrice') is not None:
            self.spot_instance_type_price = m.get('SpotInstanceTypePrice')
        if m.get('SpotOriginalPrice') is not None:
            self.spot_original_price = m.get('SpotOriginalPrice')
        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')
        if m.get('TaxPrice') is not None:
            self.tax_price = m.get('TaxPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class Promotion(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.product_code = product_code
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class PromotionParam(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.product_code = product_code
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class RenewInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        renew_duration: int = None,
        renew_duration_unit: str = None,
    ):
        self.instance_id = instance_id
        self.renew_duration = renew_duration
        self.renew_duration_unit = renew_duration_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')
        return self


class RenewInstanceParam(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        renew_duration: int = None,
        renew_duration_unit: str = None,
    ):
        self.instance_id = instance_id
        self.renew_duration = renew_duration
        self.renew_duration_unit = renew_duration_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')
        return self


class RequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ResizeDiskNodeGroupParam(TeaModel):
    def __init__(
        self,
        data_disk_capacity: int = None,
        node_group_id: str = None,
        rolling_restart: bool = None,
    ):
        self.data_disk_capacity = data_disk_capacity
        self.node_group_id = node_group_id
        self.rolling_restart = rolling_restart

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_capacity is not None:
            result['DataDiskCapacity'] = self.data_disk_capacity
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.rolling_restart is not None:
            result['RollingRestart'] = self.rolling_restart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCapacity') is not None:
            self.data_disk_capacity = m.get('DataDiskCapacity')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('RollingRestart') is not None:
            self.rolling_restart = m.get('RollingRestart')
        return self


class ScalingActivity(TeaModel):
    def __init__(
        self,
        cause: str = None,
        description: str = None,
        end_time: int = None,
        ess_scaling_rule_id: str = None,
        expect_num: int = None,
        host_group_name: str = None,
        id: str = None,
        instance_ids: str = None,
        scaling_group_id: str = None,
        scaling_rule_name: str = None,
        start_time: int = None,
        status: str = None,
        total_capacity: int = None,
        transition: str = None,
    ):
        self.cause = cause
        self.description = description
        self.end_time = end_time
        self.ess_scaling_rule_id = ess_scaling_rule_id
        self.expect_num = expect_num
        self.host_group_name = host_group_name
        self.id = id
        self.instance_ids = instance_ids
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_name = scaling_rule_name
        self.start_time = start_time
        self.status = status
        self.total_capacity = total_capacity
        self.transition = transition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ess_scaling_rule_id is not None:
            result['EssScalingRuleId'] = self.ess_scaling_rule_id
        if self.expect_num is not None:
            result['ExpectNum'] = self.expect_num
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.transition is not None:
            result['Transition'] = self.transition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EssScalingRuleId') is not None:
            self.ess_scaling_rule_id = m.get('EssScalingRuleId')
        if m.get('ExpectNum') is not None:
            self.expect_num = m.get('ExpectNum')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('Transition') is not None:
            self.transition = m.get('Transition')
        return self


class ScalingConstraints(TeaModel):
    def __init__(
        self,
        max_capacity: int = None,
        min_capacity: int = None,
    ):
        self.max_capacity = max_capacity
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')
        return self


class ScalingGroupConfigInstanceTypeList(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.spot_price_limit = spot_price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        return self


class ScalingGroupConfigMultiAvailablePolicyPolicyParam(TeaModel):
    def __init__(
        self,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
    ):
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        return self


class ScalingGroupConfigMultiAvailablePolicy(TeaModel):
    def __init__(
        self,
        policy_param: ScalingGroupConfigMultiAvailablePolicyPolicyParam = None,
        policy_type: str = None,
    ):
        self.policy_param = policy_param
        self.policy_type = policy_type

    def validate(self):
        if self.policy_param:
            self.policy_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_param is not None:
            result['PolicyParam'] = self.policy_param.to_map()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyParam') is not None:
            temp_model = ScalingGroupConfigMultiAvailablePolicyPolicyParam()
            self.policy_param = temp_model.from_map(m['PolicyParam'])
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ScalingGroupConfigNodeOfflinePolicy(TeaModel):
    def __init__(
        self,
        mode: str = None,
        timeout_ms: int = None,
    ):
        self.mode = mode
        self.timeout_ms = timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.timeout_ms is not None:
            result['TimeoutMs'] = self.timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TimeoutMs') is not None:
            self.timeout_ms = m.get('TimeoutMs')
        return self


class ScalingGroupConfigPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class ScalingGroupConfig(TeaModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_count: int = None,
        data_disk_size: int = None,
        default_cool_down_time: int = None,
        instance_type_list: List[ScalingGroupConfigInstanceTypeList] = None,
        multi_available_policy: ScalingGroupConfigMultiAvailablePolicy = None,
        node_offline_policy: ScalingGroupConfigNodeOfflinePolicy = None,
        private_pool_options: ScalingGroupConfigPrivatePoolOptions = None,
        scaling_max_size: int = None,
        scaling_min_size: int = None,
        spot_strategy: str = None,
        sys_disk_category: str = None,
        sys_disk_size: int = None,
        trigger_mode: str = None,
    ):
        self.data_disk_category = data_disk_category
        self.data_disk_count = data_disk_count
        self.data_disk_size = data_disk_size
        self.default_cool_down_time = default_cool_down_time
        self.instance_type_list = instance_type_list
        self.multi_available_policy = multi_available_policy
        self.node_offline_policy = node_offline_policy
        self.private_pool_options = private_pool_options
        self.scaling_max_size = scaling_max_size
        self.scaling_min_size = scaling_min_size
        self.spot_strategy = spot_strategy
        self.sys_disk_category = sys_disk_category
        self.sys_disk_size = sys_disk_size
        self.trigger_mode = trigger_mode

    def validate(self):
        if self.instance_type_list:
            for k in self.instance_type_list:
                if k:
                    k.validate()
        if self.multi_available_policy:
            self.multi_available_policy.validate()
        if self.node_offline_policy:
            self.node_offline_policy.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_count is not None:
            result['DataDiskCount'] = self.data_disk_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.default_cool_down_time is not None:
            result['DefaultCoolDownTime'] = self.default_cool_down_time
        result['InstanceTypeList'] = []
        if self.instance_type_list is not None:
            for k in self.instance_type_list:
                result['InstanceTypeList'].append(k.to_map() if k else None)
        if self.multi_available_policy is not None:
            result['MultiAvailablePolicy'] = self.multi_available_policy.to_map()
        if self.node_offline_policy is not None:
            result['NodeOfflinePolicy'] = self.node_offline_policy.to_map()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.scaling_max_size is not None:
            result['ScalingMaxSize'] = self.scaling_max_size
        if self.scaling_min_size is not None:
            result['ScalingMinSize'] = self.scaling_min_size
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.sys_disk_category is not None:
            result['SysDiskCategory'] = self.sys_disk_category
        if self.sys_disk_size is not None:
            result['SysDiskSize'] = self.sys_disk_size
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskCount') is not None:
            self.data_disk_count = m.get('DataDiskCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DefaultCoolDownTime') is not None:
            self.default_cool_down_time = m.get('DefaultCoolDownTime')
        self.instance_type_list = []
        if m.get('InstanceTypeList') is not None:
            for k in m.get('InstanceTypeList'):
                temp_model = ScalingGroupConfigInstanceTypeList()
                self.instance_type_list.append(temp_model.from_map(k))
        if m.get('MultiAvailablePolicy') is not None:
            temp_model = ScalingGroupConfigMultiAvailablePolicy()
            self.multi_available_policy = temp_model.from_map(m['MultiAvailablePolicy'])
        if m.get('NodeOfflinePolicy') is not None:
            temp_model = ScalingGroupConfigNodeOfflinePolicy()
            self.node_offline_policy = temp_model.from_map(m['NodeOfflinePolicy'])
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ScalingGroupConfigPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('ScalingMaxSize') is not None:
            self.scaling_max_size = m.get('ScalingMaxSize')
        if m.get('ScalingMinSize') is not None:
            self.scaling_min_size = m.get('ScalingMinSize')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SysDiskCategory') is not None:
            self.sys_disk_category = m.get('SysDiskCategory')
        if m.get('SysDiskSize') is not None:
            self.sys_disk_size = m.get('SysDiskSize')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        return self


class TimeTrigger(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        launch_expiration_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        self.end_time = end_time
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ScalingRule(TeaModel):
    def __init__(
        self,
        activity_type: str = None,
        adjustment_type: str = None,
        adjustment_value: int = None,
        by_load_scaling_rule: MetricsTrigger = None,
        by_time_scaling_rule: TimeTrigger = None,
        cool_down_interval: int = None,
        metrics_trigger: MetricsTrigger = None,
        rule_name: str = None,
        scaling_activity_type: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
        time_trigger: TimeTrigger = None,
        trigger_type: str = None,
    ):
        self.activity_type = activity_type
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.by_load_scaling_rule = by_load_scaling_rule
        self.by_time_scaling_rule = by_time_scaling_rule
        self.cool_down_interval = cool_down_interval
        self.metrics_trigger = metrics_trigger
        self.rule_name = rule_name
        self.scaling_activity_type = scaling_activity_type
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_type = scaling_rule_type
        self.time_trigger = time_trigger
        self.trigger_type = trigger_type

    def validate(self):
        if self.by_load_scaling_rule:
            self.by_load_scaling_rule.validate()
        if self.by_time_scaling_rule:
            self.by_time_scaling_rule.validate()
        if self.metrics_trigger:
            self.metrics_trigger.validate()
        if self.time_trigger:
            self.time_trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.by_load_scaling_rule is not None:
            result['ByLoadScalingRule'] = self.by_load_scaling_rule.to_map()
        if self.by_time_scaling_rule is not None:
            result['ByTimeScalingRule'] = self.by_time_scaling_rule.to_map()
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.time_trigger is not None:
            result['TimeTrigger'] = self.time_trigger.to_map()
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ByLoadScalingRule') is not None:
            temp_model = MetricsTrigger()
            self.by_load_scaling_rule = temp_model.from_map(m['ByLoadScalingRule'])
        if m.get('ByTimeScalingRule') is not None:
            temp_model = TimeTrigger()
            self.by_time_scaling_rule = temp_model.from_map(m['ByTimeScalingRule'])
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('MetricsTrigger') is not None:
            temp_model = MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m['MetricsTrigger'])
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('TimeTrigger') is not None:
            temp_model = TimeTrigger()
            self.time_trigger = temp_model.from_map(m['TimeTrigger'])
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ScalingRuleSpecByLoadScalingRuleSpec(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.statistics = statistics
        self.threshold = threshold
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.time_window is not None:
            result['TimeWindow'] = self.time_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')
        return self


class ScalingRuleSpecByTimeScalingRuleSpec(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        self.end_time = end_time
        self.launch_time = launch_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        return self


class ScalingRuleSpec(TeaModel):
    def __init__(
        self,
        adjustment_value: int = None,
        by_load_scaling_rule_spec: ScalingRuleSpecByLoadScalingRuleSpec = None,
        by_time_scaling_rule_spec: ScalingRuleSpecByTimeScalingRuleSpec = None,
        cool_down_interval: int = None,
        scaling_activity_type: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
    ):
        self.adjustment_value = adjustment_value
        self.by_load_scaling_rule_spec = by_load_scaling_rule_spec
        self.by_time_scaling_rule_spec = by_time_scaling_rule_spec
        self.cool_down_interval = cool_down_interval
        self.scaling_activity_type = scaling_activity_type
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        if self.by_load_scaling_rule_spec:
            self.by_load_scaling_rule_spec.validate()
        if self.by_time_scaling_rule_spec:
            self.by_time_scaling_rule_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.by_load_scaling_rule_spec is not None:
            result['ByLoadScalingRuleSpec'] = self.by_load_scaling_rule_spec.to_map()
        if self.by_time_scaling_rule_spec is not None:
            result['ByTimeScalingRuleSpec'] = self.by_time_scaling_rule_spec.to_map()
        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval
        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ByLoadScalingRuleSpec') is not None:
            temp_model = ScalingRuleSpecByLoadScalingRuleSpec()
            self.by_load_scaling_rule_spec = temp_model.from_map(m['ByLoadScalingRuleSpec'])
        if m.get('ByTimeScalingRuleSpec') is not None:
            temp_model = ScalingRuleSpecByTimeScalingRuleSpec()
            self.by_time_scaling_rule_spec = temp_model.from_map(m['ByTimeScalingRuleSpec'])
        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')
        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        return self


class ScalingRuleV1RuleParam(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        metric_name: str = None,
        period: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        statistics: str = None,
        threshold: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.evaluation_count = evaluation_count
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.metric_name = metric_name
        self.period = period
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ScalingRuleV1(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cool_down_time: int = None,
        rule_name: str = None,
        rule_param: ScalingRuleV1RuleParam = None,
        rule_type: str = None,
        scaling_config_biz_id: str = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.cool_down_time = cool_down_time
        self.rule_name = rule_name
        self.rule_param = rule_param
        self.rule_type = rule_type
        self.scaling_config_biz_id = scaling_config_biz_id

    def validate(self):
        if self.rule_param:
            self.rule_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_param is not None:
            result['RuleParam'] = self.rule_param.to_map()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scaling_config_biz_id is not None:
            result['ScalingConfigBizId'] = self.scaling_config_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleParam') is not None:
            temp_model = ScalingRuleV1RuleParam()
            self.rule_param = temp_model.from_map(m['RuleParam'])
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScalingConfigBizId') is not None:
            self.scaling_config_biz_id = m.get('ScalingConfigBizId')
        return self


class Script(TeaModel):
    def __init__(
        self,
        execution_fail_strategy: str = None,
        execution_moment: str = None,
        node_selector: NodeSelector = None,
        priority: int = None,
        script_args: str = None,
        script_name: str = None,
        script_path: str = None,
    ):
        self.execution_fail_strategy = execution_fail_strategy
        self.execution_moment = execution_moment
        self.node_selector = node_selector
        self.priority = priority
        self.script_args = script_args
        self.script_name = script_name
        self.script_path = script_path

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy
        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment
        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_path is not None:
            result['ScriptPath'] = self.script_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')
        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')
        if m.get('NodeSelector') is not None:
            temp_model = NodeSelector()
            self.node_selector = temp_model.from_map(m['NodeSelector'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')
        return self


class SpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class StateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class UpdateApplicationConfig(TeaModel):
    def __init__(
        self,
        config_action: str = None,
        config_description: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        config_scope: str = None,
        effective_actions: str = None,
        effective_type: str = None,
        node_group_id: str = None,
        node_id: str = None,
    ):
        self.config_action = config_action
        self.config_description = config_description
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value
        self.config_scope = config_scope
        self.effective_actions = effective_actions
        self.effective_type = effective_type
        self.node_group_id = node_group_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_action is not None:
            result['ConfigAction'] = self.config_action
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value
        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope
        if self.effective_actions is not None:
            result['EffectiveActions'] = self.effective_actions
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')
        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')
        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')
        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')
        if m.get('EffectiveActions') is not None:
            self.effective_actions = m.get('EffectiveActions')
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class UpdateSpecNodeGroup(TeaModel):
    def __init__(
        self,
        new_instance_type: str = None,
        node_group_id: str = None,
    ):
        self.new_instance_type = new_instance_type
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_instance_type is not None:
            result['NewInstanceType'] = self.new_instance_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewInstanceType') is not None:
            self.new_instance_type = m.get('NewInstanceType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class UpdateSpecNodeGroupParam(TeaModel):
    def __init__(
        self,
        new_instance_type: str = None,
        node_group_id: str = None,
    ):
        self.new_instance_type = new_instance_type
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_instance_type is not None:
            result['NewInstanceType'] = self.new_instance_type
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewInstanceType') is not None:
            self.new_instance_type = m.get('NewInstanceType')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class User(TeaModel):
    def __init__(
        self,
        group: str = None,
        password: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.group = group
        self.password = password
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UserParam(TeaModel):
    def __init__(
        self,
        password: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        application_configs: List[ApplicationConfig] = None,
        applications: List[Application] = None,
        bootstrap_scripts: List[Script] = None,
        client_token: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        deploy_mode: str = None,
        node_attributes: NodeAttributes = None,
        node_groups: List[NodeGroupConfig] = None,
        payment_type: str = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        security_mode: str = None,
        subscription_config: SubscriptionConfig = None,
        tags: List[Tag] = None,
    ):
        self.application_configs = application_configs
        self.applications = applications
        self.bootstrap_scripts = bootstrap_scripts
        self.client_token = client_token
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.deploy_mode = deploy_mode
        self.node_attributes = node_attributes
        self.node_groups = node_groups
        self.payment_type = payment_type
        self.region_id = region_id
        self.release_version = release_version
        self.resource_group_id = resource_group_id
        self.security_mode = security_mode
        self.subscription_config = subscription_config
        self.tags = tags

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()
        if self.bootstrap_scripts:
            for k in self.bootstrap_scripts:
                if k:
                    k.validate()
        if self.node_attributes:
            self.node_attributes.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k in self.application_configs:
                result['ApplicationConfigs'].append(k.to_map() if k else None)
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        result['BootstrapScripts'] = []
        if self.bootstrap_scripts is not None:
            for k in self.bootstrap_scripts:
                result['BootstrapScripts'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k in m.get('ApplicationConfigs'):
                temp_model = ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k))
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = Application()
                self.applications.append(temp_model.from_map(k))
        self.bootstrap_scripts = []
        if m.get('BootstrapScripts') is not None:
            for k in m.get('BootstrapScripts'):
                temp_model = Script()
                self.bootstrap_scripts.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('NodeAttributes') is not None:
            temp_model = NodeAttributes()
            self.node_attributes = temp_model.from_map(m['NodeAttributes'])
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = NodeGroupConfig()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        if m.get('SubscriptionConfig') is not None:
            temp_model = SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m['SubscriptionConfig'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecreaseNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        decrease_node_count: int = None,
        node_group_id: str = None,
        node_ids: List[str] = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.decrease_node_count = decrease_node_count
        self.node_group_id = node_group_id
        self.node_ids = node_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.decrease_node_count is not None:
            result['DecreaseNodeCount'] = self.decrease_node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DecreaseNodeCount') is not None:
            self.decrease_node_count = m.get('DecreaseNodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DecreaseNodesResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecreaseNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DecreaseNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DecreaseNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster: Cluster = None,
        request_id: str = None,
    ):
        self.cluster = cluster
        self.request_id = request_id

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = Cluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.node_group_id = node_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetNodeGroupResponseBody(TeaModel):
    def __init__(
        self,
        node_group: NodeGroup = None,
        request_id: str = None,
    ):
        self.node_group = node_group
        self.request_id = request_id

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroup') is not None:
            temp_model = NodeGroup()
            self.node_group = temp_model.from_map(m['NodeGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNodeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        operation_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.operation_id = operation_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOperationResponseBody(TeaModel):
    def __init__(
        self,
        operation: Operation = None,
        request_id: str = None,
    ):
        self.operation = operation
        self.request_id = request_id

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            temp_model = Operation()
            self.operation = temp_model.from_map(m['Operation'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseNodesRequest(TeaModel):
    def __init__(
        self,
        application_configs: List[ApplicationConfig] = None,
        auto_pay_order: bool = None,
        cluster_id: str = None,
        increase_node_count: int = None,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        region_id: str = None,
    ):
        self.application_configs = application_configs
        self.auto_pay_order = auto_pay_order
        self.cluster_id = cluster_id
        self.increase_node_count = increase_node_count
        self.node_group_id = node_group_id
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.region_id = region_id

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k in self.application_configs:
                result['ApplicationConfigs'].append(k.to_map() if k else None)
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.increase_node_count is not None:
            result['IncreaseNodeCount'] = self.increase_node_count
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k in m.get('ApplicationConfigs'):
                temp_model = ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k))
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IncreaseNodeCount') is not None:
            self.increase_node_count = m.get('IncreaseNodeCount')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class IncreaseNodesResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IncreaseNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IncreaseNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class JoinResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JoinResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = JoinResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_ids: List[str] = None,
        node_group_names: List[str] = None,
        node_group_states: List[str] = None,
        node_group_types: List[str] = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.max_results = max_results
        self.next_token = next_token
        self.node_group_ids = node_group_ids
        self.node_group_names = node_group_names
        self.node_group_states = node_group_states
        self.node_group_types = node_group_types
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_group_names is not None:
            result['NodeGroupNames'] = self.node_group_names
        if self.node_group_states is not None:
            result['NodeGroupStates'] = self.node_group_states
        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeGroupNames') is not None:
            self.node_group_names = m.get('NodeGroupNames')
        if m.get('NodeGroupStates') is not None:
            self.node_group_states = m.get('NodeGroupStates')
        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNodeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_groups: List[NodeGroup] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.node_groups = node_groups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = NodeGroup()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_ids: List[str] = None,
        node_ids: List[str] = None,
        node_names: List[str] = None,
        node_states: List[str] = None,
        private_ips: List[str] = None,
        public_ips: List[str] = None,
        region_id: str = None,
        tags: List[Tag] = None,
    ):
        self.cluster_id = cluster_id
        self.max_results = max_results
        self.next_token = next_token
        self.node_group_ids = node_group_ids
        self.node_ids = node_ids
        self.node_names = node_names
        self.node_states = node_states
        self.private_ips = private_ips
        self.public_ips = public_ips
        self.region_id = region_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        if self.node_states is not None:
            result['NodeStates'] = self.node_states
        if self.private_ips is not None:
            result['PrivateIps'] = self.private_ips
        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        if m.get('NodeStates') is not None:
            self.node_states = m.get('NodeStates')
        if m.get('PrivateIps') is not None:
            self.private_ips = m.get('PrivateIps')
        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        nodes: List[Node] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.nodes = nodes
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = Node()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


