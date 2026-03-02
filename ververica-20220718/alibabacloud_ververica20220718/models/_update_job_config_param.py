# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateJobConfigParam(DaraModel):
    def __init__(
        self,
        new_flink_conf: Dict[str, Any] = None,
    ):
        self.new_flink_conf = new_flink_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_flink_conf is not None:
            result['newFlinkConf'] = self.new_flink_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newFlinkConf') is not None:
            self.new_flink_conf = m.get('newFlinkConf')

        return self

