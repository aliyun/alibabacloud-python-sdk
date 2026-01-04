# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReinitInstancesRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        instance_ids: List[str] = None,
        password: str = None,
    ):
        self.image_id = image_id
        self.instance_ids = instance_ids
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

