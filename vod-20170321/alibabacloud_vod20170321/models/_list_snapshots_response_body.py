# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        media_snapshot: main_models.ListSnapshotsResponseBodyMediaSnapshot = None,
        request_id: str = None,
    ):
        # The information about the snapshot.
        self.media_snapshot = media_snapshot
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_snapshot:
            self.media_snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_snapshot is not None:
            result['MediaSnapshot'] = self.media_snapshot.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaSnapshot') is not None:
            temp_model = main_models.ListSnapshotsResponseBodyMediaSnapshot()
            self.media_snapshot = temp_model.from_map(m.get('MediaSnapshot'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSnapshotsResponseBodyMediaSnapshot(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        job_id: str = None,
        regular: str = None,
        snapshots: main_models.ListSnapshotsResponseBodyMediaSnapshotSnapshots = None,
        total: int = None,
    ):
        # The time when the snapshot job was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the snapshot job.
        self.job_id = job_id
        # The rule used to generate snapshot URLs.
        self.regular = regular
        self.snapshots = snapshots
        # The total number of snapshots.
        self.total = total

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.regular is not None:
            result['Regular'] = self.regular

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Regular') is not None:
            self.regular = m.get('Regular')

        if m.get('Snapshots') is not None:
            temp_model = main_models.ListSnapshotsResponseBodyMediaSnapshotSnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSnapshotsResponseBodyMediaSnapshotSnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[main_models.ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for v1 in self.snapshot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k1 in self.snapshot:
                result['Snapshot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k1 in m.get('Snapshot'):
                temp_model = main_models.ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k1))

        return self

class ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot(DaraModel):
    def __init__(
        self,
        index: int = None,
        url: str = None,
    ):
        self.index = index
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

