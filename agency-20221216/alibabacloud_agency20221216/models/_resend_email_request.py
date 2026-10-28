# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResendEmailRequest(DaraModel):
    def __init__(
        self,
        invite_id: int = None,
    ):
        # The invitation ID, obtained from the InviteSbuAccount operation.
        # 
        # This parameter is required.
        self.invite_id = invite_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')

        return self

