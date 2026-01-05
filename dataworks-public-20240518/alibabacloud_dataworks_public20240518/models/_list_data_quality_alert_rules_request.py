# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataQualityAlertRulesRequest(DaraModel):
    def __init__(
        self,
        data_quality_scan_id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
    ):
        # The ID of the data quality monitor that the alert rule targets.
        self.data_quality_scan_id = data_quality_scan_id
        # The page number of the results.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of records to return on each page.
        # 
        # This parameter is required.
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_scan_id is not None:
            result['DataQualityScanId'] = self.data_quality_scan_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityScanId') is not None:
            self.data_quality_scan_id = m.get('DataQualityScanId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

