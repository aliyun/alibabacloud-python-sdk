# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataDistResultShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        ens_region_ids_shrink: str = None,
        instance_ids: str = None,
        max_date: str = None,
        min_date: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data file names. This parameter is a filter condition. You can specify multiple names separated by commas (,). By default, all data files are queried.
        self.data_names = data_names
        # The data file version numbers. This parameter is a filter condition. You can specify multiple versions separated by commas (,). By default, all versions are queried.
        self.data_versions = data_versions
        # The list of ENS edge zone IDs.
        self.ens_region_ids_shrink = ens_region_ids_shrink
        # The list of edge instance IDs. This parameter is a filter condition. You can specify multiple IDs separated by commas (,). By default, all instances are queried.
        self.instance_ids = instance_ids
        # The end date of the query in the format "2006-01-02". By default, no time limit is applied.
        self.max_date = max_date
        # The start date of the query in the format "2006-01-02". By default, no time limit is applied.
        self.min_date = min_date
        # The page number, starting from 1. You do not need to specify this parameter when exporting all data.
        self.page_number = page_number
        # The number of entries per page for paging queries. This parameter is not required when exporting all data.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_names is not None:
            result['DataNames'] = self.data_names

        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions

        if self.ens_region_ids_shrink is not None:
            result['EnsRegionIds'] = self.ens_region_ids_shrink

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_date is not None:
            result['MaxDate'] = self.max_date

        if self.min_date is not None:
            result['MinDate'] = self.min_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')

        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids_shrink = m.get('EnsRegionIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')

        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

