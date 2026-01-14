# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IllustrationTaskCreateCmd(DaraModel):
    def __init__(
        self,
        background_type: int = None,
        dst_height: int = None,
        dst_width: int = None,
        idempotent_id: str = None,
        image_urls: List[str] = None,
        nums: int = None,
        oss_paths: List[str] = None,
        sticker_text: str = None,
    ):
        self.background_type = background_type
        self.dst_height = dst_height
        self.dst_width = dst_width
        self.idempotent_id = idempotent_id
        self.image_urls = image_urls
        self.nums = nums
        self.oss_paths = oss_paths
        self.sticker_text = sticker_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_type is not None:
            result['backgroundType'] = self.background_type

        if self.dst_height is not None:
            result['dstHeight'] = self.dst_height

        if self.dst_width is not None:
            result['dstWidth'] = self.dst_width

        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.nums is not None:
            result['nums'] = self.nums

        if self.oss_paths is not None:
            result['ossPaths'] = self.oss_paths

        if self.sticker_text is not None:
            result['stickerText'] = self.sticker_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundType') is not None:
            self.background_type = m.get('backgroundType')

        if m.get('dstHeight') is not None:
            self.dst_height = m.get('dstHeight')

        if m.get('dstWidth') is not None:
            self.dst_width = m.get('dstWidth')

        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('nums') is not None:
            self.nums = m.get('nums')

        if m.get('ossPaths') is not None:
            self.oss_paths = m.get('ossPaths')

        if m.get('stickerText') is not None:
            self.sticker_text = m.get('stickerText')

        return self

