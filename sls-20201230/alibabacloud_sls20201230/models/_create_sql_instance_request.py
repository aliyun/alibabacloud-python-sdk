# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSqlInstanceRequest(DaraModel):
    def __init__(
        self,
        cu: int = None,
        use_as_default: bool = None,
    ):
        # The number of compute units (CUs). When you use the Dedicated SQL feature, CUs are used in parallel.
        # 
        # This parameter is required.
        self.cu = cu
        # Specifies whether to enable the Dedicated SQL feature for the project. If you set this parameter to true, the Dedicated SQL feature is enabled for the specified project and takes effect for all query statements that you execute in the project, including the query statements for alerts and dashboards.
        # 
        # This parameter is required.
        self.use_as_default = use_as_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.use_as_default is not None:
            result['useAsDefault'] = self.use_as_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('useAsDefault') is not None:
            self.use_as_default = m.get('useAsDefault')

        return self

