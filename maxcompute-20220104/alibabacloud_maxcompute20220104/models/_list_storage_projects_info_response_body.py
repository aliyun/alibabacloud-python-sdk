# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListStorageProjectsInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListStorageProjectsInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: an informational response. The request has been received and is being processed.
        # 
        # - 2xx: a success response. The request has been successfully received, understood, and accepted by the server.
        # 
        # - 3xx: a redirection response. The request is redirected. You must take further action to complete the request.
        # 
        # - 4xx: a client error. The request contains invalid request parameters or syntax, or cannot be fulfilled.
        # 
        # - 5xx: a server error. The server fails to fulfill the request for other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListStorageProjectsInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListStorageProjectsInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_project_info_list: List[main_models.ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList] = None,
        total_count: int = None,
    ):
        # The statistics collection date.
        self.date = date
        # The page number.
        self.page_number = page_number
        # The number of entries on each page.
        self.page_size = page_size
        # The list of project-level storage information.
        self.storage_project_info_list = storage_project_info_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.storage_project_info_list:
            for v1 in self.storage_project_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['storageProjectInfoList'] = []
        if self.storage_project_info_list is not None:
            for k1 in self.storage_project_info_list:
                result['storageProjectInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.storage_project_info_list = []
        if m.get('storageProjectInfoList') is not None:
            for k1 in m.get('storageProjectInfoList'):
                temp_model = main_models.ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList()
                self.storage_project_info_list.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList(DaraModel):
    def __init__(
        self,
        date: str = None,
        long_term_storage: float = None,
        long_term_storage_unit: str = None,
        low_freq_storage: float = None,
        low_freq_storage_unit: str = None,
        project_name: str = None,
        rate: float = None,
        recycle_bin_storage: float = None,
        recycle_bin_storage_unit: str = None,
        standard_storage: float = None,
        standard_storage_unit: str = None,
        timestamp: int = None,
        total_storage: float = None,
        total_storage_unit: str = None,
    ):
        # The statistics collection date. The date is accurate to the day. The date must be in the `YYYYMMdd` format.
        self.date = date
        # The Long Term storage usage.
        self.long_term_storage = long_term_storage
        # The unit of the Long Term storage usage.
        self.long_term_storage_unit = long_term_storage_unit
        # The IA storage class usage.
        self.low_freq_storage = low_freq_storage
        # The unit of the IA storage class usage.
        self.low_freq_storage_unit = low_freq_storage_unit
        # The name of the MaxCompute project.
        self.project_name = project_name
        # The year-over-year change rate of the total storage usage in the last {$recentDays} days.
        self.rate = rate
        # The recycle bin storage usage.
        self.recycle_bin_storage = recycle_bin_storage
        # The unit of the recycle bin storage usage.
        self.recycle_bin_storage_unit = recycle_bin_storage_unit
        # The Standard storage usage.
        self.standard_storage = standard_storage
        # The unit of the Standard storage usage.
        self.standard_storage_unit = standard_storage_unit
        # The timestamp of the last data update.
        self.timestamp = timestamp
        # The total storage usage.
        self.total_storage = total_storage
        # The unit of the total storage usage.
        self.total_storage_unit = total_storage_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.long_term_storage is not None:
            result['longTermStorage'] = self.long_term_storage

        if self.long_term_storage_unit is not None:
            result['longTermStorageUnit'] = self.long_term_storage_unit

        if self.low_freq_storage is not None:
            result['lowFreqStorage'] = self.low_freq_storage

        if self.low_freq_storage_unit is not None:
            result['lowFreqStorageUnit'] = self.low_freq_storage_unit

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.rate is not None:
            result['rate'] = self.rate

        if self.recycle_bin_storage is not None:
            result['recycleBinStorage'] = self.recycle_bin_storage

        if self.recycle_bin_storage_unit is not None:
            result['recycleBinStorageUnit'] = self.recycle_bin_storage_unit

        if self.standard_storage is not None:
            result['standardStorage'] = self.standard_storage

        if self.standard_storage_unit is not None:
            result['standardStorageUnit'] = self.standard_storage_unit

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.total_storage is not None:
            result['totalStorage'] = self.total_storage

        if self.total_storage_unit is not None:
            result['totalStorageUnit'] = self.total_storage_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('longTermStorage') is not None:
            self.long_term_storage = m.get('longTermStorage')

        if m.get('longTermStorageUnit') is not None:
            self.long_term_storage_unit = m.get('longTermStorageUnit')

        if m.get('lowFreqStorage') is not None:
            self.low_freq_storage = m.get('lowFreqStorage')

        if m.get('lowFreqStorageUnit') is not None:
            self.low_freq_storage_unit = m.get('lowFreqStorageUnit')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('recycleBinStorage') is not None:
            self.recycle_bin_storage = m.get('recycleBinStorage')

        if m.get('recycleBinStorageUnit') is not None:
            self.recycle_bin_storage_unit = m.get('recycleBinStorageUnit')

        if m.get('standardStorage') is not None:
            self.standard_storage = m.get('standardStorage')

        if m.get('standardStorageUnit') is not None:
            self.standard_storage_unit = m.get('standardStorageUnit')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('totalStorage') is not None:
            self.total_storage = m.get('totalStorage')

        if m.get('totalStorageUnit') is not None:
            self.total_storage_unit = m.get('totalStorageUnit')

        return self

