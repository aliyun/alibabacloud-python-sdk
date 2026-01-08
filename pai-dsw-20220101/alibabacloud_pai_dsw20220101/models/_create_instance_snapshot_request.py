# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceSnapshotRequest(DaraModel):
    def __init__(
        self,
        exclude_paths: List[str] = None,
        image_url: str = None,
        labels: List[main_models.CreateInstanceSnapshotRequestLabels] = None,
        overwrite: bool = None,
        snapshot_description: str = None,
        snapshot_name: str = None,
    ):
        self.exclude_paths = exclude_paths
        # This parameter is required.
        self.image_url = image_url
        self.labels = labels
        self.overwrite = overwrite
        self.snapshot_description = snapshot_description
        # This parameter is required.
        self.snapshot_name = snapshot_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_paths is not None:
            result['ExcludePaths'] = self.exclude_paths

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.snapshot_description is not None:
            result['SnapshotDescription'] = self.snapshot_description

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludePaths') is not None:
            self.exclude_paths = m.get('ExcludePaths')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateInstanceSnapshotRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('SnapshotDescription') is not None:
            self.snapshot_description = m.get('SnapshotDescription')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        return self

class CreateInstanceSnapshotRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

