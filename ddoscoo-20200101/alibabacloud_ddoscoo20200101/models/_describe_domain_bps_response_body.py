# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainBpsResponseBody(DaraModel):
    def __init__(
        self,
        domain_bps: List[main_models.DescribeDomainBpsResponseBodyDomainBps] = None,
        request_id: str = None,
    ):
        # The bandwidths.
        self.domain_bps = domain_bps
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_bps:
            for v1 in self.domain_bps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainBps'] = []
        if self.domain_bps is not None:
            for k1 in self.domain_bps:
                result['DomainBps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_bps = []
        if m.get('DomainBps') is not None:
            for k1 in m.get('DomainBps'):
                temp_model = main_models.DescribeDomainBpsResponseBodyDomainBps()
                self.domain_bps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainBpsResponseBodyDomainBps(DaraModel):
    def __init__(
        self,
        in_bps: int = None,
        index: int = None,
        out_bps: int = None,
    ):
        # The inbound bandwidth. Unit: bit/s.
        self.in_bps = in_bps
        # The index number of the returned data.
        self.index = index
        # The outbound bandwidth. Unit: bit/s.
        self.out_bps = out_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.index is not None:
            result['Index'] = self.index

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        return self

