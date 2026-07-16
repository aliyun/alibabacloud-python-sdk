# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyExpressConnectRouterAssociationAllowedPrefixRequest(DaraModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        owner_account: str = None,
        version: str = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The route prefix mode.
        # 
        # *   MatchMode: After you distribute new route CIDR blocks to data centers, original specific routes that are distributed are withdrawn.
        # *   IncrementalMode: After you distribute new route CIDR blocks to data centers, the original specific routes that fall in the CIDR blocks that you configure are withdrawn, and the original specific routes that do not fall in the CIDR blocks are still distributed.
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The ID of the association between the ECR and the VPC or TR.
        # 
        # This parameter is required.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        self.owner_account = owner_account
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes

        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode

        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')

        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')

        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

