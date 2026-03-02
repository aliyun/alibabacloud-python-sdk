# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterCustomConnectorRequest(DaraModel):
    def __init__(
        self,
        jar_url: str = None,
    ):
        # The URL in which the JAR package of the custom connector is stored. The platform must be able to access this address.
        # 
        # This parameter is required.
        self.jar_url = jar_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')

        return self

