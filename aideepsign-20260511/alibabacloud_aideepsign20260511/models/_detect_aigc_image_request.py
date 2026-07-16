# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectAigcImageRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        object_key: str = None,
    ):
        # The URL of the image to detect. Only HTTP and HTTPS protocols are supported. You must provide at least one of ImageUrl and ObjectKey.
        self.image_url = image_url
        # The ObjectKey of the image to detect in OSS. When you use ObjectKey, make sure that the key belongs to the namespace of the current caller. You must provide at least one of ImageUrl and ObjectKey.
        self.object_key = object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        return self

