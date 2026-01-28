# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainSpecialBizInfoByDomainRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        domain_name: str = None,
        user_client_ip: str = None,
    ):
        # The business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

