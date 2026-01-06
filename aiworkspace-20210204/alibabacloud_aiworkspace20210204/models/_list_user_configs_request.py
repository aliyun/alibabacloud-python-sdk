# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserConfigsRequest(DaraModel):
    def __init__(
        self,
        category_names: str = None,
        config_keys: str = None,
    ):
        # The category. Currently, only DataPrivacyConfig is supported.
        self.category_names = category_names
        # The configuration item keys. Currently, only customizePAIAssumedRole is supported.
        self.config_keys = config_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_names is not None:
            result['CategoryNames'] = self.category_names

        if self.config_keys is not None:
            result['ConfigKeys'] = self.config_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryNames') is not None:
            self.category_names = m.get('CategoryNames')

        if m.get('ConfigKeys') is not None:
            self.config_keys = m.get('ConfigKeys')

        return self

