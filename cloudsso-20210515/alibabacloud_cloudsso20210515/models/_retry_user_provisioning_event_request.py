# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryUserProvisioningEventRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        duplication_strategy: str = None,
        event_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
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

        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy

        if self.event_id is not None:
            result['EventId'] = self.event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        return self

