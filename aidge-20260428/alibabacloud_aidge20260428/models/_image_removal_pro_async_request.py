# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageRemovalProAsyncRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        image_url: str = None,
    ):
        # The business order ID of the caller. This ID is recorded when the request is accepted and returned as-is when you query the asynchronous task result.
        self.biz_id = biz_id
        # The URL of the original image. The image must be in the JPG, JPEG, PNG, BMP, or WEBP format.
        # · Resolution: 256×256 to 3000×3000. File size: ≤ 10 MB.
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

