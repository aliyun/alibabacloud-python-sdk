# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListDataQualityScanRunsRequest(DaraModel):
    def __init__(
        self,
        create_time_from: int = None,
        create_time_to: int = None,
        data_quality_scan_id: int = None,
        filter: Dict[str, Any] = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        status: str = None,
    ):
        # The earliest time when the data quality monitor starts to run.
        self.create_time_from = create_time_from
        # The latest time when the data quality monitor starts to run.
        self.create_time_to = create_time_to
        # The ID of the data quality monitor.
        self.data_quality_scan_id = data_quality_scan_id
        # The extended query filter. Supported parameters:
        # 
        # *   TaskInstanceId
        self.filter = filter
        # The page number of the results. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 10.
        self.page_size = page_size
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of sorting fields. Supports fields such as last modified time and creation time. Format: "SortField+SortOrder (Desc/Asc)", where Asc is the default. Valid values:
        # 
        # *   CreateTime (Desc/Asc)
        # *   Id (Desc/Asc)
        self.sort_by = sort_by
        # The status of the data quality check result.
        # 
        # *   Pass
        # *   Running
        # *   Error
        # *   Fail
        # *   Warn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_from is not None:
            result['CreateTimeFrom'] = self.create_time_from

        if self.create_time_to is not None:
            result['CreateTimeTo'] = self.create_time_to

        if self.data_quality_scan_id is not None:
            result['DataQualityScanId'] = self.data_quality_scan_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeFrom') is not None:
            self.create_time_from = m.get('CreateTimeFrom')

        if m.get('CreateTimeTo') is not None:
            self.create_time_to = m.get('CreateTimeTo')

        if m.get('DataQualityScanId') is not None:
            self.data_quality_scan_id = m.get('DataQualityScanId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

