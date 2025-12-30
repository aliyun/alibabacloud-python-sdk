# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImagesRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        image_version: str = None,
        platform: str = None,
    ):
        # The architecture.
        self.architecture = architecture
        # The image version.
        self.image_version = image_version
        # The platform.
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.platform is not None:
            result['Platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        return self

