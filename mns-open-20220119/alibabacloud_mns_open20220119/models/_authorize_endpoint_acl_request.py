# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeEndpointAclRequest(DaraModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list: List[str] = None,
        endpoint_type: str = None,
    ):
        # The access control list (ACL) policy. Valid value:
        # 
        # - **allow**: A CIDR whitelist. Only allow is supported.
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # A list of CIDR blocks.
        # 
        # This parameter is required.
        self.cidr_list = cidr_list
        # The type of the endpoint. Valid value:
        # 
        # - **public**: An internet endpoint. Only public is supported.
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

        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')

        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

