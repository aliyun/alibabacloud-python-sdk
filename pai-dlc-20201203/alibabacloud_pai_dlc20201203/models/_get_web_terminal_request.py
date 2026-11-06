# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWebTerminalRequest(DaraModel):
    def __init__(
        self,
        container_name: str = None,
        is_shared: bool = None,
        pod_uid: str = None,
    ):
        # The name of the container. If this parameter is not specified, the WebTerminal of the primary container is accessed.
        self.container_name = container_name
        # Specifies whether to create a shareable link for accessing the container. Valid values:
        # - true: Returns a shareable link for accessing the container. The link expires after 30 seconds and can be used only once. After the container is accessed through this link, subsequent requests to access the container by using the same link become invalid.
        # - false: Returns a regular link for accessing the container. Alibaba Cloud identity verification is required when you use the link. The link expires after 30 seconds.
        self.is_shared = is_shared
        # The Pod UID.
        self.pod_uid = pod_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.is_shared is not None:
            result['IsShared'] = self.is_shared

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        return self

