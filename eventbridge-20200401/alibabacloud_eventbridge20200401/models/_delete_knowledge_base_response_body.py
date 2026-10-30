# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class DeleteKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.KnowledgeBase = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the API operation. A value of Success indicates that the call is successful. If the call fails, a specific error code is returned.
        self.code = code
        # The information about the deleted knowledge base.
        self.data = data
        # The message returned by the API operation. If the call is successful, the value is Operation success. If the call fails, a specific error description is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is successful.
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
            temp_model = main_models.KnowledgeBase()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

