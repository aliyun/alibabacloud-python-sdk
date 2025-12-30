# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVodPackagingConfigurationRequest(DaraModel):
    def __init__(
        self,
        configuration_name: str = None,
    ):
        # The name of the packaging configuration.
        self.configuration_name = configuration_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_name is not None:
            result['ConfigurationName'] = self.configuration_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationName') is not None:
            self.configuration_name = m.get('ConfigurationName')

        return self

