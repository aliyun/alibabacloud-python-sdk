# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskWorkforceStatisticRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        stat_type: str = None,
    ):
        # The page number of the member list. The value starts from 1. Default value: 1.
        self.page_number = page_number
        # The number of members per page in a paged query. Default value: 20.
        self.page_size = page_size
        # The statistics type. Valid values:
        # - ITEM: Statistics are collected based on individual review records.
        # - OPERATORCELL: Statistics are collected based on operation units. A single ITEM may contain multiple operation units.
        self.stat_type = stat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.stat_type is not None:
            result['StatType'] = self.stat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')

        return self

