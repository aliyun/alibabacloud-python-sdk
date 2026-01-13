# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_type: str = None,
    ):
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The type of the images. Valid values:
        # 
        # *   VM: Virtual Machine Image
        # *   Container: container image
        self.image_type = image_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        return self

