# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTempFileDownloadLinkRequest(DaraModel):
    def __init__(
        self,
        temp_file_key: str = None,
    ):
        # The key that is used to download a file.
        # 
        # This parameter is required.
        self.temp_file_key = temp_file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')

        return self

