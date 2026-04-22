# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribePvtzStatisticsHistoryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePvtzStatisticsHistoryResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribePvtzStatisticsHistoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePvtzStatisticsHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        domain_name: str = None,
        fail_count: int = None,
        protocol: str = None,
        qtype: str = None,
        ratio: int = None,
        success_count: int = None,
        timestamp: int = None,
        zone_name: str = None,
    ):
        self.count = count
        self.domain_name = domain_name
        self.fail_count = fail_count
        self.protocol = protocol
        self.qtype = qtype
        self.ratio = ratio
        self.success_count = success_count
        self.timestamp = timestamp
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.qtype is not None:
            result['Qtype'] = self.qtype

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Qtype') is not None:
            self.qtype = m.get('Qtype')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

