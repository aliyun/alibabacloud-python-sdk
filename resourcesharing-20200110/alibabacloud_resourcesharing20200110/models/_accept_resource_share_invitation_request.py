# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AcceptResourceShareInvitationRequest(DaraModel):
    def __init__(
        self,
        resource_share_invitation_id: str = None,
    ):
        # The ID of the resource sharing invitation.
        # 
        # You can call the [ListResourceShareInvitations](https://help.aliyun.com/document_detail/450564.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.resource_share_invitation_id = resource_share_invitation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')

        return self

