# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceInstanceSpecShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: main_models.UpdateServiceInstanceSpecShrinkRequestCommodity = None,
        dry_run: bool = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters_shrink: str = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can generate the value from your client, but you must ensure that the value is unique among different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length.
        self.client_token = client_token
        # The purchase order information for Alibaba Cloud Marketplace. This parameter is not required if the service is not listed in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # Specifies whether to perform a dry run on the request, including checks on permissions and instance status.
        # 
        # Valid values:
        # 
        # - true: sends the request but does not create a service instance.
        # 
        # - false: sends the request and creates the service instance if the check is passed.
        self.dry_run = dry_run
        # Specifies whether to enable Prometheus monitoring on the user side.
        # 
        # Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the specification modification operation.
        # 
        # You can obtain the name and content of the specification modification operation configured for the service by viewing the **ModifyParametersConfig** property of the **OperationMetadata** response parameter in the [GetService - Get service details](https://help.aliyun.com/document_detail/2340828.html) operation.
        self.operation_name = operation_name
        # The modification parameters of the service instance.
        # 
        # You can specify this parameter if the service provider set **Change Type** to **Parameter Change** when adding a specification modification operation.
        # 
        # > - You can obtain the modification parameters configured for the service by viewing the **ModifyParametersConfig** property of the **OperationMetadata** response parameter in the [GetService - Get service details](https://help.aliyun.com/document_detail/2340828.html) operation.
        # > - You can also view the modification parameters configured for the service on the **Service Instance Modification** page in the [Compute Nest console](https://computenest.console.aliyun.com/service/instance/cn-hangzhou).
        # 
        # For example, if the service is configured to upgrade the ECS instance type, you must specify an instance type that is higher than the original instance type of the service instance.
        self.parameters_shrink = parameters_shrink
        # The plan name of the service instance.
        # 
        # You can specify this parameter if the service provider set **Change Type** to **Plan Change** when adding a specification modification operation.
        # 
        # You can obtain the plan name configured for the service by viewing the **PredefinedParameters** property of the **DeployMetadata** response parameter in the [GetService - Get service details](https://help.aliyun.com/document_detail/2340828.html) operation.
        self.predefined_parameters_name = predefined_parameters_name
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances - List service instances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Commodity') is not None:
            temp_model = main_models.UpdateServiceInstanceSpecShrinkRequestCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class UpdateServiceInstanceSpecShrinkRequestCommodity(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        coupon_id: str = None,
    ):
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # - **true** (default): enables automatic payment. You must ensure that your account balance is sufficient.
        # 
        # - **false**: generates an order but does not deduct the fee. If the balance of your payment method is insufficient, you can set the AutoPay parameter to false. In this case, an unpaid order is generated, and you can log on to the [ApsaraDB RDS console](https://rdsnext.console.aliyun.com/dashboard/cn-beijing) to pay the order.
        self.auto_pay = auto_pay
        # The coupon.
        self.coupon_id = coupon_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        return self

