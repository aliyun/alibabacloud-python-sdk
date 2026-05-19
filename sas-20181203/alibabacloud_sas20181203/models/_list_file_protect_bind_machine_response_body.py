# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListFileProtectBindMachineResponseBody(DaraModel):
    def __init__(
        self,
        list: List[str] = None,
        page_info: main_models.ListFileProtectBindMachineResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.list = list
        self.page_info = page_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list is not None:
            result['List'] = self.list

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            self.list = m.get('List')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListFileProtectBindMachineResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFileProtectBindMachineResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

