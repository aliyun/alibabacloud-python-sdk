# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNetworkAclEntryRequest(DaraModel):
    def __init__(
        self,
        network_acl_entry_id: str = None,
    ):
        # The ID of the network ACL for which you want to delete a rule.
        self.network_acl_entry_id = network_acl_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        return self

