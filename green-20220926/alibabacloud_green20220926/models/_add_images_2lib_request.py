# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImages2LibRequest(DaraModel):
    def __init__(
        self,
        img_url: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        # URL of the image to be uploaded.
        self.img_url = img_url
        # The ID of image library.
        self.lib_id = lib_id
        # Region ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

