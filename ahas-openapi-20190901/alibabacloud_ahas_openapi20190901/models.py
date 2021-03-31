# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckExperimentRunnableRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name_space: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.name_space = name_space
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CheckExperimentRunnableResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckExperimentRunnableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckExperimentRunnableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckExperimentRunnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDegradeRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        strategy: int = None,
        threshold: float = None,
        enable: bool = None,
        recovery_timeout_ms: int = None,
        stat_duration_ms: int = None,
        slow_rt_ms: int = None,
        min_request_amount: int = None,
        half_open_base_amount_per_step: int = None,
        half_open_recovery_step_num: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.strategy = strategy
        self.threshold = threshold
        self.enable = enable
        self.recovery_timeout_ms = recovery_timeout_ms
        self.stat_duration_ms = stat_duration_ms
        self.slow_rt_ms = slow_rt_ms
        self.min_request_amount = min_request_amount
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateDegradeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateDegradeRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateDegradeRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateDegradeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDegradeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDegradeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDegradeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        name: str = None,
        description: str = None,
        name_space: str = None,
        ahas_region_id: str = None,
        tags: List[str] = None,
    ):
        self.definition = definition
        self.name = name
        self.description = description
        self.name_space = name_space
        self.ahas_region_id = ahas_region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        experiment_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.experiment_id = experiment_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        relation_strategy: int = None,
        threshold: float = None,
        enable: bool = None,
        resource: str = None,
        limit_origin: str = None,
        ref_resource: str = None,
        control_behavior: int = None,
        warm_up_period_sec: int = None,
        max_queueing_time_ms: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.relation_strategy = relation_strategy
        self.threshold = threshold
        self.enable = enable
        self.resource = resource
        self.limit_origin = limit_origin
        self.ref_resource = ref_resource
        self.control_behavior = control_behavior
        self.warm_up_period_sec = warm_up_period_sec
        self.max_queueing_time_ms = max_queueing_time_ms
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateFlowRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        max_queueing_time_ms: int = None,
        cluster_fallback_strategy: int = None,
        warm_up_period_sec: int = None,
        cluster_mode: bool = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_mode = cluster_mode
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateFlowRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateFlowRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFlowRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotParamItemsRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        items: str = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.items = items
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.items is not None:
            result['Items'] = self.items
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateHotParamItemsResponseBodyDataParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreateHotParamItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[CreateHotParamItemsResponseBodyDataParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = CreateHotParamItemsResponseBodyDataParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateHotParamItemsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateHotParamItemsResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateHotParamItemsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHotParamItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHotParamItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHotParamItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHotParamRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
        resource: str = None,
        param_idx: int = None,
        stat_duration_sec: int = None,
        control_behavior: int = None,
        burst_count: int = None,
        max_queueing_time_ms: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable
        self.resource = resource
        self.param_idx = param_idx
        self.stat_duration_sec = stat_duration_sec
        self.control_behavior = control_behavior
        self.burst_count = burst_count
        self.max_queueing_time_ms = max_queueing_time_ms
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateHotParamRuleResponseBodyDataParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreateHotParamRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[CreateHotParamRuleResponseBodyDataParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = CreateHotParamRuleResponseBodyDataParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateHotParamRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateHotParamRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateHotParamRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateHotParamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHotParamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHotParamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIsolationRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        relation_strategy: int = None,
        threshold: float = None,
        enable: bool = None,
        resource: str = None,
        limit_origin: str = None,
        ref_resource: str = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.relation_strategy = relation_strategy
        self.threshold = threshold
        self.enable = enable
        self.resource = resource
        self.limit_origin = limit_origin
        self.ref_resource = ref_resource
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateIsolationRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateIsolationRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateIsolationRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateIsolationRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIsolationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIsolationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIsolationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSystemRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class CreateSystemRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        metric_type: int = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.metric_type = metric_type
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class CreateSystemRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateSystemRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateSystemRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSystemRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSystemRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSystemRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDegradeRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DeleteDegradeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteDegradeRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteDegradeRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteDegradeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDegradeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDegradeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDegradeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DeleteFlowRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteFlowRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteFlowRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlowRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHotParamRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DeleteHotParamRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteHotParamRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteHotParamRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteHotParamRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteHotParamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHotParamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHotParamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIsolationRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DeleteIsolationRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteIsolationRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteIsolationRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteIsolationRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteIsolationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIsolationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIsolationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSystemRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DeleteSystemRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteSystemRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteSystemRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteSystemRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSystemRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSystemRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSystemRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
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
        message: str = None,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.regions = regions
        self.code = code
        self.success = success

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDegradeRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DisableDegradeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DisableDegradeRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DisableDegradeRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DisableDegradeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableDegradeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableDegradeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableDegradeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFlowRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DisableFlowRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        max_queueing_time_ms: int = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        warm_up_period_sec: int = None,
        cluster_fallback_strategy: int = None,
        threshold: float = None,
        cluster_mode: bool = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.threshold = threshold
        self.cluster_mode = cluster_mode
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DisableFlowRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DisableFlowRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DisableFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableFlowRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableFlowRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableFlowRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableHotParamRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DisableHotParamRuleResponseBodyDataParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DisableHotParamRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[DisableHotParamRuleResponseBodyDataParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = DisableHotParamRuleResponseBodyDataParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DisableHotParamRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DisableHotParamRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DisableHotParamRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableHotParamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableHotParamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableHotParamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIsolationRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DisableIsolationRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DisableIsolationRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DisableIsolationRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DisableIsolationRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableIsolationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableIsolationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableIsolationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSystemRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class DisableSystemRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        metric_type: int = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.metric_type = metric_type
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DisableSystemRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DisableSystemRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DisableSystemRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableSystemRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableSystemRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableSystemRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDegradeRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class EnableDegradeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class EnableDegradeRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EnableDegradeRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnableDegradeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableDegradeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableDegradeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableDegradeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFlowRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class EnableFlowRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        max_queueing_time_ms: int = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        warm_up_period_sec: int = None,
        cluster_fallback_strategy: int = None,
        threshold: float = None,
        cluster_mode: bool = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.threshold = threshold
        self.cluster_mode = cluster_mode
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class EnableFlowRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EnableFlowRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnableFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableFlowRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableFlowRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableFlowRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHotParamRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class EnableHotParamRuleResponseBodyDataParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class EnableHotParamRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[EnableHotParamRuleResponseBodyDataParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = EnableHotParamRuleResponseBodyDataParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class EnableHotParamRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EnableHotParamRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnableHotParamRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableHotParamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableHotParamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableHotParamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIsolationRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class EnableIsolationRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class EnableIsolationRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EnableIsolationRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnableIsolationRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableIsolationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableIsolationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableIsolationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSystemRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class EnableSystemRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        metric_type: int = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.metric_type = metric_type
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class EnableSystemRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EnableSystemRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnableSystemRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableSystemRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableSystemRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableSystemRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name_space: str = None,
        definition: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.name_space = name_space
        self.definition = definition
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ExecuteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.task_id = task_id
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExecuteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishExperimentTaskRequest(TeaModel):
    def __init__(
        self,
        experiment_task_id: str = None,
        name_space: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_task_id = experiment_task_id
        self.name_space = name_space
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class FinishExperimentTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FinishExperimentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FinishExperimentTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FinishExperimentTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActivityTaskRequest(TeaModel):
    def __init__(
        self,
        experiment_task_id: str = None,
        name_space: str = None,
        activity_task_id: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_task_id = experiment_task_id
        self.name_space = name_space
        self.activity_task_id = activity_task_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.activity_task_id is not None:
            result['ActivityTaskId'] = self.activity_task_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('ActivityTaskId') is not None:
            self.activity_task_id = m.get('ActivityTaskId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetActivityTaskResponseBodyHosts(TeaModel):
    def __init__(
        self,
        host_ip: str = None,
        end_time: int = None,
        start_time: int = None,
        data: str = None,
        error_message: str = None,
        exp_id: str = None,
        result: str = None,
        state: str = None,
        task_id: str = None,
    ):
        self.host_ip = host_ip
        self.end_time = end_time
        self.start_time = start_time
        self.data = data
        self.error_message = error_message
        self.exp_id = exp_id
        self.result = result
        self.state = state
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exp_id is not None:
            result['ExpId'] = self.exp_id
        if self.result is not None:
            result['Result'] = self.result
        if self.state is not None:
            result['State'] = self.state
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpId') is not None:
            self.exp_id = m.get('ExpId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetActivityTaskResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[GetActivityTaskResponseBodyHosts] = None,
        phase: str = None,
        end_time: int = None,
        request_id: str = None,
        activity_name: str = None,
        state: str = None,
        activity_id: str = None,
        experiment_task_id: str = None,
        http_status_code: int = None,
        start_time: int = None,
        run_result: str = None,
        success: bool = None,
    ):
        self.hosts = hosts
        self.phase = phase
        self.end_time = end_time
        self.request_id = request_id
        self.activity_name = activity_name
        self.state = state
        self.activity_id = activity_id
        self.experiment_task_id = experiment_task_id
        self.http_status_code = http_status_code
        self.start_time = start_time
        self.run_result = run_result
        self.success = success

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.state is not None:
            result['State'] = self.state
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = GetActivityTaskResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetActivityTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetActivityTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetActivityTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentMetaRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name_space: str = None,
    ):
        self.experiment_id = experiment_id
        self.name_space = name_space

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        return self


class GetExperimentMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        state: str = None,
        experiment_id: str = None,
        create_time: str = None,
        code: str = None,
        success: bool = None,
        tags: List[str] = None,
        name: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.state = state
        self.experiment_id = experiment_id
        self.create_time = create_time
        self.code = code
        self.success = success
        self.tags = tags
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetExperimentMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentTaskRequest(TeaModel):
    def __init__(
        self,
        experiment_task_id: str = None,
        name_space: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_task_id = experiment_task_id
        self.name_space = name_space
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetExperimentTaskResponseBodyActivities(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        check_state: str = None,
        run_result: str = None,
        state: str = None,
        activity_id: str = None,
        phase: str = None,
        activity_name: str = None,
        experiment_task_id: str = None,
        task_id: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.check_state = check_state
        self.run_result = run_result
        self.state = state
        self.activity_id = activity_id
        self.phase = phase
        self.activity_name = activity_name
        self.experiment_task_id = experiment_task_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.check_state is not None:
            result['CheckState'] = self.check_state
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        if self.state is not None:
            result['State'] = self.state
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CheckState') is not None:
            self.check_state = m.get('CheckState')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetExperimentTaskResponseBody(TeaModel):
    def __init__(
        self,
        activities: List[GetExperimentTaskResponseBodyActivities] = None,
        task_id: str = None,
        request_id: str = None,
        experiment_name: str = None,
        state: str = None,
        experiment_id: str = None,
        http_status_code: int = None,
        start_time: int = None,
        success: bool = None,
        result: str = None,
    ):
        self.activities = activities
        self.task_id = task_id
        self.request_id = request_id
        self.experiment_name = experiment_name
        self.state = state
        self.experiment_id = experiment_id
        self.http_status_code = http_status_code
        self.start_time = start_time
        self.success = success
        self.result = result

    def validate(self):
        if self.activities:
            for k in self.activities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Activities'] = []
        if self.activities is not None:
            for k in self.activities:
                result['Activities'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_name is not None:
            result['ExperimentName'] = self.experiment_name
        if self.state is not None:
            result['State'] = self.state
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activities = []
        if m.get('Activities') is not None:
            for k in m.get('Activities'):
                temp_model = GetExperimentTaskResponseBodyActivities()
                self.activities.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentName') is not None:
            self.experiment_name = m.get('ExperimentName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetExperimentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetExperimentTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseKeyRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetLicenseKeyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLicenseKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLicenseKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLicenseKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricsOfAppRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        start_time: int = None,
        end_time: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.start_time = start_time
        self.end_time = end_time
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetMetricsOfAppResponseBodyDataInnerMetrics(TeaModel):
    def __init__(
        self,
        rt_p99: float = None,
        success_qps_avg: float = None,
        passed_qps_p99: float = None,
        rt_avg: float = None,
        count: int = None,
        thread_std: float = None,
        passed_qps_avg: float = None,
        exception_p95: float = None,
        success_qps_max: float = None,
        rt_p95: float = None,
        blocked_qps_min: float = None,
        blocked_qps: float = None,
        timestamp: int = None,
        thread_p95: float = None,
        rt_std: float = None,
        passed_qps_min: float = None,
        blocked_qps_p99: float = None,
        passed_qps_max: float = None,
        exception_max: float = None,
        success_qps: float = None,
        success_qps_p75: float = None,
        thread_p75: float = None,
        success_qps_std: float = None,
        exception_min: float = None,
        passed_qps_p75: float = None,
        passed_qps: float = None,
        thread_max: float = None,
        success_qps_p99: float = None,
        success_qps_min: float = None,
        thread_p99: float = None,
        exception_std: float = None,
        blocked_qps_p95: float = None,
        thread: float = None,
        thread_min: float = None,
        rt_min: float = None,
        blocked_qps_avg: float = None,
        thread_avg: float = None,
        blocked_qps_p75: float = None,
        rt_p75: float = None,
        exception_p99: float = None,
        exception_p75: float = None,
        success_qps_p95: float = None,
        rt: float = None,
        passed_qps_p95: float = None,
        rt_max: float = None,
        blocked_qps_std: float = None,
        blocked_qps_max: float = None,
        exception: float = None,
        exception_avg: float = None,
        passed_qps_std: float = None,
    ):
        self.rt_p99 = rt_p99
        self.success_qps_avg = success_qps_avg
        self.passed_qps_p99 = passed_qps_p99
        self.rt_avg = rt_avg
        self.count = count
        self.thread_std = thread_std
        self.passed_qps_avg = passed_qps_avg
        self.exception_p95 = exception_p95
        self.success_qps_max = success_qps_max
        self.rt_p95 = rt_p95
        self.blocked_qps_min = blocked_qps_min
        self.blocked_qps = blocked_qps
        self.timestamp = timestamp
        self.thread_p95 = thread_p95
        self.rt_std = rt_std
        self.passed_qps_min = passed_qps_min
        self.blocked_qps_p99 = blocked_qps_p99
        self.passed_qps_max = passed_qps_max
        self.exception_max = exception_max
        self.success_qps = success_qps
        self.success_qps_p75 = success_qps_p75
        self.thread_p75 = thread_p75
        self.success_qps_std = success_qps_std
        self.exception_min = exception_min
        self.passed_qps_p75 = passed_qps_p75
        self.passed_qps = passed_qps
        self.thread_max = thread_max
        self.success_qps_p99 = success_qps_p99
        self.success_qps_min = success_qps_min
        self.thread_p99 = thread_p99
        self.exception_std = exception_std
        self.blocked_qps_p95 = blocked_qps_p95
        self.thread = thread
        self.thread_min = thread_min
        self.rt_min = rt_min
        self.blocked_qps_avg = blocked_qps_avg
        self.thread_avg = thread_avg
        self.blocked_qps_p75 = blocked_qps_p75
        self.rt_p75 = rt_p75
        self.exception_p99 = exception_p99
        self.exception_p75 = exception_p75
        self.success_qps_p95 = success_qps_p95
        self.rt = rt
        self.passed_qps_p95 = passed_qps_p95
        self.rt_max = rt_max
        self.blocked_qps_std = blocked_qps_std
        self.blocked_qps_max = blocked_qps_max
        self.exception = exception
        self.exception_avg = exception_avg
        self.passed_qps_std = passed_qps_std

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt_p99 is not None:
            result['RtP99'] = self.rt_p99
        if self.success_qps_avg is not None:
            result['SuccessQpsAvg'] = self.success_qps_avg
        if self.passed_qps_p99 is not None:
            result['PassedQpsP99'] = self.passed_qps_p99
        if self.rt_avg is not None:
            result['RtAvg'] = self.rt_avg
        if self.count is not None:
            result['Count'] = self.count
        if self.thread_std is not None:
            result['ThreadStd'] = self.thread_std
        if self.passed_qps_avg is not None:
            result['PassedQpsAvg'] = self.passed_qps_avg
        if self.exception_p95 is not None:
            result['ExceptionP95'] = self.exception_p95
        if self.success_qps_max is not None:
            result['SuccessQpsMax'] = self.success_qps_max
        if self.rt_p95 is not None:
            result['RtP95'] = self.rt_p95
        if self.blocked_qps_min is not None:
            result['BlockedQpsMin'] = self.blocked_qps_min
        if self.blocked_qps is not None:
            result['BlockedQps'] = self.blocked_qps
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.thread_p95 is not None:
            result['ThreadP95'] = self.thread_p95
        if self.rt_std is not None:
            result['RtStd'] = self.rt_std
        if self.passed_qps_min is not None:
            result['PassedQpsMin'] = self.passed_qps_min
        if self.blocked_qps_p99 is not None:
            result['BlockedQpsP99'] = self.blocked_qps_p99
        if self.passed_qps_max is not None:
            result['PassedQpsMax'] = self.passed_qps_max
        if self.exception_max is not None:
            result['ExceptionMax'] = self.exception_max
        if self.success_qps is not None:
            result['SuccessQps'] = self.success_qps
        if self.success_qps_p75 is not None:
            result['SuccessQpsP75'] = self.success_qps_p75
        if self.thread_p75 is not None:
            result['ThreadP75'] = self.thread_p75
        if self.success_qps_std is not None:
            result['SuccessQpsStd'] = self.success_qps_std
        if self.exception_min is not None:
            result['ExceptionMin'] = self.exception_min
        if self.passed_qps_p75 is not None:
            result['PassedQpsP75'] = self.passed_qps_p75
        if self.passed_qps is not None:
            result['PassedQps'] = self.passed_qps
        if self.thread_max is not None:
            result['ThreadMax'] = self.thread_max
        if self.success_qps_p99 is not None:
            result['SuccessQpsP99'] = self.success_qps_p99
        if self.success_qps_min is not None:
            result['SuccessQpsMin'] = self.success_qps_min
        if self.thread_p99 is not None:
            result['ThreadP99'] = self.thread_p99
        if self.exception_std is not None:
            result['ExceptionStd'] = self.exception_std
        if self.blocked_qps_p95 is not None:
            result['BlockedQpsP95'] = self.blocked_qps_p95
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.thread_min is not None:
            result['ThreadMin'] = self.thread_min
        if self.rt_min is not None:
            result['RtMin'] = self.rt_min
        if self.blocked_qps_avg is not None:
            result['BlockedQpsAvg'] = self.blocked_qps_avg
        if self.thread_avg is not None:
            result['ThreadAvg'] = self.thread_avg
        if self.blocked_qps_p75 is not None:
            result['BlockedQpsP75'] = self.blocked_qps_p75
        if self.rt_p75 is not None:
            result['RtP75'] = self.rt_p75
        if self.exception_p99 is not None:
            result['ExceptionP99'] = self.exception_p99
        if self.exception_p75 is not None:
            result['ExceptionP75'] = self.exception_p75
        if self.success_qps_p95 is not None:
            result['SuccessQpsP95'] = self.success_qps_p95
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.passed_qps_p95 is not None:
            result['PassedQpsP95'] = self.passed_qps_p95
        if self.rt_max is not None:
            result['RtMax'] = self.rt_max
        if self.blocked_qps_std is not None:
            result['BlockedQpsStd'] = self.blocked_qps_std
        if self.blocked_qps_max is not None:
            result['BlockedQpsMax'] = self.blocked_qps_max
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.exception_avg is not None:
            result['ExceptionAvg'] = self.exception_avg
        if self.passed_qps_std is not None:
            result['PassedQpsStd'] = self.passed_qps_std
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtP99') is not None:
            self.rt_p99 = m.get('RtP99')
        if m.get('SuccessQpsAvg') is not None:
            self.success_qps_avg = m.get('SuccessQpsAvg')
        if m.get('PassedQpsP99') is not None:
            self.passed_qps_p99 = m.get('PassedQpsP99')
        if m.get('RtAvg') is not None:
            self.rt_avg = m.get('RtAvg')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ThreadStd') is not None:
            self.thread_std = m.get('ThreadStd')
        if m.get('PassedQpsAvg') is not None:
            self.passed_qps_avg = m.get('PassedQpsAvg')
        if m.get('ExceptionP95') is not None:
            self.exception_p95 = m.get('ExceptionP95')
        if m.get('SuccessQpsMax') is not None:
            self.success_qps_max = m.get('SuccessQpsMax')
        if m.get('RtP95') is not None:
            self.rt_p95 = m.get('RtP95')
        if m.get('BlockedQpsMin') is not None:
            self.blocked_qps_min = m.get('BlockedQpsMin')
        if m.get('BlockedQps') is not None:
            self.blocked_qps = m.get('BlockedQps')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ThreadP95') is not None:
            self.thread_p95 = m.get('ThreadP95')
        if m.get('RtStd') is not None:
            self.rt_std = m.get('RtStd')
        if m.get('PassedQpsMin') is not None:
            self.passed_qps_min = m.get('PassedQpsMin')
        if m.get('BlockedQpsP99') is not None:
            self.blocked_qps_p99 = m.get('BlockedQpsP99')
        if m.get('PassedQpsMax') is not None:
            self.passed_qps_max = m.get('PassedQpsMax')
        if m.get('ExceptionMax') is not None:
            self.exception_max = m.get('ExceptionMax')
        if m.get('SuccessQps') is not None:
            self.success_qps = m.get('SuccessQps')
        if m.get('SuccessQpsP75') is not None:
            self.success_qps_p75 = m.get('SuccessQpsP75')
        if m.get('ThreadP75') is not None:
            self.thread_p75 = m.get('ThreadP75')
        if m.get('SuccessQpsStd') is not None:
            self.success_qps_std = m.get('SuccessQpsStd')
        if m.get('ExceptionMin') is not None:
            self.exception_min = m.get('ExceptionMin')
        if m.get('PassedQpsP75') is not None:
            self.passed_qps_p75 = m.get('PassedQpsP75')
        if m.get('PassedQps') is not None:
            self.passed_qps = m.get('PassedQps')
        if m.get('ThreadMax') is not None:
            self.thread_max = m.get('ThreadMax')
        if m.get('SuccessQpsP99') is not None:
            self.success_qps_p99 = m.get('SuccessQpsP99')
        if m.get('SuccessQpsMin') is not None:
            self.success_qps_min = m.get('SuccessQpsMin')
        if m.get('ThreadP99') is not None:
            self.thread_p99 = m.get('ThreadP99')
        if m.get('ExceptionStd') is not None:
            self.exception_std = m.get('ExceptionStd')
        if m.get('BlockedQpsP95') is not None:
            self.blocked_qps_p95 = m.get('BlockedQpsP95')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('ThreadMin') is not None:
            self.thread_min = m.get('ThreadMin')
        if m.get('RtMin') is not None:
            self.rt_min = m.get('RtMin')
        if m.get('BlockedQpsAvg') is not None:
            self.blocked_qps_avg = m.get('BlockedQpsAvg')
        if m.get('ThreadAvg') is not None:
            self.thread_avg = m.get('ThreadAvg')
        if m.get('BlockedQpsP75') is not None:
            self.blocked_qps_p75 = m.get('BlockedQpsP75')
        if m.get('RtP75') is not None:
            self.rt_p75 = m.get('RtP75')
        if m.get('ExceptionP99') is not None:
            self.exception_p99 = m.get('ExceptionP99')
        if m.get('ExceptionP75') is not None:
            self.exception_p75 = m.get('ExceptionP75')
        if m.get('SuccessQpsP95') is not None:
            self.success_qps_p95 = m.get('SuccessQpsP95')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('PassedQpsP95') is not None:
            self.passed_qps_p95 = m.get('PassedQpsP95')
        if m.get('RtMax') is not None:
            self.rt_max = m.get('RtMax')
        if m.get('BlockedQpsStd') is not None:
            self.blocked_qps_std = m.get('BlockedQpsStd')
        if m.get('BlockedQpsMax') is not None:
            self.blocked_qps_max = m.get('BlockedQpsMax')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('ExceptionAvg') is not None:
            self.exception_avg = m.get('ExceptionAvg')
        if m.get('PassedQpsStd') is not None:
            self.passed_qps_std = m.get('PassedQpsStd')
        return self


class GetMetricsOfAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        namespace: str = None,
        inner_metrics: List[GetMetricsOfAppResponseBodyDataInnerMetrics] = None,
    ):
        self.app_name = app_name
        self.namespace = namespace
        self.inner_metrics = inner_metrics

    def validate(self):
        if self.inner_metrics:
            for k in self.inner_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['InnerMetrics'] = []
        if self.inner_metrics is not None:
            for k in self.inner_metrics:
                result['InnerMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.inner_metrics = []
        if m.get('InnerMetrics') is not None:
            for k in m.get('InnerMetrics'):
                temp_model = GetMetricsOfAppResponseBodyDataInnerMetrics()
                self.inner_metrics.append(temp_model.from_map(k))
        return self


class GetMetricsOfAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMetricsOfAppResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMetricsOfAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMetricsOfAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetricsOfAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMetricsOfAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricsOfResourceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        start_time: int = None,
        end_time: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.start_time = start_time
        self.end_time = end_time
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetMetricsOfResourceResponseBodyDataInnerMetrics(TeaModel):
    def __init__(
        self,
        rt_p99: float = None,
        success_qps_avg: float = None,
        passed_qps_p99: float = None,
        rt_avg: float = None,
        count: int = None,
        thread_std: float = None,
        passed_qps_avg: float = None,
        exception_p95: float = None,
        success_qps_max: float = None,
        rt_p95: float = None,
        blocked_qps_min: float = None,
        blocked_qps: float = None,
        timestamp: int = None,
        thread_p95: float = None,
        rt_std: float = None,
        passed_qps_min: float = None,
        blocked_qps_p99: float = None,
        passed_qps_max: float = None,
        exception_max: float = None,
        success_qps: float = None,
        success_qps_p75: float = None,
        thread_p75: float = None,
        success_qps_std: float = None,
        exception_min: float = None,
        passed_qps_p75: float = None,
        passed_qps: float = None,
        thread_max: float = None,
        success_qps_p99: float = None,
        success_qps_min: float = None,
        thread_p99: float = None,
        exception_std: float = None,
        blocked_qps_p95: float = None,
        thread: float = None,
        thread_min: float = None,
        rt_min: float = None,
        blocked_qps_avg: float = None,
        thread_avg: float = None,
        blocked_qps_p75: float = None,
        rt_p75: float = None,
        exception_p99: float = None,
        exception_p75: float = None,
        success_qps_p95: float = None,
        rt: float = None,
        passed_qps_p95: float = None,
        rt_max: float = None,
        blocked_qps_std: float = None,
        blocked_qps_max: float = None,
        exception: float = None,
        exception_avg: float = None,
        passed_qps_std: float = None,
    ):
        self.rt_p99 = rt_p99
        self.success_qps_avg = success_qps_avg
        self.passed_qps_p99 = passed_qps_p99
        self.rt_avg = rt_avg
        self.count = count
        self.thread_std = thread_std
        self.passed_qps_avg = passed_qps_avg
        self.exception_p95 = exception_p95
        self.success_qps_max = success_qps_max
        self.rt_p95 = rt_p95
        self.blocked_qps_min = blocked_qps_min
        self.blocked_qps = blocked_qps
        self.timestamp = timestamp
        self.thread_p95 = thread_p95
        self.rt_std = rt_std
        self.passed_qps_min = passed_qps_min
        self.blocked_qps_p99 = blocked_qps_p99
        self.passed_qps_max = passed_qps_max
        self.exception_max = exception_max
        self.success_qps = success_qps
        self.success_qps_p75 = success_qps_p75
        self.thread_p75 = thread_p75
        self.success_qps_std = success_qps_std
        self.exception_min = exception_min
        self.passed_qps_p75 = passed_qps_p75
        self.passed_qps = passed_qps
        self.thread_max = thread_max
        self.success_qps_p99 = success_qps_p99
        self.success_qps_min = success_qps_min
        self.thread_p99 = thread_p99
        self.exception_std = exception_std
        self.blocked_qps_p95 = blocked_qps_p95
        self.thread = thread
        self.thread_min = thread_min
        self.rt_min = rt_min
        self.blocked_qps_avg = blocked_qps_avg
        self.thread_avg = thread_avg
        self.blocked_qps_p75 = blocked_qps_p75
        self.rt_p75 = rt_p75
        self.exception_p99 = exception_p99
        self.exception_p75 = exception_p75
        self.success_qps_p95 = success_qps_p95
        self.rt = rt
        self.passed_qps_p95 = passed_qps_p95
        self.rt_max = rt_max
        self.blocked_qps_std = blocked_qps_std
        self.blocked_qps_max = blocked_qps_max
        self.exception = exception
        self.exception_avg = exception_avg
        self.passed_qps_std = passed_qps_std

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt_p99 is not None:
            result['RtP99'] = self.rt_p99
        if self.success_qps_avg is not None:
            result['SuccessQpsAvg'] = self.success_qps_avg
        if self.passed_qps_p99 is not None:
            result['PassedQpsP99'] = self.passed_qps_p99
        if self.rt_avg is not None:
            result['RtAvg'] = self.rt_avg
        if self.count is not None:
            result['Count'] = self.count
        if self.thread_std is not None:
            result['ThreadStd'] = self.thread_std
        if self.passed_qps_avg is not None:
            result['PassedQpsAvg'] = self.passed_qps_avg
        if self.exception_p95 is not None:
            result['ExceptionP95'] = self.exception_p95
        if self.success_qps_max is not None:
            result['SuccessQpsMax'] = self.success_qps_max
        if self.rt_p95 is not None:
            result['RtP95'] = self.rt_p95
        if self.blocked_qps_min is not None:
            result['BlockedQpsMin'] = self.blocked_qps_min
        if self.blocked_qps is not None:
            result['BlockedQps'] = self.blocked_qps
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.thread_p95 is not None:
            result['ThreadP95'] = self.thread_p95
        if self.rt_std is not None:
            result['RtStd'] = self.rt_std
        if self.passed_qps_min is not None:
            result['PassedQpsMin'] = self.passed_qps_min
        if self.blocked_qps_p99 is not None:
            result['BlockedQpsP99'] = self.blocked_qps_p99
        if self.passed_qps_max is not None:
            result['PassedQpsMax'] = self.passed_qps_max
        if self.exception_max is not None:
            result['ExceptionMax'] = self.exception_max
        if self.success_qps is not None:
            result['SuccessQps'] = self.success_qps
        if self.success_qps_p75 is not None:
            result['SuccessQpsP75'] = self.success_qps_p75
        if self.thread_p75 is not None:
            result['ThreadP75'] = self.thread_p75
        if self.success_qps_std is not None:
            result['SuccessQpsStd'] = self.success_qps_std
        if self.exception_min is not None:
            result['ExceptionMin'] = self.exception_min
        if self.passed_qps_p75 is not None:
            result['PassedQpsP75'] = self.passed_qps_p75
        if self.passed_qps is not None:
            result['PassedQps'] = self.passed_qps
        if self.thread_max is not None:
            result['ThreadMax'] = self.thread_max
        if self.success_qps_p99 is not None:
            result['SuccessQpsP99'] = self.success_qps_p99
        if self.success_qps_min is not None:
            result['SuccessQpsMin'] = self.success_qps_min
        if self.thread_p99 is not None:
            result['ThreadP99'] = self.thread_p99
        if self.exception_std is not None:
            result['ExceptionStd'] = self.exception_std
        if self.blocked_qps_p95 is not None:
            result['BlockedQpsP95'] = self.blocked_qps_p95
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.thread_min is not None:
            result['ThreadMin'] = self.thread_min
        if self.rt_min is not None:
            result['RtMin'] = self.rt_min
        if self.blocked_qps_avg is not None:
            result['BlockedQpsAvg'] = self.blocked_qps_avg
        if self.thread_avg is not None:
            result['ThreadAvg'] = self.thread_avg
        if self.blocked_qps_p75 is not None:
            result['BlockedQpsP75'] = self.blocked_qps_p75
        if self.rt_p75 is not None:
            result['RtP75'] = self.rt_p75
        if self.exception_p99 is not None:
            result['ExceptionP99'] = self.exception_p99
        if self.exception_p75 is not None:
            result['ExceptionP75'] = self.exception_p75
        if self.success_qps_p95 is not None:
            result['SuccessQpsP95'] = self.success_qps_p95
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.passed_qps_p95 is not None:
            result['PassedQpsP95'] = self.passed_qps_p95
        if self.rt_max is not None:
            result['RtMax'] = self.rt_max
        if self.blocked_qps_std is not None:
            result['BlockedQpsStd'] = self.blocked_qps_std
        if self.blocked_qps_max is not None:
            result['BlockedQpsMax'] = self.blocked_qps_max
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.exception_avg is not None:
            result['ExceptionAvg'] = self.exception_avg
        if self.passed_qps_std is not None:
            result['PassedQpsStd'] = self.passed_qps_std
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtP99') is not None:
            self.rt_p99 = m.get('RtP99')
        if m.get('SuccessQpsAvg') is not None:
            self.success_qps_avg = m.get('SuccessQpsAvg')
        if m.get('PassedQpsP99') is not None:
            self.passed_qps_p99 = m.get('PassedQpsP99')
        if m.get('RtAvg') is not None:
            self.rt_avg = m.get('RtAvg')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ThreadStd') is not None:
            self.thread_std = m.get('ThreadStd')
        if m.get('PassedQpsAvg') is not None:
            self.passed_qps_avg = m.get('PassedQpsAvg')
        if m.get('ExceptionP95') is not None:
            self.exception_p95 = m.get('ExceptionP95')
        if m.get('SuccessQpsMax') is not None:
            self.success_qps_max = m.get('SuccessQpsMax')
        if m.get('RtP95') is not None:
            self.rt_p95 = m.get('RtP95')
        if m.get('BlockedQpsMin') is not None:
            self.blocked_qps_min = m.get('BlockedQpsMin')
        if m.get('BlockedQps') is not None:
            self.blocked_qps = m.get('BlockedQps')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ThreadP95') is not None:
            self.thread_p95 = m.get('ThreadP95')
        if m.get('RtStd') is not None:
            self.rt_std = m.get('RtStd')
        if m.get('PassedQpsMin') is not None:
            self.passed_qps_min = m.get('PassedQpsMin')
        if m.get('BlockedQpsP99') is not None:
            self.blocked_qps_p99 = m.get('BlockedQpsP99')
        if m.get('PassedQpsMax') is not None:
            self.passed_qps_max = m.get('PassedQpsMax')
        if m.get('ExceptionMax') is not None:
            self.exception_max = m.get('ExceptionMax')
        if m.get('SuccessQps') is not None:
            self.success_qps = m.get('SuccessQps')
        if m.get('SuccessQpsP75') is not None:
            self.success_qps_p75 = m.get('SuccessQpsP75')
        if m.get('ThreadP75') is not None:
            self.thread_p75 = m.get('ThreadP75')
        if m.get('SuccessQpsStd') is not None:
            self.success_qps_std = m.get('SuccessQpsStd')
        if m.get('ExceptionMin') is not None:
            self.exception_min = m.get('ExceptionMin')
        if m.get('PassedQpsP75') is not None:
            self.passed_qps_p75 = m.get('PassedQpsP75')
        if m.get('PassedQps') is not None:
            self.passed_qps = m.get('PassedQps')
        if m.get('ThreadMax') is not None:
            self.thread_max = m.get('ThreadMax')
        if m.get('SuccessQpsP99') is not None:
            self.success_qps_p99 = m.get('SuccessQpsP99')
        if m.get('SuccessQpsMin') is not None:
            self.success_qps_min = m.get('SuccessQpsMin')
        if m.get('ThreadP99') is not None:
            self.thread_p99 = m.get('ThreadP99')
        if m.get('ExceptionStd') is not None:
            self.exception_std = m.get('ExceptionStd')
        if m.get('BlockedQpsP95') is not None:
            self.blocked_qps_p95 = m.get('BlockedQpsP95')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('ThreadMin') is not None:
            self.thread_min = m.get('ThreadMin')
        if m.get('RtMin') is not None:
            self.rt_min = m.get('RtMin')
        if m.get('BlockedQpsAvg') is not None:
            self.blocked_qps_avg = m.get('BlockedQpsAvg')
        if m.get('ThreadAvg') is not None:
            self.thread_avg = m.get('ThreadAvg')
        if m.get('BlockedQpsP75') is not None:
            self.blocked_qps_p75 = m.get('BlockedQpsP75')
        if m.get('RtP75') is not None:
            self.rt_p75 = m.get('RtP75')
        if m.get('ExceptionP99') is not None:
            self.exception_p99 = m.get('ExceptionP99')
        if m.get('ExceptionP75') is not None:
            self.exception_p75 = m.get('ExceptionP75')
        if m.get('SuccessQpsP95') is not None:
            self.success_qps_p95 = m.get('SuccessQpsP95')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('PassedQpsP95') is not None:
            self.passed_qps_p95 = m.get('PassedQpsP95')
        if m.get('RtMax') is not None:
            self.rt_max = m.get('RtMax')
        if m.get('BlockedQpsStd') is not None:
            self.blocked_qps_std = m.get('BlockedQpsStd')
        if m.get('BlockedQpsMax') is not None:
            self.blocked_qps_max = m.get('BlockedQpsMax')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('ExceptionAvg') is not None:
            self.exception_avg = m.get('ExceptionAvg')
        if m.get('PassedQpsStd') is not None:
            self.passed_qps_std = m.get('PassedQpsStd')
        return self


class GetMetricsOfResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        resource: str = None,
        namespace: str = None,
        inner_metrics: List[GetMetricsOfResourceResponseBodyDataInnerMetrics] = None,
    ):
        self.app_name = app_name
        self.resource = resource
        self.namespace = namespace
        self.inner_metrics = inner_metrics

    def validate(self):
        if self.inner_metrics:
            for k in self.inner_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['InnerMetrics'] = []
        if self.inner_metrics is not None:
            for k in self.inner_metrics:
                result['InnerMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.inner_metrics = []
        if m.get('InnerMetrics') is not None:
            for k in m.get('InnerMetrics'):
                temp_model = GetMetricsOfResourceResponseBodyDataInnerMetrics()
                self.inner_metrics.append(temp_model.from_map(k))
        return self


class GetMetricsOfResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMetricsOfResourceResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMetricsOfResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMetricsOfResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetricsOfResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMetricsOfResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSentinelAppSumMetricRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        namespace: str = None,
        app_name: str = None,
        start_time: str = None,
        end_time: str = None,
        ahas_region_id: str = None,
    ):
        self.accept_language = accept_language
        self.namespace = namespace
        self.app_name = app_name
        self.start_time = start_time
        self.end_time = end_time
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetSentinelAppSumMetricResponseBodyMetricData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        pass_count: float = None,
        machine_count: int = None,
        avg_rt: float = None,
        user_id: str = None,
        namespace: str = None,
        total_count: float = None,
        block_count: float = None,
    ):
        self.app_name = app_name
        self.pass_count = pass_count
        self.machine_count = machine_count
        self.avg_rt = avg_rt
        self.user_id = user_id
        self.namespace = namespace
        self.total_count = total_count
        self.block_count = block_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        return self


class GetSentinelAppSumMetricResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
        metric_data: GetSentinelAppSumMetricResponseBodyMetricData = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success
        self.metric_data = metric_data

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('MetricData') is not None:
            temp_model = GetSentinelAppSumMetricResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m['MetricData'])
        return self


class GetSentinelAppSumMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSentinelAppSumMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSentinelAppSumMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserApplicationsRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetUserApplicationsResponseBodyAppNameAndIdPairs(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_id: str = None,
        scope_type: int = None,
        app_type: int = None,
    ):
        self.app_name = app_name
        self.app_id = app_id
        self.scope_type = scope_type
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class GetUserApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        app_name_and_id_pairs: List[GetUserApplicationsResponseBodyAppNameAndIdPairs] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.app_name_and_id_pairs = app_name_and_id_pairs
        self.code = code
        self.success = success

    def validate(self):
        if self.app_name_and_id_pairs:
            for k in self.app_name_and_id_pairs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['AppNameAndIdPairs'] = []
        if self.app_name_and_id_pairs is not None:
            for k in self.app_name_and_id_pairs:
                result['AppNameAndIdPairs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.app_name_and_id_pairs = []
        if m.get('AppNameAndIdPairs') is not None:
            for k in m.get('AppNameAndIdPairs'):
                temp_model = GetUserApplicationsResponseBodyAppNameAndIdPairs()
                self.app_name_and_id_pairs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserWorkspaceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class GetUserWorkspaceResponseBodyWorkspaceList(TeaModel):
    def __init__(
        self,
        type: int = None,
        workspace_id: str = None,
        description: str = None,
        name: str = None,
    ):
        self.type = type
        self.workspace_id = workspace_id
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetUserWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        workspace_list: List[GetUserWorkspaceResponseBodyWorkspaceList] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.workspace_list = workspace_list
        self.code = code
        self.success = success

    def validate(self):
        if self.workspace_list:
            for k in self.workspace_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['WorkspaceList'] = []
        if self.workspace_list is not None:
            for k in self.workspace_list:
                result['WorkspaceList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.workspace_list = []
        if m.get('WorkspaceList') is not None:
            for k in m.get('WorkspaceList'):
                temp_model = GetUserWorkspaceResponseBodyWorkspaceList()
                self.workspace_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActiveAppsRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_type: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_type = app_type
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListActiveAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        last_health_ping_time: int = None,
        current_level: int = None,
        namespace: str = None,
        app_type: int = None,
        dirty_level: int = None,
        ahas_app_name: str = None,
    ):
        self.app_name = app_name
        self.last_health_ping_time = last_health_ping_time
        self.current_level = current_level
        self.namespace = namespace
        self.app_type = app_type
        self.dirty_level = dirty_level
        self.ahas_app_name = ahas_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.last_health_ping_time is not None:
            result['LastHealthPingTime'] = self.last_health_ping_time
        if self.current_level is not None:
            result['CurrentLevel'] = self.current_level
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dirty_level is not None:
            result['DirtyLevel'] = self.dirty_level
        if self.ahas_app_name is not None:
            result['AhasAppName'] = self.ahas_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('LastHealthPingTime') is not None:
            self.last_health_ping_time = m.get('LastHealthPingTime')
        if m.get('CurrentLevel') is not None:
            self.current_level = m.get('CurrentLevel')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DirtyLevel') is not None:
            self.dirty_level = m.get('DirtyLevel')
        if m.get('AhasAppName') is not None:
            self.ahas_app_name = m.get('AhasAppName')
        return self


class ListActiveAppsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListActiveAppsResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListActiveAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListActiveAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListActiveAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListActiveAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDegradeRulesOfAppRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListDegradeRulesOfAppResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListDegradeRulesOfAppResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListDegradeRulesOfAppResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListDegradeRulesOfAppResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDegradeRulesOfAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDegradeRulesOfAppResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDegradeRulesOfAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDegradeRulesOfAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDegradeRulesOfAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDegradeRulesOfAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDegradeRulesOfResourceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListDegradeRulesOfResourceResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListDegradeRulesOfResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListDegradeRulesOfResourceResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListDegradeRulesOfResourceResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDegradeRulesOfResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDegradeRulesOfResourceResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDegradeRulesOfResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDegradeRulesOfResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDegradeRulesOfResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDegradeRulesOfResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentMetasRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        name_space: str = None,
        size: int = None,
        ahas_region_id: str = None,
    ):
        self.page = page
        self.name_space = name_space
        self.size = size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.size is not None:
            result['Size'] = self.size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListExperimentMetasResponseBodyContent(TeaModel):
    def __init__(
        self,
        state: str = None,
        create_time: int = None,
        experiment_id: str = None,
        tags: List[str] = None,
        name: str = None,
    ):
        self.state = state
        self.create_time = create_time
        self.experiment_id = experiment_id
        self.tags = tags
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListExperimentMetasResponseBody(TeaModel):
    def __init__(
        self,
        pages: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        current_page: int = None,
        content: List[ListExperimentMetasResponseBodyContent] = None,
        total: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.pages = pages
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.current_page = current_page
        self.content = content
        self.total = total
        self.code = code
        self.success = success

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = ListExperimentMetasResponseBodyContent()
                self.content.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExperimentMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExperimentMetasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExperimentMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRulesOfAppRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListFlowRulesOfAppResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        max_queueing_time_ms: int = None,
        cluster_fallback_strategy: int = None,
        warm_up_period_sec: int = None,
        cluster_mode: bool = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_mode = cluster_mode
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListFlowRulesOfAppResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListFlowRulesOfAppResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListFlowRulesOfAppResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowRulesOfAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListFlowRulesOfAppResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListFlowRulesOfAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFlowRulesOfAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowRulesOfAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowRulesOfAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRulesOfResourceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListFlowRulesOfResourceResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        max_queueing_time_ms: int = None,
        cluster_fallback_strategy: int = None,
        warm_up_period_sec: int = None,
        cluster_mode: bool = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_mode = cluster_mode
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListFlowRulesOfResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListFlowRulesOfResourceResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListFlowRulesOfResourceResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowRulesOfResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListFlowRulesOfResourceResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListFlowRulesOfResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFlowRulesOfResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowRulesOfResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowRulesOfResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotParamRulesOfAppRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListHotParamRulesOfAppResponseBodyDataDatasParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ListHotParamRulesOfAppResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[ListHotParamRulesOfAppResponseBodyDataDatasParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = ListHotParamRulesOfAppResponseBodyDataDatasParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListHotParamRulesOfAppResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListHotParamRulesOfAppResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListHotParamRulesOfAppResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHotParamRulesOfAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListHotParamRulesOfAppResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHotParamRulesOfAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotParamRulesOfAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHotParamRulesOfAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHotParamRulesOfAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotParamRulesOfResourceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListHotParamRulesOfResourceResponseBodyDataDatasParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ListHotParamRulesOfResourceResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[ListHotParamRulesOfResourceResponseBodyDataDatasParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = ListHotParamRulesOfResourceResponseBodyDataDatasParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListHotParamRulesOfResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListHotParamRulesOfResourceResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListHotParamRulesOfResourceResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHotParamRulesOfResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListHotParamRulesOfResourceResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHotParamRulesOfResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotParamRulesOfResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHotParamRulesOfResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHotParamRulesOfResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIsolationRulesOfAppRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListIsolationRulesOfAppResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListIsolationRulesOfAppResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListIsolationRulesOfAppResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListIsolationRulesOfAppResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIsolationRulesOfAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListIsolationRulesOfAppResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListIsolationRulesOfAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIsolationRulesOfAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIsolationRulesOfAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIsolationRulesOfAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIsolationRulesOfResourceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        resource: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.resource = resource
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListIsolationRulesOfResourceResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ListIsolationRulesOfResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListIsolationRulesOfResourceResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListIsolationRulesOfResourceResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIsolationRulesOfResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListIsolationRulesOfResourceResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListIsolationRulesOfResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIsolationRulesOfResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIsolationRulesOfResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIsolationRulesOfResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemRulesRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        app_name: str = None,
        page_index: int = None,
        page_size: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.app_name = app_name
        self.page_index = page_index
        self.page_size = page_size
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ListSystemRulesResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        namespace: str = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
        rule_id: int = None,
    ):
        self.app_name = app_name
        self.namespace = namespace
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListSystemRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        datas: List[ListSystemRulesResponseBodyDataDatas] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_index = page_index
        self.datas = datas
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListSystemRulesResponseBodyDataDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSystemRulesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListSystemRulesResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListSystemRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSystemRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSystemRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSystemRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDegradeRuleRequest(TeaModel):
    def __init__(
        self,
        strategy: int = None,
        threshold: float = None,
        rule_id: int = None,
        recovery_timeout_ms: int = None,
        stat_duration_ms: int = None,
        slow_rt_ms: int = None,
        min_request_amount: int = None,
        half_open_base_amount_per_step: int = None,
        half_open_recovery_step_num: int = None,
        ahas_region_id: str = None,
    ):
        self.strategy = strategy
        self.threshold = threshold
        self.rule_id = rule_id
        self.recovery_timeout_ms = recovery_timeout_ms
        self.stat_duration_ms = stat_duration_ms
        self.slow_rt_ms = slow_rt_ms
        self.min_request_amount = min_request_amount
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ModifyDegradeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        slow_rt_ms: int = None,
        half_open_recovery_step_num: int = None,
        namespace: str = None,
        stat_duration_ms: int = None,
        rule_id: int = None,
        strategy: int = None,
        resource: str = None,
        app_name: str = None,
        half_open_base_amount_per_step: int = None,
        recovery_timeout_ms: int = None,
        min_request_amount: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.slow_rt_ms = slow_rt_ms
        self.half_open_recovery_step_num = half_open_recovery_step_num
        self.namespace = namespace
        self.stat_duration_ms = stat_duration_ms
        self.rule_id = rule_id
        self.strategy = strategy
        self.resource = resource
        self.app_name = app_name
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        self.recovery_timeout_ms = recovery_timeout_ms
        self.min_request_amount = min_request_amount
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slow_rt_ms is not None:
            result['SlowRtMs'] = self.slow_rt_ms
        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step
        if self.recovery_timeout_ms is not None:
            result['RecoveryTimeoutMs'] = self.recovery_timeout_ms
        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowRtMs') is not None:
            self.slow_rt_ms = m.get('SlowRtMs')
        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')
        if m.get('RecoveryTimeoutMs') is not None:
            self.recovery_timeout_ms = m.get('RecoveryTimeoutMs')
        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyDegradeRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ModifyDegradeRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ModifyDegradeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDegradeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDegradeRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDegradeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowRuleRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        rule_id: int = None,
        relation_strategy: int = None,
        threshold: float = None,
        limit_origin: str = None,
        ref_resource: str = None,
        control_behavior: str = None,
        warm_up_period_sec: int = None,
        max_queueing_time_ms: int = None,
        ahas_region_id: str = None,
    ):
        self.namespace = namespace
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.threshold = threshold
        self.limit_origin = limit_origin
        self.ref_resource = ref_resource
        self.control_behavior = control_behavior
        self.warm_up_period_sec = warm_up_period_sec
        self.max_queueing_time_ms = max_queueing_time_ms
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ModifyFlowRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        ref_resource: str = None,
        cluster_fallback_threshold: int = None,
        namespace: str = None,
        limit_origin: str = None,
        stat_duration_ms: int = None,
        cluster_threshold_type: int = None,
        rule_id: int = None,
        relation_strategy: int = None,
        app_name: str = None,
        resource: str = None,
        max_queueing_time_ms: int = None,
        cluster_estimated_max_qps: float = None,
        control_behavior: int = None,
        warm_up_period_sec: int = None,
        cluster_fallback_strategy: int = None,
        threshold: float = None,
        cluster_mode: bool = None,
        enable: bool = None,
    ):
        self.ref_resource = ref_resource
        self.cluster_fallback_threshold = cluster_fallback_threshold
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.stat_duration_ms = stat_duration_ms
        self.cluster_threshold_type = cluster_threshold_type
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.app_name = app_name
        self.resource = resource
        self.max_queueing_time_ms = max_queueing_time_ms
        self.cluster_estimated_max_qps = cluster_estimated_max_qps
        self.control_behavior = control_behavior
        self.warm_up_period_sec = warm_up_period_sec
        self.cluster_fallback_strategy = cluster_fallback_strategy
        self.threshold = threshold
        self.cluster_mode = cluster_mode
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.cluster_fallback_threshold is not None:
            result['ClusterFallbackThreshold'] = self.cluster_fallback_threshold
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms
        if self.cluster_threshold_type is not None:
            result['ClusterThresholdType'] = self.cluster_threshold_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.cluster_estimated_max_qps is not None:
            result['ClusterEstimatedMaxQps'] = self.cluster_estimated_max_qps
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.warm_up_period_sec is not None:
            result['WarmUpPeriodSec'] = self.warm_up_period_sec
        if self.cluster_fallback_strategy is not None:
            result['ClusterFallbackStrategy'] = self.cluster_fallback_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('ClusterFallbackThreshold') is not None:
            self.cluster_fallback_threshold = m.get('ClusterFallbackThreshold')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')
        if m.get('ClusterThresholdType') is not None:
            self.cluster_threshold_type = m.get('ClusterThresholdType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ClusterEstimatedMaxQps') is not None:
            self.cluster_estimated_max_qps = m.get('ClusterEstimatedMaxQps')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('WarmUpPeriodSec') is not None:
            self.warm_up_period_sec = m.get('WarmUpPeriodSec')
        if m.get('ClusterFallbackStrategy') is not None:
            self.cluster_fallback_strategy = m.get('ClusterFallbackStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyFlowRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ModifyFlowRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ModifyFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyFlowRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFlowRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHotParamRuleRequest(TeaModel):
    def __init__(
        self,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
        rule_id: int = None,
        param_idx: int = None,
        stat_duration_sec: int = None,
        control_behavior: int = None,
        burst_count: int = None,
        max_queueing_time_ms: int = None,
        ahas_region_id: str = None,
    ):
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable
        self.rule_id = rule_id
        self.param_idx = param_idx
        self.stat_duration_sec = stat_duration_sec
        self.control_behavior = control_behavior
        self.burst_count = burst_count
        self.max_queueing_time_ms = max_queueing_time_ms
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ModifyHotParamRuleResponseBodyDataParamFlowItemList(TeaModel):
    def __init__(
        self,
        item_value: str = None,
        item_type: str = None,
        threshold: float = None,
    ):
        self.item_value = item_value
        self.item_type = item_type
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ModifyHotParamRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        param_idx: int = None,
        namespace: str = None,
        param_flow_item_list: List[ModifyHotParamRuleResponseBodyDataParamFlowItemList] = None,
        stat_duration_sec: int = None,
        burst_count: int = None,
        rule_id: int = None,
        resource: str = None,
        app_name: str = None,
        max_queueing_time_ms: int = None,
        control_behavior: int = None,
        metric_type: int = None,
        threshold: float = None,
        enable: bool = None,
    ):
        self.param_idx = param_idx
        self.namespace = namespace
        self.param_flow_item_list = param_flow_item_list
        self.stat_duration_sec = stat_duration_sec
        self.burst_count = burst_count
        self.rule_id = rule_id
        self.resource = resource
        self.app_name = app_name
        self.max_queueing_time_ms = max_queueing_time_ms
        self.control_behavior = control_behavior
        self.metric_type = metric_type
        self.threshold = threshold
        self.enable = enable

    def validate(self):
        if self.param_flow_item_list:
            for k in self.param_flow_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_idx is not None:
            result['ParamIdx'] = self.param_idx
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['ParamFlowItemList'] = []
        if self.param_flow_item_list is not None:
            for k in self.param_flow_item_list:
                result['ParamFlowItemList'].append(k.to_map() if k else None)
        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec
        if self.burst_count is not None:
            result['BurstCount'] = self.burst_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms
        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamIdx') is not None:
            self.param_idx = m.get('ParamIdx')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.param_flow_item_list = []
        if m.get('ParamFlowItemList') is not None:
            for k in m.get('ParamFlowItemList'):
                temp_model = ModifyHotParamRuleResponseBodyDataParamFlowItemList()
                self.param_flow_item_list.append(temp_model.from_map(k))
        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')
        if m.get('BurstCount') is not None:
            self.burst_count = m.get('BurstCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')
        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyHotParamRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ModifyHotParamRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ModifyHotParamRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyHotParamRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHotParamRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHotParamRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIsolationRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        relation_strategy: int = None,
        threshold: float = None,
        limit_origin: str = None,
        ref_resource: str = None,
        ahas_region_id: str = None,
    ):
        self.rule_id = rule_id
        self.relation_strategy = relation_strategy
        self.threshold = threshold
        self.limit_origin = limit_origin
        self.ref_resource = ref_resource
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ModifyIsolationRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        relation_strategy: int = None,
        resource: str = None,
        app_name: str = None,
        ref_resource: str = None,
        namespace: str = None,
        limit_origin: str = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.relation_strategy = relation_strategy
        self.resource = resource
        self.app_name = app_name
        self.ref_resource = ref_resource
        self.namespace = namespace
        self.limit_origin = limit_origin
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_strategy is not None:
            result['RelationStrategy'] = self.relation_strategy
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ref_resource is not None:
            result['RefResource'] = self.ref_resource
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.limit_origin is not None:
            result['LimitOrigin'] = self.limit_origin
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationStrategy') is not None:
            self.relation_strategy = m.get('RelationStrategy')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RefResource') is not None:
            self.ref_resource = m.get('RefResource')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('LimitOrigin') is not None:
            self.limit_origin = m.get('LimitOrigin')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyIsolationRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ModifyIsolationRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ModifyIsolationRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyIsolationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIsolationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyIsolationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySystemRuleRequest(TeaModel):
    def __init__(
        self,
        threshold: float = None,
        rule_id: int = None,
        ahas_region_id: str = None,
    ):
        self.threshold = threshold
        self.rule_id = rule_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class ModifySystemRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        metric_type: int = None,
        threshold: float = None,
        rule_id: int = None,
        enable: bool = None,
    ):
        self.metric_type = metric_type
        self.threshold = threshold
        self.rule_id = rule_id
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifySystemRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ModifySystemRuleResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ModifySystemRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySystemRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySystemRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySystemRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAhasServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenAhasServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class OpenAhasServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenAhasServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenAhasServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageableQueryExperimentTaskByExperimentIdRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        page: int = None,
        size: int = None,
        namespace: str = None,
        region_id: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.page = page
        self.size = size
        self.namespace = namespace
        self.region_id = region_id
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfoSchedulerConfig(TeaModel):
    def __init__(
        self,
        fixed_time: str = None,
        cron_expression: str = None,
    ):
        self.fixed_time = fixed_time
        self.cron_expression = cron_expression

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_time is not None:
            result['FixedTime'] = self.fixed_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedTime') is not None:
            self.fixed_time = m.get('FixedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        return self


class PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfo(TeaModel):
    def __init__(
        self,
        scheduler_config: PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfoSchedulerConfig = None,
    ):
        self.scheduler_config = scheduler_config

    def validate(self):
        if self.scheduler_config:
            self.scheduler_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduler_config is not None:
            result['SchedulerConfig'] = self.scheduler_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchedulerConfig') is not None:
            temp_model = PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfoSchedulerConfig()
            self.scheduler_config = temp_model.from_map(m['SchedulerConfig'])
        return self


class PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksCreator(TeaModel):
    def __init__(
        self,
        sub_user_id: str = None,
        user_id: str = None,
    ):
        self.sub_user_id = sub_user_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasks(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        result: str = None,
        state: str = None,
        current_phase: str = None,
        experiment_id: str = None,
        message: str = None,
        task_id: str = None,
        experiment_name: str = None,
        ext_info: PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfo = None,
        creator: PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksCreator = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.result = result
        self.state = state
        self.current_phase = current_phase
        self.experiment_id = experiment_id
        self.message = message
        self.task_id = task_id
        self.experiment_name = experiment_name
        self.ext_info = ext_info
        self.creator = creator

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()
        if self.creator:
            self.creator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.result is not None:
            result['Result'] = self.result
        if self.state is not None:
            result['State'] = self.state
        if self.current_phase is not None:
            result['CurrentPhase'] = self.current_phase
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.experiment_name is not None:
            result['ExperimentName'] = self.experiment_name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurrentPhase') is not None:
            self.current_phase = m.get('CurrentPhase')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ExperimentName') is not None:
            self.experiment_name = m.get('ExperimentName')
        if m.get('ExtInfo') is not None:
            temp_model = PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        if m.get('Creator') is not None:
            temp_model = PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasksCreator()
            self.creator = temp_model.from_map(m['Creator'])
        return self


class PageableQueryExperimentTaskByExperimentIdResponseBody(TeaModel):
    def __init__(
        self,
        pages: int = None,
        experiment_tasks: List[PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasks] = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        current_page: int = None,
        total: int = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.pages = pages
        self.experiment_tasks = experiment_tasks
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.current_page = current_page
        self.total = total
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.experiment_tasks:
            for k in self.experiment_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pages is not None:
            result['Pages'] = self.pages
        result['ExperimentTasks'] = []
        if self.experiment_tasks is not None:
            for k in self.experiment_tasks:
                result['ExperimentTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total is not None:
            result['Total'] = self.total
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.experiment_tasks = []
        if m.get('ExperimentTasks') is not None:
            for k in m.get('ExperimentTasks'):
                temp_model = PageableQueryExperimentTaskByExperimentIdResponseBodyExperimentTasks()
                self.experiment_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageableQueryExperimentTaskByExperimentIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PageableQueryExperimentTaskByExperimentIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PageableQueryExperimentTaskByExperimentIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageableQueryUserExperimentRequest(TeaModel):
    def __init__(
        self,
        search_key: str = None,
        state: str = None,
        page: int = None,
        size: int = None,
        namespace: str = None,
        ahas_region_id: str = None,
        workspace_id: str = None,
        region_id: str = None,
        tags: List[str] = None,
        results: List[str] = None,
    ):
        self.search_key = search_key
        self.state = state
        self.page = page
        self.size = size
        self.namespace = namespace
        self.ahas_region_id = ahas_region_id
        self.workspace_id = workspace_id
        self.region_id = region_id
        self.tags = tags
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.state is not None:
            result['State'] = self.state
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class PageableQueryUserExperimentResponseBodyExperimentList(TeaModel):
    def __init__(
        self,
        permission: int = None,
        result: str = None,
        state: str = None,
        create_time: int = None,
        experiment_id: str = None,
        tags: List[str] = None,
        mini_apps: List[str] = None,
        name: str = None,
        creator: str = None,
    ):
        self.permission = permission
        self.result = result
        self.state = state
        self.create_time = create_time
        self.experiment_id = experiment_id
        self.tags = tags
        self.mini_apps = mini_apps
        self.name = name
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.result is not None:
            result['Result'] = self.result
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.mini_apps is not None:
            result['MiniApps'] = self.mini_apps
        if self.name is not None:
            result['Name'] = self.name
        if self.creator is not None:
            result['Creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MiniApps') is not None:
            self.mini_apps = m.get('MiniApps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        return self


class PageableQueryUserExperimentResponseBody(TeaModel):
    def __init__(
        self,
        pages: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        current_page: int = None,
        total: int = None,
        experiment_list: List[PageableQueryUserExperimentResponseBodyExperimentList] = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.pages = pages
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.current_page = current_page
        self.total = total
        self.experiment_list = experiment_list
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.experiment_list:
            for k in self.experiment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total is not None:
            result['Total'] = self.total
        result['ExperimentList'] = []
        if self.experiment_list is not None:
            for k in self.experiment_list:
                result['ExperimentList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.experiment_list = []
        if m.get('ExperimentList') is not None:
            for k in m.get('ExperimentList'):
                temp_model = PageableQueryUserExperimentResponseBodyExperimentList()
                self.experiment_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageableQueryUserExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PageableQueryUserExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PageableQueryUserExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushExperimentTaskRequest(TeaModel):
    def __init__(
        self,
        experiment_task_id: str = None,
        name_space: str = None,
        ahas_region_id: str = None,
    ):
        self.experiment_task_id = experiment_task_id
        self.name_space = name_space
        self.ahas_region_id = ahas_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_task_id is not None:
            result['ExperimentTaskId'] = self.experiment_task_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentTaskId') is not None:
            self.experiment_task_id = m.get('ExperimentTaskId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        return self


class PushExperimentTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushExperimentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushExperimentTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushExperimentTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        name: str = None,
        description: str = None,
        name_space: str = None,
        experiment_id: str = None,
        ahas_region_id: str = None,
        tags: List[str] = None,
    ):
        self.definition = definition
        self.name = name
        self.description = description
        self.name_space = name_space
        self.experiment_id = experiment_id
        self.ahas_region_id = ahas_region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentBasicInfoRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name_space: str = None,
        name: str = None,
        description: str = None,
        ahas_region_id: str = None,
        tags: List[str] = None,
    ):
        self.experiment_id = experiment_id
        self.name_space = name_space
        self.name = name
        self.description = description
        self.ahas_region_id = ahas_region_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.ahas_region_id is not None:
            result['AhasRegionId'] = self.ahas_region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AhasRegionId') is not None:
            self.ahas_region_id = m.get('AhasRegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateExperimentBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateExperimentBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExperimentBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


