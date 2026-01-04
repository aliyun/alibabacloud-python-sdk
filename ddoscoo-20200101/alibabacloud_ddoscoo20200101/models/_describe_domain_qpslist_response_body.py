# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainQPSListResponseBody(DaraModel):
    def __init__(
        self,
        domain_qpslist: List[main_models.DescribeDomainQPSListResponseBodyDomainQPSList] = None,
        request_id: str = None,
    ):
        # An array that consists of the statistics on the QPS of the website.
        self.domain_qpslist = domain_qpslist
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_qpslist:
            for v1 in self.domain_qpslist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainQPSList'] = []
        if self.domain_qpslist is not None:
            for k1 in self.domain_qpslist:
                result['DomainQPSList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_qpslist = []
        if m.get('DomainQPSList') is not None:
            for k1 in m.get('DomainQPSList'):
                temp_model = main_models.DescribeDomainQPSListResponseBodyDomainQPSList()
                self.domain_qpslist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainQPSListResponseBodyDomainQPSList(DaraModel):
    def __init__(
        self,
        attack_qps: int = None,
        cache_hits: int = None,
        index: int = None,
        max_attack_qps: int = None,
        max_normal_qps: int = None,
        max_qps: int = None,
        time: int = None,
        total_count: int = None,
        total_qps: int = None,
    ):
        # The attack QPS.
        self.attack_qps = attack_qps
        # The number of cache hits.
        self.cache_hits = cache_hits
        # The index number of the returned data.
        self.index = index
        # The peak attack QPS.
        self.max_attack_qps = max_attack_qps
        # The peak of normal QPS.
        self.max_normal_qps = max_normal_qps
        # The peak of total QPS.
        self.max_qps = max_qps
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
        self.time = time
        # The total number of requests.
        self.total_count = total_count
        # The total QPS.
        self.total_qps = total_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_qps is not None:
            result['AttackQps'] = self.attack_qps

        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits

        if self.index is not None:
            result['Index'] = self.index

        if self.max_attack_qps is not None:
            result['MaxAttackQps'] = self.max_attack_qps

        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.time is not None:
            result['Time'] = self.time

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackQps') is not None:
            self.attack_qps = m.get('AttackQps')

        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('MaxAttackQps') is not None:
            self.max_attack_qps = m.get('MaxAttackQps')

        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')

        return self

