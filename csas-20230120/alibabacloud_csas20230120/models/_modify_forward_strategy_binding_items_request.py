# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyForwardStrategyBindingItemsRequest(DaraModel):
    def __init__(
        self,
        forward_id: str = None,
        item_ids: List[str] = None,
        match_mode: str = None,
        modify_type: str = None,
    ):
        # The forwarding rule ID.
        # 
        # This parameter is required.
        self.forward_id = forward_id
        # The list of binding item IDs. Must be empty when MatchMode is **UserGroupAll** or **ApplicationAll**. Required for other values. Duplicates are not allowed in the list, and the specified objects must already exist.
        self.item_ids = item_ids
        # The policy matching target type. Required. Valid values:
        # - **UserGroupAll**: associates with all users.
        # - **UserGroupNormal**: associates with specific user groups.
        # - **ApplicationAll**: all private network applications.
        # - **Application**: specific private network applications.
        # - **Tag**: private network application tags.
        # 
        # When the value is **UserGroupAll** or **ApplicationAll**, ItemIds must be empty. When the value is **UserGroupNormal**, **Application**, or **Tag**, ItemIds is required.
        # 
        # When ModifyType is not **Cover**, switching the matching target type is not allowed: **Application**, **Tag**, and **ApplicationAll** are mutually exclusive, and **UserGroupNormal** and **UserGroupAll** are mutually exclusive. If a binding item of a mutually exclusive type already exists on the same forwarding rule, the request is rejected.
        self.match_mode = match_mode
        # The modification method. Required. Valid values:
        # - **Append**: appends to existing binding items. ItemIds cannot contain objects that are already bound.
        # - **Delete**: deletes specified binding items. All objects in ItemIds must be already bound.
        # - **Cover**: overwrites binding items of the same category by clearing all existing binding items of the same category on the forwarding rule and then writing ItemIds. The same category refers to **ApplicationAll**, **Application**, and **Tag**, or **UserGroupAll** and **UserGroupNormal**.
        # 
        # When the value is **Append** or **Delete**, MatchMode cannot be **UserGroupAll** or **ApplicationAll**.
        self.modify_type = modify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_id is not None:
            result['ForwardId'] = self.forward_id

        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardId') is not None:
            self.forward_id = m.get('ForwardId')

        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        return self

