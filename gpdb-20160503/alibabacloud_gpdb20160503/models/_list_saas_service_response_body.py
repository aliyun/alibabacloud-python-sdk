# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSaasServiceResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSaasServiceResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of service details.
        self.items = items
        # The maximum number of entries returned in this request. Default value: 10.
        self.max_results = max_results
        # The token for the next query to begin with.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSaasServiceResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListSaasServiceResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cu: int = None,
        expire_time: str = None,
        pay_type: str = None,
        plan: str = None,
        service_id: str = None,
        service_name: str = None,
        service_type: str = None,
        status: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The computing resources.
        self.cu = cu
        # The expiration time.
        self.expire_time = expire_time
        # The billing type. Valid values:
        # 
        # - **POSTPAY**: pay-as-you-go.
        # - **PREPAY**: subscription.
        self.pay_type = pay_type
        # [Deprecated]
        self.plan = plan
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The service type:
        # 
        # - **memory**
        # - **drama**
        self.service_type = service_type
        # The service status:
        # 
        # - active: Running
        # - creating: Being created
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

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.plan is not None:
            result['Plan'] = self.plan

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Plan') is not None:
            self.plan = m.get('Plan')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

