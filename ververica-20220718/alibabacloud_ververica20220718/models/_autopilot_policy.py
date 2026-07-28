# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class AutopilotPolicy(DaraModel):
    def __init__(
        self,
        advanced_rules: main_models.AutopilotPolicyAdvancedRules = None,
        limits: main_models.AutopilotPolicyLimits = None,
        scale_down_rules: main_models.AutopilotPolicyScaleDownRules = None,
        scale_up_rules: main_models.AutopilotPolicyScaleUpRules = None,
        silent_period_config: main_models.AutopilotPolicySilentPeriodConfig = None,
    ):
        self.advanced_rules = advanced_rules
        self.limits = limits
        self.scale_down_rules = scale_down_rules
        self.scale_up_rules = scale_up_rules
        self.silent_period_config = silent_period_config

    def validate(self):
        if self.advanced_rules:
            self.advanced_rules.validate()
        if self.limits:
            self.limits.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()
        if self.silent_period_config:
            self.silent_period_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_rules is not None:
            result['advancedRules'] = self.advanced_rules.to_map()

        if self.limits is not None:
            result['limits'] = self.limits.to_map()

        if self.scale_down_rules is not None:
            result['scaleDownRules'] = self.scale_down_rules.to_map()

        if self.scale_up_rules is not None:
            result['scaleUpRules'] = self.scale_up_rules.to_map()

        if self.silent_period_config is not None:
            result['silentPeriodConfig'] = self.silent_period_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedRules') is not None:
            temp_model = main_models.AutopilotPolicyAdvancedRules()
            self.advanced_rules = temp_model.from_map(m.get('advancedRules'))

        if m.get('limits') is not None:
            temp_model = main_models.AutopilotPolicyLimits()
            self.limits = temp_model.from_map(m.get('limits'))

        if m.get('scaleDownRules') is not None:
            temp_model = main_models.AutopilotPolicyScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m.get('scaleDownRules'))

        if m.get('scaleUpRules') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m.get('scaleUpRules'))

        if m.get('silentPeriodConfig') is not None:
            temp_model = main_models.AutopilotPolicySilentPeriodConfig()
            self.silent_period_config = temp_model.from_map(m.get('silentPeriodConfig'))

        return self

class AutopilotPolicySilentPeriodConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        silent_periods: List[main_models.AutopilotPolicySilentPeriodConfigSilentPeriods] = None,
    ):
        self.enabled = enabled
        self.silent_periods = silent_periods

    def validate(self):
        if self.silent_periods:
            for v1 in self.silent_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['silentPeriods'] = []
        if self.silent_periods is not None:
            for k1 in self.silent_periods:
                result['silentPeriods'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.silent_periods = []
        if m.get('silentPeriods') is not None:
            for k1 in m.get('silentPeriods'):
                temp_model = main_models.AutopilotPolicySilentPeriodConfigSilentPeriods()
                self.silent_periods.append(temp_model.from_map(k1))

        return self

class AutopilotPolicySilentPeriodConfigSilentPeriods(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        level: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.level is not None:
            result['level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('level') is not None:
            self.level = m.get('level')

        return self

class AutopilotPolicyScaleUpRules(DaraModel):
    def __init__(
        self,
        delay_rule: main_models.AutopilotPolicyScaleUpRulesDelayRule = None,
        gc_rule: main_models.AutopilotPolicyScaleUpRulesGcRule = None,
        memory_scale_up_rule: main_models.AutopilotPolicyScaleUpRulesMemoryScaleUpRule = None,
        oom_scale_up_rule: main_models.AutopilotPolicyScaleUpRulesOomScaleUpRule = None,
        slot_busy_scale_up_rule: main_models.AutopilotPolicyScaleUpRulesSlotBusyScaleUpRule = None,
    ):
        self.delay_rule = delay_rule
        self.gc_rule = gc_rule
        self.memory_scale_up_rule = memory_scale_up_rule
        self.oom_scale_up_rule = oom_scale_up_rule
        self.slot_busy_scale_up_rule = slot_busy_scale_up_rule

    def validate(self):
        if self.delay_rule:
            self.delay_rule.validate()
        if self.gc_rule:
            self.gc_rule.validate()
        if self.memory_scale_up_rule:
            self.memory_scale_up_rule.validate()
        if self.oom_scale_up_rule:
            self.oom_scale_up_rule.validate()
        if self.slot_busy_scale_up_rule:
            self.slot_busy_scale_up_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_rule is not None:
            result['delayRule'] = self.delay_rule.to_map()

        if self.gc_rule is not None:
            result['gcRule'] = self.gc_rule.to_map()

        if self.memory_scale_up_rule is not None:
            result['memoryScaleUpRule'] = self.memory_scale_up_rule.to_map()

        if self.oom_scale_up_rule is not None:
            result['oomScaleUpRule'] = self.oom_scale_up_rule.to_map()

        if self.slot_busy_scale_up_rule is not None:
            result['slotBusyScaleUpRule'] = self.slot_busy_scale_up_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delayRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRulesDelayRule()
            self.delay_rule = temp_model.from_map(m.get('delayRule'))

        if m.get('gcRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRulesGcRule()
            self.gc_rule = temp_model.from_map(m.get('gcRule'))

        if m.get('memoryScaleUpRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRulesMemoryScaleUpRule()
            self.memory_scale_up_rule = temp_model.from_map(m.get('memoryScaleUpRule'))

        if m.get('oomScaleUpRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRulesOomScaleUpRule()
            self.oom_scale_up_rule = temp_model.from_map(m.get('oomScaleUpRule'))

        if m.get('slotBusyScaleUpRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleUpRulesSlotBusyScaleUpRule()
            self.slot_busy_scale_up_rule = temp_model.from_map(m.get('slotBusyScaleUpRule'))

        return self

class AutopilotPolicyScaleUpRulesSlotBusyScaleUpRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        slot_busy_scale_up_sample_interval: str = None,
        slot_busy_scale_up_threshold: float = None,
    ):
        self.enabled = enabled
        self.slot_busy_scale_up_sample_interval = slot_busy_scale_up_sample_interval
        self.slot_busy_scale_up_threshold = slot_busy_scale_up_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.slot_busy_scale_up_sample_interval is not None:
            result['slotBusyScaleUpSampleInterval'] = self.slot_busy_scale_up_sample_interval

        if self.slot_busy_scale_up_threshold is not None:
            result['slotBusyScaleUpThreshold'] = self.slot_busy_scale_up_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('slotBusyScaleUpSampleInterval') is not None:
            self.slot_busy_scale_up_sample_interval = m.get('slotBusyScaleUpSampleInterval')

        if m.get('slotBusyScaleUpThreshold') is not None:
            self.slot_busy_scale_up_threshold = m.get('slotBusyScaleUpThreshold')

        return self

class AutopilotPolicyScaleUpRulesOomScaleUpRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class AutopilotPolicyScaleUpRulesMemoryScaleUpRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        mem_usage_scale_up_threshold: float = None,
    ):
        self.enabled = enabled
        self.mem_usage_scale_up_threshold = mem_usage_scale_up_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.mem_usage_scale_up_threshold is not None:
            result['memUsageScaleUpThreshold'] = self.mem_usage_scale_up_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('memUsageScaleUpThreshold') is not None:
            self.mem_usage_scale_up_threshold = m.get('memUsageScaleUpThreshold')

        return self

class AutopilotPolicyScaleUpRulesGcRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        gc_sample_interval: str = None,
        gc_time_ratio_threshold: float = None,
    ):
        self.enabled = enabled
        self.gc_sample_interval = gc_sample_interval
        self.gc_time_ratio_threshold = gc_time_ratio_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.gc_sample_interval is not None:
            result['gcSampleInterval'] = self.gc_sample_interval

        if self.gc_time_ratio_threshold is not None:
            result['gcTimeRatioThreshold'] = self.gc_time_ratio_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('gcSampleInterval') is not None:
            self.gc_sample_interval = m.get('gcSampleInterval')

        if m.get('gcTimeRatioThreshold') is not None:
            self.gc_time_ratio_threshold = m.get('gcTimeRatioThreshold')

        return self

class AutopilotPolicyScaleUpRulesDelayRule(DaraModel):
    def __init__(
        self,
        delay_sample_interval: str = None,
        delay_threshold: str = None,
        enabled: bool = None,
    ):
        self.delay_sample_interval = delay_sample_interval
        self.delay_threshold = delay_threshold
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_sample_interval is not None:
            result['delaySampleInterval'] = self.delay_sample_interval

        if self.delay_threshold is not None:
            result['delayThreshold'] = self.delay_threshold

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delaySampleInterval') is not None:
            self.delay_sample_interval = m.get('delaySampleInterval')

        if m.get('delayThreshold') is not None:
            self.delay_threshold = m.get('delayThreshold')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class AutopilotPolicyScaleDownRules(DaraModel):
    def __init__(
        self,
        memory_scale_down_rule: main_models.AutopilotPolicyScaleDownRulesMemoryScaleDownRule = None,
        slot_busy_scale_down_rule: main_models.AutopilotPolicyScaleDownRulesSlotBusyScaleDownRule = None,
    ):
        self.memory_scale_down_rule = memory_scale_down_rule
        self.slot_busy_scale_down_rule = slot_busy_scale_down_rule

    def validate(self):
        if self.memory_scale_down_rule:
            self.memory_scale_down_rule.validate()
        if self.slot_busy_scale_down_rule:
            self.slot_busy_scale_down_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_scale_down_rule is not None:
            result['memoryScaleDownRule'] = self.memory_scale_down_rule.to_map()

        if self.slot_busy_scale_down_rule is not None:
            result['slotBusyScaleDownRule'] = self.slot_busy_scale_down_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryScaleDownRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleDownRulesMemoryScaleDownRule()
            self.memory_scale_down_rule = temp_model.from_map(m.get('memoryScaleDownRule'))

        if m.get('slotBusyScaleDownRule') is not None:
            temp_model = main_models.AutopilotPolicyScaleDownRulesSlotBusyScaleDownRule()
            self.slot_busy_scale_down_rule = temp_model.from_map(m.get('slotBusyScaleDownRule'))

        return self

class AutopilotPolicyScaleDownRulesSlotBusyScaleDownRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        slot_busy_scale_down_sample_interval: str = None,
        slot_busy_scale_down_threshold: float = None,
    ):
        self.enabled = enabled
        self.slot_busy_scale_down_sample_interval = slot_busy_scale_down_sample_interval
        self.slot_busy_scale_down_threshold = slot_busy_scale_down_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.slot_busy_scale_down_sample_interval is not None:
            result['slotBusyScaleDownSampleInterval'] = self.slot_busy_scale_down_sample_interval

        if self.slot_busy_scale_down_threshold is not None:
            result['slotBusyScaleDownThreshold'] = self.slot_busy_scale_down_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('slotBusyScaleDownSampleInterval') is not None:
            self.slot_busy_scale_down_sample_interval = m.get('slotBusyScaleDownSampleInterval')

        if m.get('slotBusyScaleDownThreshold') is not None:
            self.slot_busy_scale_down_threshold = m.get('slotBusyScaleDownThreshold')

        return self

class AutopilotPolicyScaleDownRulesMemoryScaleDownRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        mem_usage_scale_down_sample_interval: str = None,
        mem_usage_scale_down_threshold: float = None,
    ):
        self.enabled = enabled
        self.mem_usage_scale_down_sample_interval = mem_usage_scale_down_sample_interval
        self.mem_usage_scale_down_threshold = mem_usage_scale_down_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.mem_usage_scale_down_sample_interval is not None:
            result['memUsageScaleDownSampleInterval'] = self.mem_usage_scale_down_sample_interval

        if self.mem_usage_scale_down_threshold is not None:
            result['memUsageScaleDownThreshold'] = self.mem_usage_scale_down_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('memUsageScaleDownSampleInterval') is not None:
            self.mem_usage_scale_down_sample_interval = m.get('memUsageScaleDownSampleInterval')

        if m.get('memUsageScaleDownThreshold') is not None:
            self.mem_usage_scale_down_threshold = m.get('memUsageScaleDownThreshold')

        return self

class AutopilotPolicyLimits(DaraModel):
    def __init__(
        self,
        cool_down_minutes: int = None,
        job_max_cpu: float = None,
        job_max_memory: str = None,
        job_max_parallelism: int = None,
        job_min_parallelism: int = None,
    ):
        self.cool_down_minutes = cool_down_minutes
        self.job_max_cpu = job_max_cpu
        self.job_max_memory = job_max_memory
        self.job_max_parallelism = job_max_parallelism
        self.job_min_parallelism = job_min_parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cool_down_minutes is not None:
            result['coolDownMinutes'] = self.cool_down_minutes

        if self.job_max_cpu is not None:
            result['jobMaxCpu'] = self.job_max_cpu

        if self.job_max_memory is not None:
            result['jobMaxMemory'] = self.job_max_memory

        if self.job_max_parallelism is not None:
            result['jobMaxParallelism'] = self.job_max_parallelism

        if self.job_min_parallelism is not None:
            result['jobMinParallelism'] = self.job_min_parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coolDownMinutes') is not None:
            self.cool_down_minutes = m.get('coolDownMinutes')

        if m.get('jobMaxCpu') is not None:
            self.job_max_cpu = m.get('jobMaxCpu')

        if m.get('jobMaxMemory') is not None:
            self.job_max_memory = m.get('jobMaxMemory')

        if m.get('jobMaxParallelism') is not None:
            self.job_max_parallelism = m.get('jobMaxParallelism')

        if m.get('jobMinParallelism') is not None:
            self.job_min_parallelism = m.get('jobMinParallelism')

        return self



class AutopilotPolicyAdvancedRules(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        parameters: Dict[str, str] = None,
    ):
        self.enabled = enabled
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

