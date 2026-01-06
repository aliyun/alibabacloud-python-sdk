# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetQueryOptimizeExecErrorStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQueryOptimizeExecErrorStatsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of entries that are returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetQueryOptimizeExecErrorStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQueryOptimizeExecErrorStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: List[main_models.GetQueryOptimizeExecErrorStatsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The information about the SQL templates that failed to execute.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetQueryOptimizeExecErrorStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQueryOptimizeExecErrorStatsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        error_code: str = None,
        error_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        sql_id: str = None,
        sql_text: str = None,
    ):
        # The name of the database.
        self.dbname = dbname
        # The error code returned if the request failed.
        self.error_code = error_code
        # The number of errors.
        self.error_count = error_count
        # The instance ID.
        self.instance_id = instance_id
        # The alias of the database instance.
        self.instance_name = instance_name
        # The SQL template ID.
        self.sql_id = sql_id
        # The content of the SQL template.
        self.sql_text = sql_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['Dbname'] = self.dbname

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        return self

