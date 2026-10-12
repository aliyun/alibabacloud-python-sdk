# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageRequest(DaraModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to display optional information. Optional information currently includes Labels.
        # 
        # Valid values:
        # - false (default): Optional information is not displayed.
        # - true: Optional information is displayed.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

