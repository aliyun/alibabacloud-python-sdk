# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Runtime(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of a container runtime. The following types of runtime are supported by Container Service for Kubernetes (ACK).
        # 
        # *   `containerd`: supports all Kubernetes versions. We recommend that you set the parameter to this value.
        # *   `Sandboxed-Container.runv`: Sandboxed container provides enhanced isolation and supports Kubernetes 1.24 and earlier.
        # *   `docker`: supports Kubernetes 1.22 and earlier.
        # 
        # Default value: `containerd`.
        self.name = name
        # The version of the container runtime. By default, the latest version is used.
        # 
        # For more information about the changes to Sandboxed-Container, see [Sandboxed-Container release notes](https://help.aliyun.com/document_detail/160312.html).
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

