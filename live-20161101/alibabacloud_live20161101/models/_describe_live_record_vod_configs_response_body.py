# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveRecordVodConfigsResponseBody(DaraModel):
    def __init__(
        self,
        live_record_vod_configs: main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigs = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total: str = None,
    ):
        # The configurations.
        self.live_record_vod_configs = live_record_vod_configs
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.live_record_vod_configs:
            self.live_record_vod_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_record_vod_configs is not None:
            result['LiveRecordVodConfigs'] = self.live_record_vod_configs.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveRecordVodConfigs') is not None:
            temp_model = main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigs()
            self.live_record_vod_configs = temp_model.from_map(m.get('LiveRecordVodConfigs'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigs(DaraModel):
    def __init__(
        self,
        live_record_vod_config: List[main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfig] = None,
    ):
        self.live_record_vod_config = live_record_vod_config

    def validate(self):
        if self.live_record_vod_config:
            for v1 in self.live_record_vod_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveRecordVodConfig'] = []
        if self.live_record_vod_config is not None:
            for k1 in self.live_record_vod_config:
                result['LiveRecordVodConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_record_vod_config = []
        if m.get('LiveRecordVodConfig') is not None:
            for k1 in m.get('LiveRecordVodConfig'):
                temp_model = main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfig()
                self.live_record_vod_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        auto_compose: str = None,
        compose_vod_transcode_group_id: str = None,
        create_time: str = None,
        cycle_duration: int = None,
        domain_name: str = None,
        on_demand: int = None,
        storage_location: str = None,
        stream_name: str = None,
        vod_transcode_group_id: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # Indicates whether automatic merging is enabled. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.auto_compose = auto_compose
        # The ID of the transcoding template group that was used to automatically merge the VOD files created from the live streams.
        # 
        # >  This parameter is returned if the value of the AutoCompose parameter is ON.
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id
        # The time when the live stream was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The recording cycle. Unit: seconds. Default value: **3600**. Valid values: **300 to 21600**.
        self.cycle_duration = cycle_duration
        # The main streaming domain.
        self.domain_name = domain_name
        # Indicates whether on-demand recording is enabled. Valid values:
        # 
        # *   **0** (default): On-demand recording is disabled.
        # *   **1**: On-demand recording is enabled by using the HTTP callback method.
        self.on_demand = on_demand
        # The storage location.
        self.storage_location = storage_location
        # The name of the live stream.
        self.stream_name = stream_name
        # The ID of the transcoding template group in ApsaraVideo VOD.
        self.vod_transcode_group_id = vod_transcode_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auto_compose is not None:
            result['AutoCompose'] = self.auto_compose

        if self.compose_vod_transcode_group_id is not None:
            result['ComposeVodTranscodeGroupId'] = self.compose_vod_transcode_group_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.on_demand is not None:
            result['OnDemand'] = self.on_demand

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.vod_transcode_group_id is not None:
            result['VodTranscodeGroupId'] = self.vod_transcode_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AutoCompose') is not None:
            self.auto_compose = m.get('AutoCompose')

        if m.get('ComposeVodTranscodeGroupId') is not None:
            self.compose_vod_transcode_group_id = m.get('ComposeVodTranscodeGroupId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OnDemand') is not None:
            self.on_demand = m.get('OnDemand')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('VodTranscodeGroupId') is not None:
            self.vod_transcode_group_id = m.get('VodTranscodeGroupId')

        return self

