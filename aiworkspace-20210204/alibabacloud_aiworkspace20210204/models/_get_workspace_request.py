# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceRequest(DaraModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to display supplementary information such as the workspace owner. Valid values:
        # 
        # *   false (default)
        # *   true
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

