# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageRemovalProRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        image_url: str = None,
    ):
        # The call type. Valid values:
        # - true: asynchronous.
        # - false: synchronous.
        # 
        # Default value: false.
        self.async_ = async_
        # The URL of the image to process.
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
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

