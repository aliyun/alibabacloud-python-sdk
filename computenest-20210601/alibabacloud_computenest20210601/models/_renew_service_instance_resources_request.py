# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class RenewServiceInstanceResourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_period: List[main_models.RenewServiceInstanceResourcesRequestResourcePeriod] = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The renewal duration for all prepaid resources in the service instance. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration of all prepaid resources in the service instance, which is the unit for the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Region ID.
        self.region_id = region_id
        # List of resource renewals.
        self.resource_period = resource_period
        # Service instance ID.
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

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_period = []
        if m.get('ResourcePeriod') is not None:
            for k1 in m.get('ResourcePeriod'):
                temp_model = main_models.RenewServiceInstanceResourcesRequestResourcePeriod()
                self.resource_period.append(temp_model.from_map(k1))

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

class RenewServiceInstanceResourcesRequestResourcePeriod(DaraModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
    ):
        # The renewal duration for the resource. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration of the resource, which is the unit for the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Resource ARN (Aliyun Resource Name).
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

