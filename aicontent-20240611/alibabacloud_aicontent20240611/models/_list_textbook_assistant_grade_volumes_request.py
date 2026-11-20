# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTextbookAssistantGradeVolumesRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        scenario: str = None,
    ):
        # The authorization code for API calls. You can obtain it by calling the API operation that retrieves the authorization code for the English textbook AI teacher feature.
        self.auth_token = auth_token
        # Scenarios. Valid values: SYNC: synchronization practice, EXPAND: extended practice.
        # 
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.scenario is not None:
            result['scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')

        return self

