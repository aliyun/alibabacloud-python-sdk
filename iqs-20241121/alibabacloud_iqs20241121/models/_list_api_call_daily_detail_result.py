# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class ListApiCallDailyDetailResult(DaraModel):
    def __init__(
        self,
        details: List[main_models.ListApiCallDailyDetailResultDetails] = None,
    ):
        self.details = details

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['details'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k1 in m.get('details'):
                temp_model = main_models.ListApiCallDailyDetailResultDetails()
                self.details.append(temp_model.from_map(k1))

        return self



class ListApiCallDailyDetailResultDetails(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        avg_latency: int = None,
        bill_date: str = None,
        engine_type: str = None,
        failed_count: int = None,
        p_90latency: int = None,
        p_95latency: int = None,
        request_max_qps: int = None,
        sub_account_id: str = None,
        success_count: int = None,
    ):
        self.api_name = api_name
        self.avg_latency = avg_latency
        self.bill_date = bill_date
        self.engine_type = engine_type
        self.failed_count = failed_count
        self.p_90latency = p_90latency
        self.p_95latency = p_95latency
        self.request_max_qps = request_max_qps
        self.sub_account_id = sub_account_id
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.avg_latency is not None:
            result['avgLatency'] = self.avg_latency

        if self.bill_date is not None:
            result['billDate'] = self.bill_date

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.p_90latency is not None:
            result['p90Latency'] = self.p_90latency

        if self.p_95latency is not None:
            result['p95Latency'] = self.p_95latency

        if self.request_max_qps is not None:
            result['requestMaxQps'] = self.request_max_qps

        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('avgLatency') is not None:
            self.avg_latency = m.get('avgLatency')

        if m.get('billDate') is not None:
            self.bill_date = m.get('billDate')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('p90Latency') is not None:
            self.p_90latency = m.get('p90Latency')

        if m.get('p95Latency') is not None:
            self.p_95latency = m.get('p95Latency')

        if m.get('requestMaxQps') is not None:
            self.request_max_qps = m.get('requestMaxQps')

        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

