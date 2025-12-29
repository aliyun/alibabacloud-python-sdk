# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCallDetailByCallIdResponseBody(DaraModel):
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
        # The details of the call, in the JSON format.
        # 
        # *   **caller**: the calling number.
        # *   **startDate**: the time when the call was started.
        # *   **stateDesc**: the description of the call state.
        # *   **duration**: the call duration. Unit: seconds. The value **0** indicates that the user was not connected.
        # *   **callerShowNumber**: the calling number displayed to the called party.
        # *   **gmtCreate**: the time when the call request was received.
        # *   **state**: the call state. The call state is returned by the Internet service provider (ISP) in real time. For more information about call states, see [ISP-returned error codes](https://help.aliyun.com/document_detail/55085.html).
        # *   **endDate**: the time when the call was ended.
        # *   **calleeShowNumber**: the number displayed to the called party.
        # *   **callee**: the called number.
        # *   **aRingTime**: the time when Line A started to ring, in the yyyy-MM-dd HH:mm:ss format.
        # *   **aEndTime**: the time when ringing on Line A ended, in the yyyy-MM-dd HH:mm:ss format.
        # *   **bRingTime**: the time when Line B started to ring, in the yyyy-MM-dd HH:mm:ss format.
        # *   **bEndTime**: the time when ringing on Line B ended, in the yyyy-MM-dd HH:mm:ss format.
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

