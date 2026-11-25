# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListChartReleaseResponseBody(DaraModel):
    def __init__(
        self,
        chart_releases: List[main_models.ListChartReleaseResponseBodyChartReleases] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of chart versions.
        self.chart_releases = chart_releases
        # The return code.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.chart_releases:
            for v1 in self.chart_releases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChartReleases'] = []
        if self.chart_releases is not None:
            for k1 in self.chart_releases:
                result['ChartReleases'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chart_releases = []
        if m.get('ChartReleases') is not None:
            for k1 in m.get('ChartReleases'):
                temp_model = main_models.ListChartReleaseResponseBodyChartReleases()
                self.chart_releases.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListChartReleaseResponseBodyChartReleases(DaraModel):
    def __init__(
        self,
        chart: str = None,
        instance_id: str = None,
        modified_time: int = None,
        release: str = None,
        repo_id: str = None,
        size: str = None,
        status: str = None,
    ):
        # The chart version name.
        self.chart = chart
        # The instance ID.
        self.instance_id = instance_id
        # The time when the chart was last modified. The value is a UNIX timestamp in milliseconds.
        self.modified_time = modified_time
        # The chart version number.
        self.release = release
        # The chart repository ID.
        self.repo_id = repo_id
        # The size of the chart version, in bytes.
        self.size = size
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart is not None:
            result['Chart'] = self.chart

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.release is not None:
            result['Release'] = self.release

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

