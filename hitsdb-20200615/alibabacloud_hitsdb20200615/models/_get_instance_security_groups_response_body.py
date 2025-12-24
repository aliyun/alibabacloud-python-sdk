# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetInstanceSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        request_id: str = None,
        security_groups: List[str] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.instance_id = instance_id
        self.request_id = request_id
        self.security_groups = security_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')

        return self

