# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveSpecificStagingConfigRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the configuration that you want to delete. If you want to specify multiple IDs, separate them with commas (,). You can call the [DescribeLiveDomainStagingConfig](https://help.aliyun.com/document_detail/297374.html) operation to obtain the configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The accelerated domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

