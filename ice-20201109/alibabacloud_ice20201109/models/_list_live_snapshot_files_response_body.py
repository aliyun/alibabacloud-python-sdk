# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLiveSnapshotFilesResponseBody(DaraModel):
    def __init__(
        self,
        file_list: List[main_models.ListLiveSnapshotFilesResponseBodyFileList] = None,
        next_start_time: str = None,
        request_id: str = None,
    ):
        # The list of files.
        self.file_list = file_list
        # The start time of the next page. If no value is returned, the pagination ends.
        self.next_start_time = next_start_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.ListLiveSnapshotFilesResponseBodyFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveSnapshotFilesResponseBodyFileList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        is_overlay: bool = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # The creation timestamp that is used as an input parameter for a delete API operation.
        self.create_timestamp = create_timestamp
        # Specifies whether to overlay snapshots.
        self.is_overlay = is_overlay
        # The OSS bucket.
        self.oss_bucket = oss_bucket
        # The Object Storage Service (OSS) domain name.
        self.oss_endpoint = oss_endpoint
        # The location in which the OSS object is stored.
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

