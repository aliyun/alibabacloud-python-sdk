# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestoreJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        restore_id: str = None,
        success: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Description of the return message, usually \\"successful\\" when successful, and corresponding error messages when there is an error.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Restore job ID.
        self.restore_id = restore_id
        # Whether the request was successful.
        #   - true: Success
        #   - false: Failure
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

