# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScanFileInputConfig(DaraModel):
    def __init__(
        self,
        auto_crop: str = None,
        auto_rotate: str = None,
    ):
        self.auto_crop = auto_crop
        self.auto_rotate = auto_rotate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_crop is not None:
            result['autoCrop'] = self.auto_crop

        if self.auto_rotate is not None:
            result['autoRotate'] = self.auto_rotate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoCrop') is not None:
            self.auto_crop = m.get('autoCrop')

        if m.get('autoRotate') is not None:
            self.auto_rotate = m.get('autoRotate')

        return self

