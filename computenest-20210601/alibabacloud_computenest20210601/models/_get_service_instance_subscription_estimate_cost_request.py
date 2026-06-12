# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceInstanceSubscriptionEstimateCostRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        order_type: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_period: List[main_models.GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod] = None,
        service_instance_id: str = None,
    ):
        # A client-generated token that ensures the idempotence of the request. The token must be unique for each request. It can contain only ASCII characters and cannot be longer than 64 characters.
        self.client_token = client_token
        # The order type. Valid value: Renewal.
        # 
        # This parameter is required.
        self.order_type = order_type
        # The renewal duration for all subscription resources of the service instance. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the renewal duration for all subscription resources of the service instance. This is the unit for the Period parameter. Valid values: Month and Year. Default value: Month.
        self.period_unit = period_unit
        # The region ID.
        self.region_id = region_id
        # The renewal configuration for the resources.
        self.resource_period = resource_period
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.resource_period:
            for v1 in self.resource_period:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ResourcePeriod'] = []
        if self.resource_period is not None:
            for k1 in self.resource_period:
                result['ResourcePeriod'].append(k1.to_map() if k1 else None)

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_period = []
        if m.get('ResourcePeriod') is not None:
            for k1 in m.get('ResourcePeriod'):
                temp_model = main_models.GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod()
                self.resource_period.append(temp_model.from_map(k1))

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod(DaraModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
    ):
        # The renewal duration. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the renewal duration for the resource. This is the unit for the Period parameter. Valid values: Month and Year. Default value: Month.
        self.period_unit = period_unit
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        return self

