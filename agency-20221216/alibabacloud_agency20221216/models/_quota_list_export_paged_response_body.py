# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class QuotaListExportPagedResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QuotaListExportPagedResponseBodyData] = None,
        msg: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code of the returned result. A value of 200 indicates success.
        self.code = code
        # The list of returned results.
        self.data = data
        # The description of the returned result.
        self.msg = msg
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuotaListExportPagedResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QuotaListExportPagedResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        file_name: str = None,
        message: str = None,
        status: str = None,
        status_code: str = None,
        url: str = None,
    ):
        # The creation time. The time is in the YYYY-MM-DD HH:mm:ss format in the UTC+8 time zone.
        self.create_time = create_time
        # The name of the file.
        self.file_name = file_name
        # The prompt message.
        self.message = message
        # The display status of the task.
        self.status = status
        # The status code of the task. Valid values:
        # - 2: Exporting.
        # - 3: Export succeeded.
        # - -1: Export failed.
        self.status_code = status_code
        # The download URL of the file.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

