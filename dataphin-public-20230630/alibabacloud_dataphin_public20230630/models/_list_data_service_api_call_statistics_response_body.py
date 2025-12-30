# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiCallStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServiceApiCallStatisticsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDataServiceApiCallStatisticsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceApiCallStatisticsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        call_statistics_list: List[main_models.ListDataServiceApiCallStatisticsResponseBodyPageResultCallStatisticsList] = None,
        total_count: int = None,
    ):
        self.call_statistics_list = call_statistics_list
        self.total_count = total_count

    def validate(self):
        if self.call_statistics_list:
            for v1 in self.call_statistics_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallStatisticsList'] = []
        if self.call_statistics_list is not None:
            for k1 in self.call_statistics_list:
                result['CallStatisticsList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_statistics_list = []
        if m.get('CallStatisticsList') is not None:
            for k1 in m.get('CallStatisticsList'):
                temp_model = main_models.ListDataServiceApiCallStatisticsResponseBodyPageResultCallStatisticsList()
                self.call_statistics_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceApiCallStatisticsResponseBodyPageResultCallStatisticsList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        app_name_list: List[str] = None,
        authorized_app_count: int = None,
        avg_response_time: float = None,
        call_count: int = None,
        creator: str = None,
        error_count: str = None,
        error_rate: str = None,
        last_call_time: str = None,
        offline_rate: str = None,
        project_id: int = None,
        project_name: str = None,
        sql_id: int = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.app_name_list = app_name_list
        self.authorized_app_count = authorized_app_count
        self.avg_response_time = avg_response_time
        self.call_count = call_count
        self.creator = creator
        self.error_count = error_count
        self.error_rate = error_rate
        self.last_call_time = last_call_time
        self.offline_rate = offline_rate
        self.project_id = project_id
        self.project_name = project_name
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_name_list is not None:
            result['AppNameList'] = self.app_name_list

        if self.authorized_app_count is not None:
            result['AuthorizedAppCount'] = self.authorized_app_count

        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time

        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate

        if self.last_call_time is not None:
            result['LastCallTime'] = self.last_call_time

        if self.offline_rate is not None:
            result['OfflineRate'] = self.offline_rate

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppNameList') is not None:
            self.app_name_list = m.get('AppNameList')

        if m.get('AuthorizedAppCount') is not None:
            self.authorized_app_count = m.get('AuthorizedAppCount')

        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')

        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')

        if m.get('LastCallTime') is not None:
            self.last_call_time = m.get('LastCallTime')

        if m.get('OfflineRate') is not None:
            self.offline_rate = m.get('OfflineRate')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        return self

