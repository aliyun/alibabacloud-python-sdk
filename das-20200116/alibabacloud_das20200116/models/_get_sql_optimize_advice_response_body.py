# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetSqlOptimizeAdviceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSqlOptimizeAdviceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        # The details, including the total number of entries and error codes.
        self.data = data
        # The message returned for the request.
        # >If the request is successful, Successful is returned. If the request fails, an error message is returned, such as an error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: successful.
        # - **false**: failed.
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
            temp_model = main_models.GetSqlOptimizeAdviceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSqlOptimizeAdviceResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        expire_time: str = None,
        status: str = None,
        status_code: str = None,
        task_id: str = None,
    ):
        # The time when the task was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The download URL of the file.
        self.download_url = download_url
        # The time when the file expires. The value is a UNIX timestamp. Unit: milliseconds.
        # >The file expires three days after the task is created.
        self.expire_time = expire_time
        # The task status. Valid values:
        # 
        # - **INIT**: initializing.
        # - **RUNNING**: running.
        # - **FINISH**: completed.
        # - **FAILED**: failed.
        self.status = status
        # The task status code. Valid values:
        # 
        # - **NO_DATA**: no data available.
        # - **INTERNAL_ERROR**: internal error.
        # - **SUCCESS**: successful.
        self.status_code = status_code
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

