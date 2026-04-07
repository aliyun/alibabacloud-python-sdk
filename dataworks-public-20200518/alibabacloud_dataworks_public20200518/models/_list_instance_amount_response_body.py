# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListInstanceAmountResponseBody(DaraModel):
    def __init__(
        self,
        instance_counts: List[main_models.ListInstanceAmountResponseBodyInstanceCounts] = None,
        request_id: str = None,
    ):
        # The trend of the number of auto triggered node instances within the specified period of time.
        self.instance_counts = instance_counts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_counts:
            for v1 in self.instance_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceCounts'] = []
        if self.instance_counts is not None:
            for k1 in self.instance_counts:
                result['InstanceCounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_counts = []
        if m.get('InstanceCounts') is not None:
            for k1 in m.get('InstanceCounts'):
                temp_model = main_models.ListInstanceAmountResponseBodyInstanceCounts()
                self.instance_counts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstanceAmountResponseBodyInstanceCounts(DaraModel):
    def __init__(
        self,
        count: int = None,
        date: int = None,
    ):
        # The number of auto triggered node instances.
        self.count = count
        # The data timestamp at which the number of auto triggered node instances was obtained. This value is a UNIX timestamp.
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

