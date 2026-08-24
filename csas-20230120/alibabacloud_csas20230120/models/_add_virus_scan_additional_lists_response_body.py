# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddVirusScanAdditionalListsResponseBody(DaraModel):
    def __init__(
        self,
        list_ids: List[str] = None,
        request_id: str = None,
    ):
        # The list of IDs for the newly added entries. The order is consistent with AdditionalLists in the request.
        self.list_ids = list_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_ids is not None:
            result['ListIds'] = self.list_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListIds') is not None:
            self.list_ids = m.get('ListIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

