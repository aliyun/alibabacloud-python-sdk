# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWebTerminalRequest(DaraModel):
    def __init__(
        self,
        is_shared: bool = None,
        pod_uid: str = None,
    ):
        # Specifies whether to create a shareable link to access the container. Valid values:
        # 
        # *   true: returns a shareable link to access the container. The link will expire after 30 seconds and can only be used once. After you access the container by using the link, other requests that use this link to access the container become invalid.
        # *   false: returns a common shareable link to access the container. If you use a common shareable link to access a container, Alibaba Cloud identity authentication is required. The link will expire after 30 seconds.
        self.is_shared = is_shared
        # The pod UID.
        self.pod_uid = pod_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        return self

