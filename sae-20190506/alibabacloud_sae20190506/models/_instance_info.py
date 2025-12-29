# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceInfo(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        instance_id: str = None,
        status: str = None,
        version_id: str = None,
    ):
        self.image_url = image_url
        self.instance_id = instance_id
        self.status = status
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.status is not None:
            result['status'] = self.status

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

