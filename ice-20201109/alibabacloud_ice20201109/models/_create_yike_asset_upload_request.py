# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeAssetUploadRequest(DaraModel):
    def __init__(
        self,
        file_ext: str = None,
    ):
        # This parameter is required.
        self.file_ext = file_ext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_ext is not None:
            result['FileExt'] = self.file_ext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')

        return self

