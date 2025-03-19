# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
    ):
        # The ID of the resource group into which you want to change.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The region ID.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLdpsColumnarIndexStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CheckLdpsColumnarIndexStatusResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        opened: bool = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.opened = opened
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.opened is not None:
            result['Opened'] = self.opened
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Opened') is not None:
            self.opened = m.get('Opened')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckLdpsColumnarIndexStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckLdpsColumnarIndexStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckLdpsColumnarIndexStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoScalingConfigRequestScaleRuleList(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step
        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')
        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')
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


class CreateAutoScalingConfigRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_rule_list: List[CreateAutoScalingConfigRequestScaleRuleList] = None,
        scale_type: str = None,
        security_token: str = None,
        spec_id: str = None,
    ):
        # This parameter is required.
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        # This parameter is required.
        self.engine = engine
        # This parameter is required.
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_rule_list = scale_rule_list
        # This parameter is required.
        self.scale_type = scale_type
        self.security_token = security_token
        # This parameter is required.
        self.spec_id = spec_id

    def validate(self):
        if self.scale_rule_list:
            for k in self.scale_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end
        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max
        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['ScaleRuleList'] = []
        if self.scale_rule_list is not None:
            for k in self.scale_rule_list:
                result['ScaleRuleList'].append(k.to_map() if k else None)
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')
        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')
        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.scale_rule_list = []
        if m.get('ScaleRuleList') is not None:
            for k in m.get('ScaleRuleList'):
                temp_model = CreateAutoScalingConfigRequestScaleRuleList()
                self.scale_rule_list.append(temp_model.from_map(k))
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class CreateAutoScalingConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_rule_list_shrink: str = None,
        scale_type: str = None,
        security_token: str = None,
        spec_id: str = None,
    ):
        # This parameter is required.
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        # This parameter is required.
        self.engine = engine
        # This parameter is required.
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_rule_list_shrink = scale_rule_list_shrink
        # This parameter is required.
        self.scale_type = scale_type
        self.security_token = security_token
        # This parameter is required.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end
        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max
        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scale_rule_list_shrink is not None:
            result['ScaleRuleList'] = self.scale_rule_list_shrink
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')
        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')
        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScaleRuleList') is not None:
            self.scale_rule_list_shrink = m.get('ScaleRuleList')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class CreateAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAutoScalingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoScalingRuleRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAutoScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAutoScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAutoScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateAutoScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLdpsComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        properties: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.properties = properties
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateLdpsComputeGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLdpsComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLdpsComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateLdpsComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLindormInstanceRequestTag(TeaModel):
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


class CreateLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        auto_renew_duration: str = None,
        auto_renewal: bool = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        disk_category: str = None,
        duration: str = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_alias: str = None,
        instance_storage: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        lts_num: str = None,
        lts_spec: str = None,
        multi_zone_combination: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        stream_num: int = None,
        stream_spec: str = None,
        tag: List[CreateLindormInstanceRequestTag] = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch that is specified for the zone for the coordinate node of the instance. The vSwitch must be deployed in the zone specified by the ArbiterZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The ID of the zone for the coordinate node of the instance. **This parameter is required if you want to create a multi-zone instance**.
        self.arbiter_zone_id = arbiter_zone_id
        # The architecture of the instance. Valid values:
        # 
        # *   **1.0**: The instance that you want to create is a single-zone instance.
        # *   **2.0**: The instance that you want to create is a multi-zone instance.
        # 
        # By default, the value of this parameter is 1.0. To create a multi-zone instance, set this parameter to 2.0. **This parameter is required if you want to create a multi-zone instance**.
        self.arch_version = arch_version
        # The auto-renewal duration. Unit: month.
        # 
        # Valid values: **1** to **12**.
        # 
        # >  This parameter is available only when the **AutoRenewal** parameter is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        # 
        # Default value: false.
        # 
        # >  This parameter is available only when the **PayType** parameter is set to **PREPAY**.
        self.auto_renewal = auto_renewal
        # The cold storage capacity of the instance. By default, if you leave this parameter unspecified, cold storage is not enabled for the instance. Unit: GB. Valid values: **800** to **1000000**.
        self.cold_storage = cold_storage
        # The storage capacity of the disk of a single core node. Valid values: 400 to 64000. Unit: GB. **This parameter is required if you want to create a multi-zone instance**.
        self.core_single_storage = core_single_storage
        # The specification of the nodes in the instance if you set DiskCategory to local_ssd_pro or local_hdd_pro.
        # 
        # When DiskCategory is set to local_ssd_pro, you can set this parameter to the following values:
        # 
        # *   **lindorm.i2.xlarge**: Each node has 4 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.i2.2xlarge**: Each node has 8 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.i2.4xlarge**: Each node has 16 dedicated CPU cores and 128 GB of dedicated memory.
        # *   **lindorm.i2.8xlarge**: Each node has 32 dedicated CPU cores and 256 GB of dedicated memory.
        # 
        # When DiskCategory is set to local_hdd_pro, you can set this parameter to the following values:
        # 
        # *   **lindorm.d1.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.d1.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.d1.6xlarge**: Each node has 24 dedicated CPU cores and 96 GB of dedicated memory.
        self.core_spec = core_spec
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **capacity_cloud_storage**: This instance uses the Capacity type of storage.
        # *   **local_ssd_pro**: This instance uses local SSDs.
        # *   **local_hdd_pro**: This instance uses local HDDs.
        # 
        # This parameter is required.
        self.disk_category = disk_category
        # The subscription period of the instance. The valid values of this parameter depend on the value of the PricingCycle parameter.
        # 
        # *   If PricingCycle is set to **Month**, set this parameter to an integer that ranges from **1** to **9**.
        # *   If PricingCycle is set to **Year**, set this parameter to an integer that ranges from **1** to **3**.
        # 
        # > This parameter is available and required when the PayType parameter is set to **PREPAY**.
        self.duration = duration
        # The number of LindormDFS nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **60**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **8**.
        self.filestore_num = filestore_num
        # The specification of LindormDFS nodes in the instance. Set the value of this parameter to **lindorm.c.xlarge**, which indicates that each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        self.filestore_spec = filestore_spec
        # The name of the instance that you want to create.
        self.instance_alias = instance_alias
        # The storage capacity of the instance you want to create. Unit: GB.
        self.instance_storage = instance_storage
        # The number of LindormTable nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **90**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **400**.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.  The valid values of this parameter range from 4 to 400 if you want to create a multi-zone instance.
        self.lindorm_num = lindorm_num
        # The specification of LindormTable nodes in the instance. Valid values:
        # 
        # *   **lindorm.c.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        self.lindorm_spec = lindorm_spec
        # The disk type of the log nodes. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.log_disk_category = log_disk_category
        # The number of the log nodes. Valid values: 4 to 400. **This parameter is required if you want to create a multi-zone instance**.
        self.log_num = log_num
        # The storage capacity of the disk of a single log node. Valid values: 400 to 64000. Unit: GB. **This parameter is required if you want to create a multi-zone instance**.
        self.log_single_storage = log_single_storage
        # The type of the log nodes. Valid values:
        # 
        # *   **lindorm.sn1.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.sn1.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.log_spec = log_spec
        # The number of LTS nodes in the instance. Valid values: **0** to **60**.
        self.lts_num = lts_num
        # The specification of LTS nodes in the instance. Valid values:
        # 
        # *   **lindorm.c.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.lts_spec = lts_spec
        # The combinations of zones that are available for the multi-zone instance. You can go to the purchase page of Lindorm to view the supported zone combinations.
        # 
        # *   **ap-southeast-5abc-aliyun**: Zone A+B+C in the Indonesia (Jakarta) region.
        # *   **cn-hangzhou-ehi-aliyun**: Zone E+H+I in the China (Hangzhou) region.
        # *   **cn-beijing-acd-aliyun**: Zone A+C+D in the China (Beijing) region.
        # *   **ap-southeast-1-abc-aliyun**: Zone A+B+C in the Singapore region.
        # *   **cn-zhangjiakou-abc-aliyun**: Zone A+B+C in the China (Zhangjiakou) region.
        # *   **cn-shanghai-efg-aliyun**: Zone E+F+G in the China (Shanghai) region.
        # *   **cn-shanghai-abd-aliyun**: Zone A+B+D in the China (Shanghai) region.
        # *   **cn-hangzhou-bef-aliyun**: Zone B+E+F in the China (Hangzhou) region.
        # *   **cn-hangzhou-bce-aliyun**: Zone B+C+E in the China (Hangzhou) region.
        # *   **cn-beijing-fgh-aliyun**: Zone F+G+H in the China (Beijing) region.
        # *   **cn-shenzhen-abc-aliyun**: Zone A+B+C in the China (Shenzhen) region.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.multi_zone_combination = multi_zone_combination
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance you want to create. Valid values:
        # 
        # *   **PREPAY**: subscription.
        # *   **POSTPAY**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The period based on which you are charged for the instance. Valid values:
        # 
        # *   **Month**: You are charged for the instance on a monthly basis.
        # *   **Year**: You are charged for the instance on a yearly basis.
        # 
        # > This parameter is available and required when the PayType parameter is set to **PREPAY**.
        self.pricing_cycle = pricing_cycle
        # The ID of the vSwitch that is specified for the secondary zone of the instance. The vSwitch must be deployed in the zone specified by the StandbyZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.primary_vswitch_id = primary_vswitch_id
        # Multi-zone instance, availability zone ID of the primary zone. **This parameter is required if you need to create a multi-zone instance.**\
        self.primary_zone_id = primary_zone_id
        # The ID of the region in which you want to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region in which you can create the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Lindorm instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of LindormSearch nodes in the instance. Valid values: integers from **0** to **60**.
        self.solr_num = solr_num
        # The specification of the LindormSearch nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.solr_spec = solr_spec
        # The ID of the vSwitch that is specified for the secondary zone of the instance. The vSwitch must be deployed in the zone specified by the StandbyZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.standby_vswitch_id = standby_vswitch_id
        # The ID of the secondary zone of the instance. **This parameter is required if you want to create a multi-zone instance**.
        self.standby_zone_id = standby_zone_id
        # The number of LindormStream nodes in the instance. Valid values: integers from **0** to **60**.
        self.stream_num = stream_num
        # The specification of the LindormStream nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.stream_spec = stream_spec
        self.tag = tag
        # The number of the LindormTSDB nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **24**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **32**.
        self.tsdb_num = tsdb_num
        # The specification of the LindormTSDB nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.tsdb_spec = tsdb_spec
        # The ID of the VPC in which you want to create the instance.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The ID of the vSwitch to which you want the instance to connect.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the zone in which you want to create the instance.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num
        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num
        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec
        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.lts_num is not None:
            result['LtsNum'] = self.lts_num
        if self.lts_spec is not None:
            result['LtsSpec'] = self.lts_spec
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num
        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        if self.stream_spec is not None:
            result['StreamSpec'] = self.stream_spec
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num
        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')
        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')
        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')
        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('LtsNum') is not None:
            self.lts_num = m.get('LtsNum')
        if m.get('LtsSpec') is not None:
            self.lts_spec = m.get('LtsSpec')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')
        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        if m.get('StreamSpec') is not None:
            self.stream_spec = m.get('StreamSpec')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateLindormInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')
        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The ID of the Lindorm instance that is created.
        self.instance_id = instance_id
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLindormV2InstanceRequestEngineListNodeGroupList(TeaModel):
    def __init__(
        self,
        node_count: int = None,
        node_disk_size: int = None,
        node_disk_type: str = None,
        node_spec: str = None,
        resource_group_name: str = None,
    ):
        # This parameter is required.
        self.node_count = node_count
        self.node_disk_size = node_disk_size
        self.node_disk_type = node_disk_type
        # This parameter is required.
        self.node_spec = node_spec
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size
        if self.node_disk_type is not None:
            result['NodeDiskType'] = self.node_disk_type
        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')
        if m.get('NodeDiskType') is not None:
            self.node_disk_type = m.get('NodeDiskType')
        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class CreateLindormV2InstanceRequestEngineList(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        node_group_list: List[CreateLindormV2InstanceRequestEngineListNodeGroupList] = None,
    ):
        # This parameter is required.
        self.engine_type = engine_type
        self.node_group_list = node_group_list

    def validate(self):
        if self.node_group_list:
            for k in self.node_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        result['NodeGroupList'] = []
        if self.node_group_list is not None:
            for k in self.node_group_list:
                result['NodeGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        self.node_group_list = []
        if m.get('NodeGroupList') is not None:
            for k in m.get('NodeGroupList'):
                temp_model = CreateLindormV2InstanceRequestEngineListNodeGroupList()
                self.node_group_list.append(temp_model.from_map(k))
        return self


class CreateLindormV2InstanceRequest(TeaModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        auto_renew_duration: str = None,
        auto_renewal: bool = None,
        capacity_storage_size: int = None,
        cloud_storage_size: int = None,
        cloud_storage_type: str = None,
        cluster_mode: str = None,
        cluster_pattern: str = None,
        duration: int = None,
        enable_capacity_storage: bool = None,
        engine_list: List[CreateLindormV2InstanceRequestEngineList] = None,
        instance_alias: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.arch_version = arch_version
        self.auto_renew_duration = auto_renew_duration
        self.auto_renewal = auto_renewal
        self.capacity_storage_size = capacity_storage_size
        self.cloud_storage_size = cloud_storage_size
        self.cloud_storage_type = cloud_storage_type
        self.cluster_mode = cluster_mode
        self.cluster_pattern = cluster_pattern
        self.duration = duration
        self.enable_capacity_storage = enable_capacity_storage
        # This parameter is required.
        self.engine_list = engine_list
        self.instance_alias = instance_alias
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_zone_id = primary_zone_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id
        # This parameter is required.
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.capacity_storage_size is not None:
            result['CapacityStorageSize'] = self.capacity_storage_size
        if self.cloud_storage_size is not None:
            result['CloudStorageSize'] = self.cloud_storage_size
        if self.cloud_storage_type is not None:
            result['CloudStorageType'] = self.cloud_storage_type
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_pattern is not None:
            result['ClusterPattern'] = self.cluster_pattern
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.enable_capacity_storage is not None:
            result['EnableCapacityStorage'] = self.enable_capacity_storage
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('CapacityStorageSize') is not None:
            self.capacity_storage_size = m.get('CapacityStorageSize')
        if m.get('CloudStorageSize') is not None:
            self.cloud_storage_size = m.get('CloudStorageSize')
        if m.get('CloudStorageType') is not None:
            self.cloud_storage_type = m.get('CloudStorageType')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterPattern') is not None:
            self.cluster_pattern = m.get('ClusterPattern')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnableCapacityStorage') is not None:
            self.enable_capacity_storage = m.get('EnableCapacityStorage')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = CreateLindormV2InstanceRequestEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLindormV2InstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLindormV2InstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLindormV2InstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateLindormV2InstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoScalingConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAutoScalingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoScalingRuleRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_id: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.rule_id = rule_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteAutoScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAutoScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAutoScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAutoScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomResourceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteCustomResourceResponseBody(TeaModel):
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


class DeleteCustomResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteCustomResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLdpsComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteLdpsComputeGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLdpsComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLdpsComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteLdpsComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployLdpsSemiManagedComponentRequest(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.component_name = component_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeployLdpsSemiManagedComponentResponseBody(TeaModel):
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


class DeployLdpsSemiManagedComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployLdpsSemiManagedComponentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployLdpsSemiManagedComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The display language of the regions in the returned results. Valid values:
        # 
        # *   **zh-CN** (default): Chinese.
        # *   **en-US**: English.
        self.accept_language = accept_language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint for the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The regions supported by Lindorm.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoScalingConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetAutoScalingConfigResponseBodyDataScaleRuleList(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step
        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')
        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')
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


class GetAutoScalingConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        scale_rule_list: List[GetAutoScalingConfigResponseBodyDataScaleRuleList] = None,
        scale_type: str = None,
        spec_id: str = None,
    ):
        self.config_id = config_id
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        self.engine = engine
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.scale_rule_list = scale_rule_list
        self.scale_type = scale_type
        self.spec_id = spec_id

    def validate(self):
        if self.scale_rule_list:
            for k in self.scale_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end
        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max
        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min
        result['ScaleRuleList'] = []
        if self.scale_rule_list is not None:
            for k in self.scale_rule_list:
                result['ScaleRuleList'].append(k.to_map() if k else None)
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')
        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')
        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')
        self.scale_rule_list = []
        if m.get('ScaleRuleList') is not None:
            for k in m.get('ScaleRuleList'):
                temp_model = GetAutoScalingConfigResponseBodyDataScaleRuleList()
                self.scale_rule_list.append(temp_model.from_map(k))
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class GetAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetAutoScalingConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAutoScalingConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoScalingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoScalingRuleRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_id: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.rule_id = rule_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetAutoScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step
        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')
        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')
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


class GetAutoScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetAutoScalingRuleResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAutoScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAutoScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClientSourceIpRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetClientSourceIpResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        client_ip: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.client_ip = client_ip
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClientSourceIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClientSourceIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetClientSourceIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEngineDefaultAuthRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetEngineDefaultAuthResponseBodyAuthInfos(TeaModel):
    def __init__(
        self,
        engine: str = None,
        password: str = None,
        username: str = None,
    ):
        self.engine = engine
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetEngineDefaultAuthResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        auth_infos: List[GetEngineDefaultAuthResponseBodyAuthInfos] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.auth_infos = auth_infos
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        if self.auth_infos:
            for k in self.auth_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['AuthInfos'] = []
        if self.auth_infos is not None:
            for k in self.auth_infos:
                result['AuthInfos'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.auth_infos = []
        if m.get('AuthInfos') is not None:
            for k in m.get('AuthInfos'):
                temp_model = GetEngineDefaultAuthResponseBodyAuthInfos()
                self.auth_infos.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEngineDefaultAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEngineDefaultAuthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetEngineDefaultAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the instance whose whitelists you want to query. You can call the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426068.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetInstanceIpWhiteListResponseBodyGroupList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        security_ip_list: str = None,
    ):
        # The name of the IP address whitelist.
        self.group_name = group_name
        # The IP addresses in the whitelist.
        self.security_ip_list = security_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        return self


class GetInstanceIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        group_list: List[GetInstanceIpWhiteListResponseBodyGroupList] = None,
        instance_id: str = None,
        ip_list: List[str] = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The details about the IP address whitelists.
        self.group_list = group_list
        # The ID of the Lindorm instance.
        self.instance_id = instance_id
        # The list of IP addresses in the whitelist of the instance.
        self.ip_list = ip_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = GetInstanceIpWhiteListResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetInstanceSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        request_id: str = None,
        security_groups: List[str] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.instance_id = instance_id
        self.request_id = request_id
        self.security_groups = security_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        return self


class GetInstanceSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLdpsComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLdpsComputeGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        properties: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.group_name = group_name
        self.properties = properties
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLdpsComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLdpsComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLdpsComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLdpsNamespacedQuotaRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace = namespace
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas(TeaModel):
    def __init__(
        self,
        cpu_amount: str = None,
        memory_amount: str = None,
        name: str = None,
        used_cpu: str = None,
        used_memory: str = None,
    ):
        self.cpu_amount = cpu_amount
        self.memory_amount = memory_amount
        self.name = name
        self.used_cpu = used_cpu
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_amount is not None:
            result['CpuAmount'] = self.cpu_amount
        if self.memory_amount is not None:
            result['MemoryAmount'] = self.memory_amount
        if self.name is not None:
            result['Name'] = self.name
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAmount') is not None:
            self.cpu_amount = m.get('CpuAmount')
        if m.get('MemoryAmount') is not None:
            self.memory_amount = m.get('MemoryAmount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class GetLdpsNamespacedQuotaResponseBody(TeaModel):
    def __init__(
        self,
        namespaced_quotas: List[GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas] = None,
        request_id: str = None,
    ):
        self.namespaced_quotas = namespaced_quotas
        self.request_id = request_id

    def validate(self):
        if self.namespaced_quotas:
            for k in self.namespaced_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NamespacedQuotas'] = []
        if self.namespaced_quotas is not None:
            for k in self.namespaced_quotas:
                result['NamespacedQuotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaced_quotas = []
        if m.get('NamespacedQuotas') is not None:
            for k in m.get('NamespacedQuotas'):
                temp_model = GetLdpsNamespacedQuotaResponseBodyNamespacedQuotas()
                self.namespaced_quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLdpsNamespacedQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLdpsNamespacedQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLdpsNamespacedQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLdpsResourceCostRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.job_id = job_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetLdpsResourceCostResponseBody(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        request_id: str = None,
        start_time: int = None,
        total_resource: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.job_id = job_id
        self.request_id = request_id
        self.start_time = start_time
        self.total_resource = total_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_resource is not None:
            result['TotalResource'] = self.total_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalResource') is not None:
            self.total_resource = m.get('TotalResource')
        return self


class GetLdpsResourceCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLdpsResourceCostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLdpsResourceCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormFsUsedDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormFsUsedDetailResponseBodyLStorageUsageList(TeaModel):
    def __init__(
        self,
        capacity: str = None,
        disk_type: str = None,
        used: str = None,
        used_lindorm_search: str = None,
        used_lindorm_spark: str = None,
        used_lindorm_table: str = None,
        used_lindorm_tsdb: str = None,
        used_other: str = None,
    ):
        self.capacity = capacity
        self.disk_type = disk_type
        self.used = used
        self.used_lindorm_search = used_lindorm_search
        self.used_lindorm_spark = used_lindorm_spark
        self.used_lindorm_table = used_lindorm_table
        self.used_lindorm_tsdb = used_lindorm_tsdb
        self.used_other = used_other

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.used is not None:
            result['Used'] = self.used
        if self.used_lindorm_search is not None:
            result['UsedLindormSearch'] = self.used_lindorm_search
        if self.used_lindorm_spark is not None:
            result['UsedLindormSpark'] = self.used_lindorm_spark
        if self.used_lindorm_table is not None:
            result['UsedLindormTable'] = self.used_lindorm_table
        if self.used_lindorm_tsdb is not None:
            result['UsedLindormTsdb'] = self.used_lindorm_tsdb
        if self.used_other is not None:
            result['UsedOther'] = self.used_other
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        if m.get('UsedLindormSearch') is not None:
            self.used_lindorm_search = m.get('UsedLindormSearch')
        if m.get('UsedLindormSpark') is not None:
            self.used_lindorm_spark = m.get('UsedLindormSpark')
        if m.get('UsedLindormTable') is not None:
            self.used_lindorm_table = m.get('UsedLindormTable')
        if m.get('UsedLindormTsdb') is not None:
            self.used_lindorm_tsdb = m.get('UsedLindormTsdb')
        if m.get('UsedOther') is not None:
            self.used_other = m.get('UsedOther')
        return self


class GetLindormFsUsedDetailResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        fs_capacity: str = None,
        fs_capacity_cold: str = None,
        fs_capacity_hot: str = None,
        fs_used_cold: str = None,
        fs_used_cold_on_lindorm_search: str = None,
        fs_used_cold_on_lindorm_tsdb: str = None,
        fs_used_cold_on_lindorm_table: str = None,
        fs_used_hot: str = None,
        fs_used_hot_on_lindorm_search: str = None,
        fs_used_hot_on_lindorm_tsdb: str = None,
        fs_used_hot_on_lindorm_table: str = None,
        fs_used_on_lindorm_search: str = None,
        fs_used_on_lindorm_tsdb: str = None,
        fs_used_on_lindorm_table: str = None,
        fs_used_on_lindorm_table_data: str = None,
        fs_used_on_lindorm_table_wal: str = None,
        lstorage_usage_list: List[GetLindormFsUsedDetailResponseBodyLStorageUsageList] = None,
        request_id: str = None,
        valid: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.fs_capacity = fs_capacity
        self.fs_capacity_cold = fs_capacity_cold
        self.fs_capacity_hot = fs_capacity_hot
        self.fs_used_cold = fs_used_cold
        self.fs_used_cold_on_lindorm_search = fs_used_cold_on_lindorm_search
        self.fs_used_cold_on_lindorm_tsdb = fs_used_cold_on_lindorm_tsdb
        self.fs_used_cold_on_lindorm_table = fs_used_cold_on_lindorm_table
        self.fs_used_hot = fs_used_hot
        self.fs_used_hot_on_lindorm_search = fs_used_hot_on_lindorm_search
        self.fs_used_hot_on_lindorm_tsdb = fs_used_hot_on_lindorm_tsdb
        self.fs_used_hot_on_lindorm_table = fs_used_hot_on_lindorm_table
        self.fs_used_on_lindorm_search = fs_used_on_lindorm_search
        self.fs_used_on_lindorm_tsdb = fs_used_on_lindorm_tsdb
        self.fs_used_on_lindorm_table = fs_used_on_lindorm_table
        self.fs_used_on_lindorm_table_data = fs_used_on_lindorm_table_data
        self.fs_used_on_lindorm_table_wal = fs_used_on_lindorm_table_wal
        self.lstorage_usage_list = lstorage_usage_list
        self.request_id = request_id
        self.valid = valid

    def validate(self):
        if self.lstorage_usage_list:
            for k in self.lstorage_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.fs_capacity is not None:
            result['FsCapacity'] = self.fs_capacity
        if self.fs_capacity_cold is not None:
            result['FsCapacityCold'] = self.fs_capacity_cold
        if self.fs_capacity_hot is not None:
            result['FsCapacityHot'] = self.fs_capacity_hot
        if self.fs_used_cold is not None:
            result['FsUsedCold'] = self.fs_used_cold
        if self.fs_used_cold_on_lindorm_search is not None:
            result['FsUsedColdOnLindormSearch'] = self.fs_used_cold_on_lindorm_search
        if self.fs_used_cold_on_lindorm_tsdb is not None:
            result['FsUsedColdOnLindormTSDB'] = self.fs_used_cold_on_lindorm_tsdb
        if self.fs_used_cold_on_lindorm_table is not None:
            result['FsUsedColdOnLindormTable'] = self.fs_used_cold_on_lindorm_table
        if self.fs_used_hot is not None:
            result['FsUsedHot'] = self.fs_used_hot
        if self.fs_used_hot_on_lindorm_search is not None:
            result['FsUsedHotOnLindormSearch'] = self.fs_used_hot_on_lindorm_search
        if self.fs_used_hot_on_lindorm_tsdb is not None:
            result['FsUsedHotOnLindormTSDB'] = self.fs_used_hot_on_lindorm_tsdb
        if self.fs_used_hot_on_lindorm_table is not None:
            result['FsUsedHotOnLindormTable'] = self.fs_used_hot_on_lindorm_table
        if self.fs_used_on_lindorm_search is not None:
            result['FsUsedOnLindormSearch'] = self.fs_used_on_lindorm_search
        if self.fs_used_on_lindorm_tsdb is not None:
            result['FsUsedOnLindormTSDB'] = self.fs_used_on_lindorm_tsdb
        if self.fs_used_on_lindorm_table is not None:
            result['FsUsedOnLindormTable'] = self.fs_used_on_lindorm_table
        if self.fs_used_on_lindorm_table_data is not None:
            result['FsUsedOnLindormTableData'] = self.fs_used_on_lindorm_table_data
        if self.fs_used_on_lindorm_table_wal is not None:
            result['FsUsedOnLindormTableWAL'] = self.fs_used_on_lindorm_table_wal
        result['LStorageUsageList'] = []
        if self.lstorage_usage_list is not None:
            for k in self.lstorage_usage_list:
                result['LStorageUsageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('FsCapacity') is not None:
            self.fs_capacity = m.get('FsCapacity')
        if m.get('FsCapacityCold') is not None:
            self.fs_capacity_cold = m.get('FsCapacityCold')
        if m.get('FsCapacityHot') is not None:
            self.fs_capacity_hot = m.get('FsCapacityHot')
        if m.get('FsUsedCold') is not None:
            self.fs_used_cold = m.get('FsUsedCold')
        if m.get('FsUsedColdOnLindormSearch') is not None:
            self.fs_used_cold_on_lindorm_search = m.get('FsUsedColdOnLindormSearch')
        if m.get('FsUsedColdOnLindormTSDB') is not None:
            self.fs_used_cold_on_lindorm_tsdb = m.get('FsUsedColdOnLindormTSDB')
        if m.get('FsUsedColdOnLindormTable') is not None:
            self.fs_used_cold_on_lindorm_table = m.get('FsUsedColdOnLindormTable')
        if m.get('FsUsedHot') is not None:
            self.fs_used_hot = m.get('FsUsedHot')
        if m.get('FsUsedHotOnLindormSearch') is not None:
            self.fs_used_hot_on_lindorm_search = m.get('FsUsedHotOnLindormSearch')
        if m.get('FsUsedHotOnLindormTSDB') is not None:
            self.fs_used_hot_on_lindorm_tsdb = m.get('FsUsedHotOnLindormTSDB')
        if m.get('FsUsedHotOnLindormTable') is not None:
            self.fs_used_hot_on_lindorm_table = m.get('FsUsedHotOnLindormTable')
        if m.get('FsUsedOnLindormSearch') is not None:
            self.fs_used_on_lindorm_search = m.get('FsUsedOnLindormSearch')
        if m.get('FsUsedOnLindormTSDB') is not None:
            self.fs_used_on_lindorm_tsdb = m.get('FsUsedOnLindormTSDB')
        if m.get('FsUsedOnLindormTable') is not None:
            self.fs_used_on_lindorm_table = m.get('FsUsedOnLindormTable')
        if m.get('FsUsedOnLindormTableData') is not None:
            self.fs_used_on_lindorm_table_data = m.get('FsUsedOnLindormTableData')
        if m.get('FsUsedOnLindormTableWAL') is not None:
            self.fs_used_on_lindorm_table_wal = m.get('FsUsedOnLindormTableWAL')
        self.lstorage_usage_list = []
        if m.get('LStorageUsageList') is not None:
            for k in m.get('LStorageUsageList'):
                temp_model = GetLindormFsUsedDetailResponseBodyLStorageUsageList()
                self.lstorage_usage_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetLindormFsUsedDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormFsUsedDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormFsUsedDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The disk type of the log nodes. This parameter is returned only for multi-zone instances. Valid values:
        # 
        # *   **cloud_efficiency**: The nodes use the Standard type of storage.
        # *   **cloud_ssd**: The nodes use the Performance type of storage.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormInstanceResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        core_count: str = None,
        cpu_count: str = None,
        engine: str = None,
        is_last_version: bool = None,
        latest_version: str = None,
        memory_size: str = None,
        specification: str = None,
        version: str = None,
    ):
        # The number of engine nodes.
        self.core_count = core_count
        # The number of CPU cores on the engine node.
        self.cpu_count = cpu_count
        # The engine type. Valid values:
        # 
        # *   **lindorm**: LindormTable.
        # *   **tsdb**: LindormTSDB.
        # *   **solr**: LindormSearch.
        # *   **store**: LindormDFS.
        # *   **bds**: Lindorm Tunnel Service (LTS).
        # *   **compute**: Lindorm Distributed Processing System (LDPS).
        self.engine = engine
        # Indicates whether the version of the engine is the latest. Valid values:
        # 
        # *   **true**: The version of the engine is the latest.
        # *   **false**: The version of the engine is not the latest.
        self.is_last_version = is_last_version
        # The latest version number of the engine.
        self.latest_version = latest_version
        # The memory size of the engine nodes.
        self.memory_size = memory_size
        self.specification = specification
        # The version of the engine.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_count is not None:
            result['CoreCount'] = self.core_count
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        archive_storage: int = None,
        auto_renew: bool = None,
        cold_storage: int = None,
        core_disk_category: str = None,
        core_num: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        create_milliseconds: int = None,
        create_time: str = None,
        deletion_protection: str = None,
        disk_category: str = None,
        disk_threshold: str = None,
        disk_usage: str = None,
        enable_blob: bool = None,
        enable_cdc: bool = None,
        enable_compute: bool = None,
        enable_kms: bool = None,
        enable_lproxy: bool = None,
        enable_lts: bool = None,
        enable_lsql_version_v3: bool = None,
        enable_mlctrl: bool = None,
        enable_ssl: bool = None,
        enable_shs: bool = None,
        enable_store_tde: bool = None,
        enable_stream: bool = None,
        engine_list: List[GetLindormInstanceResponseBodyEngineList] = None,
        engine_type: int = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        multi_zone_combination: str = None,
        network_type: str = None,
        pay_type: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # 16-digit AliUid of the Alibaba Cloud primary account (main account).
        self.ali_uid = ali_uid
        # Multi-AZ instance, coordinating Availability Zone virtual switch ID, which must be located in the Availability Zone corresponding to ArbiterZoneId.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # Multi-zone instance, coordinating Availability Zone ID.
        self.arbiter_zone_id = arbiter_zone_id
        # The architecture of the instance. Valid values:
        # 
        # *   **1.0**: The instance is deployed in a single zone.
        # *   **2.0**: The instance is deployed across multiple zones.
        self.arch_version = arch_version
        # The Archive storage size of the instance.
        self.archive_storage = archive_storage
        # Indicates whether auto-renewal is enabled, with the following returns:
        # - **true**: Enabled. - **false**: Disabled.
        # > This parameter is returned when the instance\\"s payment type is prepaid.
        self.auto_renew = auto_renew
        # The Capacity storage size of the instance.
        self.cold_storage = cold_storage
        # The disk type of the core nodes. This parameter is returned only for multi-zone instances. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **cloud_essd**: This instance uses ESSDs for storage.
        # *   **cloud_essd_pl0**: This instance uses PL0 ESSDs for storage.
        self.core_disk_category = core_disk_category
        # Multi-zone instance, number of core nodes.
        self.core_num = core_num
        # Multi-zone instance, core single-node disk capacity.
        self.core_single_storage = core_single_storage
        # Multi-zone instance, core node specification.
        self.core_spec = core_spec
        # The timestamp in milliseconds between the instance creation time and 1970-01-01 00:00:00.
        self.create_milliseconds = create_milliseconds
        # The storage capacity of the disk of a single log node. This parameter is returned only for multi-zone instances.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled, returning:
        # - **true**: Enabled. - **false**: Disabled.
        self.deletion_protection = deletion_protection
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **cloud_essd**: This instance uses ESSDs for storage.
        # *   **cloud_essd_pl0**: This instance uses PL0 ESSDs for storage.
        # *   **capacity_cloud_storage**: This instance uses the Capacity type of storage.
        # *   **local_ssd_pro**: This instance uses local SSDs for storage.
        # *   **local_hdd_pro**: This instance uses local HDDs for storage.
        self.disk_category = disk_category
        # The threshold for disk space.
        self.disk_threshold = disk_threshold
        # Disk space usage rate.
        self.disk_usage = disk_usage
        # Indicates whether LBlob is enabled for the instance. Valid values:
        # 
        # true: LBlob is enabled for the instance. false: LBlob is not enabled for the instance.
        self.enable_blob = enable_blob
        # Indicates whether the data subscription feature for the instance is enabled. Returns:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_cdc = enable_cdc
        # Indicates whether the instance\\"s compute engine is enabled, returning:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_compute = enable_compute
        # Indicates whether the Key Management Service (KMS) is enabled, returning:
        # - **true**: Enabled. - **false**: Disabled.
        self.enable_kms = enable_kms
        # Indicates whether the wide-table engine supports Thrift and CQL protocols. If not supported, the SwitchLProxyService interface can be used to enable or disable.
        # True indicates support
        # False indicates no support
        self.enable_lproxy = enable_lproxy
        # Indicates whether the LTS engine is activated for the instance. Valid values:
        # 
        # *   **true**: The LTS engine is activated for the instance.
        # *   **false**: The LTS engine is not activated for the instance.
        self.enable_lts = enable_lts
        # Indicates whether LindormTable of the instance supports LindormSQL V3 that is compatible with MySQL. By default, LindormTable of instances that are purchased after October 24, 2023 supports LindormSQL V3. If your instance is purchased before this date and want to enable LindormSQL V3, contact the technical support.
        # 
        # *   True: LindormTable supports LindormSQL V3.
        # *   False: LindormTable does not support LindormSQL V3.
        self.enable_lsql_version_v3 = enable_lsql_version_v3
        # Indicates whether AI control nodes are enabled for the instance.
        # 
        # *   True: AI control nodes are enabled for the instance.
        # *   False: AI control nodes are not enabled for the instance.
        self.enable_mlctrl = enable_mlctrl
        # Indicates whether SSL link encryption is enabled, returning:
        # - **true**: Enabled. - **false**: Disabled.
        self.enable_ssl = enable_ssl
        # Whether to enable the Compute Engine History Server.
        self.enable_shs = enable_shs
        # Indicates whether the Transparent Data Encryption (TDE) is enabled, returning:
        # - **true**: Enabled. - **false**: Disabled.
        self.enable_store_tde = enable_store_tde
        # Indicates whether the instance has the stream engine enabled. Return values:
        # - **true**: Stream engine is enabled. - **false**: Stream engine is not enabled.
        self.enable_stream = enable_stream
        # The latest version number of the engine.
        self.engine_list = engine_list
        # Supported engine types, the return value is obtained by performing addition operations on the values of the following engine types.
        # - 1: Search Engine - 2: Time Series Engine - 4: Wide Table Engine - 8: File Engine
        # > For example: If EngineType is 15, where 15 = 8 + 4 + 2 + 1, it indicates that the instance supports Search Engine, Time Series Engine, Wide Table Engine, and File Engine. If EngineType is 6, where 6 = 4 + 2, it signifies that the instance supports Time Series Engine and Wide Table Engine.
        self.engine_type = engine_type
        # Expiration time of the instance, format: **yyyy-MM-dd HH:mm:ss**.
        # > This parameter is only returned when the payment type is pre-paid.
        self.expire_time = expire_time
        # The millisecond value between the instance expiration time and 1970-01-01 00:00:00.
        self.expired_milliseconds = expired_milliseconds
        # Instance name.
        self.instance_alias = instance_alias
        # Instance ID.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **COLD_EXPANDING**: The Capacity storage of the instance is being scaled up.
        # *   **MINOR_VERSION_TRANSING**: The minor version of the instance is being updated.
        # *   **RESIZING**: The nodes in the instance are being scaled up.
        # *   **SHRINKING**: The nodes in the instance are being scaled down.
        # *   **CLASS_CHANGING**: The specification of the instance is being changed.
        # *   **SSL_SWITCHING: SSL**: The SSL configurations of the instance are being changed.
        # *   **CDC_OPENING**: Data subscription is being enabled for the instance.
        # *   **TRANSFER**: The data of the instance is being transferred.
        # *   **DATABASE_TRANSFER**: The data of the instance is being transferred to databases.
        # *   **GUARD_CREATING**: A disaster recovery instance is being created.
        # *   **BACKUP_RECOVERING**: The data of the instance is being restored from a backup.
        # *   **DATABASE_IMPORTING**: Data is being imported to the instance.
        # *   **NET_MODIFYING**: The network configurations of the instance are being changed.
        # *   **NET_SWITCHING**: The network of the instance is being switched between a virtual private cloud (VPC) and the Internet.
        # *   **NET_CREATING**: The connection to the instance is being created.
        # *   **NET_DELETING**: The connection to the instance is being deleted.
        # *   **DELETING**: The instance is being deleted.
        # *   **RESTARTING**: The instance is restarting.
        # *   **LOCKED**: The instance is locked because it expires.
        self.instance_status = instance_status
        # Instance\\"s storage capacity.
        self.instance_storage = instance_storage
        # Multi-zone instance, log node disk type, returns:
        # - **cloud_efficiency**：Standard cloud storage. - **cloud_ssd**：Performance cloud storage.
        self.log_disk_category = log_disk_category
        # Multi-zone instance, number of log nodes.
        self.log_num = log_num
        # The storage capacity of the disk of a single log node. This parameter is returned only for multi-zone instances.
        self.log_single_storage = log_single_storage
        # Multi-zone instance, log node specification.
        self.log_spec = log_spec
        # Maintainable end time.
        self.maintain_end_time = maintain_end_time
        # Maintainable start time.
        self.maintain_start_time = maintain_start_time
        # Multi-zone combinations. For support details on zone combinations, please refer to the product page.
        # - **ap-southeast-5abc-aliyun**: Indonesia (Jakarta) A+B+C. - **cn-hangzhou-ehi-aliyun**: East China 1 (Hangzhou) E+H+I. - **cn-beijing-acd-aliyun**: North China 2 (Beijing) A+C+D. - **ap-southeast-1-abc-aliyun**: Singapore A+B+C. - **cn-zhangjiakou-abc-aliyun**: North China 3 (Zhangjiakou) A+B+C. - **cn-shanghai-efg-aliyun**: East China 2 (Shanghai) E+F+G. - **cn-shanghai-abd-aliyun**: East China 2 (Shanghai) A+B+D. - **cn-hangzhou-bef-aliyun**: East China 1 (Hangzhou) B+E+F. - **cn-hangzhou-bce-aliyun**: East China 1 (Hangzhou) B+C+E. - **cn-beijing-fgh-aliyun**: North China 2 (Beijing) F+G+H. - **cn-shenzhen-abc-aliyun**: South China 1 (Shenzhen) A+B+C.
        self.multi_zone_combination = multi_zone_combination
        # Instance\\"s network type.
        self.network_type = network_type
        # 400
        self.pay_type = pay_type
        # Multi-zone instance, the virtual switch ID of the primary availability zone, which must be in the availability zone corresponding to PrimaryZoneId.
        self.primary_vswitch_id = primary_vswitch_id
        # Multi-zone instance, availability zone ID of the primary zone.
        self.primary_zone_id = primary_zone_id
        # Region ID.
        self.region_id = region_id
        # Request ID.
        self.request_id = request_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Instance type, valid values:
        # - **lindorm**：represents a Lindorm single-zone instance. - **lindorm_multizone**：represents a Lindorm multi-zone instance. - **serverless_lindorm**：represents a Lindorm Serverless instance. - **lindorm_standalone**：represents a Lindorm standalone instance. - **lts**：represents the Lindorm Data Channel Service type.
        self.service_type = service_type
        # Multi-zone instance, the virtual switch ID of the backup availability zone, which must be in the availability zone corresponding to StandbyZoneId.
        self.standby_vswitch_id = standby_vswitch_id
        # Multi-zone instance, backup availability zone\\"s availability zone ID.
        self.standby_zone_id = standby_zone_id
        # The type of the log nodes. This parameter is returned only for multi-zone instances.
        self.vpc_id = vpc_id
        # The number of the log nodes. This parameter is returned only for multi-zone instances.
        self.vswitch_id = vswitch_id
        # Availability Zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.archive_storage is not None:
            result['ArchiveStorage'] = self.archive_storage
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_disk_category is not None:
            result['CoreDiskCategory'] = self.core_disk_category
        if self.core_num is not None:
            result['CoreNum'] = self.core_num
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec
        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_threshold is not None:
            result['DiskThreshold'] = self.disk_threshold
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.enable_blob is not None:
            result['EnableBlob'] = self.enable_blob
        if self.enable_cdc is not None:
            result['EnableCdc'] = self.enable_cdc
        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute
        if self.enable_kms is not None:
            result['EnableKms'] = self.enable_kms
        if self.enable_lproxy is not None:
            result['EnableLProxy'] = self.enable_lproxy
        if self.enable_lts is not None:
            result['EnableLTS'] = self.enable_lts
        if self.enable_lsql_version_v3 is not None:
            result['EnableLsqlVersionV3'] = self.enable_lsql_version_v3
        if self.enable_mlctrl is not None:
            result['EnableMLCtrl'] = self.enable_mlctrl
        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl
        if self.enable_shs is not None:
            result['EnableShs'] = self.enable_shs
        if self.enable_store_tde is not None:
            result['EnableStoreTDE'] = self.enable_store_tde
        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('ArchiveStorage') is not None:
            self.archive_storage = m.get('ArchiveStorage')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreDiskCategory') is not None:
            self.core_disk_category = m.get('CoreDiskCategory')
        if m.get('CoreNum') is not None:
            self.core_num = m.get('CoreNum')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')
        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskThreshold') is not None:
            self.disk_threshold = m.get('DiskThreshold')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('EnableBlob') is not None:
            self.enable_blob = m.get('EnableBlob')
        if m.get('EnableCdc') is not None:
            self.enable_cdc = m.get('EnableCdc')
        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')
        if m.get('EnableKms') is not None:
            self.enable_kms = m.get('EnableKms')
        if m.get('EnableLProxy') is not None:
            self.enable_lproxy = m.get('EnableLProxy')
        if m.get('EnableLTS') is not None:
            self.enable_lts = m.get('EnableLTS')
        if m.get('EnableLsqlVersionV3') is not None:
            self.enable_lsql_version_v3 = m.get('EnableLsqlVersionV3')
        if m.get('EnableMLCtrl') is not None:
            self.enable_mlctrl = m.get('EnableMLCtrl')
        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')
        if m.get('EnableShs') is not None:
            self.enable_shs = m.get('EnableShs')
        if m.get('EnableStoreTDE') is not None:
            self.enable_store_tde = m.get('EnableStoreTDE')
        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceEngineListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Instance ID, which can be obtained by calling the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) interface.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormInstanceEngineListResponseBodyEngineListNetInfoList(TeaModel):
    def __init__(
        self,
        access_type: int = None,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
    ):
        # The method by which the connection information can be used to access LindormTable. Valid values:
        # 
        # *   **0**: The default value. This value can be ignored.
        # *   **1**: The connection information can be used to access LindormTable by using ApsaraDB for HBase API for Java.
        # *   **2**: The connection information can be used to access LindormTable by using ApsaraDB for HBase API for a non-Java language.
        # *   **3**: The connection information can be used to access LindormTable by using the LindormTable endpoint for CQL.
        # *   **4**: The connection information can be used to access LindormTable by using the LindormTable endpoint for SQL.
        # *   **5**: The connection information can be used to access Lindorm by using the LindormTable endpoint for Amazon S3.
        # *   **6**: The connection information can be used to access Lindorm by using the LindormTable endpoint for MySQL.
        self.access_type = access_type
        # The endpoint that is used to connect to the engine.
        self.connection_string = connection_string
        # The network type of the endpoint. Valid values:
        # 
        # *   **0**: Internet
        # *   **2**: virtual private cloud (VPC)
        self.net_type = net_type
        # The port number used to connect to the engine.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class GetLindormInstanceEngineListResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        net_info_list: List[GetLindormInstanceEngineListResponseBodyEngineListNetInfoList] = None,
    ):
        # The type of engine that can run on the instance. Valid values:
        # 
        # *   **lindorm**: LindormTable.
        # *   **tsdb**: LindormTSDB.
        # *   **solr**: LindormSearch.
        # *   **store**: LindormDFS.
        self.engine_type = engine_type
        # The list of connection information about the engine.
        self.net_info_list = net_info_list

    def validate(self):
        if self.net_info_list:
            for k in self.net_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        result['NetInfoList'] = []
        if self.net_info_list is not None:
            for k in self.net_info_list:
                result['NetInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        self.net_info_list = []
        if m.get('NetInfoList') is not None:
            for k in m.get('NetInfoList'):
                temp_model = GetLindormInstanceEngineListResponseBodyEngineListNetInfoList()
                self.net_info_list.append(temp_model.from_map(k))
        return self


class GetLindormInstanceEngineListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        engine_list: List[GetLindormInstanceEngineListResponseBodyEngineList] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The list of engines that can run on the specified instance.
        self.engine_list = engine_list
        # Instance ID.
        self.instance_id = instance_id
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceEngineListResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLindormInstanceEngineListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceEngineListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormInstanceEngineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceListRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the instances you want to query. You can specify 1 to 20 tag keys.
        # 
        # > You can specify the keys of multiple tags. For example, you can specify the key of the first tag in the first key-value pair contained in the value of this parameter and specify the key of the second tag in the second key-value pair.
        self.key = key
        # The value of tag N of the instances you want to query. You can specify 1 to 20 tag values.
        # 
        # > You can specify the values of multiple tags. For example, you can specify the value of the first tag in the first key-value pair contained in the value of this parameter and specify the value of the second tag in the second key-value pair.
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


class GetLindormInstanceListRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_str: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        service_type: str = None,
        support_engine: int = None,
        tag: List[GetLindormInstanceListRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the pages to return,
        self.page_number = page_number
        # The number of instances to return on each page.
        self.page_size = page_size
        # The keyword contained in the names of Lindorm instances you want to query. Fuzzy queries based on the keyword is supported.
        self.query_str = query_str
        # The ID of the region in which the instances that you want to query is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The series of instances that you want to query. Valid values:
        # 
        # *   **lindorm**: The instance is a single-zone Lindorm instance.
        # *   **lindorm_multizone**: The instance is a multi-zone Lindorm instance.
        # *   **serverless_lindorm**: The instance is a Lindorm Serverless instance.
        # *   **lindorm_standalone**: The instance is a single-node Lindorm instance.
        # *   **lts**: The instance is an LTS instance.
        self.service_type = service_type
        # The engine supported by the instances that you want to query. The engines are indicated by different numbers:
        # 
        # *   **1**: LindormSearch.
        # *   **2**: LindormTSDB.
        # *   **4**: LindormTable.
        # *   **8**: LindormDFS.
        # 
        # > The value of this parameter is the sum of all numbers that indicate the engines supported by the instance. For example, if you set the value of this parameter to 15, which is the sum of 1, 2, 4, and 8, this operation queries instances that support all four engines. If you set the value of this parameter to 6, which is the sum of 2 and 4, this operation queries instances that support LindormTSDB and LindormTable.
        self.support_engine = support_engine
        # The list of tags associated with the specified instances.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.support_engine is not None:
            result['SupportEngine'] = self.support_engine
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupportEngine') is not None:
            self.support_engine = m.get('SupportEngine')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetLindormInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetLindormInstanceListResponseBodyInstanceListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class GetLindormInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_milliseconds: int = None,
        create_time: str = None,
        enable_column: bool = None,
        enable_compute: bool = None,
        enable_lts: bool = None,
        enable_message: bool = None,
        enable_row: bool = None,
        enable_stream: bool = None,
        enable_vector: bool = None,
        engine_type: str = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        tags: List[GetLindormInstanceListResponseBodyInstanceListTags] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The 16-digit AliUid of the Alibaba Cloud account that owns the instance.
        self.ali_uid = ali_uid
        # The time when the instance is created. This value is a UNIX timestamp that indicates the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_milliseconds = create_milliseconds
        # The time when the instance is created.
        self.create_time = create_time
        # Indicates whether the column storage engine is enabled, returning:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_column = enable_column
        # Indicates whether LDPS is activated for the instance. Valid values:
        # 
        # *   **true**: LDPS is activated for the instance.
        # *   **false**: LDPS is not activated for the instance.
        self.enable_compute = enable_compute
        # Indicates whether the LTS engine is enabled, returning:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_lts = enable_lts
        # Indicates whether the message engine is enabled, returning:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_message = enable_message
        self.enable_row = enable_row
        # Indicates whether the Lindorm streaming engine is activated for the instance. Valid values:
        # 
        # *   **true**: The Lindorm streaming engine is activated for the instance.
        # *   **false**: The Lindorm streaming engine is not activated for the instance.
        self.enable_stream = enable_stream
        # Whether the vector engine is enabled, returns:
        # - **true**: Enabled. - **false**: Not enabled.
        self.enable_vector = enable_vector
        # The engine supported by the instance. The engines are indicated by different numbers:
        # 
        # *   **1**: LindormSearch.
        # *   **2**: LindormTSDB.
        # *   **4**: LindormTable.
        # *   **8**: LindormDFS.
        # 
        # > The value of this parameter is the sum of all numbers that indicate the engines supported by the instance. For example, if the value of this parameter is 15, which is the sum of 1, 2, 4, and 8, the instance supports all four engines. If the value of this parameter is 6, which is the sum of 2 and 4, the instance supports LindormTSDB and LindormTable.
        self.engine_type = engine_type
        # The time when the instance expires.
        # 
        # > This parameter is returned only if the billing method of the instance is subscription.
        self.expire_time = expire_time
        # The time when the instance expires. This value is a UNIX timestamp that indicates the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.expired_milliseconds = expired_milliseconds
        # The name of the VPC.
        self.instance_alias = instance_alias
        # The ID of the instance
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **COLD_EXPANDING**: The Capacity storage of the instance is being scaled up.
        # *   **MINOR_VERSION_TRANSING**: The minor version of the instance is being updated.
        # *   **RESIZING**: The nodes in the instance are being scaled up.
        # *   **SHRINKING**: The nodes in the instance are being scaled down.
        # *   **CLASS_CHANGING**: The specification of the instance is being changed.
        # *   **SSL_SWITCHING: SSL**: The SSL configurations of the instance are being changed.
        # *   **CDC_OPENING**: Data subscription is being enabled for the instance.
        # *   **TRANSFER**: The data of the instance is being transferred.
        # *   **DATABASE_TRANSFER**: The data of the instance is being transferred to databases.
        # *   **GUARD_CREATING**: A disaster recovery instance is being created.
        # *   **BACKUP_RECOVERING**: The data of the instance is being restored from a backup.
        # *   **DATABASE_IMPORTING**: Data is being imported to the instance.
        # *   **NET_MODIFYING**: The network configurations of the instance are being changed.
        # *   **NET_SWITCHING**: The network of the instance is being switched between a virtual private cloud (VPC) and the Internet.
        # *   **NET_CREATING**: The connection to the instance is being created.
        # *   **NET_DELETING**: The connection to the instance is being deleted.
        # *   **DELETING**: The instance is being deleted.
        # *   **RESTARTING**: The instance is restarting.
        # *   **LOCKED**: The instance is locked because it expires.
        self.instance_status = instance_status
        # The storage capacity of the instance.
        self.instance_storage = instance_storage
        # The network type of the instance.
        self.network_type = network_type
        # The billing method of the instance. Valid values:
        # 
        # *   **PREPAY**: subscription.
        # *   **POSTPAY**: pay-as-you-go.
        self.pay_type = pay_type
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The series of the instance. Valid values:
        # 
        # *   **lindorm**: The instance is a Lindorm instance.
        # *   **serverless_lindorm**: The instance is a Lindorm Serverless instance.
        # *   **lindorm_standalone**: The instance is a single-node Lindorm instance.
        # *   **lts**: The instance is an LTS instance.
        self.service_type = service_type
        # The list of tags associated with the specified instances.
        self.tags = tags
        # The ID of the VPC in which the instance is deployed.
        self.vpc_id = vpc_id
        # The ID of the zone in which the instance is created.
        self.zone_id = zone_id

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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_column is not None:
            result['EnableColumn'] = self.enable_column
        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute
        if self.enable_lts is not None:
            result['EnableLts'] = self.enable_lts
        if self.enable_message is not None:
            result['EnableMessage'] = self.enable_message
        if self.enable_row is not None:
            result['EnableRow'] = self.enable_row
        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream
        if self.enable_vector is not None:
            result['EnableVector'] = self.enable_vector
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableColumn') is not None:
            self.enable_column = m.get('EnableColumn')
        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')
        if m.get('EnableLts') is not None:
            self.enable_lts = m.get('EnableLts')
        if m.get('EnableMessage') is not None:
            self.enable_message = m.get('EnableMessage')
        if m.get('EnableRow') is not None:
            self.enable_row = m.get('EnableRow')
        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')
        if m.get('EnableVector') is not None:
            self.enable_vector = m.get('EnableVector')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetLindormInstanceListResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLindormInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: List[GetLindormInstanceListResponseBodyInstanceList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of instance.
        self.instance_list = instance_list
        # The number of returned pages.
        self.page_number = page_number
        # The number of instances that are returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned instances.
        self.total = total

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetLindormInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLindormInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormV2InstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormV2InstanceResponseBodyEngineListConnectAddressList(TeaModel):
    def __init__(
        self,
        address: str = None,
        port: str = None,
        type: str = None,
    ):
        self.address = address
        self.port = port
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLindormV2InstanceResponseBodyEngineListNodeGroup(TeaModel):
    def __init__(
        self,
        category: str = None,
        cpu_core_count: int = None,
        enable_attach_local_disk: bool = None,
        local_disk_capacity: int = None,
        local_disk_category: str = None,
        memory_size_gi_b: int = None,
        node_spec: str = None,
        quantity: int = None,
        resource_group_name: str = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.category = category
        self.cpu_core_count = cpu_core_count
        self.enable_attach_local_disk = enable_attach_local_disk
        self.local_disk_capacity = local_disk_capacity
        self.local_disk_category = local_disk_category
        self.memory_size_gi_b = memory_size_gi_b
        self.node_spec = node_spec
        self.quantity = quantity
        self.resource_group_name = resource_group_name
        self.spec_id = spec_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.enable_attach_local_disk is not None:
            result['EnableAttachLocalDisk'] = self.enable_attach_local_disk
        if self.local_disk_capacity is not None:
            result['LocalDiskCapacity'] = self.local_disk_capacity
        if self.local_disk_category is not None:
            result['LocalDiskCategory'] = self.local_disk_category
        if self.memory_size_gi_b is not None:
            result['MemorySizeGiB'] = self.memory_size_gi_b
        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('EnableAttachLocalDisk') is not None:
            self.enable_attach_local_disk = m.get('EnableAttachLocalDisk')
        if m.get('LocalDiskCapacity') is not None:
            self.local_disk_capacity = m.get('LocalDiskCapacity')
        if m.get('LocalDiskCategory') is not None:
            self.local_disk_category = m.get('LocalDiskCategory')
        if m.get('MemorySizeGiB') is not None:
            self.memory_size_gi_b = m.get('MemorySizeGiB')
        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLindormV2InstanceResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        connect_address_list: List[GetLindormV2InstanceResponseBodyEngineListConnectAddressList] = None,
        engine: str = None,
        is_last_version: bool = None,
        latest_version: str = None,
        node_group: List[GetLindormV2InstanceResponseBodyEngineListNodeGroup] = None,
        version: str = None,
    ):
        self.connect_address_list = connect_address_list
        self.engine = engine
        self.is_last_version = is_last_version
        self.latest_version = latest_version
        self.node_group = node_group
        self.version = version

    def validate(self):
        if self.connect_address_list:
            for k in self.connect_address_list:
                if k:
                    k.validate()
        if self.node_group:
            for k in self.node_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectAddressList'] = []
        if self.connect_address_list is not None:
            for k in self.connect_address_list:
                result['ConnectAddressList'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        result['NodeGroup'] = []
        if self.node_group is not None:
            for k in self.node_group:
                result['NodeGroup'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connect_address_list = []
        if m.get('ConnectAddressList') is not None:
            for k in m.get('ConnectAddressList'):
                temp_model = GetLindormV2InstanceResponseBodyEngineListConnectAddressList()
                self.connect_address_list.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        self.node_group = []
        if m.get('NodeGroup') is not None:
            for k in m.get('NodeGroup'):
                temp_model = GetLindormV2InstanceResponseBodyEngineListNodeGroup()
                self.node_group.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetLindormV2InstanceResponseBodyStorageUsage(TeaModel):
    def __init__(
        self,
        capacity_by_disk_category: List[Dict[str, Any]] = None,
        engine_usage: Dict[str, Any] = None,
    ):
        self.capacity_by_disk_category = capacity_by_disk_category
        self.engine_usage = engine_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_by_disk_category is not None:
            result['CapacityByDiskCategory'] = self.capacity_by_disk_category
        if self.engine_usage is not None:
            result['EngineUsage'] = self.engine_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityByDiskCategory') is not None:
            self.capacity_by_disk_category = m.get('CapacityByDiskCategory')
        if m.get('EngineUsage') is not None:
            self.engine_usage = m.get('EngineUsage')
        return self


class GetLindormV2InstanceResponseBodyWhiteIpList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ip_list: str = None,
    ):
        self.group_name = group_name
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class GetLindormV2InstanceResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        auto_renew: bool = None,
        cold_storage: int = None,
        create_milliseconds: int = None,
        deletion_protection: str = None,
        disk_category: str = None,
        disk_threshold: str = None,
        disk_usage: str = None,
        enable_compute: bool = None,
        engine_list: List[GetLindormV2InstanceResponseBodyEngineList] = None,
        expired_milliseconds: int = None,
        initial_root_password: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        storage_usage: GetLindormV2InstanceResponseBodyStorageUsage = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        white_ip_list: List[GetLindormV2InstanceResponseBodyWhiteIpList] = None,
        zone_engine_info_map: Dict[str, Any] = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.auto_renew = auto_renew
        self.cold_storage = cold_storage
        self.create_milliseconds = create_milliseconds
        self.deletion_protection = deletion_protection
        self.disk_category = disk_category
        self.disk_threshold = disk_threshold
        self.disk_usage = disk_usage
        self.enable_compute = enable_compute
        self.engine_list = engine_list
        self.expired_milliseconds = expired_milliseconds
        self.initial_root_password = initial_root_password
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.network_type = network_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.service_type = service_type
        self.storage_usage = storage_usage
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.white_ip_list = white_ip_list
        self.zone_engine_info_map = zone_engine_info_map
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()
        if self.storage_usage:
            self.storage_usage.validate()
        if self.white_ip_list:
            for k in self.white_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_threshold is not None:
            result['DiskThreshold'] = self.disk_threshold
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds
        if self.initial_root_password is not None:
            result['InitialRootPassword'] = self.initial_root_password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        result['WhiteIpList'] = []
        if self.white_ip_list is not None:
            for k in self.white_ip_list:
                result['WhiteIpList'].append(k.to_map() if k else None)
        if self.zone_engine_info_map is not None:
            result['ZoneEngineInfoMap'] = self.zone_engine_info_map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskThreshold') is not None:
            self.disk_threshold = m.get('DiskThreshold')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormV2InstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')
        if m.get('InitialRootPassword') is not None:
            self.initial_root_password = m.get('InitialRootPassword')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StorageUsage') is not None:
            temp_model = GetLindormV2InstanceResponseBodyStorageUsage()
            self.storage_usage = temp_model.from_map(m['StorageUsage'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        self.white_ip_list = []
        if m.get('WhiteIpList') is not None:
            for k in m.get('WhiteIpList'):
                temp_model = GetLindormV2InstanceResponseBodyWhiteIpList()
                self.white_ip_list.append(temp_model.from_map(k))
        if m.get('ZoneEngineInfoMap') is not None:
            self.zone_engine_info_map = m.get('ZoneEngineInfoMap')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLindormV2InstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormV2InstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormV2InstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormV2InstanceEngineListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormV2InstanceEngineListResponseBodyEngineListNetInfoList(TeaModel):
    def __init__(
        self,
        access_type: int = None,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
    ):
        self.access_type = access_type
        self.connection_string = connection_string
        self.net_type = net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class GetLindormV2InstanceEngineListResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        net_info_list: List[GetLindormV2InstanceEngineListResponseBodyEngineListNetInfoList] = None,
    ):
        self.engine_type = engine_type
        self.net_info_list = net_info_list

    def validate(self):
        if self.net_info_list:
            for k in self.net_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        result['NetInfoList'] = []
        if self.net_info_list is not None:
            for k in self.net_info_list:
                result['NetInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        self.net_info_list = []
        if m.get('NetInfoList') is not None:
            for k in m.get('NetInfoList'):
                temp_model = GetLindormV2InstanceEngineListResponseBodyEngineListNetInfoList()
                self.net_info_list.append(temp_model.from_map(k))
        return self


class GetLindormV2InstanceEngineListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        engine_list: List[GetLindormV2InstanceEngineListResponseBodyEngineList] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.engine_list = engine_list
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormV2InstanceEngineListResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLindormV2InstanceEngineListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormV2InstanceEngineListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormV2InstanceEngineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormV2StorageUsageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormV2StorageUsageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        capacity_by_disk_category: List[Dict[str, Any]] = None,
        instance_storage_zone_map: Dict[str, Any] = None,
        request_id: str = None,
        usage_by_disk_category: List[Dict[str, Any]] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.capacity_by_disk_category = capacity_by_disk_category
        self.instance_storage_zone_map = instance_storage_zone_map
        self.request_id = request_id
        self.usage_by_disk_category = usage_by_disk_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.capacity_by_disk_category is not None:
            result['CapacityByDiskCategory'] = self.capacity_by_disk_category
        if self.instance_storage_zone_map is not None:
            result['InstanceStorageZoneMap'] = self.instance_storage_zone_map
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_by_disk_category is not None:
            result['UsageByDiskCategory'] = self.usage_by_disk_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('CapacityByDiskCategory') is not None:
            self.capacity_by_disk_category = m.get('CapacityByDiskCategory')
        if m.get('InstanceStorageZoneMap') is not None:
            self.instance_storage_zone_map = m.get('InstanceStorageZoneMap')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageByDiskCategory') is not None:
            self.usage_by_disk_category = m.get('UsageByDiskCategory')
        return self


class GetLindormV2StorageUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormV2StorageUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetLindormV2StorageUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoScalingConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step
        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')
        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')
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


class ListAutoScalingConfigsResponseBodyDataScaleConfigs(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        scale_rule_list: List[ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList] = None,
        scale_type: str = None,
        spec_id: str = None,
    ):
        self.config_id = config_id
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        self.engine = engine
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.scale_rule_list = scale_rule_list
        self.scale_type = scale_type
        self.spec_id = spec_id

    def validate(self):
        if self.scale_rule_list:
            for k in self.scale_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end
        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max
        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min
        result['ScaleRuleList'] = []
        if self.scale_rule_list is not None:
            for k in self.scale_rule_list:
                result['ScaleRuleList'].append(k.to_map() if k else None)
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')
        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')
        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')
        self.scale_rule_list = []
        if m.get('ScaleRuleList') is not None:
            for k in m.get('ScaleRuleList'):
                temp_model = ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList()
                self.scale_rule_list.append(temp_model.from_map(k))
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class ListAutoScalingConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        scale_configs: List[ListAutoScalingConfigsResponseBodyDataScaleConfigs] = None,
    ):
        self.scale_configs = scale_configs

    def validate(self):
        if self.scale_configs:
            for k in self.scale_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScaleConfigs'] = []
        if self.scale_configs is not None:
            for k in self.scale_configs:
                result['ScaleConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scale_configs = []
        if m.get('ScaleConfigs') is not None:
            for k in m.get('ScaleConfigs'):
                temp_model = ListAutoScalingConfigsResponseBodyDataScaleConfigs()
                self.scale_configs.append(temp_model.from_map(k))
        return self


class ListAutoScalingConfigsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListAutoScalingConfigsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAutoScalingConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutoScalingConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAutoScalingConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAutoScalingConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoScalingRecordsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListAutoScalingRecordsResponseBodyDataScaleRecords(TeaModel):
    def __init__(
        self,
        detail: str = None,
        end_time: str = None,
        id: str = None,
        instance_id: str = None,
        old_value: str = None,
        resource_type: str = None,
        spec_group_id: str = None,
        start_time: str = None,
        status: str = None,
        strategy: str = None,
        target_value: str = None,
    ):
        self.detail = detail
        self.end_time = end_time
        self.id = id
        self.instance_id = instance_id
        self.old_value = old_value
        self.resource_type = resource_type
        self.spec_group_id = spec_group_id
        self.start_time = start_time
        self.status = status
        self.strategy = strategy
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spec_group_id is not None:
            result['SpecGroupId'] = self.spec_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpecGroupId') is not None:
            self.spec_group_id = m.get('SpecGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class ListAutoScalingRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        scale_records: List[ListAutoScalingRecordsResponseBodyDataScaleRecords] = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.scale_records = scale_records
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.scale_records:
            for k in self.scale_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ScaleRecords'] = []
        if self.scale_records is not None:
            for k in self.scale_records:
                result['ScaleRecords'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.scale_records = []
        if m.get('ScaleRecords') is not None:
            for k in m.get('ScaleRecords'):
                temp_model = ListAutoScalingRecordsResponseBodyDataScaleRecords()
                self.scale_records.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListAutoScalingRecordsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListAutoScalingRecordsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAutoScalingRecordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutoScalingRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAutoScalingRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAutoScalingRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoScalingRulesRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListAutoScalingRulesResponseBodyDataScaleRules(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step
        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')
        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')
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


class ListAutoScalingRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        scale_rules: List[ListAutoScalingRulesResponseBodyDataScaleRules] = None,
    ):
        self.scale_rules = scale_rules

    def validate(self):
        if self.scale_rules:
            for k in self.scale_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScaleRules'] = []
        if self.scale_rules is not None:
            for k in self.scale_rules:
                result['ScaleRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scale_rules = []
        if m.get('ScaleRules') is not None:
            for k in m.get('ScaleRules'):
                temp_model = ListAutoScalingRulesResponseBodyDataScaleRules()
                self.scale_rules.append(temp_model.from_map(k))
        return self


class ListAutoScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListAutoScalingRulesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAutoScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutoScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAutoScalingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAutoScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLdpsComputeGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListLdpsComputeGroupsResponseBodyGroupList(TeaModel):
    def __init__(
        self,
        exception_info: str = None,
        group_name: str = None,
        is_default: bool = None,
        properties: Dict[str, Any] = None,
        state: str = None,
        web_ui: str = None,
    ):
        self.exception_info = exception_info
        self.group_name = group_name
        self.is_default = is_default
        self.properties = properties
        self.state = state
        self.web_ui = web_ui

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_info is not None:
            result['ExceptionInfo'] = self.exception_info
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.state is not None:
            result['State'] = self.state
        if self.web_ui is not None:
            result['WebUI'] = self.web_ui
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionInfo') is not None:
            self.exception_info = m.get('ExceptionInfo')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WebUI') is not None:
            self.web_ui = m.get('WebUI')
        return self


class ListLdpsComputeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        group_list: List[ListLdpsComputeGroupsResponseBodyGroupList] = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.group_list = group_list
        self.request_id = request_id

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = ListLdpsComputeGroupsResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLdpsComputeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLdpsComputeGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListLdpsComputeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The keys of the tags associated with the instances you want to query.
        # 
        # > You can specify the keys of multiple tags. For example, you can specify the key of the first tag in the first key-value pair contained in the value of this parameter and specify the key of the second tag in the second key-value pair.
        self.key = key
        # The values of the tags associated with the instances you want to query.
        # 
        # > You can specify the values of multiple tags. For example, you can specify the value of the first tag in the first key-value pair contained in the value of this parameter and specify the value of the second tag in the second key-value pair.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The token used to start the next query to retrieve more results.
        # 
        # > This parameter is not required in the first query. If not all results are returned in one query, you can pass in the **NextToken** value returned for the query to perform the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region in which the instances whose tags you want to query are located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to **INSTANCE**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        self.security_token = security_token
        # The list of tags associated with the instances you want to query.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource, which is the ID of the instance.
        self.resource_id = resource_id
        # The type of the resources. The returned value is fixed to **ALIYUN::HITSDB::INSTANCE**.
        self.resource_type = resource_type
        # The key of the tag associated with the instance.
        self.tag_key = tag_key
        # The value of the tag associated with the instance.
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The token used to start the next query.
        # 
        # > If not all results are returned in the first query, this parameter is returned. You can pass in the returned value of this parameter for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The list of resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoScalingConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_type: str = None,
        security_token: str = None,
        spec_id: str = None,
    ):
        # This parameter is required.
        self.config_id = config_id
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        self.engine = engine
        # This parameter is required.
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_type = scale_type
        self.security_token = security_token
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end
        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max
        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')
        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')
        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class ModifyAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAutoScalingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoScalingRuleRequest(TeaModel):
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
        rule_id: str = None,
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
        self.rule_id = rule_id
        self.rule_name = rule_name
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
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
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
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


class ModifyAutoScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAutoScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAutoScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyAutoScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstancePayTypeRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The subscription duration of the instance. The parameter is required if the instance is an subscription instance.
        # 
        # *   If PricingCycle is set to Month, set this parameter to an integer that ranges from 1 to 9.
        # *   If PricingCycle is set to Year, set this parameter to an integer that ranges from 1 to 3.
        self.duration = duration
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # *   **PREPAY**: subscription.
        # *   **POSTPAY**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration for the instance. Valid values:
        # 
        # *   Month
        # *   Year
        self.pricing_cycle = pricing_cycle
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstancePayTypeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstancePayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstancePayTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyInstancePayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLindormV2InstanceRequestNodeGroupList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        node_count: str = None,
        node_disk_size: int = None,
        node_disk_type: str = None,
        node_spec: str = None,
        resource_group_name: str = None,
    ):
        self.group_id = group_id
        self.node_count = node_count
        self.node_disk_size = node_disk_size
        self.node_disk_type = node_disk_type
        self.node_spec = node_spec
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size
        if self.node_disk_type is not None:
            result['NodeDiskType'] = self.node_disk_type
        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')
        if m.get('NodeDiskType') is not None:
            self.node_disk_type = m.get('NodeDiskType')
        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        return self


class ModifyLindormV2InstanceRequest(TeaModel):
    def __init__(
        self,
        cloud_storage_size: int = None,
        cloud_storage_type: str = None,
        engine_type: str = None,
        instance_id: str = None,
        node_group_list: List[ModifyLindormV2InstanceRequestNodeGroupList] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        upgrade_type: str = None,
    ):
        self.cloud_storage_size = cloud_storage_size
        self.cloud_storage_type = cloud_storage_type
        self.engine_type = engine_type
        # This parameter is required.
        self.instance_id = instance_id
        self.node_group_list = node_group_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is required.
        self.upgrade_type = upgrade_type

    def validate(self):
        if self.node_group_list:
            for k in self.node_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_size is not None:
            result['CloudStorageSize'] = self.cloud_storage_size
        if self.cloud_storage_type is not None:
            result['CloudStorageType'] = self.cloud_storage_type
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['NodeGroupList'] = []
        if self.node_group_list is not None:
            for k in self.node_group_list:
                result['NodeGroupList'].append(k.to_map() if k else None)
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudStorageSize') is not None:
            self.cloud_storage_size = m.get('CloudStorageSize')
        if m.get('CloudStorageType') is not None:
            self.cloud_storage_type = m.get('CloudStorageType')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.node_group_list = []
        if m.get('NodeGroupList') is not None:
            for k in m.get('NodeGroupList'):
                temp_model = ModifyLindormV2InstanceRequestNodeGroupList()
                self.node_group_list.append(temp_model.from_map(k))
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class ModifyLindormV2InstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLindormV2InstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLindormV2InstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyLindormV2InstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLindormV2WhiteIpListRequest(TeaModel):
    def __init__(
        self,
        delete_group: bool = None,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        white_ip_list: str = None,
    ):
        self.delete_group = delete_group
        # This parameter is required.
        self.group_name = group_name
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is required.
        self.white_ip_list = white_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_group is not None:
            result['DeleteGroup'] = self.delete_group
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.white_ip_list is not None:
            result['WhiteIpList'] = self.white_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteGroup') is not None:
            self.delete_group = m.get('DeleteGroup')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('WhiteIpList') is not None:
            self.white_ip_list = m.get('WhiteIpList')
        return self


class ModifyLindormV2WhiteIpListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLindormV2WhiteIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLindormV2WhiteIpListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyLindormV2WhiteIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenComputeEngineRequest(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        instance_id: str = None,
        memory_limit: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.cpu_limit = cpu_limit
        # This parameter is required.
        self.instance_id = instance_id
        self.memory_limit = memory_limit
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class OpenComputeEngineResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenComputeEngineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenComputeEngineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = OpenComputeEngineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenComputePreCheckRequest(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        instance_id: str = None,
        memory_limit: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.cpu_limit = cpu_limit
        # This parameter is required.
        self.instance_id = instance_id
        self.memory_limit = memory_limit
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class OpenComputePreCheckResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenComputePreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenComputePreCheckResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = OpenComputePreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        immediately: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to release the instance immediately. If you set this parameter to false, data in the released instance is retained for seven days before it is completely deleted. If you set this parameter to true, data in the released instance is immediately deleted. The default value is false.
        self.immediately = immediately
        # Instance ID, which can be obtained by calling the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) interface.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID.
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


class ReleaseLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReleaseLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseLindormV2InstanceRequest(TeaModel):
    def __init__(
        self,
        immediately: bool = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.immediately = immediately
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseLindormV2InstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseLindormV2InstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseLindormV2InstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReleaseLindormV2InstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The subscription duration of the instance. The valid values of this parameter depend on the value of the PricingCycle parameter.
        # 
        # *   If PricingCycle is set to **Month**, set this parameter to an integer that ranges from **1** to **9**.
        # *   If PricingCycle is set to **Year**, set this parameter to an integer that ranges from **1** to **3**.
        # 
        # This parameter is required.
        self.duration = duration
        # The ID of the instance that you want to renew. You can call the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The period based on which you are charged for the instance. Valid values:
        # 
        # *   **Month**: You are charged for the instance based on months.
        # *   **Year**: You are charged for the instance based on years.
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # The ID of the region in which the instance that you want to renew is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RenewLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the order. You can obtain the order ID on the Orders page of the Expenses and Costs console.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RenewLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartLdpsComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RestartLdpsComputeGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartLdpsComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartLdpsComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RestartLdpsComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultOlapComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        is_default: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.is_default = is_default
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDefaultOlapComputeGroupResponseBody(TeaModel):
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


class SetDefaultOlapComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDefaultOlapComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetDefaultOlapComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchLSQLV3MySQLServiceRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The type of the operation. Valid value:
        # 
        # *   1: enables the MySQL compatibility feature.
        # *   0: disables the MySQL compatibility feature.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SwitchLSQLV3MySQLServiceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchLSQLV3MySQLServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchLSQLV3MySQLServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SwitchLSQLV3MySQLServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that you want to associate with the resource.
        # 
        # > You can specify the keys of multiple tags. For example, you can specify the key of the first tag in the first key-value pair contained in the value of this parameter and specify the key of the second tag in the second key-value pair.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that you want to associate with the resource.
        # 
        # > You can specify the values of multiple tags. For example, you can specify the value of the first tag in the first key-value pair contained in the value of this parameter and specify the value of the second tag in the second key-value pair.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region in which the instances you want to associate tags with are located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to **INSTANCE**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        self.security_token = security_token
        # The tags that you want to associate with the resource.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the instances. Valid values:
        # 
        # *   **true**: Remove all tags from the instances.
        # *   **false**: Do not remove all tags from the instances.
        # 
        # >  The default value of this parameter is false.
        # 
        # 
        # 
        # *   If you specify this parameter together with the TagKey parameter, this parameter does not take effect.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IDs of instances.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to **INSTANCE**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        self.security_token = security_token
        # The list of keys of the tags that you want to remove.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        delete: bool = None,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_list: str = None,
        security_token: str = None,
    ):
        # Specifies whether to clear all IP addresses and CIDR blocks in the whitelist.
        self.delete = delete
        # The name of the IP whitelist. Default value: user.
        self.group_name = group_name
        # The ID of the instance for which you want to configure a whitelist. You can call the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP addresses or CIDR blocks that you want to add to the whitelist.
        # 
        # >  If you add 127.0.0.1 to the whitelist, all IP addresses cannot be used to access the Lindorm instance. If you add the CIDR block 192.168.0.0/24 to the whitelist, you can use all IP addresses in the CIDR block to access the Lindorm instance. Separate multiple IP addresses or CIDR blocks with commas (,).
        # 
        # This parameter is required.
        self.security_ip_list = security_ip_list
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete is not None:
            result['Delete'] = self.delete
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delete') is not None:
            self.delete = m.get('Delete')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UpdateInstanceIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_groups: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.security_groups = security_groups
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UpdateInstanceSecurityGroupsResponseBody(TeaModel):
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


class UpdateInstanceSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLdpsComputeGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        properties: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.group_name = group_name
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.properties = properties
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class UpdateLdpsComputeGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLdpsComputeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLdpsComputeGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateLdpsComputeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLindormV2InstanceParameterRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_key: str = None,
        parameter_value: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        update_type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.parameter_key = parameter_key
        # This parameter is required.
        self.parameter_value = parameter_value
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        return self


class UpdateLindormV2InstanceParameterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLindormV2InstanceParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLindormV2InstanceParameterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateLindormV2InstanceParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_storage: int = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_id: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        lts_core_num: int = None,
        lts_core_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        stream_num: int = None,
        stream_spec: str = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        upgrade_type: str = None,
        zone_id: str = None,
    ):
        # The storage capacity of the instance after it is upgraded. Unit: GB. Valid values: **480** to **1017600**.
        self.cluster_storage = cluster_storage
        # The cold storage capacity of the instance after it is upgraded. Unit: GB. Valid values: **800** to **1000000**.
        self.cold_storage = cold_storage
        # The storage capacity of a single core node in the instance after the instance upgraded. This parameter is available only if the instance you want to upgrade is a multi-zone instance. Unit: GB. Valid values: 400 to 64000. **This parameter is optional**.
        self.core_single_storage = core_single_storage
        # The number of LindormDFS nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **60**.
        self.filestore_num = filestore_num
        # The specification of LindormDFS nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.filestore_spec = filestore_spec
        # The ID of the instance that you want to upgrade, scale up, or enable cold storage. You can call the [GetLindormInstanceList](https://help.aliyun.com/document_detail/426069.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of LindormTable nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **90**.
        # 
        # > This parameter must be specified together with the LindormSpec parameter.
        self.lindorm_num = lindorm_num
        # The specification of LindormTable nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.c.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        self.lindorm_spec = lindorm_spec
        # The number of log nodes in the instance after the instance is upgraded. This parameter is available only if the instance you want to upgrade is a multi-zone instance. **This parameter is optional**.
        self.log_num = log_num
        # The storage capacity of a single log node in the instance after the instance upgraded. This parameter is available only if the instance you want to upgrade is a multi-zone instance. **This parameter is optional**.
        self.log_single_storage = log_single_storage
        # The specification of log nodes in the instance after the instance is upgraded. This parameter is available only if the instance you want to upgrade is a multi-zone instance. Valid values:
        # 
        # *   **lindorm.sn1.large**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.sn1.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # 
        # **This parameter is optional**.
        self.log_spec = log_spec
        # The number of LTS nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **50**.
        self.lts_core_num = lts_core_num
        # The specification of Lindorm Tunnel Service (LTS) nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        self.lts_core_spec = lts_core_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region in which the instance that you want to upgrade, scale up, or enable cold storage is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of LindormSearch nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **60**.
        self.solr_num = solr_num
        # The specification of LindormSearch nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.solr_spec = solr_spec
        # The number of LindormStream nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **60**.
        self.stream_num = stream_num
        # The specification of LindormStream nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.stream_spec = stream_spec
        # The number of LindormTSDB nodes in the instance after the instance is upgraded. Valid values: integers from **0** to **24**.
        self.tsdb_num = tsdb_num
        # The specification of LindormTSDB nodes in the instance after the instance is upgraded. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.tsdb_spec = tsdb_spec
        # The upgrade type of the operation. For more information about upgrade types, see the UpgradeType parameters section.
        # 
        # This parameter is required.
        self.upgrade_type = upgrade_type
        # The ID of the zone in which the instance that you want to upgrade, scale up, or enable cold storage is located. You can call the [GetLindormInstance](https://help.aliyun.com/document_detail/426067.html) operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_storage is not None:
            result['ClusterStorage'] = self.cluster_storage
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num
        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num
        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.lts_core_num is not None:
            result['LtsCoreNum'] = self.lts_core_num
        if self.lts_core_spec is not None:
            result['LtsCoreSpec'] = self.lts_core_spec
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num
        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        if self.stream_spec is not None:
            result['StreamSpec'] = self.stream_spec
        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num
        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterStorage') is not None:
            self.cluster_storage = m.get('ClusterStorage')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')
        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')
        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('LtsCoreNum') is not None:
            self.lts_core_num = m.get('LtsCoreNum')
        if m.get('LtsCoreSpec') is not None:
            self.lts_core_spec = m.get('LtsCoreSpec')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')
        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        if m.get('StreamSpec') is not None:
            self.stream_spec = m.get('StreamSpec')
        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')
        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpgradeLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeLindormV2StreamEngineRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        quantity: int = None,
        resource_group_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        spec: str = None,
        spec_id: str = None,
        upgrade_type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.quantity = quantity
        self.resource_group_name = resource_group_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is required.
        self.spec = spec
        # This parameter is required.
        self.spec_id = spec_id
        # This parameter is required.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        return self


class UpgradeLindormV2StreamEngineResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeLindormV2StreamEngineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeLindormV2StreamEngineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeLindormV2StreamEngineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


