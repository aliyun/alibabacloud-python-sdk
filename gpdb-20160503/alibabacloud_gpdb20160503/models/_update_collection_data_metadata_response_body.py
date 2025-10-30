# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCollectionDataMetadataResponseBody(DaraModel):
    def __init__(
        self,
        applied_rows: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # Number of effective entries.
        self.applied_rows = applied_rows
        # Detailed information when the request fails.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Status, with the following values:
        # 
        # - **success**: Success.
        # - **fail**: Failure.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_rows is not None:
            result['AppliedRows'] = self.applied_rows

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedRows') is not None:
            self.applied_rows = m.get('AppliedRows')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

