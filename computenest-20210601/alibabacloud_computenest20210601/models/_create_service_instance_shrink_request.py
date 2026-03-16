# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class CreateServiceInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: main_models.CreateServiceInstanceShrinkRequestCommodity = None,
        contact_group: str = None,
        dry_run: bool = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: bool = None,
        name: str = None,
        operation_metadata: main_models.CreateServiceInstanceShrinkRequestOperationMetadata = None,
        parameters_shrink: str = None,
        region_id: str = None,
        resource_auto_pay: bool = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_code: str = None,
        specification_name: str = None,
        tag: List[main_models.CreateServiceInstanceShrinkRequestTag] = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # The alert contact group.
        self.contact_group = contact_group
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   **true**: performs a dry run for the request, but does not create a service instance.
        # *   **false**: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_instance_ops = enable_instance_ops
        # Specifies whether to enable the Prometheus monitoring feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_user_prometheus = enable_user_prometheus
        # The serviceInstance name.
        self.name = name
        # The operation metadata.
        self.operation_metadata = operation_metadata
        # The parameters that the customer specifies to deploy the service instance.
        # 
        # >  If region information is required to create a service instance, you must specify the region ID in the value of Parameters.
        self.parameters_shrink = parameters_shrink
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to automatically deduct the resource fees from the account balance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.resource_auto_pay = resource_auto_pay
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The trial service instance id witch you want to convert to formal
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # Specification code.
        self.specification_code = specification_code
        # The package name.
        self.specification_name = specification_name
        # The tags.
        self.tag = tag
        # The name of the template.
        self.template_name = template_name
        # The trial type of the service instance. Valid values:
        # 
        # *   **Trial**: Trials are supported.
        # *   **NotTrial**: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops

        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_auto_pay is not None:
            result['ResourceAutoPay'] = self.resource_auto_pay

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Commodity') is not None:
            temp_model = main_models.CreateServiceInstanceShrinkRequestCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')

        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationMetadata') is not None:
            temp_model = main_models.CreateServiceInstanceShrinkRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m.get('OperationMetadata'))

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceAutoPay') is not None:
            self.resource_auto_pay = m.get('ResourceAutoPay')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateServiceInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

class CreateServiceInstanceShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateServiceInstanceShrinkRequestOperationMetadata(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        extra_info: str = None,
        resources: str = None,
        service_instance_id: str = None,
        start_time: str = None,
    ):
        # The operation end time.
        self.end_time = end_time
        # The additional information.
        self.extra_info = extra_info
        # Imported resource.
        self.resources = resources
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The operation start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateServiceInstanceShrinkRequestCommodity(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        coupon_id: str = None,
        pay_period: int = None,
        pay_period_unit: str = None,
        quotation_id: str = None,
    ):
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the service instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_renew = auto_renew
        # The coupon ID.
        self.coupon_id = coupon_id
        # The subscription duration.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # *   **Day**
        self.pay_period_unit = pay_period_unit
        # privet offer Id
        self.quotation_id = quotation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period

        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit

        if self.quotation_id is not None:
            result['QuotationId'] = self.quotation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')

        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')

        if m.get('QuotationId') is not None:
            self.quotation_id = m.get('QuotationId')

        return self

