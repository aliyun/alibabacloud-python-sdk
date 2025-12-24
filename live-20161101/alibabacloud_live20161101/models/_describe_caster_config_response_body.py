# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterConfigResponseBody(DaraModel):
    def __init__(
        self,
        auto_switch_urgent_config: str = None,
        auto_switch_urgent_on: str = None,
        callback_url: str = None,
        caster_id: str = None,
        caster_name: str = None,
        channel_enable: int = None,
        delay: float = None,
        domain_name: str = None,
        program_effect: int = None,
        program_name: str = None,
        record_config: main_models.DescribeCasterConfigResponseBodyRecordConfig = None,
        request_id: str = None,
        side_output_url: str = None,
        side_output_url_list: str = None,
        sync_groups_config: main_models.DescribeCasterConfigResponseBodySyncGroupsConfig = None,
        transcode_config: main_models.DescribeCasterConfigResponseBodyTranscodeConfig = None,
        urgent_image_id: str = None,
        urgent_image_url: str = None,
        urgent_live_stream_url: str = None,
        urgent_material_id: str = None,
    ):
        # The configuration for automatic switchover to the standby resource. The `eofThres` field specifies the duration after which the production studio automatically switches to the standby resource if a stream interruption occurs. Unit: seconds.
        self.auto_switch_urgent_config = auto_switch_urgent_config
        # Indicates whether the production studio automatically switches to the standby resource in case of a stream interruption.
        # 
        # *   **true**
        # *   **false**
        self.auto_switch_urgent_on = auto_switch_urgent_on
        # The callback URL.
        self.callback_url = callback_url
        # The ID of the production studio.
        self.caster_id = caster_id
        # The name of the production studio.
        self.caster_name = caster_name
        # Indicates whether channels are enabled for the production studio. Valid values:
        # 
        # *   **0**: Channels are disabled.
        # *   **1**: Channels are enabled.
        self.channel_enable = channel_enable
        # Indicates whether stream delay is enabled. Unit: seconds.
        # 
        # *   **0**: Stream delay is disabled.
        # *   **A value greater than 0**: Stream delay is enabled.
        self.delay = delay
        # The main streaming domain.
        self.domain_name = domain_name
        # Indicates whether the carousel playback feature is enabled. Valid values:
        # 
        # *   **0**: The carousel playback feature is disabled.
        # *   **1**: The carousel playback feature is enabled.
        self.program_effect = program_effect
        # The name of the playlist for carousel playback.
        self.program_name = program_name
        # The recording configuration. If this parameter is empty, the recording feature is disabled.
        self.record_config = record_config
        # The ID of the request.
        self.request_id = request_id
        # The custom stream redirect URL.
        self.side_output_url = side_output_url
        # The list of custom stream redirect URLs.
        self.side_output_url_list = side_output_url_list
        # The storage configuration.
        self.sync_groups_config = sync_groups_config
        # The transcoding configuration.
        self.transcode_config = transcode_config
        # Prepared broadcast image media asset ID.
        self.urgent_image_id = urgent_image_id
        # URL of the standby image material.
        self.urgent_image_url = urgent_image_url
        # The URL of the standby live stream.
        self.urgent_live_stream_url = urgent_live_stream_url
        # The ID of the material that is used as the standby video from the media library.
        self.urgent_material_id = urgent_material_id

    def validate(self):
        if self.record_config:
            self.record_config.validate()
        if self.sync_groups_config:
            self.sync_groups_config.validate()
        if self.transcode_config:
            self.transcode_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_switch_urgent_config is not None:
            result['AutoSwitchUrgentConfig'] = self.auto_switch_urgent_config

        if self.auto_switch_urgent_on is not None:
            result['AutoSwitchUrgentOn'] = self.auto_switch_urgent_on

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.caster_name is not None:
            result['CasterName'] = self.caster_name

        if self.channel_enable is not None:
            result['ChannelEnable'] = self.channel_enable

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.program_effect is not None:
            result['ProgramEffect'] = self.program_effect

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.record_config is not None:
            result['RecordConfig'] = self.record_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.side_output_url is not None:
            result['SideOutputUrl'] = self.side_output_url

        if self.side_output_url_list is not None:
            result['SideOutputUrlList'] = self.side_output_url_list

        if self.sync_groups_config is not None:
            result['SyncGroupsConfig'] = self.sync_groups_config.to_map()

        if self.transcode_config is not None:
            result['TranscodeConfig'] = self.transcode_config.to_map()

        if self.urgent_image_id is not None:
            result['UrgentImageId'] = self.urgent_image_id

        if self.urgent_image_url is not None:
            result['UrgentImageUrl'] = self.urgent_image_url

        if self.urgent_live_stream_url is not None:
            result['UrgentLiveStreamUrl'] = self.urgent_live_stream_url

        if self.urgent_material_id is not None:
            result['UrgentMaterialId'] = self.urgent_material_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSwitchUrgentConfig') is not None:
            self.auto_switch_urgent_config = m.get('AutoSwitchUrgentConfig')

        if m.get('AutoSwitchUrgentOn') is not None:
            self.auto_switch_urgent_on = m.get('AutoSwitchUrgentOn')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('CasterName') is not None:
            self.caster_name = m.get('CasterName')

        if m.get('ChannelEnable') is not None:
            self.channel_enable = m.get('ChannelEnable')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ProgramEffect') is not None:
            self.program_effect = m.get('ProgramEffect')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('RecordConfig') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyRecordConfig()
            self.record_config = temp_model.from_map(m.get('RecordConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SideOutputUrl') is not None:
            self.side_output_url = m.get('SideOutputUrl')

        if m.get('SideOutputUrlList') is not None:
            self.side_output_url_list = m.get('SideOutputUrlList')

        if m.get('SyncGroupsConfig') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodySyncGroupsConfig()
            self.sync_groups_config = temp_model.from_map(m.get('SyncGroupsConfig'))

        if m.get('TranscodeConfig') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyTranscodeConfig()
            self.transcode_config = temp_model.from_map(m.get('TranscodeConfig'))

        if m.get('UrgentImageId') is not None:
            self.urgent_image_id = m.get('UrgentImageId')

        if m.get('UrgentImageUrl') is not None:
            self.urgent_image_url = m.get('UrgentImageUrl')

        if m.get('UrgentLiveStreamUrl') is not None:
            self.urgent_live_stream_url = m.get('UrgentLiveStreamUrl')

        if m.get('UrgentMaterialId') is not None:
            self.urgent_material_id = m.get('UrgentMaterialId')

        return self

class DescribeCasterConfigResponseBodyTranscodeConfig(DaraModel):
    def __init__(
        self,
        caster_template: str = None,
        custom_params: main_models.DescribeCasterConfigResponseBodyTranscodeConfigCustomParams = None,
        live_template_ids: main_models.DescribeCasterConfigResponseBodyTranscodeConfigLiveTemplateIds = None,
    ):
        # The transcoding template of the production studio. Valid values:
        # 
        # *   **lp_ld**: low definition
        # *   **lp_sd**: standard definition
        # *   **lp_hd**: high definition
        # *   **lp_ud**: ultra high definition
        # *   **lp_ld_v**: low definition (portrait mode)
        # *   **lp_sd_v**: standard definition (portrait mode)
        # *   **lp_hd_v**: high definition (portrait mode)
        # *   **lp_ud_v**: ultra high definition (portrait mode)
        self.caster_template = caster_template
        # The custom settings.
        self.custom_params = custom_params
        # The transcoding setting for live streams.
        self.live_template_ids = live_template_ids

    def validate(self):
        if self.custom_params:
            self.custom_params.validate()
        if self.live_template_ids:
            self.live_template_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_template is not None:
            result['CasterTemplate'] = self.caster_template

        if self.custom_params is not None:
            result['CustomParams'] = self.custom_params.to_map()

        if self.live_template_ids is not None:
            result['LiveTemplateIds'] = self.live_template_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterTemplate') is not None:
            self.caster_template = m.get('CasterTemplate')

        if m.get('CustomParams') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyTranscodeConfigCustomParams()
            self.custom_params = temp_model.from_map(m.get('CustomParams'))

        if m.get('LiveTemplateIds') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyTranscodeConfigLiveTemplateIds()
            self.live_template_ids = temp_model.from_map(m.get('LiveTemplateIds'))

        return self

class DescribeCasterConfigResponseBodyTranscodeConfigLiveTemplateIds(DaraModel):
    def __init__(
        self,
        location_id: List[str] = None,
    ):
        self.location_id = location_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location_id is not None:
            result['LocationId'] = self.location_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        return self

class DescribeCasterConfigResponseBodyTranscodeConfigCustomParams(DaraModel):
    def __init__(
        self,
        video: main_models.DescribeCasterConfigResponseBodyTranscodeConfigCustomParamsVideo = None,
    ):
        # The video parameters.
        self.video = video

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video is not None:
            result['video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('video') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyTranscodeConfigCustomParamsVideo()
            self.video = temp_model.from_map(m.get('video'))

        return self

class DescribeCasterConfigResponseBodyTranscodeConfigCustomParamsVideo(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        fps: int = None,
        height: int = None,
        width: int = None,
    ):
        # The video bitrate.
        self.bitrate = bitrate
        # The video frame rate.
        self.fps = fps
        # The video height. Unit: pixels.
        self.height = height
        # The video width. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate

        if self.fps is not None:
            result['fps'] = self.fps

        if self.height is not None:
            result['height'] = self.height

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')

        if m.get('fps') is not None:
            self.fps = m.get('fps')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class DescribeCasterConfigResponseBodySyncGroupsConfig(DaraModel):
    def __init__(
        self,
        sync_group: List[main_models.DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroup] = None,
    ):
        self.sync_group = sync_group

    def validate(self):
        if self.sync_group:
            for v1 in self.sync_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SyncGroup'] = []
        if self.sync_group is not None:
            for k1 in self.sync_group:
                result['SyncGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sync_group = []
        if m.get('SyncGroup') is not None:
            for k1 in m.get('SyncGroup'):
                temp_model = main_models.DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroup()
                self.sync_group.append(temp_model.from_map(k1))

        return self

class DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroup(DaraModel):
    def __init__(
        self,
        host_resource_id: str = None,
        mode: int = None,
        resource_ids: main_models.DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroupResourceIds = None,
    ):
        # The ID of the resource in the production studio.
        self.host_resource_id = host_resource_id
        # The cache mode of the Static Page Caching policy. Valid values:
        # 
        # *   0: standard mode
        # *   1: force mode
        # *   2: no cache
        self.mode = mode
        # The IDs of the resources for which you want to modify the resource group. The number of resource IDs is 1 to 50.
        self.resource_ids = resource_ids

    def validate(self):
        if self.resource_ids:
            self.resource_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_resource_id is not None:
            result['HostResourceId'] = self.host_resource_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostResourceId') is not None:
            self.host_resource_id = m.get('HostResourceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ResourceIds') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroupResourceIds()
            self.resource_ids = temp_model.from_map(m.get('ResourceIds'))

        return self

class DescribeCasterConfigResponseBodySyncGroupsConfigSyncGroupResourceIds(DaraModel):
    def __init__(
        self,
        resource_id: List[str] = None,
    ):
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

class DescribeCasterConfigResponseBodyRecordConfig(DaraModel):
    def __init__(
        self,
        on_demand: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        record_format: main_models.DescribeCasterConfigResponseBodyRecordConfigRecordFormat = None,
    ):
        # On-demand recording. Values:
        # - 0: Off. 
        # - 1: Via HTTP callback. 
        # - 2: Parse streaming parameters for on-demand recording. 
        # - 7: Default to not record.
        self.on_demand = on_demand
        # The OSS bucket for storage.
        self.oss_bucket = oss_bucket
        # The Object Storage Service (OSS) endpoint.
        self.oss_endpoint = oss_endpoint
        # The recording configuration.
        self.record_format = record_format

    def validate(self):
        if self.record_format:
            self.record_format.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.on_demand is not None:
            result['OnDemand'] = self.on_demand

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.record_format is not None:
            result['RecordFormat'] = self.record_format.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnDemand') is not None:
            self.on_demand = m.get('OnDemand')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('RecordFormat') is not None:
            temp_model = main_models.DescribeCasterConfigResponseBodyRecordConfigRecordFormat()
            self.record_format = temp_model.from_map(m.get('RecordFormat'))

        return self

class DescribeCasterConfigResponseBodyRecordConfigRecordFormat(DaraModel):
    def __init__(
        self,
        record_format: List[main_models.DescribeCasterConfigResponseBodyRecordConfigRecordFormatRecordFormat] = None,
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
                temp_model = main_models.DescribeCasterConfigResponseBodyRecordConfigRecordFormatRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        return self

class DescribeCasterConfigResponseBodyRecordConfigRecordFormatRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_oss_object_prefix: str = None,
    ):
        # The length of the recording.
        self.cycle_duration = cycle_duration
        # The format of the recording.
        self.format = format
        # The name of the recording.
        self.oss_object_prefix = oss_object_prefix
        # The name of the segment.
        self.slice_oss_object_prefix = slice_oss_object_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.format is not None:
            result['Format'] = self.format

        if self.oss_object_prefix is not None:
            result['OssObjectPrefix'] = self.oss_object_prefix

        if self.slice_oss_object_prefix is not None:
            result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OssObjectPrefix') is not None:
            self.oss_object_prefix = m.get('OssObjectPrefix')

        if m.get('SliceOssObjectPrefix') is not None:
            self.slice_oss_object_prefix = m.get('SliceOssObjectPrefix')

        return self

