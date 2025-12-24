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
        # The configuration for automatic switchover to the standby resource.
        # 
        # The `eofThres` field specifies the duration after which the production studio automatically switches to the standby resource if a stream interruption occurs. Unit: seconds.
        self.auto_switch_urgent_config = auto_switch_urgent_config
        # Specifies whether the production studio automatically switches to the standby resource in case of a stream interruption.
        # 
        # *   **true**
        # *   **false**
        self.auto_switch_urgent_on = auto_switch_urgent_on
        # The callback URL. Enter a valid HTTP address for receiving callback notifications. If you do not specify this parameter, the production studio does not send callback notifications.
        # 
        # >  For more information about production studio callbacks, see [Production studio callbacks](https://help.aliyun.com/document_detail/213633.html).
        self.callback_url = callback_url
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The name of the production studio.
        self.caster_name = caster_name
        # Specifies whether to enable channels. Valid values:
        # 
        # *   **0** (default): disables channels.
        # *   **1**: enables channels.
        # 
        # > You cannot disable channels after you enable them. If you set this parameter to 0, the production studio references video resources in a layout without using channels. If you enable channels for the first time, make sure that the production studio is in the idle state. After you enable channels, a new layout that references video resources by using channels is generated to replace the original one. Therefore, you must specify video resources for channels. You can use the channels to change the playback progress or status. If the video resource, preview, and program modules of the production studio use the same video source, the three modules display the same content.
        self.channel_enable = channel_enable
        # Specifies whether to enable stream delay. Unit: seconds. Valid values:
        # 
        # *   **0** (default): disables stream delay.
        # 
        # *   **A value greater than 0**: enables stream delay.
        # 
        # *   **Empty**: clears the stream delay configuration.
        # 
        #     **
        # 
        #     **Note **The maximum value can be 300 seconds.
        self.delay = delay
        # The main streaming domain.
        # 
        # Complete the configuration of the domain name before the production studio is started. If you do not specify this parameter, the domain configuration for the production studio is cleared.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # Specifies whether to enable the carousel playback feature. Valid values:
        # 
        # *   **0**: disables carousel playback.
        # *   **1**: enables carousel playback.
        self.program_effect = program_effect
        # The name of the playlist for carousel playback. You can specify this parameter if you enable the carousel playback feature.
        self.program_name = program_name
        # The recording configuration. The value is a JSON string. You can configure the following fields:
        # 
        # *   **endpoint**: the API server address of an Alibaba Cloud service.
        # *   **ossBucket**: the name of the Object Storage Service (OSS) bucket.
        # *   **videoFormat**: the format in which the video file can be exported. Example: `[{\\"OssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{StartTime}_{EndTime}\\",\\"Format\\":\\"m3u8\\",\\"CycleDuration\\":21600,\\"SliceOssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{UnixTimestamp}\\"},{\\"OssObjectPrefix\\":\\"record/{AppName}/{StreamName}/{StartTime}_{EndTime}\\",\\"Format\\":\\"flv\\",\\"CycleDuration\\":21600}]`.
        # *   **interval**: the interval between recordings. Unit: milliseconds.
        # 
        # > If you do not specify this parameter, the recording feature is disabled and the recording configuration for the production studio is cleared.
        self.record_config = record_config
        self.region_id = region_id
        # The custom stream redirect URL.
        # 
        # If you do not specify this parameter, the production studio uses the redirect URL generated by the system.
        # 
        # > Redirect URLs support only the Real-Time Messaging Protocol (RTMP) protocol.
        self.side_output_url = side_output_url
        # The stream relay URLs. A relay URL can be an Alibaba Cloud URL or a URL from a third-party CDN provider. You can specify up to 20 relay URLs over the RTMP protocol.
        # 
        # > Use the following format to specify multiple relay URLs: "rtmp://domain/app1/stream1","rtmp://domain/app2/stream2".
        self.side_output_url_list = side_output_url_list
        # The multi-view synchronization configuration. You can specify this parameter to synchronize multiple video sources.
        # 
        # There are two modes of multi-view synchronization.
        # 
        # *   A value of 0 for the mode field specifies the streamer mode. In this mode, multiple video sources are synchronized based on the settings by the streamer.
        # *   A value of 1 for the mode field specifies the conference mode. In this mode, all video sources are synchronized.
        # 
        # In the streamer mode, the hostResourceId field specifies the video source on the streamer side.
        # 
        # In the conference mode, the hostResourceId field is not available. You need to provide only resource IDs that are required.
        self.sync_groups_config = sync_groups_config
        # The transcoding configuration.
        # 
        # The value is a JSON string. Use upper camel case for fields of the string. If you do not specify this parameter, the transcoding configuration is cleared. If no transcoding template is available, an error occurs when the production studio is started.
        self.transcode_config = transcode_config
        # The ID of the standby image from the media library.
        self.urgent_image_id = urgent_image_id
        # The URL of the standby image.
        self.urgent_image_url = urgent_image_url
        # The URL of the standby live stream.
        self.urgent_live_stream_url = urgent_live_stream_url
        # The ID of the standby video from the media library. If you do not specify this parameter, the standby video configuration for the production studio is cleared.
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

