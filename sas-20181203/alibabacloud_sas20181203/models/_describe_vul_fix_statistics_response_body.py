# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulFixStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        fix_stat: List[main_models.DescribeVulFixStatisticsResponseBodyFixStat] = None,
        fix_total: main_models.DescribeVulFixStatisticsResponseBodyFixTotal = None,
        request_id: str = None,
    ):
        # An array that consists of the statistics of vulnerability fixes by vulnerability type.
        self.fix_stat = fix_stat
        # The total statistics of vulnerability fixes.
        self.fix_total = fix_total
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.fix_stat:
            for v1 in self.fix_stat:
                 if v1:
                    v1.validate()
        if self.fix_total:
            self.fix_total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FixStat'] = []
        if self.fix_stat is not None:
            for k1 in self.fix_stat:
                result['FixStat'].append(k1.to_map() if k1 else None)

        if self.fix_total is not None:
            result['FixTotal'] = self.fix_total.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fix_stat = []
        if m.get('FixStat') is not None:
            for k1 in m.get('FixStat'):
                temp_model = main_models.DescribeVulFixStatisticsResponseBodyFixStat()
                self.fix_stat.append(temp_model.from_map(k1))

        if m.get('FixTotal') is not None:
            temp_model = main_models.DescribeVulFixStatisticsResponseBodyFixTotal()
            self.fix_total = temp_model.from_map(m.get('FixTotal'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVulFixStatisticsResponseBodyFixTotal(DaraModel):
    def __init__(
        self,
        fixed_today_num: int = None,
        fixed_total_num: int = None,
        fixing_num: int = None,
        need_fix_num: int = None,
    ):
        # The number of vulnerabilities that are fixed on the current day.
        self.fixed_today_num = fixed_today_num
        # The total number of fixed vulnerabilities.
        self.fixed_total_num = fixed_total_num
        # The number of vulnerabilities that are being fixed.
        self.fixing_num = fixing_num
        # The number of unfixed vulnerabilities.
        self.need_fix_num = need_fix_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_today_num is not None:
            result['FixedTodayNum'] = self.fixed_today_num

        if self.fixed_total_num is not None:
            result['FixedTotalNum'] = self.fixed_total_num

        if self.fixing_num is not None:
            result['FixingNum'] = self.fixing_num

        if self.need_fix_num is not None:
            result['NeedFixNum'] = self.need_fix_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedTodayNum') is not None:
            self.fixed_today_num = m.get('FixedTodayNum')

        if m.get('FixedTotalNum') is not None:
            self.fixed_total_num = m.get('FixedTotalNum')

        if m.get('FixingNum') is not None:
            self.fixing_num = m.get('FixingNum')

        if m.get('NeedFixNum') is not None:
            self.need_fix_num = m.get('NeedFixNum')

        return self

class DescribeVulFixStatisticsResponseBodyFixStat(DaraModel):
    def __init__(
        self,
        fixed_today_num: int = None,
        fixed_total_num: int = None,
        fixing_num: int = None,
        need_fix_num: int = None,
        type: str = None,
    ):
        # The number of vulnerabilities that are fixed on the current day.
        self.fixed_today_num = fixed_today_num
        # The total number of fixed vulnerabilities.
        self.fixed_total_num = fixed_total_num
        # The number of vulnerabilities that are being fixed.
        self.fixing_num = fixing_num
        # The number of unfixed vulnerabilities.
        self.need_fix_num = need_fix_num
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **app**: application vulnerability
        # *   **emg**: urgent vulnerability
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_today_num is not None:
            result['FixedTodayNum'] = self.fixed_today_num

        if self.fixed_total_num is not None:
            result['FixedTotalNum'] = self.fixed_total_num

        if self.fixing_num is not None:
            result['FixingNum'] = self.fixing_num

        if self.need_fix_num is not None:
            result['NeedFixNum'] = self.need_fix_num

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedTodayNum') is not None:
            self.fixed_today_num = m.get('FixedTodayNum')

        if m.get('FixedTotalNum') is not None:
            self.fixed_total_num = m.get('FixedTotalNum')

        if m.get('FixingNum') is not None:
            self.fixing_num = m.get('FixingNum')

        if m.get('NeedFixNum') is not None:
            self.need_fix_num = m.get('NeedFixNum')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

