# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileTypeFilters(DaraModel):
    def __init__(
        self,
        exclude_dir: bool = None,
        exclude_symlink: bool = None,
    ):
        self.exclude_dir = exclude_dir
        self.exclude_symlink = exclude_symlink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_dir is not None:
            result['ExcludeDir'] = self.exclude_dir

        if self.exclude_symlink is not None:
            result['ExcludeSymlink'] = self.exclude_symlink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDir') is not None:
            self.exclude_dir = m.get('ExcludeDir')

        if m.get('ExcludeSymlink') is not None:
            self.exclude_symlink = m.get('ExcludeSymlink')

        return self

