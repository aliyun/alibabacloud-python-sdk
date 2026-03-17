# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateACLResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the ACL.
        self.acl_id = acl_id
        # The type of SAG instance to be associated with the ACL.
        self.acl_type = acl_type
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the ACL belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

