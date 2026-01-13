# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

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
        # Queries job filter conditions.
        self.filter = filter
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries on the current page. Default value: 50. Maximum value: 100.
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
        # The sorting label. Valid values:
        # 
        # *   time_start
        # *   job_name
        self.label = label
        # The sorting order. Valid values:
        # 
        # *   ASC (default): ascending order
        # *   DESC: descending order
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
        job_name: str = None,
        status: str = None,
        time_created_after: int = None,
        time_created_before: int = None,
    ):
        # The ID of the job.
        self.job_id = job_id
        # The job name. Fuzzy search is supported.
        self.job_name = job_name
        # The job status. Valid values:
        # 
        # *   Pending
        # *   initing
        # *   Succeed
        # *   Failed
        # *   Running
        # *   Exception
        # *   Retrying
        # *   Expired
        # *   Suspended
        # *   Restarting
        # *   Deleted
        self.status = status
        # For jobs submitted after this time, the time in the region is converted into a UNIX timestamp (UI8).
        self.time_created_after = time_created_after
        # For jobs submitted before this time, the time in the region is converted into a Unix timestamp (for domestic sites, the UI8 region).
        self.time_created_before = time_created_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.status is not None:
            result['Status'] = self.status

        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after

        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')

        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')

        return self

