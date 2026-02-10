# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePluginSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribePluginSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the plug-in data.
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
            temp_model = main_models.DescribePluginSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePluginSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_cnt: int = None,
        failed_reasons: List[main_models.DescribePluginSummaryResponseBodyDataFailedReasons] = None,
        offline_cnt: int = None,
        online_cnt: int = None,
        switch_off_cnt: int = None,
        total_cnt: int = None,
    ):
        # The number of hosts on which the plug-in failed to be installed.
        self.failed_cnt = failed_cnt
        # The causes of installation failures.
        self.failed_reasons = failed_reasons
        # The number of hosts on which the plug-in is offline.
        self.offline_cnt = offline_cnt
        # The number of hosts on which the plug-in is online.
        self.online_cnt = online_cnt
        # The number of hosts for which the plug-in is not enabled.
        self.switch_off_cnt = switch_off_cnt
        # The total number of hosts.
        self.total_cnt = total_cnt

    def validate(self):
        if self.failed_reasons:
            for v1 in self.failed_reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_cnt is not None:
            result['FailedCnt'] = self.failed_cnt

        result['FailedReasons'] = []
        if self.failed_reasons is not None:
            for k1 in self.failed_reasons:
                result['FailedReasons'].append(k1.to_map() if k1 else None)

        if self.offline_cnt is not None:
            result['OfflineCnt'] = self.offline_cnt

        if self.online_cnt is not None:
            result['OnlineCnt'] = self.online_cnt

        if self.switch_off_cnt is not None:
            result['SwitchOffCnt'] = self.switch_off_cnt

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCnt') is not None:
            self.failed_cnt = m.get('FailedCnt')

        self.failed_reasons = []
        if m.get('FailedReasons') is not None:
            for k1 in m.get('FailedReasons'):
                temp_model = main_models.DescribePluginSummaryResponseBodyDataFailedReasons()
                self.failed_reasons.append(temp_model.from_map(k1))

        if m.get('OfflineCnt') is not None:
            self.offline_cnt = m.get('OfflineCnt')

        if m.get('OnlineCnt') is not None:
            self.online_cnt = m.get('OnlineCnt')

        if m.get('SwitchOffCnt') is not None:
            self.switch_off_cnt = m.get('SwitchOffCnt')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribePluginSummaryResponseBodyDataFailedReasons(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        reason: str = None,
    ):
        # The error code for the installation failure.
        self.code = code
        # The number of hosts on which the installation failed for this reason.
        self.count = count
        # The cause of the installation failure.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

