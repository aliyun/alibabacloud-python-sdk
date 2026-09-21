# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCloudPhoneNodeSystemImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        node_ids: List[str] = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The list of cloud phone normal matrix IDs.
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        return self

