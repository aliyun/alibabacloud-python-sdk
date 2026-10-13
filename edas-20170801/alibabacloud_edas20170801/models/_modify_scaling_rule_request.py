# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScalingRuleRequest(DaraModel):
    def __init__(
        self,
        accept_eula: bool = None,
        app_id: str = None,
        group_id: str = None,
        in_condition: str = None,
        in_cpu: int = None,
        in_duration: int = None,
        in_enable: bool = None,
        in_instance_num: int = None,
        in_load: int = None,
        in_rt: int = None,
        in_step: int = None,
        key_pair_name: str = None,
        multi_az_policy: str = None,
        out_cpu: int = None,
        out_condition: str = None,
        out_duration: int = None,
        out_enable: bool = None,
        out_instance_num: int = None,
        out_load: int = None,
        out_rt: int = None,
        out_step: int = None,
        password: str = None,
        resource_from: str = None,
        scaling_policy: str = None,
        template_id: str = None,
        template_instance_id: str = None,
        template_instance_name: str = None,
        template_version: int = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # Must be set to true if auto scaling is used.
        self.accept_eula = accept_eula
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The deployment group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The trigger condition. Valid values:
        # 
        # - OR: Any condition.
        # - AND: All conditions.
        self.in_condition = in_condition
        # The trigger metric: CPU utilization.
        self.in_cpu = in_cpu
        # The duration, in minutes.
        self.in_duration = in_duration
        # Specifies whether to include the scale-in rule. Valid values:
        # 
        # - true: Included.
        # - false: Not included.
        self.in_enable = in_enable
        # The minimum number of instances to retain when the group scales in.
        self.in_instance_num = in_instance_num
        # The trigger metric: system load.
        self.in_load = in_load
        # The trigger metric: service latency. Unit: milliseconds. Minimum value: 0.
        self.in_rt = in_rt
        # The number of instances to scale in at a time.
        self.in_step = in_step
        # The name of the logon key pair for the instance. This parameter is valid only when the existing instance rule is used for auto scaling.
        self.key_pair_name = key_pair_name
        # The multi-zone scaling policy for auto scaling. Valid values:
        # - PRIORITY: Priority policy.
        # - BALANCE: Balanced distribution policy.
        self.multi_az_policy = multi_az_policy
        # The trigger metric: CPU utilization.
        self.out_cpu = out_cpu
        # The trigger condition. Valid values:
        # 
        # - OR: Any condition.
        # - AND: All conditions.
        self.out_condition = out_condition
        # The duration, in minutes.
        self.out_duration = out_duration
        # Specifies whether to include the scale-out rule.
        self.out_enable = out_enable
        # The maximum number of instances when the group scales out.
        self.out_instance_num = out_instance_num
        # The trigger metric: system load.
        self.out_load = out_load
        # The trigger metric: service latency. Unit: milliseconds. Minimum value: 0.
        self.out_rt = out_rt
        # The number of instances to scale out at a time.
        self.out_step = out_step
        # The logon password of the instance. This parameter is valid only when the existing instance rule is used for auto scaling.
        self.password = password
        # The source of instances for scale-out. Valid values:
        # - NEW: Elastic resources.
        # - AVAILABLE: Existing resources. To prioritize existing resources, use AVAILABLE_FIRST.
        # 
        # If you set this parameter to NEW or AVAILABLE_FIRST, you must specify auto scaling parameters. Auto scaling includes two modes: launch template and existing instance rule.
        self.resource_from = resource_from
        # The reclamation mode for scale-in. Valid values:
        # - release: Release mode.
        # - recycle: Stop and reclaim mode.
        self.scaling_policy = scaling_policy
        # The launch template ID for auto scaling. This parameter is valid only when OutEnable is set to true, and it has a higher priority than TemplateInstanceId.
        self.template_id = template_id
        # The instance ID for the existing instance rule of auto scaling. This parameter is valid only when OutEnable is set to true.
        self.template_instance_id = template_instance_id
        # The instance name for the existing instance rule of auto scaling. This parameter is valid only when TemplateInstanceId is specified.
        self.template_instance_name = template_instance_name
        # The launch template version for auto scaling. This parameter is valid only when OutEnable is set to true. Set this parameter to `-1` to use the default template version, or set it to a specific version number.
        self.template_version = template_version
        # The list of vSwitch IDs in the VPC. Separate multiple IDs with commas (,).
        self.v_switch_ids = v_switch_ids
        # The VPC ID associated with the launch template or existing instance rule for auto scaling.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_eula is not None:
            result['AcceptEULA'] = self.accept_eula

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.in_condition is not None:
            result['InCondition'] = self.in_condition

        if self.in_cpu is not None:
            result['InCpu'] = self.in_cpu

        if self.in_duration is not None:
            result['InDuration'] = self.in_duration

        if self.in_enable is not None:
            result['InEnable'] = self.in_enable

        if self.in_instance_num is not None:
            result['InInstanceNum'] = self.in_instance_num

        if self.in_load is not None:
            result['InLoad'] = self.in_load

        if self.in_rt is not None:
            result['InRT'] = self.in_rt

        if self.in_step is not None:
            result['InStep'] = self.in_step

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.multi_az_policy is not None:
            result['MultiAzPolicy'] = self.multi_az_policy

        if self.out_cpu is not None:
            result['OutCPU'] = self.out_cpu

        if self.out_condition is not None:
            result['OutCondition'] = self.out_condition

        if self.out_duration is not None:
            result['OutDuration'] = self.out_duration

        if self.out_enable is not None:
            result['OutEnable'] = self.out_enable

        if self.out_instance_num is not None:
            result['OutInstanceNum'] = self.out_instance_num

        if self.out_load is not None:
            result['OutLoad'] = self.out_load

        if self.out_rt is not None:
            result['OutRT'] = self.out_rt

        if self.out_step is not None:
            result['OutStep'] = self.out_step

        if self.password is not None:
            result['Password'] = self.password

        if self.resource_from is not None:
            result['ResourceFrom'] = self.resource_from

        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_instance_id is not None:
            result['TemplateInstanceId'] = self.template_instance_id

        if self.template_instance_name is not None:
            result['TemplateInstanceName'] = self.template_instance_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptEULA') is not None:
            self.accept_eula = m.get('AcceptEULA')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InCondition') is not None:
            self.in_condition = m.get('InCondition')

        if m.get('InCpu') is not None:
            self.in_cpu = m.get('InCpu')

        if m.get('InDuration') is not None:
            self.in_duration = m.get('InDuration')

        if m.get('InEnable') is not None:
            self.in_enable = m.get('InEnable')

        if m.get('InInstanceNum') is not None:
            self.in_instance_num = m.get('InInstanceNum')

        if m.get('InLoad') is not None:
            self.in_load = m.get('InLoad')

        if m.get('InRT') is not None:
            self.in_rt = m.get('InRT')

        if m.get('InStep') is not None:
            self.in_step = m.get('InStep')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('MultiAzPolicy') is not None:
            self.multi_az_policy = m.get('MultiAzPolicy')

        if m.get('OutCPU') is not None:
            self.out_cpu = m.get('OutCPU')

        if m.get('OutCondition') is not None:
            self.out_condition = m.get('OutCondition')

        if m.get('OutDuration') is not None:
            self.out_duration = m.get('OutDuration')

        if m.get('OutEnable') is not None:
            self.out_enable = m.get('OutEnable')

        if m.get('OutInstanceNum') is not None:
            self.out_instance_num = m.get('OutInstanceNum')

        if m.get('OutLoad') is not None:
            self.out_load = m.get('OutLoad')

        if m.get('OutRT') is not None:
            self.out_rt = m.get('OutRT')

        if m.get('OutStep') is not None:
            self.out_step = m.get('OutStep')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ResourceFrom') is not None:
            self.resource_from = m.get('ResourceFrom')

        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateInstanceId') is not None:
            self.template_instance_id = m.get('TemplateInstanceId')

        if m.get('TemplateInstanceName') is not None:
            self.template_instance_name = m.get('TemplateInstanceName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

