# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentDataSemanticsStageProgress(DaraModel):
    def __init__(
        self,
        stage: str = None,
        status: str = None,
    ):
        # The stage name.
        # 
        # This parameter is required.
        self.stage = stage
        # The stage status.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage is not None:
            result['Stage'] = self.stage

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

