# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateStorageVolumeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        volume_id: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # An array of volume IDs.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')

        return self

