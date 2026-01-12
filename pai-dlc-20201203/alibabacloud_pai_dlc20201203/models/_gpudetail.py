# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GPUDetail(DaraModel):
    def __init__(
        self,
        gpu: str = None,
        gputype: str = None,
        gputype_full_name: str = None,
    ):
        self.gpu = gpu
        self.gputype = gputype
        self.gputype_full_name = gputype_full_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')

        return self

