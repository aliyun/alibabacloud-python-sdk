# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateSceneKeyResponseBody(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        expire_time: str = None,
        key: str = None,
        request_id: str = None,
        scene_url: str = None,
    ):
        # The Agent Gateway endpoint, which includes the cluster offset mapping port. This parameter is returned only for desktop scenarios.
        self.base_url = base_url
        # The expiration time of the key.
        self.expire_time = expire_time
        # The scenario access key.
        self.key = key
        # The request ID.
        self.request_id = request_id
        # The scenario access URL.
        self.scene_url = scene_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.key is not None:
            result['Key'] = self.key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scene_url is not None:
            result['SceneUrl'] = self.scene_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SceneUrl') is not None:
            self.scene_url = m.get('SceneUrl')

        return self

