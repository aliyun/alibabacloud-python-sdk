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
        delay_time: int = None,
        domain_name: str = None,
        format_config: bool = None,
        on_demand: int = None,
        record_content: str = None,
        record_format_list: main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatList = None,
        space_id: str = None,
        storage_location: str = None,
        stream_name: str = None,
        transcode_templates: str = None,
        vod_transcode_group_id: str = None,
    ):
        self.app_name = app_name
        self.auto_compose = auto_compose
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id
        self.create_time = create_time
        self.cycle_duration = cycle_duration
        self.delay_time = delay_time
        self.domain_name = domain_name
        self.format_config = format_config
        self.on_demand = on_demand
        self.record_content = record_content
        self.record_format_list = record_format_list
        self.space_id = space_id
        self.storage_location = storage_location
        self.stream_name = stream_name
        self.transcode_templates = transcode_templates
        self.vod_transcode_group_id = vod_transcode_group_id

    def validate(self):
        if self.record_format_list:
            self.record_format_list.validate()

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

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.format_config is not None:
            result['FormatConfig'] = self.format_config

        if self.on_demand is not None:
            result['OnDemand'] = self.on_demand

        if self.record_content is not None:
            result['RecordContent'] = self.record_content

        if self.record_format_list is not None:
            result['RecordFormatList'] = self.record_format_list.to_map()

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.transcode_templates is not None:
            result['TranscodeTemplates'] = self.transcode_templates

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

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FormatConfig') is not None:
            self.format_config = m.get('FormatConfig')

        if m.get('OnDemand') is not None:
            self.on_demand = m.get('OnDemand')

        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')

        if m.get('RecordFormatList') is not None:
            temp_model = main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatList()
            self.record_format_list = temp_model.from_map(m.get('RecordFormatList'))

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TranscodeTemplates') is not None:
            self.transcode_templates = m.get('TranscodeTemplates')

        if m.get('VodTranscodeGroupId') is not None:
            self.vod_transcode_group_id = m.get('VodTranscodeGroupId')

        return self

class DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatList(DaraModel):
    def __init__(
        self,
        record_format: List[main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatListRecordFormat] = None,
    ):
        self.record_format = record_format

    def validate(self):
        if self.record_format:
            for v1 in self.record_format:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatListRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        return self

class DescribeLiveRecordVodConfigsResponseBodyLiveRecordVodConfigsLiveRecordVodConfigRecordFormatListRecordFormat(DaraModel):
    def __init__(
        self,
        auto_compose: str = None,
        format: str = None,
        process_method: str = None,
        process_template_id: str = None,
        slice_duration: int = None,
        tags: str = None,
        video_process: str = None,
    ):
        self.auto_compose = auto_compose
        self.format = format
        self.process_method = process_method
        self.process_template_id = process_template_id
        self.slice_duration = slice_duration
        self.tags = tags
        self.video_process = video_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_compose is not None:
            result['AutoCompose'] = self.auto_compose

        if self.format is not None:
            result['Format'] = self.format

        if self.process_method is not None:
            result['ProcessMethod'] = self.process_method

        if self.process_template_id is not None:
            result['ProcessTemplateId'] = self.process_template_id

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.video_process is not None:
            result['VideoProcess'] = self.video_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCompose') is not None:
            self.auto_compose = m.get('AutoCompose')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('ProcessMethod') is not None:
            self.process_method = m.get('ProcessMethod')

        if m.get('ProcessTemplateId') is not None:
            self.process_template_id = m.get('ProcessTemplateId')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VideoProcess') is not None:
            self.video_process = m.get('VideoProcess')

        return self

