# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudProductFieldStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        grouped_fields: main_models.DescribeCloudProductFieldStatisticsResponseBodyGroupedFields = None,
        request_id: str = None,
    ):
        # The statistics of cloud services that are protected by Security Center.
        self.grouped_fields = grouped_fields
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.grouped_fields:
            self.grouped_fields.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grouped_fields is not None:
            result['GroupedFields'] = self.grouped_fields.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupedFields') is not None:
            temp_model = main_models.DescribeCloudProductFieldStatisticsResponseBodyGroupedFields()
            self.grouped_fields = temp_model.from_map(m.get('GroupedFields'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudProductFieldStatisticsResponseBodyGroupedFields(DaraModel):
    def __init__(
        self,
        category_count: str = None,
        instance_count: int = None,
        risk_instance_count: int = None,
    ):
        # The statistics of different types of assets. **MachineType** indicates the type of the asset. **Count** indicates the number of assets of a specific type.
        # 
        # Valid values of **MachineType**:
        # 
        # *   **1**: Server Load Balancer (SLB) instance
        # *   **2**: NAT gateway instance
        # *   **3**: ApsaraDB RDS instance
        # *   **4**: ApsaraDB for MongoDB instance
        self.category_count = category_count
        # The total number of cloud services that are protected by Security Center.
        self.instance_count = instance_count
        # The number of cloud services that are at risk.
        self.risk_instance_count = risk_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_count is not None:
            result['CategoryCount'] = self.category_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCount') is not None:
            self.category_count = m.get('CategoryCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        return self

