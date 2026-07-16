# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRcsSignMenuRequest(DaraModel):
    def __init__(
        self,
        menu_content: str = None,
        sign_name: str = None,
    ):
        # This parameter is required.
        self.menu_content = menu_content
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.menu_content is not None:
            result['MenuContent'] = self.menu_content

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MenuContent') is not None:
            self.menu_content = m.get('MenuContent')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

