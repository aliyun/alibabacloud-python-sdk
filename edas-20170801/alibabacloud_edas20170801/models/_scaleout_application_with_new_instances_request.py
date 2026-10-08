# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleoutApplicationWithNewInstancesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cluster_id: str = None,
        group_id: str = None,
        instance_charge_period: int = None,
        instance_charge_period_unit: str = None,
        instance_charge_type: str = None,
        scaling_num: int = None,
        scaling_policy: str = None,
        template_id: str = None,
        template_instance_id: str = None,
        template_version: str = None,
    ):
        # The ID of the application that you want to scale out. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        self.app_id = app_id
        # Specifies whether to enable auto-renewal. This parameter takes effect only when the InstanceChargeType parameter is set to PrePaid. Valid values:
        # 
        # *   true: enables auto-renewal.
        # *   false: does not enable auto-renewal. This is the default value.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # 
        # *   If the InstanceChargePeriodUnit parameter is set to Week, the valid values of the AutoRenewPeriod parameter are 1, 2, and 3.
        # *   If the InstanceChargePeriodUnit parameter is set to Month, the valid values of the AutoRenewPeriod parameter are 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The ID of the cluster to which you want to add ECS instances. If the application and application instance group for the scale-out are specified, this parameter is ignored.
        self.cluster_id = cluster_id
        # The ID of the instance group that you want to scale out. You can call the ListDeployGroup operation to query the group ID. For more information, see [ListDeployGroup](https://help.aliyun.com/document_detail/62077.html).
        self.group_id = group_id
        # The duration of the subscription. The unit of the subscription duration is specified by the InstanceChargePeriodUnit parameter. This parameter takes effect only when the InstanceChargeType parameter is set to PrePaid.
        # 
        # *   If the InstanceChargePeriodUnit parameter is set to Week, the valid values of the InstanceChargePeriod parameter are 1, 2, 3, and 4.
        # *   If the InstanceChargePeriodUnit parameter is set to Month, the valid values of the InstanceChargePeriod parameter are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.instance_charge_period = instance_charge_period
        # The unit of the subscription period. Valid values:
        # 
        # *   Week: billed on a weekly basis.
        # *   Month: billed on a monthly basis. This is the default value.
        self.instance_charge_period_unit = instance_charge_period_unit
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go. This is the default value.
        self.instance_charge_type = instance_charge_type
        # The number of instances to be added for the scale-out.
        # 
        # This parameter is required.
        self.scaling_num = scaling_num
        # The instance reclaim mode of the scaling group. Valid values:
        # 
        # *   recycle: economical mode
        # *   release: release mode
        # 
        # For more information about how to remove instances from a specified scaling group, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The ID of the ECS instance launch template. You can call the DescribeLaunchTemplates operation to query the launch template ID. For more information, see [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        self.template_id = template_id
        # The ID of the existing ECS instance used for the scale-out. If this parameter is specified, the specifications and configurations of the specified ECS instance are used as a template to purchase new instances.
        self.template_instance_id = template_instance_id
        # The version of the ECS instance launch template. You can call the DescribeLaunchTemplateVersions operation to query the launch template version. For more information, see [DescribeLaunchTemplateVersions](https://help.aliyun.com/document_detail/73761.html).
        # 
        # > If you set this parameter to `-1`, the default launch template version is used.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_charge_period is not None:
            result['InstanceChargePeriod'] = self.instance_charge_period

        if self.instance_charge_period_unit is not None:
            result['InstanceChargePeriodUnit'] = self.instance_charge_period_unit

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.scaling_num is not None:
            result['ScalingNum'] = self.scaling_num

        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_instance_id is not None:
            result['TemplateInstanceId'] = self.template_instance_id

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceChargePeriod') is not None:
            self.instance_charge_period = m.get('InstanceChargePeriod')

        if m.get('InstanceChargePeriodUnit') is not None:
            self.instance_charge_period_unit = m.get('InstanceChargePeriodUnit')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('ScalingNum') is not None:
            self.scaling_num = m.get('ScalingNum')

        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateInstanceId') is not None:
            self.template_instance_id = m.get('TemplateInstanceId')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

