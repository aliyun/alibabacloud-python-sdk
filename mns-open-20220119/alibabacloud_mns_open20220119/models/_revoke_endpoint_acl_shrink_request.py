# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeEndpointAclShrinkRequest(DaraModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list_shrink: str = None,
        endpoint_type: str = None,
    ):
        # The ACL policy. Valid values:
        # 
        # - **allow**: The operation is for a Classless Inter-Domain Routing (CIDR) whitelist. Currently, only \\`allow\\` is supported.
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # The list of network segments.
        # 
        # This parameter is required.
        self.cidr_list_shrink = cidr_list_shrink
        # The endpoint type. Valid values:
        # 
        # - **public**: The Internet endpoint. Currently, only \\`public\\` is supported.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy

        if self.cidr_list_shrink is not None:
            result['CidrList'] = self.cidr_list_shrink

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')

        if m.get('CidrList') is not None:
            self.cidr_list_shrink = m.get('CidrList')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

