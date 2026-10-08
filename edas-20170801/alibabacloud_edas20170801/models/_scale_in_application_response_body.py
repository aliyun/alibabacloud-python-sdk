# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleInApplicationResponseBody(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        code: int = None,
        message: str = None,
    ):
        # The ID of the change process for this operation. You can call the GetChangeOrderInfo operation to query the progress of this scale-in. For more information, see [GetChangeOrderInfo](https://help.aliyun.com/document_detail/62072.html). No ID is generated if the ForceStatus parameter is set to true. You can check whether the request is successful based on the value of the Code parameter.
        self.change_order_id = change_order_id
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

