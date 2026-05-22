# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteLogsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        site_log_details: List[main_models.DescribeSiteLogsResponseBodySiteLogDetails] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the website log files.
        self.site_log_details = site_log_details

    def validate(self):
        if self.site_log_details:
            for v1 in self.site_log_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SiteLogDetails'] = []
        if self.site_log_details is not None:
            for k1 in self.site_log_details:
                result['SiteLogDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.site_log_details = []
        if m.get('SiteLogDetails') is not None:
            for k1 in m.get('SiteLogDetails'):
                temp_model = main_models.DescribeSiteLogsResponseBodySiteLogDetails()
                self.site_log_details.append(temp_model.from_map(k1))

        return self

class DescribeSiteLogsResponseBodySiteLogDetails(DaraModel):
    def __init__(
        self,
        log_count: int = None,
        log_infos: List[main_models.DescribeSiteLogsResponseBodySiteLogDetailsLogInfos] = None,
        page_infos: main_models.DescribeSiteLogsResponseBodySiteLogDetailsPageInfos = None,
        site_id: int = None,
        site_name: str = None,
    ):
        # The total number of entries returned on the current page.
        self.log_count = log_count
        # The details of the website log files.
        self.log_infos = log_infos
        # Pagination information.
        self.page_infos = page_infos
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name

    def validate(self):
        if self.log_infos:
            for v1 in self.log_infos:
                 if v1:
                    v1.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_count is not None:
            result['LogCount'] = self.log_count

        result['LogInfos'] = []
        if self.log_infos is not None:
            for k1 in self.log_infos:
                result['LogInfos'].append(k1.to_map() if k1 else None)

        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        self.log_infos = []
        if m.get('LogInfos') is not None:
            for k1 in m.get('LogInfos'):
                temp_model = main_models.DescribeSiteLogsResponseBodySiteLogDetailsLogInfos()
                self.log_infos.append(temp_model.from_map(k1))

        if m.get('PageInfos') is not None:
            temp_model = main_models.DescribeSiteLogsResponseBodySiteLogDetailsPageInfos()
            self.page_infos = temp_model.from_map(m.get('PageInfos'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        return self

class DescribeSiteLogsResponseBodySiteLogDetailsPageInfos(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number returned.
        self.page_index = page_index
        # The number of entries per page. Default value: **300**. Valid values: **1 to 1000**.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSiteLogsResponseBodySiteLogDetailsLogInfos(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        log_name: str = None,
        log_path: str = None,
        log_size: int = None,
        start_time: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The name of the log file.
        self.log_name = log_name
        # The log path.
        # 
        # >  Take note of the Expires field (expiration timestamp) in this parameter. If the log download URL expires, you must reobtain the URL.
        self.log_path = log_path
        # The size of the log file. Unit: bytes.
        self.log_size = log_size
        # The create time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_name is not None:
            result['LogName'] = self.log_name

        if self.log_path is not None:
            result['LogPath'] = self.log_path

        if self.log_size is not None:
            result['LogSize'] = self.log_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')

        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')

        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

