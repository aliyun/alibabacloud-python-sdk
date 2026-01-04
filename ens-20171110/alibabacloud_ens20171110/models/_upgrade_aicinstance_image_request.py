# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpgradeAICInstanceImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        server_ids: List[str] = None,
        timeout: int = None,
    ):
        # The ID of the AIC image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The IDs of the servers.
        # 
        # This parameter is required.
        self.server_ids = server_ids
        # The timeout period of the update. Unit: seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

