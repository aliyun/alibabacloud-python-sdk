# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPolarClawConfigRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        config_path: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.config_path = config_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.config_path is not None:
            result['ConfigPath'] = self.config_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ConfigPath') is not None:
            self.config_path = m.get('ConfigPath')

        return self

