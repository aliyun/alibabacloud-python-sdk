# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCasterConfigRequest(DaraModel):
    def __init__(
        self,
        auto_switch_urgent_config: str = None,
        auto_switch_urgent_on: bool = None,
        callback_url: str = None,
        caster_id: str = None,
        caster_name: str = None,
        channel_enable: int = None,
        delay: float = None,
        domain_name: str = None,
        owner_id: int = None,
        program_effect: int = None,
        program_name: str = None,
        record_config: str = None,
        region_id: str = None,
        side_output_url: str = None,
        side_output_url_list: str = None,
        sync_groups_config: str = None,
        transcode_config: str = None,
        urgent_image_id: str = None,
        urgent_image_url: str = None,
        urgent_live_stream_url: str = None,
        urgent_material_id: str = None,
    ):
        # The automatic standby switchover configuration.
        # `eofThres`: the duration of stream interruption after which the system automatically switches to the standby video, in seconds.
        self.auto_switch_urgent_config = auto_switch_urgent_config
        # Specifies whether to enable automatic switchover to the standby video when the stream is interrupted.
        # - **true**: enabled.
        # - **false**: disabled.
        self.auto_switch_urgent_on = auto_switch_urgent_on
        # The callback URL. To receive callback notifications, enter a valid receiving address that accepts the HTTP protocol. If this parameter is set to empty, callback notifications for the production studio are canceled by default.
        # > For more information about production studio callbacks, see [Cloud production studio callback information](https://help.aliyun.com/document_detail/213633.html).
        self.callback_url = callback_url
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** to view the ID.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page of the ApsaraVideo Live console is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The name of the production studio.
        self.caster_name = caster_name
        # Specifies whether to enable Channel. If Channel was previously enabled (ChannelEnable=1), you must explicitly pass ChannelEnable=1 in each call to maintain the channel status. Otherwise, the error InvalidCaster.ChannelDisableUnsupported is returned.
        #          
        # - **0** (default): disabled.
        # - **1**: enabled. 
        # 
        # > Channel is disabled by default and cannot be disabled after it is enabled. When Channel is disabled, resources are directly referenced by layouts. To enable Channel for the first time, the production studio must be stopped. Existing layouts are discarded. Resources must first be assigned to a Channel, and new layouts directly reference the Channel. Through Channel, you can adjust the playback progress and status of video sources. In this mode, if the video source, PVW, and PGM areas reference the same resource, the corresponding views remain synchronized.
        self.channel_enable = channel_enable
        # The stream delay, in seconds.
        # 
        # - **0** (default): disables stream delay.
        # - Greater than **0**: enables stream delay.
        # - **Empty**: clears the stream delay configuration by default.
        # > The maximum value is 300 seconds.
        self.delay = delay
        # The primary streaming domain.
        # 
        # Complete the domain name configuration before starting the production studio. If this parameter is empty, the domain name configuration of the production studio is cleared by default.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # Specifies whether the program list takes effect. 
        # 
        # - **0**: does not take effect.
        # - **1**: takes effect.
        self.program_effect = program_effect
        # The name of the program list. This parameter can be configured when the program list feature is used.
        self.program_name = program_name
        # The recording configuration in JSON format. The configuration elements are as follows:
        # 
        # - **endpoint**: the API endpoint of the Alibaba Cloud service.
        # - **ossBucket**: the name of the OSS bucket.
        # - **videoFormat**: the video file formats supported for export. Example: `[{\\"OssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{StartTime}_{EndTime}\\",\\"Format\\":\\"m3u8\\",\\"CycleDuration\\":21600,\\"SliceOssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{UnixTimestamp}\\"},{\\"OssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{StartTime}_{EndTime}\\",\\"Format\\":\\"flv\\",\\"CycleDuration\\":21600}]`.
        # - **interval**: the time interval, in milliseconds (ms).
        # 
        # >If this parameter is set to empty, the recording feature is not enabled. If this parameter is set to empty, the recording configuration is cleared by default.
        self.record_config = record_config
        # The region ID.
        self.region_id = region_id
        # The ingest URL that corresponds to the custom bypass output address of the production studio. 
        # If this parameter is empty, the ingest URL that corresponds to the output address automatically generated by Alibaba Cloud is used by default.
        # > Currently, SideOutputUrl supports only the RTMP protocol for stream ingest.
        self.side_output_url = side_output_url
        # The list of multi-destination relay streaming addresses. The addresses can be CDN ingest URLs from Alibaba Cloud or third-party providers. A maximum of 20 RTMP relay addresses can be added to a production studio.
        # 
        # 
        # > Specify multiple addresses in the array format: ["rtmp://domain/app1/stream1","rtmp://domain/app2/stream2"].
        self.side_output_url_list = side_output_url_list
        # The multi-view synchronization configuration that synchronizes multiple video sources.
        # Multi-view synchronization has two modes:
        # 
        # - mode: 0 (streamer mode. Multiple video sources are synchronized based on the specified mode.)
        # 
        # - mode: 1 (conference mode. There is no concept of a streamer video. All video sources are synchronized with each other.)
        # 
        # 
        # 
        # Streamer mode: hostResourceId: the streamer video source in streamer mode.
        # 
        # Conference mode: the hostResourceId field is not required. Only the resource IDs in resourceIds need to be provided.
        self.sync_groups_config = sync_groups_config
        # The transcoding configuration. 
        # 
        # A JSON-formatted string. Use upper camel case for internal fields of the struct. If this parameter is set to empty, the transcoding configuration is cleared by default. If the transcoding template is empty, an error is returned when the production studio starts.
        self.transcode_config = transcode_config
        # The media asset ID of the standby image in the media library.
        self.urgent_image_id = urgent_image_id
        # The URL of the standby image.
        self.urgent_image_url = urgent_image_url
        # The URL of the standby live stream.
        self.urgent_live_stream_url = urgent_live_stream_url
        # The media asset ID of the standby video in the media library. If this parameter is set to empty, the standby configuration is cleared by default.
        self.urgent_material_id = urgent_material_id

    def validate(self):
        pass

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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.program_effect is not None:
            result['ProgramEffect'] = self.program_effect

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.record_config is not None:
            result['RecordConfig'] = self.record_config

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.side_output_url is not None:
            result['SideOutputUrl'] = self.side_output_url

        if self.side_output_url_list is not None:
            result['SideOutputUrlList'] = self.side_output_url_list

        if self.sync_groups_config is not None:
            result['SyncGroupsConfig'] = self.sync_groups_config

        if self.transcode_config is not None:
            result['TranscodeConfig'] = self.transcode_config

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProgramEffect') is not None:
            self.program_effect = m.get('ProgramEffect')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('RecordConfig') is not None:
            self.record_config = m.get('RecordConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SideOutputUrl') is not None:
            self.side_output_url = m.get('SideOutputUrl')

        if m.get('SideOutputUrlList') is not None:
            self.side_output_url_list = m.get('SideOutputUrlList')

        if m.get('SyncGroupsConfig') is not None:
            self.sync_groups_config = m.get('SyncGroupsConfig')

        if m.get('TranscodeConfig') is not None:
            self.transcode_config = m.get('TranscodeConfig')

        if m.get('UrgentImageId') is not None:
            self.urgent_image_id = m.get('UrgentImageId')

        if m.get('UrgentImageUrl') is not None:
            self.urgent_image_url = m.get('UrgentImageUrl')

        if m.get('UrgentLiveStreamUrl') is not None:
            self.urgent_live_stream_url = m.get('UrgentLiveStreamUrl')

        if m.get('UrgentMaterialId') is not None:
            self.urgent_material_id = m.get('UrgentMaterialId')

        return self

