# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class PatchPolarClawConfigRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        config_patch: Dict[str, Any] = None,
        restart: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # A JSON merge-patch object.
        self.config_patch = config_patch
        # Specifies whether to restart the gateway after applying the patch. The default is `true`.
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.config_patch is not None:
            result['ConfigPatch'] = self.config_patch

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ConfigPatch') is not None:
            self.config_patch = m.get('ConfigPatch')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

