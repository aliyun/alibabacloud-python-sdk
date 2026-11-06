# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataProcessJobsRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        source_id: str = None,
    ):
        # The ID of the data processing job used for filtering.
        self.job_id = job_id
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30.
        self.page_size = page_size
        # The ID of the region where the job resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the source PolarFS instance.
        # 
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

