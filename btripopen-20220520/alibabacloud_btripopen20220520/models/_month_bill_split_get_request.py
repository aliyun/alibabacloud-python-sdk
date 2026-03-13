# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MonthBillSplitGetRequest(DaraModel):
    def __init__(
        self,
        bill_batch: str = None,
        bill_month: str = None,
        bill_split_key_list: List[str] = None,
        bill_split_mode: str = None,
    ):
        self.bill_batch = bill_batch
        self.bill_month = bill_month
        self.bill_split_key_list = bill_split_key_list
        # This parameter is required.
        self.bill_split_mode = bill_split_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_batch is not None:
            result['bill_batch'] = self.bill_batch

        if self.bill_month is not None:
            result['bill_month'] = self.bill_month

        if self.bill_split_key_list is not None:
            result['bill_split_key_list'] = self.bill_split_key_list

        if self.bill_split_mode is not None:
            result['bill_split_mode'] = self.bill_split_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_batch') is not None:
            self.bill_batch = m.get('bill_batch')

        if m.get('bill_month') is not None:
            self.bill_month = m.get('bill_month')

        if m.get('bill_split_key_list') is not None:
            self.bill_split_key_list = m.get('bill_split_key_list')

        if m.get('bill_split_mode') is not None:
            self.bill_split_mode = m.get('bill_split_mode')

        return self

