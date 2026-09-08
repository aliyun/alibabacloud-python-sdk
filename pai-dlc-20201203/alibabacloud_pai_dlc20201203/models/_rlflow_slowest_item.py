# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowSlowestItem(DaraModel):
    def __init__(
        self,
        prompt_uid: str = None,
        sample_index: str = None,
        sec: float = None,
    ):
        # The UID of the sample.
        self.prompt_uid = prompt_uid
        # The ordinal number of the event trace.
        self.sample_index = sample_index
        # The execution duration of the stage, in seconds.
        self.sec = sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt_uid is not None:
            result['PromptUid'] = self.prompt_uid

        if self.sample_index is not None:
            result['SampleIndex'] = self.sample_index

        if self.sec is not None:
            result['Sec'] = self.sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptUid') is not None:
            self.prompt_uid = m.get('PromptUid')

        if m.get('SampleIndex') is not None:
            self.sample_index = m.get('SampleIndex')

        if m.get('Sec') is not None:
            self.sec = m.get('Sec')

        return self

