# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotsOutput(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        snapshots: List[main_models.Snapshot] = None,
    ):
        # The token used to retrieve the next page of results. This parameter is not returned if no more results are available.
        self.next_token = next_token
        # The list of snapshots.
        # 
        # This parameter is required.
        self.snapshots = snapshots

    def validate(self):
        if self.snapshots:
            for v1 in self.snapshots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['snapshots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.snapshots = []
        if m.get('snapshots') is not None:
            for k1 in m.get('snapshots'):
                temp_model = main_models.Snapshot()
                self.snapshots.append(temp_model.from_map(k1))

        return self

