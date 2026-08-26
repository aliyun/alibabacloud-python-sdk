# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetLiveDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        dry_run: bool = None,
        functions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The domain names that you want to configure in batches. Valid values: ingest domain names, primary streaming domain names, and secondary streaming domain names. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_names = domain_names
        self.dry_run = dry_run
        # The list of features.
        # 
        # Some features, such as `filetype_based_ttl_set`, allow you to set multiple records. If you want to update a specific record, you can specify the record by its `configId`. For more information, refer to **Functions format description** and **Functions feature description** below.
        # 
        # This parameter is required.
        self.functions = functions
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.functions is not None:
            result['Functions'] = self.functions

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Functions') is not None:
            self.functions = m.get('Functions')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

