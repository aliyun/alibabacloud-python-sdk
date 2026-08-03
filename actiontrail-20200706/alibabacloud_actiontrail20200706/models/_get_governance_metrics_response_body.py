# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetGovernanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGovernanceMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetGovernanceMetricsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGovernanceMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        governance_metrics: List[main_models.GetGovernanceMetricsResponseBodyDataGovernanceMetrics] = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # A collection of governance items that contain multiple compliance assessment dimensions.
        self.governance_metrics = governance_metrics

    def validate(self):
        if self.governance_metrics:
            for v1 in self.governance_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        result['GovernanceMetrics'] = []
        if self.governance_metrics is not None:
            for k1 in self.governance_metrics:
                result['GovernanceMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        self.governance_metrics = []
        if m.get('GovernanceMetrics') is not None:
            for k1 in m.get('GovernanceMetrics'):
                temp_model = main_models.GetGovernanceMetricsResponseBodyDataGovernanceMetrics()
                self.governance_metrics.append(temp_model.from_map(k1))

        return self

class GetGovernanceMetricsResponseBodyDataGovernanceMetrics(DaraModel):
    def __init__(
        self,
        columns_schema: str = None,
        governance_item: str = None,
        governance_score: str = None,
    ):
        # The details of the resource.
        # 
        # This parameter contains the detailed configurations of all compliant resources for the governance item. This parameter is returned only if a resource instance exists.
        self.columns_schema = columns_schema
        # The governance item. This indicates a specific category of compliance check.
        self.governance_item = governance_item
        # The compliance score for the governance item.
        # 
        # Valid values: 0 to 100.
        self.governance_score = governance_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns_schema is not None:
            result['ColumnsSchema'] = self.columns_schema

        if self.governance_item is not None:
            result['GovernanceItem'] = self.governance_item

        if self.governance_score is not None:
            result['GovernanceScore'] = self.governance_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnsSchema') is not None:
            self.columns_schema = m.get('ColumnsSchema')

        if m.get('GovernanceItem') is not None:
            self.governance_item = m.get('GovernanceItem')

        if m.get('GovernanceScore') is not None:
            self.governance_score = m.get('GovernanceScore')

        return self

