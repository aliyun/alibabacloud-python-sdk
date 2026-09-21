# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteRoutineEnvironmentVariablesResponseBody(DaraModel):
    def __init__(
        self,
        deleted_keys: List[str] = None,
        failed_keys: List[str] = None,
        request_id: str = None,
    ):
        # The list of environment variable keys that were deleted successfully.
        self.deleted_keys = deleted_keys
        # The list of environment variable keys that failed to be deleted.
        self.failed_keys = failed_keys
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted_keys is not None:
            result['DeletedKeys'] = self.deleted_keys

        if self.failed_keys is not None:
            result['FailedKeys'] = self.failed_keys

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedKeys') is not None:
            self.deleted_keys = m.get('DeletedKeys')

        if m.get('FailedKeys') is not None:
            self.failed_keys = m.get('FailedKeys')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

