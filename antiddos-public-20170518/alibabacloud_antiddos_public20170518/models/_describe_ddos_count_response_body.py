# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeDdosCountResponseBody(DaraModel):
    def __init__(
        self,
        ddos_count: main_models.DescribeDdosCountResponseBodyDdosCount = None,
        request_id: str = None,
    ):
        # The number of assets that are under DDoS attacks.
        self.ddos_count = ddos_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ddos_count:
            self.ddos_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_count is not None:
            result['DdosCount'] = self.ddos_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosCount') is not None:
            temp_model = main_models.DescribeDdosCountResponseBodyDdosCount()
            self.ddos_count = temp_model.from_map(m.get('DdosCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDdosCountResponseBodyDdosCount(DaraModel):
    def __init__(
        self,
        blackhole_count: int = None,
        defense_count: int = None,
        instacen_count: int = None,
    ):
        # The number of assets for which blackhole filtering is triggered.
        self.blackhole_count = blackhole_count
        # The number of assets for which traffic scrubbing is triggered.
        self.defense_count = defense_count
        # The total number of assets.
        self.instacen_count = instacen_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blackhole_count is not None:
            result['BlackholeCount'] = self.blackhole_count

        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count

        if self.instacen_count is not None:
            result['InstacenCount'] = self.instacen_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeCount') is not None:
            self.blackhole_count = m.get('BlackholeCount')

        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')

        if m.get('InstacenCount') is not None:
            self.instacen_count = m.get('InstacenCount')

        return self

