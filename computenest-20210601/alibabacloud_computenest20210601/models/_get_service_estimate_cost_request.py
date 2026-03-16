# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceEstimateCostRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: main_models.GetServiceEstimateCostRequestCommodity = None,
        operation_name: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the subscription duration.
        self.commodity = commodity
        # The name of the configuration change operation.
        self.operation_name = operation_name
        # The parameters that are specified to deploy the service instance.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The name of the package specification.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

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

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name

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
            temp_model = main_models.GetServiceEstimateCostRequestCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

class GetServiceEstimateCostRequestCommodity(DaraModel):
    def __init__(
        self,
        coupon_id: str = None,
        pay_period: int = None,
        pay_period_unit: str = None,
        quotation_id: str = None,
    ):
        # The coupon ID.
        self.coupon_id = coupon_id
        # The subscription duration of the instance.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   Year.
        # *   Month.
        # *   Day.
        self.pay_period_unit = pay_period_unit
        # The PrivateOffer ID of the Alibaba Cloud Marketplace.
        self.quotation_id = quotation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')

        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')

        if m.get('QuotationId') is not None:
            self.quotation_id = m.get('QuotationId')

        return self

