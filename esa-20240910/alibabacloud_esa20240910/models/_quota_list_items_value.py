# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class QuotaListItemsValue(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        value: main_models.WafQuotaString = None,
    ):
        # The switch for the type of item in the custom list.
        self.enable = enable
        # Format restrictions for the type of item in the custom list.
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.value is not None:
            result['Value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Value') is not None:
            temp_model = main_models.WafQuotaString()
            self.value = temp_model.from_map(m.get('Value'))

        return self

