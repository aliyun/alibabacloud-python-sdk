# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamSnapshotInfoResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_snapshot_info_list: main_models.DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoList = None,
        next_start_time: str = None,
        request_id: str = None,
    ):
        # The snapshots.
        self.live_stream_snapshot_info_list = live_stream_snapshot_info_list
        # The time when the next call occurred. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # >  If the number of snapshots that were captured within the specified time period exceeds the value of the Limit parameter, this parameter is returned. It indicates the time when the DescribeLiveStreamSnapshotInfo operation was called again. If this parameter is not returned, the number of snapshots that are captured within the specified time period does not exceed the specified limit.
        self.next_start_time = next_start_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_stream_snapshot_info_list:
            self.live_stream_snapshot_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_stream_snapshot_info_list is not None:
            result['LiveStreamSnapshotInfoList'] = self.live_stream_snapshot_info_list.to_map()

        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamSnapshotInfoList') is not None:
            temp_model = main_models.DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoList()
            self.live_stream_snapshot_info_list = temp_model.from_map(m.get('LiveStreamSnapshotInfoList'))

        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoList(DaraModel):
    def __init__(
        self,
        live_stream_snapshot_info: List[main_models.DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoListLiveStreamSnapshotInfo] = None,
    ):
        self.live_stream_snapshot_info = live_stream_snapshot_info

    def validate(self):
        if self.live_stream_snapshot_info:
            for v1 in self.live_stream_snapshot_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamSnapshotInfo'] = []
        if self.live_stream_snapshot_info is not None:
            for k1 in self.live_stream_snapshot_info:
                result['LiveStreamSnapshotInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_snapshot_info = []
        if m.get('LiveStreamSnapshotInfo') is not None:
            for k1 in m.get('LiveStreamSnapshotInfo'):
                temp_model = main_models.DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoListLiveStreamSnapshotInfo()
                self.live_stream_snapshot_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamSnapshotInfoResponseBodyLiveStreamSnapshotInfoListLiveStreamSnapshotInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        is_overlay: bool = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
    ):
        # The time when the snapshot was captured. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The timestamp when the snapshot file was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The snapshot mode. Valid values:
        # 
        # *   **true**: overwrite mode, which means that a new snapshot overwrites the previous snapshot.
        # *   **false**: sequence mode, which means that a new snapshot does not overwrite the previous snapshot.
        self.is_overlay = is_overlay
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The name of the snapshot stored in Object Storage Service (OSS).
        self.oss_object = oss_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.is_overlay is not None:
            result['IsOverlay'] = self.is_overlay

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('IsOverlay') is not None:
            self.is_overlay = m.get('IsOverlay')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        return self

