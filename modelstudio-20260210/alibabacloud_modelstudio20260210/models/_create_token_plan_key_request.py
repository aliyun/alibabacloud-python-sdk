# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTokenPlanKeyRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        caller_uac_account_id: str = None,
        description: str = None,
        namespace_id: str = None,
        workspace_id: str = None,
    ):
        # The account ID.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The account ID of the caller that identifies the initiator of this call.
        self.caller_uac_account_id = caller_uac_account_id
        # The description of the key.
        self.description = description
        # The product namespace ID. For the TokenPlan product, this field is fixed to namespace-1.
        self.namespace_id = namespace_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.caller_uac_account_id is not None:
            result['CallerUacAccountId'] = self.caller_uac_account_id

        if self.description is not None:
            result['Description'] = self.description

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CallerUacAccountId') is not None:
            self.caller_uac_account_id = m.get('CallerUacAccountId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

