# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecycleBinConfig(DaraModel):
    def __init__(
        self,
        auto_delete_enabled: bool = None,
        auto_delete_keep_second: int = None,
        delete_trash_normal_file_disabled: bool = None,
    ):
        self.auto_delete_enabled = auto_delete_enabled
        self.auto_delete_keep_second = auto_delete_keep_second
        self.delete_trash_normal_file_disabled = delete_trash_normal_file_disabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_delete_enabled is not None:
            result['auto_delete_enabled'] = self.auto_delete_enabled

        if self.auto_delete_keep_second is not None:
            result['auto_delete_keep_second'] = self.auto_delete_keep_second

        if self.delete_trash_normal_file_disabled is not None:
            result['delete_trash_normal_file_disabled'] = self.delete_trash_normal_file_disabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_delete_enabled') is not None:
            self.auto_delete_enabled = m.get('auto_delete_enabled')

        if m.get('auto_delete_keep_second') is not None:
            self.auto_delete_keep_second = m.get('auto_delete_keep_second')

        if m.get('delete_trash_normal_file_disabled') is not None:
            self.delete_trash_normal_file_disabled = m.get('delete_trash_normal_file_disabled')

        return self

