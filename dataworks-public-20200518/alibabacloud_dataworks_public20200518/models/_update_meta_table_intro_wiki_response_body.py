# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaTableIntroWikiResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        update_result: bool = None,
    ):
        # The request ID. You can troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the instructions on how to use the table are updated.
        self.update_result = update_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_result is not None:
            result['UpdateResult'] = self.update_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateResult') is not None:
            self.update_result = m.get('UpdateResult')

        return self

