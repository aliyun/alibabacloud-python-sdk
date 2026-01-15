# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageByTextRequest(DaraModel):
    def __init__(
        self,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        score_threshold: str = None,
        start: int = None,
        text: str = None,
    ):
        self.distinct_product_id = distinct_product_id
        self.filter = filter
        # This parameter is required.
        self.instance_name = instance_name
        self.num = num
        self.score_threshold = score_threshold
        self.start = start
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.start is not None:
            result['Start'] = self.start

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

