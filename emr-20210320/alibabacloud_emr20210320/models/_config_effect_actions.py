# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigEffectActions(DaraModel):
    def __init__(
        self,
        config_effect_action: str = None,
        config_files: List[str] = None,
    ):
        # 配置生效动作。
        self.config_effect_action = config_effect_action
        # 配置生效配置文件。
        self.config_files = config_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_effect_action is not None:
            result['ConfigEffectAction'] = self.config_effect_action

        if self.config_files is not None:
            result['ConfigFiles'] = self.config_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigEffectAction') is not None:
            self.config_effect_action = m.get('ConfigEffectAction')

        if m.get('ConfigFiles') is not None:
            self.config_files = m.get('ConfigFiles')

        return self

