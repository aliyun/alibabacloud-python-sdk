# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTasksRequest(DaraModel):
    def __init__(
        self,
        sorter: main_models.ListMmsTasksRequestSorter = None,
        dst_db_name: str = None,
        dst_table_name: str = None,
        job_id: int = None,
        job_name: str = None,
        page_num: int = None,
        page_size: int = None,
        partition: str = None,
        src_db_name: str = None,
        src_table_name: str = None,
        status: str = None,
    ):
        self.sorter = sorter
        self.dst_db_name = dst_db_name
        self.dst_table_name = dst_table_name
        self.job_id = job_id
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.partition = partition
        self.src_db_name = src_db_name
        self.src_table_name = src_table_name
        self.status = status

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()

        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name

        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.partition is not None:
            result['partition'] = self.partition

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = main_models.ListMmsTasksRequestSorter()
            self.sorter = temp_model.from_map(m.get('sorter'))

        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')

        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('partition') is not None:
            self.partition = m.get('partition')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListMmsTasksRequestSorter(DaraModel):
    def __init__(
        self,
        start_time: str = None,
        status: str = None,
    ):
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

