# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartPolarClawGatewayRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        mode: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The restart mode. Valid values:
        # - in-process: lightweight restart without applying environment variable changes. This is the default value.
        # - pkill: cold start that applies environment variable changes.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

