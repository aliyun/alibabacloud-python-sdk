# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class GetIqsUsageResult(DaraModel):
    def __init__(
        self,
        records: List[main_models.GetIqsUsageResultRecords] = None,
    ):
        self.records = records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetIqsUsageResultRecords()
                self.records.append(temp_model.from_map(k1))

        return self



class GetIqsUsageResultRecords(DaraModel):
    def __init__(
        self,
        api: str = None,
        billing_qps: int = None,
        date: str = None,
        engine_type: str = None,
        failed_calls: int = None,
        ladder_type: str = None,
        main_account_id: str = None,
        sub_account_id: str = None,
        success_calls: int = None,
        total_calls: int = None,
        value_added_advanced: int = None,
        value_added_summary: int = None,
    ):
        self.api = api
        self.billing_qps = billing_qps
        self.date = date
        self.engine_type = engine_type
        self.failed_calls = failed_calls
        self.ladder_type = ladder_type
        self.main_account_id = main_account_id
        self.sub_account_id = sub_account_id
        self.success_calls = success_calls
        self.total_calls = total_calls
        self.value_added_advanced = value_added_advanced
        self.value_added_summary = value_added_summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['api'] = self.api

        if self.billing_qps is not None:
            result['billingQps'] = self.billing_qps

        if self.date is not None:
            result['date'] = self.date

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.failed_calls is not None:
            result['failedCalls'] = self.failed_calls

        if self.ladder_type is not None:
            result['ladderType'] = self.ladder_type

        if self.main_account_id is not None:
            result['mainAccountId'] = self.main_account_id

        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id

        if self.success_calls is not None:
            result['successCalls'] = self.success_calls

        if self.total_calls is not None:
            result['totalCalls'] = self.total_calls

        if self.value_added_advanced is not None:
            result['valueAddedAdvanced'] = self.value_added_advanced

        if self.value_added_summary is not None:
            result['valueAddedSummary'] = self.value_added_summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            self.api = m.get('api')

        if m.get('billingQps') is not None:
            self.billing_qps = m.get('billingQps')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('failedCalls') is not None:
            self.failed_calls = m.get('failedCalls')

        if m.get('ladderType') is not None:
            self.ladder_type = m.get('ladderType')

        if m.get('mainAccountId') is not None:
            self.main_account_id = m.get('mainAccountId')

        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')

        if m.get('successCalls') is not None:
            self.success_calls = m.get('successCalls')

        if m.get('totalCalls') is not None:
            self.total_calls = m.get('totalCalls')

        if m.get('valueAddedAdvanced') is not None:
            self.value_added_advanced = m.get('valueAddedAdvanced')

        if m.get('valueAddedSummary') is not None:
            self.value_added_summary = m.get('valueAddedSummary')

        return self

