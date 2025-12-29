# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ListCallTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCallTaskDetailResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        total_page: int = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The information about the task.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of called numbers.
        self.total = total
        # The total number of pages.
        self.total_page = total_page

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCallTaskDetailResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListCallTaskDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        called_num: str = None,
        caller: str = None,
        duration: int = None,
        id: int = None,
        status: str = None,
    ):
        # The called number.
        self.called_num = called_num
        # The calling number.
        self.caller = caller
        # The call duration. Unit: seconds.
        self.duration = duration
        # This parameter is unavailable.
        self.id = id
        # The task state. Valid values:
        # 
        # *   **SUCCESS**: The task was successful.
        # *   **FAIL**: The task failed.
        # *   **INIT**: The task was not started.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_num is not None:
            result['CalledNum'] = self.called_num

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

