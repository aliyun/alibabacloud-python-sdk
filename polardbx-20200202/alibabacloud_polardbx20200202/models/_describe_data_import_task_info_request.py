# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataImportTaskInfoRequest(DaraModel):
    def __init__(
        self,
        fail_page_number: int = None,
        fail_page_size: int = None,
        region_id: str = None,
        slink_task_id: str = None,
        success_page_number: int = None,
        success_page_size: int = None,
    ):
        self.fail_page_number = fail_page_number
        self.fail_page_size = fail_page_size
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.slink_task_id = slink_task_id
        self.success_page_number = success_page_number
        self.success_page_size = success_page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_page_number is not None:
            result['FailPageNumber'] = self.fail_page_number

        if self.fail_page_size is not None:
            result['FailPageSize'] = self.fail_page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        if self.success_page_number is not None:
            result['SuccessPageNumber'] = self.success_page_number

        if self.success_page_size is not None:
            result['SuccessPageSize'] = self.success_page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailPageNumber') is not None:
            self.fail_page_number = m.get('FailPageNumber')

        if m.get('FailPageSize') is not None:
            self.fail_page_size = m.get('FailPageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        if m.get('SuccessPageNumber') is not None:
            self.success_page_number = m.get('SuccessPageNumber')

        if m.get('SuccessPageSize') is not None:
            self.success_page_size = m.get('SuccessPageSize')

        return self

