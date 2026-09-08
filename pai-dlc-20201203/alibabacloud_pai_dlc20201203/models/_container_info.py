# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ContainerInfo(DaraModel):
    def __init__(
        self,
        main_container: str = None,
        sidecar_containers: List[str] = None,
    ):
        # The name of the main container.
        self.main_container = main_container
        # The list of sidecar container names.
        self.sidecar_containers = sidecar_containers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_container is not None:
            result['MainContainer'] = self.main_container

        if self.sidecar_containers is not None:
            result['SidecarContainers'] = self.sidecar_containers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainContainer') is not None:
            self.main_container = m.get('MainContainer')

        if m.get('SidecarContainers') is not None:
            self.sidecar_containers = m.get('SidecarContainers')

        return self

