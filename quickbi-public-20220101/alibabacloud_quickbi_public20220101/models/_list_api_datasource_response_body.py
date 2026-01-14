# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListApiDatasourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListApiDatasourceResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The query results are returned.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListApiDatasourceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApiDatasourceResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListApiDatasourceResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
    ):
        # The list of API data sources that were queried.
        self.data = data
        # The page number.
        self.page_num = page_num
        # The number of rows per page set when the interface is requested.
        self.page_size = page_size
        # The total number of rows.
        self.total_num = total_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListApiDatasourceResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListApiDatasourceResponseBodyResultData(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        body: str = None,
        data_size: float = None,
        date_update_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        job_id: str = None,
        parameters: str = None,
        show_name: str = None,
        status_type: int = None,
    ):
        # The ID of the API data source.
        self.api_id = api_id
        # The parameter configuration of the query statement in JSON format. You can customize the parameter configuration.
        self.body = body
        # The data volume of the API data source.
        # 
        # *   Unit: Kbit/s
        self.data_size = data_size
        # The last synchronization time of the API data source.
        self.date_update_time = date_update_time
        # The time when the quota plan was created.
        self.gmt_create = gmt_create
        # The time when the optimization job was modified.
        self.gmt_modified = gmt_modified
        # The job ID.
        self.job_id = job_id
        # The parameter configurations in the JSONArray format.
        # 
        # *   name: parameter name
        # *   value: the parameter value
        self.parameters = parameters
        # The name of the API data source.
        self.show_name = show_name
        # The status of the API data source synchronization task.
        # 
        # Valid values:
        # 
        # *   0: the to be run.
        # *   1: The is running.
        # *   2: The is successfully.
        # *   3: failed.
        self.status_type = status_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.body is not None:
            result['Body'] = self.body

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.date_update_time is not None:
            result['DateUpdateTime'] = self.date_update_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.status_type is not None:
            result['StatusType'] = self.status_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DateUpdateTime') is not None:
            self.date_update_time = m.get('DateUpdateTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('StatusType') is not None:
            self.status_type = m.get('StatusType')

        return self

