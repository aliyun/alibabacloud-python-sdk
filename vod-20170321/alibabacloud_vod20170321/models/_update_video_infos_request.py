# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVideoInfosRequest(DaraModel):
    def __init__(
        self,
        update_content: str = None,
    ):
        # The update content. You can modify object information of up to 20 audio or video files at a time. Separate object information of multiple audio or video files with commas (,). If you attempt to update more than 20 files at a time, the update fails and the `CountExceededMax` error is returned.
        # The value must be a JSON string. For more information about how to construct the parameters, see the **UpdateContent** table below.
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

