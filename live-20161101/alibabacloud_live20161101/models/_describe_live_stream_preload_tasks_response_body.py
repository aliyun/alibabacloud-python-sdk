# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamPreloadTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        preload_tasks: main_models.DescribeLiveStreamPreloadTasksResponseBodyPreloadTasks = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The details of the prefetch task.
        self.preload_tasks = preload_tasks
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.preload_tasks:
            self.preload_tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.preload_tasks is not None:
            result['PreloadTasks'] = self.preload_tasks.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PreloadTasks') is not None:
            temp_model = main_models.DescribeLiveStreamPreloadTasksResponseBodyPreloadTasks()
            self.preload_tasks = temp_model.from_map(m.get('PreloadTasks'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveStreamPreloadTasksResponseBodyPreloadTasks(DaraModel):
    def __init__(
        self,
        preload_task: List[main_models.DescribeLiveStreamPreloadTasksResponseBodyPreloadTasksPreloadTask] = None,
    ):
        self.preload_task = preload_task

    def validate(self):
        if self.preload_task:
            for v1 in self.preload_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreloadTask'] = []
        if self.preload_task is not None:
            for k1 in self.preload_task:
                result['PreloadTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.preload_task = []
        if m.get('PreloadTask') is not None:
            for k1 in m.get('PreloadTask'):
                temp_model = main_models.DescribeLiveStreamPreloadTasksResponseBodyPreloadTasksPreloadTask()
                self.preload_task.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamPreloadTasksResponseBodyPreloadTasksPreloadTask(DaraModel):
    def __init__(
        self,
        area: str = None,
        create_time: str = None,
        description: str = None,
        domain_name: str = None,
        play_url: str = None,
        preloaded_end_time: str = None,
        preloaded_start_time: str = None,
        process: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The acceleration region where the live content is prefetched. Valid values:
        # 
        # *   domestic: regions in the Chinese mainland.
        # *   overseas: regions outside the Chinese mainland.
        # *   global: regions in and outside the Chinese mainland.
        # 
        # >  If this parameter is left empty, the acceleration region configured for the domain name is returned.
        self.area = area
        # The time when the prefetch task was created.
        self.create_time = create_time
        # Indicates whether the prefetch task is successful. Valid values:
        # 
        # *   Successfully
        # *   InternalError
        self.description = description
        # The streaming domain name.
        self.domain_name = domain_name
        # The streaming URL.
        self.play_url = play_url
        # The time when the prefetch task ended.
        self.preloaded_end_time = preloaded_end_time
        # The time when the prefetch task started.
        self.preloaded_start_time = preloaded_start_time
        # The progress of the prefetch task.
        self.process = process
        # The status of the prefetch task. Valid values:
        # 
        # *   Success
        # *   Failed
        # 
        # >  Success is returned only if the prefetch task is configured for all streaming URLs.
        self.status = status
        # The ID of the prefetch task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.preloaded_end_time is not None:
            result['PreloadedEndTime'] = self.preloaded_end_time

        if self.preloaded_start_time is not None:
            result['PreloadedStartTime'] = self.preloaded_start_time

        if self.process is not None:
            result['Process'] = self.process

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('PreloadedEndTime') is not None:
            self.preloaded_end_time = m.get('PreloadedEndTime')

        if m.get('PreloadedStartTime') is not None:
            self.preloaded_start_time = m.get('PreloadedStartTime')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

