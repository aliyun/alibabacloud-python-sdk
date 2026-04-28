# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomizedStoryResponseBody(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.story_id is not None:
            result['story_id'] = self.story_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        return self

