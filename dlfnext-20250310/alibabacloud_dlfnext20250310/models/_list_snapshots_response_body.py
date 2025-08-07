# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 
from typing import List


class ListSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        snapshots: List[main_models.Snapshot] = None,
    ):
        self.next_page_token = next_page_token
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
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        result['snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['snapshots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        self.snapshots = []
        if m.get('snapshots') is not None:
            for k1 in m.get('snapshots'):
                temp_model = main_models.Snapshot()
                self.snapshots.append(temp_model.from_map(k1))

        return self

