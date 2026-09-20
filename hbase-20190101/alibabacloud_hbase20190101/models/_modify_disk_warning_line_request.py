# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskWarningLineRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        warning_line: int = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The alert threshold. Valid values: 50 to 90.
        # 
        # This parameter is required.
        self.warning_line = warning_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')

        return self

