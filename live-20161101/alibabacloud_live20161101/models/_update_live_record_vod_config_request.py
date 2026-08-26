# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class UpdateLiveRecordVodConfigRequest(DaraModel):
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
        record_format: List[main_models.UpdateLiveRecordVodConfigRequestRecordFormat] = None,
        region_id: str = None,
        stream_name: str = None,
        transcode_templates: List[str] = None,
        vod_transcode_group_id: str = None,
    ):
        # The application name. You can view the `AppName` on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        # 
        # This parameter is required.
        self.app_name = app_name
        # >Notice: This parameter is ignored if the `RecordFormat` parameter is specified.
        # Specifies whether to enable automatic composition. Valid values:
        # 
        # - **ON**: Enables automatic composition. If you set this value to ON, you must also specify the `ComposeVodTranscodeGroupId` parameter.
        self.auto_compose = auto_compose
        # >Notice: This parameter is ignored if the `RecordFormat` parameter is specified.
        # The ID of the ApsaraVideo for VOD transcoding template group used to transcode the video after automatic composition.
        # 
        # > You can get the ID by calling the [Query Transcoding Configuration List](https://help.aliyun.com/document_detail/454928.html) operation.
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id
        # The duration of each cyclical recording file, in seconds. Default value: **3600**. Valid values: **300** to **21600**.
        self.cycle_duration = cycle_duration
        # The maximum duration of a stream interruption, in seconds. If a stream interruption exceeds this duration, the system generates a new file. Valid values: 15 to 21600.
        self.delay_time = delay_time
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The on-demand recording mode. Valid values:
        # 
        # - **0** (default): Disables on-demand recording.
        # 
        # - **1**: Enables on-demand recording triggered by an HTTP callback.
        # 
        # - **2**: Triggers recording by parsing push streaming parameters.
        # 
        # - **7**: Manual recording. Call the [RealTimeRecordCommand](https://help.aliyun.com/document_detail/2847882.html) operation to start or stop recording.
        self.on_demand = on_demand
        self.owner_id = owner_id
        # A list of parameters for each recording format.
        self.record_format = record_format
        # The region ID.
        self.region_id = region_id
        # The stream name. You can view the `StreamName` on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page.
        self.stream_name = stream_name
        # A list of transcoding templates.
        self.transcode_templates = transcode_templates
        # >Notice: This parameter is ignored if the `RecordFormat` parameter is specified. The ID of the ApsaraVideo for VOD transcoding template group.
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

        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.UpdateLiveRecordVodConfigRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TranscodeTemplates') is not None:
            self.transcode_templates = m.get('TranscodeTemplates')

        if m.get('VodTranscodeGroupId') is not None:
            self.vod_transcode_group_id = m.get('VodTranscodeGroupId')

        return self

class UpdateLiveRecordVodConfigRequestRecordFormat(DaraModel):
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
        # Specifies whether to enable automatic composition. Valid values:
        # 
        # - `ON`: Enables automatic composition.
        # 
        # - `OFF`: Disables automatic composition.
        self.auto_compose = auto_compose
        # The recording storage format.
        self.format = format
        # The video processing method. Valid values:
        # 
        # - `transcode`: Processes the video by using a transcoding template group.
        # 
        # - `workflow`: Processes the video by using a workflow.
        self.process_method = process_method
        # The ID of the transcoding template group or workflow.
        # 
        # > ## The ID must match the video processing method specified in ProcessMethod. For example, if ProcessMethod is set to transcode, you must use a transcoding template group ID.
        self.process_template_id = process_template_id
        # The duration of each segment, in seconds.
        # >Notice: This parameter applies only to the `m3u8` format.
        # The default value is 30. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # A tag for video classification.
        self.tags = tags
        # The video source to process. Valid values:
        # 
        # - `origin` (default): Processes the source video.
        # 
        # - `compose`: Processes the composed video.
        # 
        # To process both the source and composed videos, separate the values with a comma. For example, `origin,compose`.
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

