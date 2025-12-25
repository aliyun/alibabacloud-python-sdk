# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccessControlListRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        cidr: str = None,
        instance_id: str = None,
    ):
        # The ID of public network access control
        self.acl_id = acl_id
        # The CIDR blocks.
        self.cidr = cidr
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

