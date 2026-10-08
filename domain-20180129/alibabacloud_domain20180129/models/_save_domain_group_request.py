# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveDomainGroupRequest(DaraModel):
    def __init__(
        self,
        domain_group_id: int = None,
        domain_group_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # Domain group ID. If this parameter is not provided, a new group is created. If it is provided, the domain group name is updated.
        self.domain_group_id = domain_group_id
        # Domain Name Group Name.
        # 
        # This parameter is required.
        self.domain_group_name = domain_group_name
        # Language for error messages returned by the API. Valid values:  
        # - **zh**: Chinese;  
        # - **en**: English.  
        # 
        # Default value is **en**.
        self.lang = lang
        # User IP address.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_group_name is not None:
            result['DomainGroupName'] = self.domain_group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

