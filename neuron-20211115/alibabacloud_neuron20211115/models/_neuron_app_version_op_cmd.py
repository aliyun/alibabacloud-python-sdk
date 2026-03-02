# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronAppVersionOpCmd(DaraModel):
    def __init__(
        self,
        app_version_id: int = None,
    ):
        # This parameter is required.
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version_id is not None:
            result['appVersionId'] = self.app_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersionId') is not None:
            self.app_version_id = m.get('appVersionId')

        return self

