# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoutineBuildConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        routine_build_configuration_id: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ER build configuration ID.
        self.routine_build_configuration_id = routine_build_configuration_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.routine_build_configuration_id is not None:
            result['RoutineBuildConfigurationId'] = self.routine_build_configuration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoutineBuildConfigurationId') is not None:
            self.routine_build_configuration_id = m.get('RoutineBuildConfigurationId')

        return self

