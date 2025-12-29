# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationImageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        image_url: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The URL of the image.
        # 
        # This parameter is required.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

