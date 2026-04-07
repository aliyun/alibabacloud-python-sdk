# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClusterConfig(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        enable_overwrite: bool = None,
        module_name: str = None,
    ):
        # The configuration value.
        self.config_value = config_value
        # Specifies whether to overwrite the advanced settings of nodes in DataStudio. Valid values:
        # 
        # *   true
        # *   false
        self.enable_overwrite = enable_overwrite
        # The module in which the cluster is configured. Valid values:
        # 
        # *   ide: DataStudio.
        # *   da: DataAnalysis.
        # *   scheduler.auto: Operation Center - auto triggered instances.
        # *   scheduler.backfill: Operation Center - data backfill instances.
        # *   scheduler.test: Operation Center - test instances.
        # *   scheduler.manual: Operation Center - manually triggered instances.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.enable_overwrite is not None:
            result['EnableOverwrite'] = self.enable_overwrite

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('EnableOverwrite') is not None:
            self.enable_overwrite = m.get('EnableOverwrite')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

