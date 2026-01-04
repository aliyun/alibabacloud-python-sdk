# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIPv6TranslatorAclListEntryResponseBody(DaraModel):
    def __init__(
        self,
        acl_entry_id: str = None,
        request_id: str = None,
    ):
        # The ID of the ACL entry.
        self.acl_entry_id = acl_entry_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entry_id is not None:
            result['AclEntryId'] = self.acl_entry_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryId') is not None:
            self.acl_entry_id = m.get('AclEntryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

