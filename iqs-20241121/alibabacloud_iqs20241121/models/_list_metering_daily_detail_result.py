# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class ListMeteringDailyDetailResult(DaraModel):
    def __init__(
        self,
        metering_daily_detail_list: List[main_models.ListMeteringDailyDetailResultMeteringDailyDetailList] = None,
    ):
        self.metering_daily_detail_list = metering_daily_detail_list

    def validate(self):
        if self.metering_daily_detail_list:
            for v1 in self.metering_daily_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['meteringDailyDetailList'] = []
        if self.metering_daily_detail_list is not None:
            for k1 in self.metering_daily_detail_list:
                result['meteringDailyDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metering_daily_detail_list = []
        if m.get('meteringDailyDetailList') is not None:
            for k1 in m.get('meteringDailyDetailList'):
                temp_model = main_models.ListMeteringDailyDetailResultMeteringDailyDetailList()
                self.metering_daily_detail_list.append(temp_model.from_map(k1))

        return self

class ListMeteringDailyDetailResultMeteringDailyDetailList(DaraModel):
    def __init__(
        self,
        bill_date: str = None,
        bill_period: str = None,
        billing_function_item: str = None,
        billing_item: str = None,
        billing_qps: int = None,
        failed_count: int = None,
        ladder_type_code: int = None,
        sub_account_id: str = None,
        success_count: int = None,
    ):
        self.bill_date = bill_date
        self.bill_period = bill_period
        self.billing_function_item = billing_function_item
        self.billing_item = billing_item
        self.billing_qps = billing_qps
        self.failed_count = failed_count
        self.ladder_type_code = ladder_type_code
        self.sub_account_id = sub_account_id
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_date is not None:
            result['billDate'] = self.bill_date

        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period

        if self.billing_function_item is not None:
            result['billingFunctionItem'] = self.billing_function_item

        if self.billing_item is not None:
            result['billingItem'] = self.billing_item

        if self.billing_qps is not None:
            result['billingQps'] = self.billing_qps

        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        if self.ladder_type_code is not None:
            result['ladderTypeCode'] = self.ladder_type_code

        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billDate') is not None:
            self.bill_date = m.get('billDate')

        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')

        if m.get('billingFunctionItem') is not None:
            self.billing_function_item = m.get('billingFunctionItem')

        if m.get('billingItem') is not None:
            self.billing_item = m.get('billingItem')

        if m.get('billingQps') is not None:
            self.billing_qps = m.get('billingQps')

        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        if m.get('ladderTypeCode') is not None:
            self.ladder_type_code = m.get('ladderTypeCode')

        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

