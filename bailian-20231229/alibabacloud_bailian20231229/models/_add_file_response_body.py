# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The data returned for the request.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code of the request.
        self.status = status
        # Indicates whether the API call was successful. Valid values:
        # 
        # - `true`: The call was successful.
        # 
        # - `false`: The call failed.
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

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddFileResponseBodyData(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        parser: str = None,
    ):
        # The ID of the file. Save this ID for use in subsequent API calls involving this file.
        self.file_id = file_id
        # The parser that was used for the file. A possible value is:
        # 
        # - `DASHSCOPE_DOCMIND`: Alibaba Cloud Document Intelligence
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.parser is not None:
            result['Parser'] = self.parser

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        return self

