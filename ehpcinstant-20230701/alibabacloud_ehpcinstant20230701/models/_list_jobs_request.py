# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.ListJobsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: main_models.ListJobsRequestSortBy = None,
    ):
        # The filter conditions for querying jobs.
        self.filter = filter
        # The current page number.
        # 
        # Start value: 1
        # 
        # Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page. The default value is 50. The maximum value is 100.
        self.page_size = page_size
        # The sorting method.
        self.sort_by = sort_by

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.sort_by:
            self.sort_by.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.ListJobsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            temp_model = main_models.ListJobsRequestSortBy()
            self.sort_by = temp_model.from_map(m.get('SortBy'))

        return self

class ListJobsRequestSortBy(DaraModel):
    def __init__(
        self,
        label: str = None,
        order: str = None,
    ):
        # The field to sort by. Valid values:
        # 
        # - time_start
        # 
        # - job_name
        self.label = label
        # The sort order. Valid values:
        # 
        # - ASC (default): Ascending
        # 
        # - DESC: Descending
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

class ListJobsRequestFilter(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        job_ids: List[str] = None,
        job_name: str = None,
        job_template_id: str = None,
        status: str = None,
        tag: List[main_models.ListJobsRequestFilterTag] = None,
        time_created_after: int = None,
        time_created_before: int = None,
    ):
        # The ID of the job.
        self.job_id = job_id
        self.job_ids = job_ids
        # The name of the job. Fuzzy search is supported.
        self.job_name = job_name
        self.job_template_id = job_template_id
        # The status of the job. Valid values:
        # 
        # - Pending: The job is in the queue.
        # 
        # - Initing: The job is initializing.
        # 
        # - Succeeded: The job was successful.
        # 
        # - Failed: The job failed.
        # 
        # - Running: The job is running.
        # 
        # - Exception: A scheduling exception occurred.
        # 
        # - Retrying: The job is being retried.
        # 
        # - Expired: The job timed out.
        # 
        # - Suspended: The job is in hibernation.
        # 
        # - Restarting: The job is restarting.
        # 
        # - Deleted: The job is deleted.
        self.status = status
        self.tag = tag
        # The time after which the jobs were submitted. This is a UNIX timestamp based on the local time of the region. For sites in the Chinese mainland, the time zone is UTC+8.
        self.time_created_after = time_created_after
        # The time before which the jobs were submitted. This is a UNIX timestamp based on the local time of the region. For sites in the Chinese mainland, the time zone is UTC+8.
        self.time_created_before = time_created_before

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_template_id is not None:
            result['JobTemplateId'] = self.job_template_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after

        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobTemplateId') is not None:
            self.job_template_id = m.get('JobTemplateId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListJobsRequestFilterTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')

        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')

        return self

class ListJobsRequestFilterTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

