# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainLogResponseBody(DaraModel):
    def __init__(
        self,
        domain_log_details: main_models.DescribeLiveDomainLogResponseBodyDomainLogDetails = None,
        domain_name: str = None,
        request_id: str = None,
    ):
        # The log information.
        self.domain_log_details = domain_log_details
        # The streaming domain or ingest domain.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = main_models.DescribeLiveDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m.get('DomainLogDetails'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainLogResponseBodyDomainLogDetails(DaraModel):
    def __init__(
        self,
        domain_log_detail: List[main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetail] = None,
    ):
        self.domain_log_detail = domain_log_detail

    def validate(self):
        if self.domain_log_detail:
            for v1 in self.domain_log_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainLogDetail'] = []
        if self.domain_log_detail is not None:
            for k1 in self.domain_log_detail:
                result['DomainLogDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log_detail = []
        if m.get('DomainLogDetail') is not None:
            for k1 in m.get('DomainLogDetail'):
                temp_model = main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetail(DaraModel):
    def __init__(
        self,
        log_count: int = None,
        log_infos: main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
        page_infos: main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
    ):
        # The total number of entries returned on the current page.
        self.log_count = log_count
        # Details about the logs.
        self.log_infos = log_infos
        # The page information.
        self.page_infos = page_infos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_count is not None:
            result['LogCount'] = self.log_count

        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()

        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        if m.get('LogInfos') is not None:
            temp_model = main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m.get('LogInfos'))

        if m.get('PageInfos') is not None:
            temp_model = main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m.get('PageInfos'))

        return self

class DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(DaraModel):
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

class DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(DaraModel):
    def __init__(
        self,
        log_info_detail: List[main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
    ):
        self.log_info_detail = log_info_detail

    def validate(self):
        if self.log_info_detail:
            for v1 in self.log_info_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogInfoDetail'] = []
        if self.log_info_detail is not None:
            for k1 in self.log_info_detail:
                result['LogInfoDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info_detail = []
        if m.get('LogInfoDetail') is not None:
            for k1 in m.get('LogInfoDetail'):
                temp_model = main_models.DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        log_name: str = None,
        log_path: str = None,
        log_size: int = None,
        start_time: str = None,
    ):
        # The end of the time range for which the logs were queried.
        self.end_time = end_time
        # The name of the log file.
        self.log_name = log_name
        # The path of the log file.
        self.log_path = log_path
        # The size of the log file.
        self.log_size = log_size
        # The beginning of the time range for which the logs were queried.
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

