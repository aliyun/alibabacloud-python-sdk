# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCheckReportRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        check_result: int = None,
        job_status: int = None,
        page_index: int = None,
        page_size: int = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.batch_id = batch_id
        self.check_result = check_result
        self.job_status = job_status
        self.page_index = page_index
        self.page_size = page_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.table_name is not None:
            result['tableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        return self

