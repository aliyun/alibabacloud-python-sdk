# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        auto_renew_enabled: bool = None,
        client_token: str = None,
        name: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        remark: str = None,
        spec: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the Alibaba Cloud resource group.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The tags.
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        # Specifies whether to enable auto-renewal.
        self.auto_renew_enabled = auto_renew_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The name of the serverless resource group. The name can be a maximum of 128 characters in length and can contain letters, digits, and underscores (_). The name must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The subscription duration.
        self.payment_duration = payment_duration
        # The unit of the subscription duration. Valid values: Month and Year.
        self.payment_duration_unit = payment_duration_unit
        # The billing method of the serverless resource group. Valid values: PrePaid and PostPaid. The value PrePaid indicates the subscription billing method, and the value PostPaid indicates the pay-as-you-go billing method.
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The description of the serverless resource group. The description can be a maximum of 128 characters in length and can contain letters, digits, and underscores (_).
        self.remark = remark
        # The specifications of the serverless resource group. Unit: CU. This parameter is required only if you set the PaymentType parameter to PrePaid.
        self.spec = spec
        # The ID of the virtual private cloud (VPC) with which the serverless resource group is associated by default.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the vSwitch with which the serverless resource group is associated by default.
        # 
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        if self.aliyun_resource_tags_shrink is not None:
            result['AliyunResourceTags'] = self.aliyun_resource_tags_shrink

        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')

        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

