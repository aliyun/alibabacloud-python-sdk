# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTuringTaskRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        idempotent_key: str = None,
        img_url: str = None,
        resolution: str = None,
        resource_type: str = None,
        task_type: str = None,
    ):
        self.duration = duration
        self.idempotent_key = idempotent_key
        self.img_url = img_url
        self.resolution = resolution
        self.resource_type = resource_type
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.idempotent_key is not None:
            result['idempotentKey'] = self.idempotent_key

        if self.img_url is not None:
            result['imgUrl'] = self.img_url

        if self.resolution is not None:
            result['resolution'] = self.resolution

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('idempotentKey') is not None:
            self.idempotent_key = m.get('idempotentKey')

        if m.get('imgUrl') is not None:
            self.img_url = m.get('imgUrl')

        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

