# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRtcCloudRecordingShrinkRequest(DaraModel):
    def __init__(
        self,
        mix_layout_params_shrink: str = None,
        subscribe_params_shrink: str = None,
        task_id: str = None,
    ):
        self.mix_layout_params_shrink = mix_layout_params_shrink
        # This parameter is required.
        self.subscribe_params_shrink = subscribe_params_shrink
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mix_layout_params_shrink is not None:
            result['MixLayoutParams'] = self.mix_layout_params_shrink

        if self.subscribe_params_shrink is not None:
            result['SubscribeParams'] = self.subscribe_params_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MixLayoutParams') is not None:
            self.mix_layout_params_shrink = m.get('MixLayoutParams')

        if m.get('SubscribeParams') is not None:
            self.subscribe_params_shrink = m.get('SubscribeParams')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

