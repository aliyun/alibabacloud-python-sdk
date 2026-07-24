# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileUploadRequest(DaraModel):
    def __init__(
        self,
        file_content: str = None,
        order_num: int = None,
    ):
        # The Base64-encoded string of the attachment image file. Supported image types: .jpg, .png, and .jpeg.
        # 
        # This parameter is required.
        self.file_content = file_content
        # The forward order number.
        # 
        # This parameter is required.
        self.order_num = order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_content is not None:
            result['file_content'] = self.file_content

        if self.order_num is not None:
            result['order_num'] = self.order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_content') is not None:
            self.file_content = m.get('file_content')

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        return self

