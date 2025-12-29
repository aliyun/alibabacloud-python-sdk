# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotInfoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The basic information about the robot, in the JSON format. The basic information contains the following parameters:
        # 
        # *   **id**: the robot ID.
        # *   **robotName**: the robot name.
        # *   **robotType**: the robot type.
        # *   **auditStatus**: the review state.
        # *   **gmtCreate**: the time when the task was created.
        # *   **gmtModified**: the time when the task was modified.
        # *   **partnerId**: the partner ID.
        # *   **asrId**: the ID of the automatic speech recognition (ASR) model.
        # *   **asrType**: the ASR type. Valid values: **Public** and **Private**.
        # *   **remark**: the additional information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

