# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PunishFileRequest(DaraModel):
    def __init__(
        self,
        action_code: str = None,
        drive_id: str = None,
        file_id: str = None,
        punish_reason: str = None,
    ):
        # This parameter is required.
        self.action_code = action_code
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id
        self.punish_reason = punish_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_code is not None:
            result['action_code'] = self.action_code

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.punish_reason is not None:
            result['punish_reason'] = self.punish_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_code') is not None:
            self.action_code = m.get('action_code')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('punish_reason') is not None:
            self.punish_reason = m.get('punish_reason')

        return self

