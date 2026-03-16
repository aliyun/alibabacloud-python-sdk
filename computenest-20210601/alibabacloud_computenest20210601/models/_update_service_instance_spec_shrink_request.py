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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # Specifies whether to perform only a dry run, without performing the actual request. A dry run includes checks on the permissions and instance state.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run but does not create a service instance.
        # *   false: performs a dry run and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether to enable Prometheus monitoring on the user side.
        # 
        # Valid values:
        # 
        # true
        # 
        # false
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the configuration change operation.
        # 
        # To obtain the names and content of the configuration change operations of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        self.operation_name = operation_name
        # The configuration parameter.
        # 
        # This parameter is available if the service provider set **Method** to **Change Parameter** when configuring configuration change operations.
        # 
        # > 
        # 
        # *   To obtain the parameters of the service that support configuration change, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        # 
        # *   You can also view the parameters of the service that support configuration change in the **configuration change** dialog box in the [Compute Nest console](https://computenest.console.aliyun.com/service/instance/cn-hangzhou).
        # 
        # For example, if the service supports Elastic Compute Service (ECS) instance type upgrade, you must specify an instance type that has higher specifications than the current one.
        self.parameters_shrink = parameters_shrink
        # The name of the configuration plan.
        # 
        # This parameter is available if the service provider set **Method** to **Change Plan** when configuring configuration change operations.
        # 
        # To obtain the configuration plan names of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **PredefinedParameters** in the value of **DeployMetadata**.
        self.predefined_parameters_name = predefined_parameters_name
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the ID of the service instance.
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
    ):
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   **true (default)**: automatically completes the payment. You must make sure that your account balance is sufficient.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated. If your account balance is insufficient, you can set AutoPay to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.[](https://rdsnext.console.aliyun.com/dashboard/cn-beijing)
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        return self

