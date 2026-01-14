# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserRequest(DaraModel):
    def __init__(
        self,
        transfer_user_id: str = None,
        user_id: str = None,
    ):
        # The ID of the successor. If not empty, the report resources in the workspace of the deleted user will be transferred to the successor; otherwise, they will be transferred to the space owner.
        # - The successor cannot be an organization visitor
        # - The permissions of the successor in the workspace must not be less than those of the deleted user, with management permissions > development permissions > sharing permissions > viewing permissions
        # - If the successor is not in the workspace, they will be automatically added to the workspace
        self.transfer_user_id = transfer_user_id
        # The ID of the user to be deleted. This user ID is the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transfer_user_id is not None:
            result['TransferUserId'] = self.transfer_user_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransferUserId') is not None:
            self.transfer_user_id = m.get('TransferUserId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

