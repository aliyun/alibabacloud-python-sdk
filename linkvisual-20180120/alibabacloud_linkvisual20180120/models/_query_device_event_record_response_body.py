# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryDeviceEventRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.QueryDeviceEventRecordResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code:
        # 
        # - **200**: The call was successful.
        # - Other: An error code. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The query results.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success

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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryDeviceEventRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDeviceEventRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        file_name: str = None,
        vod_url: str = None,
    ):
        # The start time of the recording.
        self.begin_time = begin_time
        # The end time of the recording.
        self.end_time = end_time
        # The name of the recording file.
        self.file_name = file_name
        # The URL of the recording file.
        # 
        # > The URL contains authentication information and is valid only for a single use. It cannot be reused.
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')

        return self

