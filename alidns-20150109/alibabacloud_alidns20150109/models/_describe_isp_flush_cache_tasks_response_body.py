# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeIspFlushCacheTasksResponseBody(DaraModel):
    def __init__(
        self,
        isp_flush_cache_tasks: List[main_models.DescribeIspFlushCacheTasksResponseBodyIspFlushCacheTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.isp_flush_cache_tasks = isp_flush_cache_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.isp_flush_cache_tasks:
            for v1 in self.isp_flush_cache_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspFlushCacheTasks'] = []
        if self.isp_flush_cache_tasks is not None:
            for k1 in self.isp_flush_cache_tasks:
                result['IspFlushCacheTasks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_flush_cache_tasks = []
        if m.get('IspFlushCacheTasks') is not None:
            for k1 in m.get('IspFlushCacheTasks'):
                temp_model = main_models.DescribeIspFlushCacheTasksResponseBodyIspFlushCacheTasks()
                self.isp_flush_cache_tasks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeIspFlushCacheTasksResponseBodyIspFlushCacheTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        domain_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isp = isp
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

