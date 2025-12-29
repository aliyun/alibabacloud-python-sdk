# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ContainerdConfig(DaraModel):
    def __init__(
        self,
        ignore_image_defined_volume: bool = None,
        insecure_registries: List[str] = None,
        limit_core: int = None,
        limit_mem_lock: int = None,
        limit_no_file: int = None,
        max_concurrent_downloads: int = None,
        registry_mirrors: List[str] = None,
    ):
        self.ignore_image_defined_volume = ignore_image_defined_volume
        self.insecure_registries = insecure_registries
        self.limit_core = limit_core
        self.limit_mem_lock = limit_mem_lock
        self.limit_no_file = limit_no_file
        self.max_concurrent_downloads = max_concurrent_downloads
        self.registry_mirrors = registry_mirrors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_image_defined_volume is not None:
            result['ignoreImageDefinedVolume'] = self.ignore_image_defined_volume

        if self.insecure_registries is not None:
            result['insecureRegistries'] = self.insecure_registries

        if self.limit_core is not None:
            result['limitCore'] = self.limit_core

        if self.limit_mem_lock is not None:
            result['limitMemLock'] = self.limit_mem_lock

        if self.limit_no_file is not None:
            result['limitNoFile'] = self.limit_no_file

        if self.max_concurrent_downloads is not None:
            result['maxConcurrentDownloads'] = self.max_concurrent_downloads

        if self.registry_mirrors is not None:
            result['registryMirrors'] = self.registry_mirrors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ignoreImageDefinedVolume') is not None:
            self.ignore_image_defined_volume = m.get('ignoreImageDefinedVolume')

        if m.get('insecureRegistries') is not None:
            self.insecure_registries = m.get('insecureRegistries')

        if m.get('limitCore') is not None:
            self.limit_core = m.get('limitCore')

        if m.get('limitMemLock') is not None:
            self.limit_mem_lock = m.get('limitMemLock')

        if m.get('limitNoFile') is not None:
            self.limit_no_file = m.get('limitNoFile')

        if m.get('maxConcurrentDownloads') is not None:
            self.max_concurrent_downloads = m.get('maxConcurrentDownloads')

        if m.get('registryMirrors') is not None:
            self.registry_mirrors = m.get('registryMirrors')

        return self

