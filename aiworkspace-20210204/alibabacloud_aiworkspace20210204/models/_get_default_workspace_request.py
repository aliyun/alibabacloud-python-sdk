# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDefaultWorkspaceRequest(DaraModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to return detailed information about the default workspace. The detailed information includes the Conditions list. Valid values:
        # 
        # - false (default): Detailed information is not returned.
        # 
        # - true: Detailed information is returned.
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

