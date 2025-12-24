# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUserTrafficLogResponseBody(DaraModel):
    def __init__(
        self,
        domain_log_details: main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetails = None,
        domain_name: str = None,
        request_id: str = None,
    ):
        self.domain_log_details = domain_log_details
        self.domain_name = domain_name
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
            temp_model = main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m.get('DomainLogDetails'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveUserTrafficLogResponseBodyDomainLogDetails(DaraModel):
    def __init__(
        self,
        domain_log_detail: List[main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetail] = None,
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
                temp_model = main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k1))

        return self

class DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetail(DaraModel):
    def __init__(
        self,
        log_count: int = None,
        log_infos: main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos = None,
        page_infos: main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos = None,
    ):
        self.log_count = log_count
        self.log_infos = log_infos
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
            temp_model = main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m.get('LogInfos'))

        if m.get('PageInfos') is not None:
            temp_model = main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m.get('PageInfos'))

        return self

class DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
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

class DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(DaraModel):
    def __init__(
        self,
        log_info_detail: List[main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail] = None,
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
                temp_model = main_models.DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k1))

        return self

class DescribeLiveUserTrafficLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        log_name: str = None,
        log_path: str = None,
        log_size: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.log_name = log_name
        self.log_path = log_path
        self.log_size = log_size
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

