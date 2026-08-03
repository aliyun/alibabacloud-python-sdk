# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetInsightsEventsCountResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInsightsEventsCountResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the Insights events.
        self.data = data
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetInsightsEventsCountResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInsightsEventsCountResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        insight_type: str = None,
        region_id: str = None,
    ):
        # The number of Insights events.
        self.count = count
        # The type of the Insights event. Valid values:
        # 
        # - IpInsight: IP request events.
        # 
        # - ApiCallRateInsight: High-risk API call events.
        # 
        # - ApiErrorRateInsight: API error events.
        # 
        # - AkInsight: AccessKey pair call events.
        # 
        # - PolicyChangeInsight: Permission change events.
        # 
        # - PasswordChangeInsight: Password change events.
        # 
        # - TrailConcealmentInsight: Trail concealment events.
        self.insight_type = insight_type
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.insight_type is not None:
            result['InsightType'] = self.insight_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('InsightType') is not None:
            self.insight_type = m.get('InsightType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

