# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMultimodalLabelStudioServiceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_ids: List[str] = None,
        password: str = None,
        source_region_id: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dataset_ids = dataset_ids
        # This parameter is required.
        self.password = password
        self.source_region_id = source_region_id
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids

        if self.password is not None:
            result['Password'] = self.password

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

