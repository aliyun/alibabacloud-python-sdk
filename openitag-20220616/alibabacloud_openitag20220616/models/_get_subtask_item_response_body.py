# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class GetSubtaskItemResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        error_code: str = None,
        item: main_models.SubtaskItemDetail = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return code. The default value is 0, indicating normal execution.
        self.code = code
        # Details.
        self.details = details
        # Error code.
        self.error_code = error_code
        # Data item.
        self.item = item
        # Return message of the request.
        # 
        # This parameter is required.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation succeeded. Valid values:
        # - true: The request succeeded.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.item is not None:
            result['Item'] = self.item.to_map()

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

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Item') is not None:
            temp_model = main_models.SubtaskItemDetail()
            self.item = temp_model.from_map(m.get('Item'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

