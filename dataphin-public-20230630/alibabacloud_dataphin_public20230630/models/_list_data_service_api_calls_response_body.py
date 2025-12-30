# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiCallsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServiceApiCallsResponseBodyPageResult = None,
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
            temp_model = main_models.ListDataServiceApiCallsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceApiCallsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        call_log_list: List[main_models.ListDataServiceApiCallsResponseBodyPageResultCallLogList] = None,
        total_count: int = None,
    ):
        self.call_log_list = call_log_list
        self.total_count = total_count

    def validate(self):
        if self.call_log_list:
            for v1 in self.call_log_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallLogList'] = []
        if self.call_log_list is not None:
            for k1 in self.call_log_list:
                result['CallLogList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_log_list = []
        if m.get('CallLogList') is not None:
            for k1 in m.get('CallLogList'):
                temp_model = main_models.ListDataServiceApiCallsResponseBodyPageResultCallLogList()
                self.call_log_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceApiCallsResponseBodyPageResultCallLogList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        app_key: int = None,
        app_name: str = None,
        biz_code: str = None,
        biz_code_description: str = None,
        client_ip: str = None,
        cost_time: int = None,
        end_time: str = None,
        env: int = None,
        execute_cost_time: int = None,
        execute_mode: int = None,
        http_status_code: str = None,
        http_status_description: str = None,
        job_id: str = None,
        project_id: int = None,
        project_name: str = None,
        request_id: str = None,
        request_parameter: str = None,
        request_size: int = None,
        response_parameter: str = None,
        response_size: int = None,
        result_count: int = None,
        sql: str = None,
        start_time: str = None,
        status: int = None,
        successful: bool = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.app_key = app_key
        self.app_name = app_name
        self.biz_code = biz_code
        self.biz_code_description = biz_code_description
        self.client_ip = client_ip
        self.cost_time = cost_time
        self.end_time = end_time
        self.env = env
        self.execute_cost_time = execute_cost_time
        self.execute_mode = execute_mode
        self.http_status_code = http_status_code
        self.http_status_description = http_status_description
        self.job_id = job_id
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id
        self.request_parameter = request_parameter
        self.request_size = request_size
        self.response_parameter = response_parameter
        self.response_size = response_size
        self.result_count = result_count
        self.sql = sql
        self.start_time = start_time
        self.status = status
        self.successful = successful

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

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_code_description is not None:
            result['BizCodeDescription'] = self.biz_code_description

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env is not None:
            result['Env'] = self.env

        if self.execute_cost_time is not None:
            result['ExecuteCostTime'] = self.execute_cost_time

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.http_status_description is not None:
            result['HttpStatusDescription'] = self.http_status_description

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_parameter is not None:
            result['RequestParameter'] = self.request_parameter

        if self.request_size is not None:
            result['RequestSize'] = self.request_size

        if self.response_parameter is not None:
            result['ResponseParameter'] = self.response_parameter

        if self.response_size is not None:
            result['ResponseSize'] = self.response_size

        if self.result_count is not None:
            result['ResultCount'] = self.result_count

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.successful is not None:
            result['Successful'] = self.successful

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizCodeDescription') is not None:
            self.biz_code_description = m.get('BizCodeDescription')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExecuteCostTime') is not None:
            self.execute_cost_time = m.get('ExecuteCostTime')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('HttpStatusDescription') is not None:
            self.http_status_description = m.get('HttpStatusDescription')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestParameter') is not None:
            self.request_parameter = m.get('RequestParameter')

        if m.get('RequestSize') is not None:
            self.request_size = m.get('RequestSize')

        if m.get('ResponseParameter') is not None:
            self.response_parameter = m.get('ResponseParameter')

        if m.get('ResponseSize') is not None:
            self.response_size = m.get('ResponseSize')

        if m.get('ResultCount') is not None:
            self.result_count = m.get('ResultCount')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Successful') is not None:
            self.successful = m.get('Successful')

        return self

