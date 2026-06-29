# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportAnnotationsRequest(DaraModel):
    def __init__(
        self,
        oss_path: str = None,
        register_dataset: str = None,
        target: str = None,
    ):
        # OSS path.
        # 
        # This parameter is required.
        self.oss_path = oss_path
        # Specifies whether to register the result as a PAI dataset. Valid values:
        # - true: Registers the annotation result as a PAI dataset.
        # - false: Exports the annotation result directly to an OSS folder without registering it as a dataset.
        self.register_dataset = register_dataset
        # Target.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.register_dataset is not None:
            result['RegisterDataset'] = self.register_dataset

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('RegisterDataset') is not None:
            self.register_dataset = m.get('RegisterDataset')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

