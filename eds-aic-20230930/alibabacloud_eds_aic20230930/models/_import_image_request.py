# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportImageRequest(DaraModel):
    def __init__(
        self,
        image_description: str = None,
        image_file_url: str = None,
        image_name: str = None,
    ):
        self.image_description = image_description
        self.image_file_url = image_file_url
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_description is not None:
            result['ImageDescription'] = self.image_description

        if self.image_file_url is not None:
            result['ImageFileURL'] = self.image_file_url

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageDescription') is not None:
            self.image_description = m.get('ImageDescription')

        if m.get('ImageFileURL') is not None:
            self.image_file_url = m.get('ImageFileURL')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        return self

