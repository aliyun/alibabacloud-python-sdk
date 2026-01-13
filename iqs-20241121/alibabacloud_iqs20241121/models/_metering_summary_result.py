# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class MeteringSummaryResult(DaraModel):
    def __init__(
        self,
        metering_summary_list: List[main_models.MeteringSummaryResultMeteringSummaryList] = None,
    ):
        self.metering_summary_list = metering_summary_list

    def validate(self):
        if self.metering_summary_list:
            for v1 in self.metering_summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['meteringSummaryList'] = []
        if self.metering_summary_list is not None:
            for k1 in self.metering_summary_list:
                result['meteringSummaryList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metering_summary_list = []
        if m.get('meteringSummaryList') is not None:
            for k1 in m.get('meteringSummaryList'):
                temp_model = main_models.MeteringSummaryResultMeteringSummaryList()
                self.metering_summary_list.append(temp_model.from_map(k1))

        return self

class MeteringSummaryResultMeteringSummaryList(DaraModel):
    def __init__(
        self,
        billing_function_item: str = None,
        billing_item: str = None,
        fail_count: int = None,
        success_count: int = None,
    ):
        self.billing_function_item = billing_function_item
        self.billing_item = billing_item
        self.fail_count = fail_count
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_function_item is not None:
            result['billingFunctionItem'] = self.billing_function_item

        if self.billing_item is not None:
            result['billingItem'] = self.billing_item

        if self.fail_count is not None:
            result['failCount'] = self.fail_count

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingFunctionItem') is not None:
            self.billing_function_item = m.get('billingFunctionItem')

        if m.get('billingItem') is not None:
            self.billing_item = m.get('billingItem')

        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

