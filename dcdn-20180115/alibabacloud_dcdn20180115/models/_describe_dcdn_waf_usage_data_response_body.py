# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        waf_usage_data: main_models.DescribeDcdnWafUsageDataResponseBodyWafUsageData = None,
    ):
        # The operation that you want to perform. Set the value to **DescribeDcdnWafUsageData**.
        self.end_time = end_time
        # Specifies how query results are grouped. By default, this parameter is empty. Valid values:
        # 
        # *   domain: Query results are grouped by accelerated domain name.
        # *   An empty string: Query results are not grouped.
        self.request_id = request_id
        # The accelerated domain name.
        self.start_time = start_time
        # The number of monitored requests.
        self.waf_usage_data = waf_usage_data

    def validate(self):
        if self.waf_usage_data:
            self.waf_usage_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.waf_usage_data is not None:
            result['WafUsageData'] = self.waf_usage_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WafUsageData') is not None:
            temp_model = main_models.DescribeDcdnWafUsageDataResponseBodyWafUsageData()
            self.waf_usage_data = temp_model.from_map(m.get('WafUsageData'))

        return self

class DescribeDcdnWafUsageDataResponseBodyWafUsageData(DaraModel):
    def __init__(
        self,
        waf_usage_data_item: List[main_models.DescribeDcdnWafUsageDataResponseBodyWafUsageDataWafUsageDataItem] = None,
    ):
        self.waf_usage_data_item = waf_usage_data_item

    def validate(self):
        if self.waf_usage_data_item:
            for v1 in self.waf_usage_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WafUsageDataItem'] = []
        if self.waf_usage_data_item is not None:
            for k1 in self.waf_usage_data_item:
                result['WafUsageDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.waf_usage_data_item = []
        if m.get('WafUsageDataItem') is not None:
            for k1 in m.get('WafUsageDataItem'):
                temp_model = main_models.DescribeDcdnWafUsageDataResponseBodyWafUsageDataWafUsageDataItem()
                self.waf_usage_data_item.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafUsageDataResponseBodyWafUsageDataWafUsageDataItem(DaraModel):
    def __init__(
        self,
        access_cnt: int = None,
        block_cnt: int = None,
        domain: str = None,
        observe_cnt: int = None,
        sec_cu: int = None,
        time_stamp: str = None,
    ):
        # The number of blocked requests.
        self.access_cnt = access_cnt
        # The number of allowed requests.
        self.block_cnt = block_cnt
        # The domain name that you want to query. If you do not specify an accelerated domain name, all accelerated domain names are queried by default.
        self.domain = domain
        # The end of the time range during which data was queried.
        self.observe_cnt = observe_cnt
        # The time granularity for a query. Unit: seconds.
        # 
        # The time granularity varies with the maximum time range per query. Valid values: 300 (5 minutes), 3600 (1 hour), and 86400 (1 day).
        self.sec_cu = sec_cu
        # The beginning of the time range during which data was queried.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_cnt is not None:
            result['AccessCnt'] = self.access_cnt

        if self.block_cnt is not None:
            result['BlockCnt'] = self.block_cnt

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.observe_cnt is not None:
            result['ObserveCnt'] = self.observe_cnt

        if self.sec_cu is not None:
            result['SecCu'] = self.sec_cu

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCnt') is not None:
            self.access_cnt = m.get('AccessCnt')

        if m.get('BlockCnt') is not None:
            self.block_cnt = m.get('BlockCnt')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ObserveCnt') is not None:
            self.observe_cnt = m.get('ObserveCnt')

        if m.get('SecCu') is not None:
            self.sec_cu = m.get('SecCu')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

