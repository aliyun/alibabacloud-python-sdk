# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConsumerGroupPasswordResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The current password of the consumer group.
        self.err_code = err_code
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.err_message = err_message
        # The username of the consumer group. You can call the [DescribeConsumerGroup](https://help.aliyun.com/document_detail/122886.html) operation to query the username.
        self.request_id = request_id
        # The new password of the consumer group.
        # 
        # *   A password must contain two or more of the following characters: uppercase letters, lowercase letters, digits, and special characters.
        # *   A password must be 8 to 32 characters in length.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

