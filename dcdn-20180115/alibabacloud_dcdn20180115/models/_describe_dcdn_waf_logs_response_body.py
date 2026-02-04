# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafLogsResponseBody(DaraModel):
    def __init__(
        self,
        domain_log_details: List[main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetails] = None,
        request_id: str = None,
    ):
        # Details about logs returned.
        self.domain_log_details = domain_log_details
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_log_details:
            for v1 in self.domain_log_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainLogDetails'] = []
        if self.domain_log_details is not None:
            for k1 in self.domain_log_details:
                result['DomainLogDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log_details = []
        if m.get('DomainLogDetails') is not None:
            for k1 in m.get('DomainLogDetails'):
                temp_model = main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetails()
                self.domain_log_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafLogsResponseBodyDomainLogDetails(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        log_count: int = None,
        log_infos: List[main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetailsLogInfos] = None,
        page_infos: main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetailsPageInfos = None,
    ):
        # The WAF domain name.
        self.domain_name = domain_name
        # The total number of entries returned on the current page.
        self.log_count = log_count
        # The log information.
        self.log_infos = log_infos
        # The page information.
        self.page_infos = page_infos

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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.log_count is not None:
            result['LogCount'] = self.log_count

        result['LogInfos'] = []
        if self.log_infos is not None:
            for k1 in self.log_infos:
                result['LogInfos'].append(k1.to_map() if k1 else None)

        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        self.log_infos = []
        if m.get('LogInfos') is not None:
            for k1 in m.get('LogInfos'):
                temp_model = main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetailsLogInfos()
                self.log_infos.append(temp_model.from_map(k1))

        if m.get('PageInfos') is not None:
            temp_model = main_models.DescribeDcdnWafLogsResponseBodyDomainLogDetailsPageInfos()
            self.page_infos = temp_model.from_map(m.get('PageInfos'))

        return self

class DescribeDcdnWafLogsResponseBodyDomainLogDetailsPageInfos(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The page number of the returned page.
        self.page_index = page_index
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDcdnWafLogsResponseBodyDomainLogDetailsLogInfos(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        log_name: str = None,
        log_path: str = None,
        log_size: int = None,
        start_time: str = None,
    ):
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The name of the log file.
        self.log_name = log_name
        # The path of the log file.
        self.log_path = log_path
        # The size of the log file. Unit: bytes.
        self.log_size = log_size
        # The beginning of the time range during which data was queried.
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

