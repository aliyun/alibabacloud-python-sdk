# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveSnapshotConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_snapshot_config_list: main_models.DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigList = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The snapshot configurations.
        self.live_stream_snapshot_config_list = live_stream_snapshot_config_list
        # The sort order.
        self.order = order
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries that meet the specified conditions.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.live_stream_snapshot_config_list:
            self.live_stream_snapshot_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_stream_snapshot_config_list is not None:
            result['LiveStreamSnapshotConfigList'] = self.live_stream_snapshot_config_list.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamSnapshotConfigList') is not None:
            temp_model = main_models.DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigList()
            self.live_stream_snapshot_config_list = temp_model.from_map(m.get('LiveStreamSnapshotConfigList'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigList(DaraModel):
    def __init__(
        self,
        live_stream_snapshot_config: List[main_models.DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigListLiveStreamSnapshotConfig] = None,
    ):
        self.live_stream_snapshot_config = live_stream_snapshot_config

    def validate(self):
        if self.live_stream_snapshot_config:
            for v1 in self.live_stream_snapshot_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamSnapshotConfig'] = []
        if self.live_stream_snapshot_config is not None:
            for k1 in self.live_stream_snapshot_config:
                result['LiveStreamSnapshotConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_snapshot_config = []
        if m.get('LiveStreamSnapshotConfig') is not None:
            for k1 in m.get('LiveStreamSnapshotConfig'):
                temp_model = main_models.DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigListLiveStreamSnapshotConfig()
                self.live_stream_snapshot_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveSnapshotConfigResponseBodyLiveStreamSnapshotConfigListLiveStreamSnapshotConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        callback: str = None,
        create_time: str = None,
        domain_name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        overwrite_oss_object: str = None,
        sequence_oss_object: str = None,
        time_interval: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The callback URL that is used to receive notifications about snapshot capture.
        self.callback = callback
        # The time when the configuration was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The main streaming domain.
        self.domain_name = domain_name
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The naming format of snapshots that are stored in the overwrite mode, which means that a new snapshot overwrites the previous snapshot.
        self.overwrite_oss_object = overwrite_oss_object
        # The naming format of snapshots that are stored in sequence, which means that a new snapshot does not overwrite the previous snapshot.
        self.sequence_oss_object = sequence_oss_object
        # The interval at which snapshots are captured. Unit: seconds.
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.callback is not None:
            result['Callback'] = self.callback

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.overwrite_oss_object is not None:
            result['OverwriteOssObject'] = self.overwrite_oss_object

        if self.sequence_oss_object is not None:
            result['SequenceOssObject'] = self.sequence_oss_object

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OverwriteOssObject') is not None:
            self.overwrite_oss_object = m.get('OverwriteOssObject')

        if m.get('SequenceOssObject') is not None:
            self.sequence_oss_object = m.get('SequenceOssObject')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

