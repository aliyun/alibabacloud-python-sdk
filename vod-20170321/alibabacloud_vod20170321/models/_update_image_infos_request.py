# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageInfosRequest(DaraModel):
    def __init__(
        self,
        update_content: str = None,
    ):
        # The new information about the one or more images. You can modify the information about up to 20 images at a time. For more information about the parameter structure, see the **UpdateContent** section.
        # 
        # >  The values of the nested parameters Title, Description, and Tags under the UpdateContent parameter cannot contain emoticons.
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

