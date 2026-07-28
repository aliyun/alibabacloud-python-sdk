# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveSharedAccountsRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The list of Alibaba Cloud account IDs.
        # 
        # This parameter is required.
        self.account_ids = account_ids
        # The ID of the resource to unshare.
        # 
        #  - If the type is Namespace, set this parameter to the workspace name. 
        # 
        # - If the type is RegistryModule, set this parameter to \\<namespaceName>/\\<ModuleName>.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - RegistryModule: Registry template.
        # - Namespace: workspace.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

