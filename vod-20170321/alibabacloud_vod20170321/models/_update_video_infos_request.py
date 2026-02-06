# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoInfosRequest(DaraModel):
    def __init__(
        self,
        update_content: str = None,
    ):
        # The new information about audios or videos. You can modify the information about up to 20 audios or videos at a time. Separate multiple audios or videos with commas (,). When you modify the information exceed 20 audios or videos at a time, the update will fail with an error code **CountExceededMax**.
        # 
        # The value is a JSON string. For more information, see the **UpdateContent** section of this topic.
        # 
        # This parameter is required.
        self.update_content = update_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')

        return self

