# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateAclsWithListenerResponseBody(DaraModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        # The ID of the ACL.
        self.acl_ids = acl_ids
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

