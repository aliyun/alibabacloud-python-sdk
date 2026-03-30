# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDefaultDomainRequest(DaraModel):
    def __init__(
        self,
        default_domain_name: str = None,
    ):
        # The default domain name.
        # 
        # The default domain name is in the format of `<AccountAlias>.onaliyun.com`. `<AccountAlias>` indicates the account alias. By default, the value of AccountAlias is the ID of the Alibaba Cloud account. The default domain name must end with `.onaliyun.com`.
        # 
        # The default domain name can contain up to 64 characters in length. The default domain name can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  The default domain name cannot start or end with a hyphen (-) and cannot contain two consecutive hyphens (-).
        # 
        # This parameter is required.
        self.default_domain_name = default_domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')

        return self

