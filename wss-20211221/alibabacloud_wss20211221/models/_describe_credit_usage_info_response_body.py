# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeCreditUsageInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_info_list: List[main_models.DescribeCreditUsageInfoResponseBodyUsageInfoList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The array of usage data.
        self.usage_info_list = usage_info_list

    def validate(self):
        if self.usage_info_list:
            for v1 in self.usage_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UsageInfoList'] = []
        if self.usage_info_list is not None:
            for k1 in self.usage_info_list:
                result['UsageInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usage_info_list = []
        if m.get('UsageInfoList') is not None:
            for k1 in m.get('UsageInfoList'):
                temp_model = main_models.DescribeCreditUsageInfoResponseBodyUsageInfoList()
                self.usage_info_list.append(temp_model.from_map(k1))

        return self

class DescribeCreditUsageInfoResponseBodyUsageInfoList(DaraModel):
    def __init__(
        self,
        usage_info: main_models.DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfo = None,
        usage_info_key: str = None,
    ):
        # The usage data details.
        self.usage_info = usage_info
        # The usage primary key. When `UsageType=User`, this is the `aliUid`. When `UsageType=CreditPackage`, this is the credit package instance ID. When `UsageType=Agent`, this is the `AgentId`.
        self.usage_info_key = usage_info_key

    def validate(self):
        if self.usage_info:
            self.usage_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.usage_info is not None:
            result['UsageInfo'] = self.usage_info.to_map()

        if self.usage_info_key is not None:
            result['UsageInfoKey'] = self.usage_info_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsageInfo') is not None:
            temp_model = main_models.DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfo()
            self.usage_info = temp_model.from_map(m.get('UsageInfo'))

        if m.get('UsageInfoKey') is not None:
            self.usage_info_key = m.get('UsageInfoKey')

        return self

class DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfo(DaraModel):
    def __init__(
        self,
        credit_trend_list: List[main_models.DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfoCreditTrendList] = None,
        current_instance_id: str = None,
        current_remain_credit: int = None,
        current_total_credit: int = None,
        current_used_credit: int = None,
        day_used_credit: int = None,
        period_total_credit: int = None,
        period_used_credit: int = None,
        remain_credit: int = None,
        today_used: str = None,
        total_credit: int = None,
        total_used: str = None,
        total_used_credit: int = None,
        warn_percent: int = None,
        week_used_credit: int = None,
    ):
        # The hourly consumption samples of the current credit package.
        self.credit_trend_list = credit_trend_list
        # The instance ID of the current active credit package.
        self.current_instance_id = current_instance_id
        # The remaining credits of the current active credit package.
        self.current_remain_credit = current_remain_credit
        # The total credits of the current active credit package.
        self.current_total_credit = current_total_credit
        # The used credits of the current active credit package.
        self.current_used_credit = current_used_credit
        # The credit usage in the last 1 day.
        self.day_used_credit = day_used_credit
        # The shared credit quota in the current active period.
        self.period_total_credit = period_total_credit
        # The shared credit usage in the current active period.
        self.period_used_credit = period_used_credit
        # The cumulative remaining credits.
        self.remain_credit = remain_credit
        self.today_used = today_used
        # The cumulative total credits.
        self.total_credit = total_credit
        self.total_used = total_used
        # The cumulative credit usage.
        self.total_used_credit = total_used_credit
        # The alert threshold percentage (0–100).
        self.warn_percent = warn_percent
        # The credit usage in the last 1 week.
        self.week_used_credit = week_used_credit

    def validate(self):
        if self.credit_trend_list:
            for v1 in self.credit_trend_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreditTrendList'] = []
        if self.credit_trend_list is not None:
            for k1 in self.credit_trend_list:
                result['CreditTrendList'].append(k1.to_map() if k1 else None)

        if self.current_instance_id is not None:
            result['CurrentInstanceId'] = self.current_instance_id

        if self.current_remain_credit is not None:
            result['CurrentRemainCredit'] = self.current_remain_credit

        if self.current_total_credit is not None:
            result['CurrentTotalCredit'] = self.current_total_credit

        if self.current_used_credit is not None:
            result['CurrentUsedCredit'] = self.current_used_credit

        if self.day_used_credit is not None:
            result['DayUsedCredit'] = self.day_used_credit

        if self.period_total_credit is not None:
            result['PeriodTotalCredit'] = self.period_total_credit

        if self.period_used_credit is not None:
            result['PeriodUsedCredit'] = self.period_used_credit

        if self.remain_credit is not None:
            result['RemainCredit'] = self.remain_credit

        if self.today_used is not None:
            result['TodayUsed'] = self.today_used

        if self.total_credit is not None:
            result['TotalCredit'] = self.total_credit

        if self.total_used is not None:
            result['TotalUsed'] = self.total_used

        if self.total_used_credit is not None:
            result['TotalUsedCredit'] = self.total_used_credit

        if self.warn_percent is not None:
            result['WarnPercent'] = self.warn_percent

        if self.week_used_credit is not None:
            result['WeekUsedCredit'] = self.week_used_credit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credit_trend_list = []
        if m.get('CreditTrendList') is not None:
            for k1 in m.get('CreditTrendList'):
                temp_model = main_models.DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfoCreditTrendList()
                self.credit_trend_list.append(temp_model.from_map(k1))

        if m.get('CurrentInstanceId') is not None:
            self.current_instance_id = m.get('CurrentInstanceId')

        if m.get('CurrentRemainCredit') is not None:
            self.current_remain_credit = m.get('CurrentRemainCredit')

        if m.get('CurrentTotalCredit') is not None:
            self.current_total_credit = m.get('CurrentTotalCredit')

        if m.get('CurrentUsedCredit') is not None:
            self.current_used_credit = m.get('CurrentUsedCredit')

        if m.get('DayUsedCredit') is not None:
            self.day_used_credit = m.get('DayUsedCredit')

        if m.get('PeriodTotalCredit') is not None:
            self.period_total_credit = m.get('PeriodTotalCredit')

        if m.get('PeriodUsedCredit') is not None:
            self.period_used_credit = m.get('PeriodUsedCredit')

        if m.get('RemainCredit') is not None:
            self.remain_credit = m.get('RemainCredit')

        if m.get('TodayUsed') is not None:
            self.today_used = m.get('TodayUsed')

        if m.get('TotalCredit') is not None:
            self.total_credit = m.get('TotalCredit')

        if m.get('TotalUsed') is not None:
            self.total_used = m.get('TotalUsed')

        if m.get('TotalUsedCredit') is not None:
            self.total_used_credit = m.get('TotalUsedCredit')

        if m.get('WarnPercent') is not None:
            self.warn_percent = m.get('WarnPercent')

        if m.get('WeekUsedCredit') is not None:
            self.week_used_credit = m.get('WeekUsedCredit')

        return self

class DescribeCreditUsageInfoResponseBodyUsageInfoListUsageInfoCreditTrendList(DaraModel):
    def __init__(
        self,
        time_point: str = None,
        used_credit: int = None,
    ):
        # The time point in the format of `yyyy-MM-dd HH` (accurate to the hour).
        self.time_point = time_point
        # The number of credits consumed during the hour.
        self.used_credit = used_credit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        if self.used_credit is not None:
            result['UsedCredit'] = self.used_credit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        if m.get('UsedCredit') is not None:
            self.used_credit = m.get('UsedCredit')

        return self

