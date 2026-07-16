# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateFileTagShrinkRequest(DaraModel):
    def __init__(
        self,
        file_infos_shrink: str = None,
        update_mode: str = None,
    ):
        # A list of files to update.
        # 
        # This parameter is required.
        self.file_infos_shrink = file_infos_shrink
        # The update mode. Valid values are APPEND and OVERWRITE.
        self.update_mode = update_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_infos_shrink is not None:
            result['FileInfos'] = self.file_infos_shrink

        if self.update_mode is not None:
            result['UpdateMode'] = self.update_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileInfos') is not None:
            self.file_infos_shrink = m.get('FileInfos')

        if m.get('UpdateMode') is not None:
            self.update_mode = m.get('UpdateMode')

        return self

