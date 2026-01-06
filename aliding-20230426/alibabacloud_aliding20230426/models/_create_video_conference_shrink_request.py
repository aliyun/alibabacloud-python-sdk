# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVideoConferenceShrinkRequest(DaraModel):
    def __init__(
        self,
        conf_title: str = None,
        invite_caller: bool = None,
        invite_user_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.conf_title = conf_title
        self.invite_caller = invite_caller
        self.invite_user_ids_shrink = invite_user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conf_title is not None:
            result['ConfTitle'] = self.conf_title

        if self.invite_caller is not None:
            result['InviteCaller'] = self.invite_caller

        if self.invite_user_ids_shrink is not None:
            result['InviteUserIds'] = self.invite_user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfTitle') is not None:
            self.conf_title = m.get('ConfTitle')

        if m.get('InviteCaller') is not None:
            self.invite_caller = m.get('InviteCaller')

        if m.get('InviteUserIds') is not None:
            self.invite_user_ids_shrink = m.get('InviteUserIds')

        return self

