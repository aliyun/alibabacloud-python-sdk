# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetQueryOptimizeExecErrorSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQueryOptimizeExecErrorSampleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetQueryOptimizeExecErrorSampleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQueryOptimizeExecErrorSampleResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: List[main_models.GetQueryOptimizeExecErrorSampleResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # A reserved parameter.
        self.extra = extra
        # The queried data.
        self.list = list
        # A reserved parameter.
        self.page_no = page_no
        # A reserved parameter.
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
                temp_model = main_models.GetQueryOptimizeExecErrorSampleResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQueryOptimizeExecErrorSampleResponseBodyDataList(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        error_code: str = None,
        orig_host: str = None,
        sql_id: str = None,
        sql_text: str = None,
        timestamp: int = None,
        user: str = None,
    ):
        # The name of the database.
        self.dbname = dbname
        # The error code returned.
        self.error_code = error_code
        # The IP address of the client that executes the SQL statement.
        self.orig_host = orig_host
        # The SQL template ID.
        self.sql_id = sql_id
        # The content of the SQL statement that failed to be executed.
        self.sql_text = sql_text
        # The point in time when the failed SQL statement was executed. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The username of the client that executes the SQL statement.
        self.user = user

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

        if self.orig_host is not None:
            result['OrigHost'] = self.orig_host

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('OrigHost') is not None:
            self.orig_host = m.get('OrigHost')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

