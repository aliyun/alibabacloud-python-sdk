# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationsRequest(DaraModel):
    def __init__(
        self,
        app_versions: str = None,
        cluster_names: str = None,
        level: str = None,
        max_date: str = None,
        min_date: str = None,
        out_app_info_params: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The version number of the application. Separate multiple version numbers with commas (,). If you want to query data of all versions of applications, specify All for this parameter. By default, only data of applications in the stable versions are queried.
        self.app_versions = app_versions
        # The name of the application cluster. Separate multiple names with commas (,). If you want to query applications of all clusters in your account, specify All for this parameter. Default value: All.
        self.cluster_names = cluster_names
        # The region level by which edge resources of the application are collected. The value is of the enumeration type. Valid values:
        # 
        # *   National: Chinese mainland
        # *   Big: area
        # *   Middle: province
        # *   Small: city
        # *   RegionId: edge node
        # 
        # Default value: National.
        self.level = level
        # The end of the time range to query. Specify the time in the 2006-01-02 format. By default, the time range to query is not restricted.
        self.max_date = max_date
        # The beginning of the time range to query. Specify the time in the 2006-01-02 format. By default, the time range to query is not restricted.
        self.min_date = min_date
        # Specifies whether to return other information about the application, such as statistics on resource instances and pods. The value must be a JSON string. By default, all information is returned.
        self.out_app_info_params = out_app_info_params
        # The page number. Pages start from page 1. This parameter is optional if you want to return the push status of all data files.
        self.page_number = page_number
        # The number of entries per page. This parameter is optional if you want to return all information about the applications.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions

        if self.cluster_names is not None:
            result['ClusterNames'] = self.cluster_names

        if self.level is not None:
            result['Level'] = self.level

        if self.max_date is not None:
            result['MaxDate'] = self.max_date

        if self.min_date is not None:
            result['MinDate'] = self.min_date

        if self.out_app_info_params is not None:
            result['OutAppInfoParams'] = self.out_app_info_params

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')

        if m.get('ClusterNames') is not None:
            self.cluster_names = m.get('ClusterNames')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')

        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')

        if m.get('OutAppInfoParams') is not None:
            self.out_app_info_params = m.get('OutAppInfoParams')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

