# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveSnapshotDetectPornConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_snapshot_detect_porn_config_list: main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigList = None,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The list of video moderation configurations.
        self.live_snapshot_detect_porn_config_list = live_snapshot_detect_porn_config_list
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
        if self.live_snapshot_detect_porn_config_list:
            self.live_snapshot_detect_porn_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_snapshot_detect_porn_config_list is not None:
            result['LiveSnapshotDetectPornConfigList'] = self.live_snapshot_detect_porn_config_list.to_map()

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
        if m.get('LiveSnapshotDetectPornConfigList') is not None:
            temp_model = main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigList()
            self.live_snapshot_detect_porn_config_list = temp_model.from_map(m.get('LiveSnapshotDetectPornConfigList'))

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

class DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigList(DaraModel):
    def __init__(
        self,
        live_snapshot_detect_porn_config: List[main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig] = None,
    ):
        self.live_snapshot_detect_porn_config = live_snapshot_detect_porn_config

    def validate(self):
        if self.live_snapshot_detect_porn_config:
            for v1 in self.live_snapshot_detect_porn_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveSnapshotDetectPornConfig'] = []
        if self.live_snapshot_detect_porn_config is not None:
            for k1 in self.live_snapshot_detect_porn_config:
                result['LiveSnapshotDetectPornConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_snapshot_detect_porn_config = []
        if m.get('LiveSnapshotDetectPornConfig') is not None:
            for k1 in m.get('LiveSnapshotDetectPornConfig'):
                temp_model = main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig()
                self.live_snapshot_detect_porn_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        interval: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        scenes: main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes = None,
    ):
        # The application name.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The interval at which snapshots are captured from the live stream. Unit: seconds.
        self.interval = interval
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The name of the storage file in Object Storage Service (OSS).
        self.oss_object = oss_object
        # The moderation scenario array.
        self.scenes = scenes

    def validate(self):
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('Scenes') is not None:
            temp_model = main_models.DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes()
            self.scenes = temp_model.from_map(m.get('Scenes'))

        return self

class DescribeLiveSnapshotDetectPornConfigResponseBodyLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes(DaraModel):
    def __init__(
        self,
        scene: List[str] = None,
    ):
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        return self

