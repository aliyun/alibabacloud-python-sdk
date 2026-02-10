# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallHybridProxyRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        install_code: str = None,
        yundun_uuids: List[str] = None,
    ):
        # The cluster name.
        self.cluster_name = cluster_name
        # The installation code.
        self.install_code = install_code
        # The UUIDs of the proxy servers.
        self.yundun_uuids = yundun_uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.install_code is not None:
            result['InstallCode'] = self.install_code

        if self.yundun_uuids is not None:
            result['YundunUuids'] = self.yundun_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('InstallCode') is not None:
            self.install_code = m.get('InstallCode')

        if m.get('YundunUuids') is not None:
            self.yundun_uuids = m.get('YundunUuids')

        return self

