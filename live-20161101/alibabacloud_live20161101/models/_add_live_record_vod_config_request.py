# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddLiveRecordVodConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        auto_compose: str = None,
        compose_vod_transcode_group_id: str = None,
        cycle_duration: int = None,
        delay_time: int = None,
        domain_name: str = None,
        on_demand: int = None,
        owner_id: int = None,
        record_content: str = None,
        record_format: List[main_models.AddLiveRecordVodConfigRequestRecordFormat] = None,
        region_id: str = None,
        space_id: str = None,
        storage_location: str = None,
        stream_name: str = None,
        transcode_templates: List[str] = None,
        vod_transcode_group_id: str = None,
    ):
        # The name of the application that the stream belongs to. You can find this value on the [stream management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # This parameter is required.
        self.app_name = app_name
        # >Notice: This parameter is ignored if `RecordFormat` is specified.
        # Specifies whether to automatically merge files from multiple recording cycles into a single file after a live stream ends.
        # 
        # A value of **ON** enables automatic merging. If enabled, you must also specify the `ComposeVodTranscodeGroupId` parameter. By default, automatic merging is disabled.
        self.auto_compose = auto_compose
        # >Notice: This parameter is ignored if `RecordFormat` is specified.
        # The ID of the ApsaraVideo VOD transcoding template group for transcoding the merged video. This parameter is required if `AutoCompose` is set to `ON`.
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id
        # The cycle duration, in seconds. The default value is **3600**. The value must be between **300** and **21600**.
        self.cycle_duration = cycle_duration
        # The stream interruption timeout, in seconds. If a stream interruption is shorter than this duration, recording continues in the same file. If the interruption is longer, a new file is created. Valid values: 15 to 21600.
        self.delay_time = delay_time
        # The streaming domain.
        # 
        # > Ensure ApsaraVideo VOD is activated in the same region as the streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The recording trigger mode. Valid values:
        # 
        # - **0** (Default): Automatic recording.
        # 
        # - **1**: On-demand recording triggered by an HTTP callback.
        # 
        # - **2**: On-demand recording triggered by ingest parameters.
        # 
        # - **7**: Manual recording. Allows you to start and stop recording by calling the `RealTimeRecordCommand` operation.
        self.on_demand = on_demand
        self.owner_id = owner_id
        # The recorded content. Valid values:
        # 
        # - `raw` (Default): Records the source stream.
        # 
        # - `transcode`: Records transcoded streams.
        # 
        # To record both source and transcoded streams, provide a comma-separated list, for example, `raw,transcode`.
        # 
        # > If this parameter is set to include `transcode`, you must specify at least one template in the `TranscodeTemplates` parameter.
        self.record_content = record_content
        # A list of format-specific recording configurations.
        self.record_format = record_format
        # The region ID. The example value `cn-shanghai` indicates the China (Shanghai) region.
        self.region_id = region_id
        # The ID of the VOD application space. You can obtain this ID from the **VOD console** or by calling an [API operation to query application information](https://help.aliyun.com/document_detail/454873.html). This parameter applies only when the VOD application space feature is enabled.
        self.space_id = space_id
        # The storage location.
        self.storage_location = storage_location
        # The stream name. You can find this value on the [stream management](https://help.aliyun.com/document_detail/197397.html) page.
        self.stream_name = stream_name
        # A list of transcoding templates for recording transcoded streams.
        self.transcode_templates = transcode_templates
        # >Notice: This parameter is ignored if `RecordFormat` is specified.
        # The ID of the ApsaraVideo VOD transcoding template group for transcoding recorded videos.
        self.vod_transcode_group_id = vod_transcode_group_id

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
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auto_compose is not None:
            result['AutoCompose'] = self.auto_compose

        if self.compose_vod_transcode_group_id is not None:
            result['ComposeVodTranscodeGroupId'] = self.compose_vod_transcode_group_id

        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.on_demand is not None:
            result['OnDemand'] = self.on_demand

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.record_content is not None:
            result['RecordContent'] = self.record_content

        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OnDemand') is not None:
            self.on_demand = m.get('OnDemand')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.AddLiveRecordVodConfigRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

class AddLiveRecordVodConfigRequestRecordFormat(DaraModel):
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
        # Specifies whether to automatically merge recording files for this format after the stream ends. Valid values:
        # 
        # - `ON`: Enables automatic merging.
        # 
        # - `OFF`: Disables automatic merging.
        self.auto_compose = auto_compose
        # The recording format. Valid values:
        # 
        # - `m3u8`
        # 
        # - `flv`
        # 
        # - `mp4`
        self.format = format
        # The video processing method. Valid values:
        # 
        # - `transcode`: Uses a transcoding template group to process the video.
        # 
        # - `workflow`: Uses a workflow to process the video.
        self.process_method = process_method
        # The ID of the transcoding template group or workflow.
        # 
        # > The specified ID must match the `ProcessMethod`. For example, provide a transcoding template group ID if `ProcessMethod` is `transcode`, or a workflow ID if `ProcessMethod` is `workflow`.
        self.process_template_id = process_template_id
        # The slice duration, in seconds.
        # 
        # This parameter applies only to the `m3u8` format.
        # 
        # The value must be between 5 and 30. The default is 30.
        self.slice_duration = slice_duration
        # The tags for video categorization.
        self.tags = tags
        # The video source to process. Valid values:
        # 
        # - `origin` (Default): The per-cycle recording files.
        # 
        # - `compose`: The single video file composed from all cycles.
        # 
        # To process both video sources, separate the values with a comma (,), for example, `origin,compose`.
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

