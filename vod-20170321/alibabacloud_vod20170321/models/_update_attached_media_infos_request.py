# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAttachedMediaInfosRequest(DaraModel):
    def __init__(
        self,
        update_content: str = None,
    ):
        # The update content. You can update the information of up to 20 auxiliary media assets at a time. For the parameter structure, see the **UpdateContent** table below.
        # >- The `Title`, `Description`, and `Tags` fields cannot contain emoticons.
        # >- If a parameter is specified, the corresponding field is updated. Otherwise, the corresponding field is not overwritten or updated.
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

