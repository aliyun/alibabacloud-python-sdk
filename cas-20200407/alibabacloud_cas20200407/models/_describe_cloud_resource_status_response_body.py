# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudResourceStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeCloudResourceStatusResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeCloudResourceStatusResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudResourceStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        cloud_name: str = None,
        cloud_product: str = None,
        total_count: int = None,
    ):
        # The cloud service provider.
        self.cloud_name = cloud_name
        # The cloud service.
        self.cloud_product = cloud_product
        # The total number of cloud resources on which certificates are deployed.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

