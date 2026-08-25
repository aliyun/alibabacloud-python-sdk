# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserProvisioningEventRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        event_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning event.
        # 
        # You can call the [ListUserProvisioningEvents](https://help.aliyun.com/document_detail/2636305.html) operation to query the value of `EventId`.
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        return self

