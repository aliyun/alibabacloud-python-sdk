# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class QueryDISyncTaskConfigProcessResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryDISyncTaskConfigProcessResultResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information returned for the parameters that are asynchronously generated and used to create or update a real-time synchronization task in Data Integration.
        self.data = data
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryDISyncTaskConfigProcessResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDISyncTaskConfigProcessResultResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
        task_content: str = None,
    ):
        # The reason why the parameters fail to be obtained. If the parameters are obtained, the value null is returned.
        self.message = message
        # Indicates whether the parameters are obtained. Valid values:
        # 
        # *   success: The parameters are obtained.
        # *   fail: The parameters fail to be obtained. You can view the reason for the failure and troubleshoot the issue based on the reason.
        self.status = status
        # The parameters that are obtained. The parameters are used as the request parameters of the [CreateDISyncTask](https://help.aliyun.com/document_detail/278725.html) or [UpdateDISyncTask](https://help.aliyun.com/document_detail/289109.html) operation to create or update a real-time synchronization task in Data Integration.
        self.task_content = task_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.task_content is not None:
            result['TaskContent'] = self.task_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskContent') is not None:
            self.task_content = m.get('TaskContent')

        return self

