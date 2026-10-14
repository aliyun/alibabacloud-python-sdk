# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class DeviceGroupDynamicRule(DaraModel):
    def __init__(
        self,
        args: Any = None,
        key: str = None,
        operator: str = None,
    ):
        # The list of matching parameters. The meaning of the parameters is determined by both Key and Operator. When Key is set to dev_type and Operator is set to in, specify the operating system types to match.
        self.args = args
        # The user endpoint device property key used for dynamic matching. The example value dev_type indicates the operating system type of the endpoint device.
        self.key = key
        # The matching operator applied to the property specified by Key. The example value in indicates that the property value belongs to the list of parameters specified by Args.
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

