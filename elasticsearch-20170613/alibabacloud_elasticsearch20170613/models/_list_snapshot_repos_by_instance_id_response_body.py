# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotReposByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListSnapshotReposByInstanceIdResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListSnapshotReposByInstanceIdResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListSnapshotReposByInstanceIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_path: str = None,
        snap_warehouse: str = None,
        status: str = None,
    ):
        # Reference instance ID.
        self.instance_id = instance_id
        # The address of the repository.
        self.repo_path = repo_path
        # Reference warehouse name.
        self.snap_warehouse = snap_warehouse
        # Reference warehouse status. available indicates that it is valid. unavailable indicates that it is invalid.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.repo_path is not None:
            result['repoPath'] = self.repo_path

        if self.snap_warehouse is not None:
            result['snapWarehouse'] = self.snap_warehouse

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')

        if m.get('snapWarehouse') is not None:
            self.snap_warehouse = m.get('snapWarehouse')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

