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
        # Set the value to true if scale-outs are allowed.
        self.accept_eula = accept_eula
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the instance group to which the application is deployed.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The relationship among the conditions that trigger a scale-in.
        # 
        # - OR: one of the conditions
        # 
        # - AND: all conditions
        self.in_condition = in_condition
        # The CPU utilization that triggers a scale-in.
        self.in_cpu = in_cpu
        # The duration in which the metric threshold is exceeded. Unit: minutes.
        self.in_duration = in_duration
        # Specifies whether to allow scale-ins.
        # 
        # - true: allows scale-ins.
        # 
        # - false: does not allow scale-ins.
        self.in_enable = in_enable
        # The minimum number of instances that must be retained in each group when a scale-in is performed.
        self.in_instance_num = in_instance_num
        # The system load that triggers a scale-in.
        self.in_load = in_load
        # The minimum service latency that triggers a scale-in. The lower limit is 0. Unit: milliseconds.
        self.in_rt = in_rt
        # The number of instances that are removed during each scale-in.
        self.in_step = in_step
        # The key pair that is used to log on to the instance. This parameter takes effect only if you choose to create instances based on the specifications of an existing instance during a scale-out.
        self.key_pair_name = key_pair_name
        # The multi-zone scaling policy. Valid values:
        # 
        # - PRIORITY: The vSwitch that is first selected has the highest priority.
        # 
        # - BALANCE: This policy evenly distributes instances across zones in which the vSwitches reside.
        self.multi_az_policy = multi_az_policy
        # The CPU utilization that triggers a scale-out.
        self.out_cpu = out_cpu
        # The relationship among the conditions that trigger a scale-out.
        # 
        # - OR: one of the conditions
        # 
        # - AND: all conditions
        self.out_condition = out_condition
        # The duration in which the metric threshold is exceeded. Unit: minutes.
        self.out_duration = out_duration
        # Specifies whether to allow scale-outs.
        self.out_enable = out_enable
        # The maximum number of instances in each group when a scale-out is performed.
        self.out_instance_num = out_instance_num
        # The system load that triggers a scale-out.
        self.out_load = out_load
        # The minimum service latency that triggers a scale-out. The lower limit is 0. Unit: milliseconds.
        self.out_rt = out_rt
        # The number of instances that are added during each scale-out.
        self.out_step = out_step
        # The password that is used to log on to the instance. This parameter takes effect only if you choose to create instances based on the specifications of an existing instance during a scale-out.
        self.password = password
        # The source of the instance to be added during a scale-out. Valid values:
        # 
        # - NEW: elastic resources
        # 
        # - AVAILABLE: existing resources If you prefer existing resources to elastic resources, set this parameter to AVAILABLE_FIRST.
        # 
        # If you set this parameter to NEW or AVAILABLE_FIRST, you must specify the auto-scaling parameters. If you set this parameter to NEW, instances are created based on a launch template or the specifications of an existing instance.
        self.resource_from = resource_from
        # The instance handling mode during a scale-in. Valid values:
        # 
        # - release: When a scale-in is performed, instances that are no longer used are released.
        # 
        # - recycle: When a scale-in is performed, instances that are no longer used are stopped and reclaimed.
        self.scaling_policy = scaling_policy
        # The ID of the launch template that is used to create instances during a scale-out. This parameter takes effect only if you set the OutEnable parameter to true. This parameter takes precedence over the TemplateInstanceId parameter.
        self.template_id = template_id
        # The ID of the instance whose specifications are used to create instances during a scale-out. This parameter is valid only when you set the OutEnable parameter to true.
        self.template_instance_id = template_instance_id
        # The name of the instance whose specifications are used to create instances during a scale-out. This parameter takes effect only if you specify the TemplateInstanceId parameter.
        self.template_instance_name = template_instance_name
        # The version of the launch template that is used to create instances during a scale-out. This parameter takes effect only if you set the OutEnable parameter to true. To use the default template version, set this parameter to `-1`. Otherwise, set this parameter to the version that you want to use.
        self.template_version = template_version
        # The IDs of the vSwitches that are associated with the VPC. Separate multiple IDs with commas (,).
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC) that is associated with the instances created based on a launch template or the specifications of an existing instance.
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

