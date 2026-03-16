# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[main_models.ListServiceInstanceResourcesResponseBodyResources] = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListServiceInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class ListServiceInstanceResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        pay_type: str = None,
        product_code: str = None,
        product_type: str = None,
        renew_status: str = None,
        renewal_period: int = None,
        renewal_period_unit: str = None,
        resource_arn: str = None,
        status: str = None,
    ):
        # The time when the resource was created.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The billing method. Valid values:
        # 
        # *   Subscription
        # *   PayAsYouGo
        self.pay_type = pay_type
        # The code of the cloud service.
        self.product_code = product_code
        # The type of the cloud service.
        self.product_type = product_type
        # The renewal state. Valid values:
        # 
        # *   AutoRenewal
        # *   ManualRenewal
        # *   NotRenewal
        self.renew_status = renew_status
        # The renewal period.
        self.renewal_period = renewal_period
        # The unit of the renewal period. Valid values:
        # 
        # *   Month
        # *   Year
        self.renewal_period_unit = renewal_period_unit
        # The ARN of the resource.
        self.resource_arn = resource_arn
        # The state of the resource. Valid values:
        # 
        # *   running
        # *   waiting
        # *   terminated
        # 
        # >  This parameter is returned only for containers.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status

        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period

        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit

        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')

        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')

        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')

        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

