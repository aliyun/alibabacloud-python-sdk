# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasourceFeatureViewsRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        end_date: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        project_name: str = None,
        show_storage_usage: bool = None,
        sort_by: str = None,
        start_date: str = None,
        type: str = None,
        verbose: bool = None,
    ):
        self.all = all
        self.end_date = end_date
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.project_name = project_name
        self.show_storage_usage = show_storage_usage
        self.sort_by = sort_by
        self.start_date = start_date
        self.type = type
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.show_storage_usage is not None:
            result['ShowStorageUsage'] = self.show_storage_usage

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.type is not None:
            result['Type'] = self.type

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ShowStorageUsage') is not None:
            self.show_storage_usage = m.get('ShowStorageUsage')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

