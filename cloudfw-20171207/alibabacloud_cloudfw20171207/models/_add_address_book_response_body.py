# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAddressBookResponseBody(DaraModel):
    def __init__(
        self,
        group_uuid: str = None,
        request_id: str = None,
    ):
        # The UUID of the returned address book.
        self.group_uuid = group_uuid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

