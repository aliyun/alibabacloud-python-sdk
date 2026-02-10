# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartPreCheckDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        create_mark: str = None,
        request_id: str = None,
    ):
        # The ID of the database precheck task.
        self.create_mark = create_mark
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_mark is not None:
            result['CreateMark'] = self.create_mark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMark') is not None:
            self.create_mark = m.get('CreateMark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

