# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScgSearchShrinkRequest(DaraModel):
    def __init__(
        self,
        scg_filter_shrink: str = None,
        topic_id: str = None,
    ):
        # Query filter
        # 
        # This parameter is required.
        self.scg_filter_shrink = scg_filter_shrink
        # Selection pool ID. Optional values: MC201132 (Ethnic Chinese Style), MC201136 (Pop Music), MC201139 (Sweet Love), MC201133 (Folk), MC201137 (Relaxing Reading), MC201138 (Happiness), PA202029 (Stories), PA202030 (Children\\"s Songs), PA202028 (Chinese Classics and History), PA202032 (Encyclopedia), PA202031 (English Children\\"s Songs)
        # 
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scg_filter_shrink is not None:
            result['ScgFilter'] = self.scg_filter_shrink

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            self.scg_filter_shrink = m.get('ScgFilter')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

