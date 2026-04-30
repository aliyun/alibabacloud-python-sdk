# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterSaveFlowConfigRequest(DaraModel):
    def __init__(
        self,
        model_id: int = None,
        rpm: int = None,
        smooth_flow_enabled: bool = None,
        tpm: int = None,
    ):
        # This parameter is required.
        self.model_id = model_id
        self.rpm = rpm
        self.smooth_flow_enabled = smooth_flow_enabled
        self.tpm = tpm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.rpm is not None:
            result['rpm'] = self.rpm

        if self.smooth_flow_enabled is not None:
            result['smoothFlowEnabled'] = self.smooth_flow_enabled

        if self.tpm is not None:
            result['tpm'] = self.tpm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('rpm') is not None:
            self.rpm = m.get('rpm')

        if m.get('smoothFlowEnabled') is not None:
            self.smooth_flow_enabled = m.get('smoothFlowEnabled')

        if m.get('tpm') is not None:
            self.tpm = m.get('tpm')

        return self

