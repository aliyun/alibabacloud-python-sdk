# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportImageResponseBody(DaraModel):
    def __init__(
        self,
        exported_image_url: str = None,
        request_id: str = None,
    ):
        # The URL that points to the exported image.
        self.exported_image_url = exported_image_url
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

