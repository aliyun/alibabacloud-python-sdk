# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoInfosRequest(DaraModel):
    def __init__(
        self,
        update_content: str = None,
    ):
        # The update content. You can modify the information about up to 20 audio and video files at a time. Separate multiple audio and video object information entries with commas (,). If you specify more than 20 objects, the update is failed and the `CountExceededMax` error is returned.
        # The value is a JSON character string. For more details about the parameters, see the **UpdateContent** table below.
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

