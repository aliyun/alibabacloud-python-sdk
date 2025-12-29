# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebInstanceInfo(DaraModel):
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
            result['ImageUrl'] = self.image_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

