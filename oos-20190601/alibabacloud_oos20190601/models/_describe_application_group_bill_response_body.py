# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationGroupBillResponseBody(DaraModel):
    def __init__(
        self,
        application_group_consume: List[main_models.DescribeApplicationGroupBillResponseBodyApplicationGroupConsume] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The consume of application group.
        self.application_group_consume = application_group_consume
        # The number of entries per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_group_consume:
            for v1 in self.application_group_consume:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationGroupConsume'] = []
        if self.application_group_consume is not None:
            for k1 in self.application_group_consume:
                result['ApplicationGroupConsume'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_group_consume = []
        if m.get('ApplicationGroupConsume') is not None:
            for k1 in m.get('ApplicationGroupConsume'):
                temp_model = main_models.DescribeApplicationGroupBillResponseBodyApplicationGroupConsume()
                self.application_group_consume.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApplicationGroupBillResponseBodyApplicationGroupConsume(DaraModel):
    def __init__(
        self,
        amount: float = None,
        creation_time: str = None,
        currency: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        optimization: str = None,
        peak_type: str = None,
        performance: str = None,
        status: str = None,
    ):
        # The amount consumed by the instance.
        self.amount = amount
        # The time when the instance was created.
        self.creation_time = creation_time
        # The currency unit.
        self.currency = currency
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # Optimization suggestions.
        self.optimization = optimization
        # The peak type.
        self.peak_type = peak_type
        # The performance of the data synchronization instance.
        self.performance = performance
        # The status of instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.optimization is not None:
            result['Optimization'] = self.optimization

        if self.peak_type is not None:
            result['PeakType'] = self.peak_type

        if self.performance is not None:
            result['Performance'] = self.performance

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Optimization') is not None:
            self.optimization = m.get('Optimization')

        if m.get('PeakType') is not None:
            self.peak_type = m.get('PeakType')

        if m.get('Performance') is not None:
            self.performance = m.get('Performance')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

