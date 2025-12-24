# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAutoScalingRuleRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        security_token: str = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.rule_name = rule_name
        # This parameter is required.
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
        self.security_token = security_token
        self.silence_time = silence_time
        self.start_time = start_time
        self.target_metric = target_metric
        self.target_nodes = target_nodes
        self.threshold_lower = threshold_lower
        self.threshold_upper = threshold_upper
        self.trigger_cron_expr = trigger_cron_expr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.observation_window is not None:
            result['ObservationWindow'] = self.observation_window

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step

        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_metric is not None:
            result['TargetMetric'] = self.target_metric

        if self.target_nodes is not None:
            result['TargetNodes'] = self.target_nodes

        if self.threshold_lower is not None:
            result['ThresholdLower'] = self.threshold_lower

        if self.threshold_upper is not None:
            result['ThresholdUpper'] = self.threshold_upper

        if self.trigger_cron_expr is not None:
            result['TriggerCronExpr'] = self.trigger_cron_expr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ObservationWindow') is not None:
            self.observation_window = m.get('ObservationWindow')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')

        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetMetric') is not None:
            self.target_metric = m.get('TargetMetric')

        if m.get('TargetNodes') is not None:
            self.target_nodes = m.get('TargetNodes')

        if m.get('ThresholdLower') is not None:
            self.threshold_lower = m.get('ThresholdLower')

        if m.get('ThresholdUpper') is not None:
            self.threshold_upper = m.get('ThresholdUpper')

        if m.get('TriggerCronExpr') is not None:
            self.trigger_cron_expr = m.get('TriggerCronExpr')

        return self

