# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFilterRequest(DaraModel):
    def __init__(
        self,
        filter_configuration: str = None,
        filter_name: str = None,
    ):
        # The configurations of the filter.
        # 
        # This parameter is required.
        self.filter_configuration = filter_configuration
        # The name of the filter.
        # 
        # This parameter is required.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_configuration is not None:
            result['FilterConfiguration'] = self.filter_configuration

        if self.filter_name is not None:
            result['FilterName'] = self.filter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConfiguration') is not None:
            self.filter_configuration = m.get('FilterConfiguration')

        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')

        return self

