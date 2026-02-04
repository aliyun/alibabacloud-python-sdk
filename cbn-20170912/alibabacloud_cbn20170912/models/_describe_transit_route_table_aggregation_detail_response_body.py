# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouteTableAggregationDetailResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.DescribeTransitRouteTableAggregationDetailResponseBodyData] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The number of entries returned per page.
        self.count = count
        # The configuration of the aggregate route.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeTransitRouteTableAggregationDetailResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeTransitRouteTableAggregationDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        # The error message returned if the configuration of the aggregate route fails.
        self.description = description
        # The ID of the virtual private cloud (VPC) for which the aggregate route is configured.
        self.instance_id = instance_id
        # The status of the aggregate route. Valid values:
        # 
        # *   **Configured**: The aggregate route is advertised to the VPC.
        # *   **Configuring**: The aggregate route is being advertised.
        # *   **ConfigFailed**: The aggregate route failed to be advertised.
        # *   **PartialConfigured**: Failed to advertise the aggregate route to some VPCs.
        # *   **Deleting**: The aggregate route is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

