# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Application(DaraModel):
    def __init__(
        self,
        application_name: str = None,
    ):
        # The application name. You can find the list of application names for each EMR distribution on the cluster creation page in the EMR console.
        # 
        # This parameter is required.
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        return self

