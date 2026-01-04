# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkAclResponseBody(DaraModel):
    def __init__(
        self,
        network_acl_id: str = None,
        request_id: str = None,
    ):
        # The ID of the network ACL.
        self.network_acl_id = network_acl_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

