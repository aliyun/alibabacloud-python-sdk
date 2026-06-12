# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceInstanceBillRequest(DaraModel):
    def __init__(
        self,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        max_results: int = None,
        next_token: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # The billing cycle in the YYYY-MM format.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only when **Granularity** is set to DAILY. The format is YYYY-MM-DD.
        self.billing_date = billing_date
        # The granularity at which you want to query bills. Valid values:
        # 
        # - MONTHLY: by month. The bill details are consistent with the bills on the By Billing Cycle tab of the Bill Details page in User Center.
        # 
        # - DAILY: by day. The bill details are consistent with the bills on the By Day tab of the Bill Details page in User Center.
        # 
        # > If you set this parameter to DAILY, you must specify BillingDate.
        self.granularity = granularity
        # The number of entries to return on each page. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The token that is used to start the next query. Valid values:
        # 
        # - If **NextToken** is empty, no more results exist.
        # 
        # - If **NextToken** has a value, the value is the token that is used to start the next query.
        self.next_token = next_token
        # The service ID.
        self.service_id = service_id
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

