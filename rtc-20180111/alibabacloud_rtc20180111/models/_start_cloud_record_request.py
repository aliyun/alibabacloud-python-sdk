# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartCloudRecordRequest(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        app_id: str = None,
        backgrounds: List[main_models.StartCloudRecordRequestBackgrounds] = None,
        bg_color: main_models.StartCloudRecordRequestBgColor = None,
        channel_id: str = None,
        clock_widgets: List[main_models.StartCloudRecordRequestClockWidgets] = None,
        crop_mode: int = None,
        images: List[main_models.StartCloudRecordRequestImages] = None,
        layout_specified_users: main_models.StartCloudRecordRequestLayoutSpecifiedUsers = None,
        panes: List[main_models.StartCloudRecordRequestPanes] = None,
        record_mode: int = None,
        region_color: main_models.StartCloudRecordRequestRegionColor = None,
        reserve_pane_for_no_camera_user: bool = None,
        show_default_background_on_mute: bool = None,
        single_streaming_record: main_models.StartCloudRecordRequestSingleStreamingRecord = None,
        start_without_channel: bool = None,
        start_without_channel_wait_time: int = None,
        storage_config: main_models.StartCloudRecordRequestStorageConfig = None,
        sub_high_resolution_stream: bool = None,
        task_id: str = None,
        template_id: str = None,
        texts: List[main_models.StartCloudRecordRequestTexts] = None,
    ):
        self.annotation = annotation
        # appId
        # 
        # This parameter is required.
        self.app_id = app_id
        self.backgrounds = backgrounds
        self.bg_color = bg_color
        # channelName
        # 
        # This parameter is required.
        self.channel_id = channel_id
        self.clock_widgets = clock_widgets
        self.crop_mode = crop_mode
        self.images = images
        self.layout_specified_users = layout_specified_users
        # panes
        self.panes = panes
        self.record_mode = record_mode
        self.region_color = region_color
        self.reserve_pane_for_no_camera_user = reserve_pane_for_no_camera_user
        self.show_default_background_on_mute = show_default_background_on_mute
        self.single_streaming_record = single_streaming_record
        self.start_without_channel = start_without_channel
        self.start_without_channel_wait_time = start_without_channel_wait_time
        # storageConfig
        # 
        # This parameter is required.
        self.storage_config = storage_config
        self.sub_high_resolution_stream = sub_high_resolution_stream
        # taskId
        self.task_id = task_id
        # templateId
        # 
        # This parameter is required.
        self.template_id = template_id
        self.texts = texts

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.bg_color:
            self.bg_color.validate()
        if self.clock_widgets:
            for v1 in self.clock_widgets:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.layout_specified_users:
            self.layout_specified_users.validate()
        if self.panes:
            for v1 in self.panes:
                 if v1:
                    v1.validate()
        if self.region_color:
            self.region_color.validate()
        if self.single_streaming_record:
            self.single_streaming_record.validate()
        if self.storage_config:
            self.storage_config.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['Annotation'] = self.annotation

        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        if self.bg_color is not None:
            result['BgColor'] = self.bg_color.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k1 in self.clock_widgets:
                result['ClockWidgets'].append(k1.to_map() if k1 else None)

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.layout_specified_users is not None:
            result['LayoutSpecifiedUsers'] = self.layout_specified_users.to_map()

        result['Panes'] = []
        if self.panes is not None:
            for k1 in self.panes:
                result['Panes'].append(k1.to_map() if k1 else None)

        if self.record_mode is not None:
            result['RecordMode'] = self.record_mode

        if self.region_color is not None:
            result['RegionColor'] = self.region_color.to_map()

        if self.reserve_pane_for_no_camera_user is not None:
            result['ReservePaneForNoCameraUser'] = self.reserve_pane_for_no_camera_user

        if self.show_default_background_on_mute is not None:
            result['ShowDefaultBackgroundOnMute'] = self.show_default_background_on_mute

        if self.single_streaming_record is not None:
            result['SingleStreamingRecord'] = self.single_streaming_record.to_map()

        if self.start_without_channel is not None:
            result['StartWithoutChannel'] = self.start_without_channel

        if self.start_without_channel_wait_time is not None:
            result['StartWithoutChannelWaitTime'] = self.start_without_channel_wait_time

        if self.storage_config is not None:
            result['StorageConfig'] = self.storage_config.to_map()

        if self.sub_high_resolution_stream is not None:
            result['SubHighResolutionStream'] = self.sub_high_resolution_stream

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.StartCloudRecordRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        if m.get('BgColor') is not None:
            temp_model = main_models.StartCloudRecordRequestBgColor()
            self.bg_color = temp_model.from_map(m.get('BgColor'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.StartCloudRecordRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.StartCloudRecordRequestImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('LayoutSpecifiedUsers') is not None:
            temp_model = main_models.StartCloudRecordRequestLayoutSpecifiedUsers()
            self.layout_specified_users = temp_model.from_map(m.get('LayoutSpecifiedUsers'))

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.StartCloudRecordRequestPanes()
                self.panes.append(temp_model.from_map(k1))

        if m.get('RecordMode') is not None:
            self.record_mode = m.get('RecordMode')

        if m.get('RegionColor') is not None:
            temp_model = main_models.StartCloudRecordRequestRegionColor()
            self.region_color = temp_model.from_map(m.get('RegionColor'))

        if m.get('ReservePaneForNoCameraUser') is not None:
            self.reserve_pane_for_no_camera_user = m.get('ReservePaneForNoCameraUser')

        if m.get('ShowDefaultBackgroundOnMute') is not None:
            self.show_default_background_on_mute = m.get('ShowDefaultBackgroundOnMute')

        if m.get('SingleStreamingRecord') is not None:
            temp_model = main_models.StartCloudRecordRequestSingleStreamingRecord()
            self.single_streaming_record = temp_model.from_map(m.get('SingleStreamingRecord'))

        if m.get('StartWithoutChannel') is not None:
            self.start_without_channel = m.get('StartWithoutChannel')

        if m.get('StartWithoutChannelWaitTime') is not None:
            self.start_without_channel_wait_time = m.get('StartWithoutChannelWaitTime')

        if m.get('StorageConfig') is not None:
            temp_model = main_models.StartCloudRecordRequestStorageConfig()
            self.storage_config = temp_model.from_map(m.get('StorageConfig'))

        if m.get('SubHighResolutionStream') is not None:
            self.sub_high_resolution_stream = m.get('SubHighResolutionStream')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartCloudRecordRequestTexts()
                self.texts.append(temp_model.from_map(k1))

        return self

class StartCloudRecordRequestTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordRequestTextsBoxColor = None,
        font: int = None,
        font_color: main_models.StartCloudRecordRequestTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.texture = texture
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.texture is not None:
            result['Texture'] = self.texture

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordRequestTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordRequestTextsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Texture') is not None:
            self.texture = m.get('Texture')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordRequestTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestStorageConfig(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        bucket: str = None,
        endpoint: str = None,
        region: int = None,
        secret_key: str = None,
        vendor: int = None,
    ):
        # accessKey
        # 
        # This parameter is required.
        self.access_key = access_key
        # bucket
        # 
        # This parameter is required.
        self.bucket = bucket
        self.endpoint = endpoint
        # region
        # 
        # This parameter is required.
        self.region = region
        # secretKey
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # vendor
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class StartCloudRecordRequestSingleStreamingRecord(DaraModel):
    def __init__(
        self,
        av_merge: bool = None,
        specified_streams: List[main_models.StartCloudRecordRequestSingleStreamingRecordSpecifiedStreams] = None,
        transcoding_parameters: main_models.StartCloudRecordRequestSingleStreamingRecordTranscodingParameters = None,
    ):
        self.av_merge = av_merge
        # This parameter is required.
        self.specified_streams = specified_streams
        self.transcoding_parameters = transcoding_parameters

    def validate(self):
        if self.specified_streams:
            for v1 in self.specified_streams:
                 if v1:
                    v1.validate()
        if self.transcoding_parameters:
            self.transcoding_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.av_merge is not None:
            result['AvMerge'] = self.av_merge

        result['SpecifiedStreams'] = []
        if self.specified_streams is not None:
            for k1 in self.specified_streams:
                result['SpecifiedStreams'].append(k1.to_map() if k1 else None)

        if self.transcoding_parameters is not None:
            result['TranscodingParameters'] = self.transcoding_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvMerge') is not None:
            self.av_merge = m.get('AvMerge')

        self.specified_streams = []
        if m.get('SpecifiedStreams') is not None:
            for k1 in m.get('SpecifiedStreams'):
                temp_model = main_models.StartCloudRecordRequestSingleStreamingRecordSpecifiedStreams()
                self.specified_streams.append(temp_model.from_map(k1))

        if m.get('TranscodingParameters') is not None:
            temp_model = main_models.StartCloudRecordRequestSingleStreamingRecordTranscodingParameters()
            self.transcoding_parameters = temp_model.from_map(m.get('TranscodingParameters'))

        return self

class StartCloudRecordRequestSingleStreamingRecordTranscodingParameters(DaraModel):
    def __init__(
        self,
        audio: main_models.StartCloudRecordRequestSingleStreamingRecordTranscodingParametersAudio = None,
        container: str = None,
    ):
        self.audio = audio
        self.container = container

    def validate(self):
        if self.audio:
            self.audio.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.StartCloudRecordRequestSingleStreamingRecordTranscodingParametersAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            self.container = m.get('Container')

        return self

class StartCloudRecordRequestSingleStreamingRecordTranscodingParametersAudio(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        codec: str = None,
        sample_rate: int = None,
    ):
        self.bitrate = bitrate
        self.codec = codec
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

class StartCloudRecordRequestSingleStreamingRecordSpecifiedStreams(DaraModel):
    def __init__(
        self,
        ids: List[str] = None,
        stream_type: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.ids = ids
        # This parameter is required.
        self.stream_type = stream_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class StartCloudRecordRequestRegionColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestPanes(DaraModel):
    def __init__(
        self,
        backgrounds: List[main_models.StartCloudRecordRequestPanesBackgrounds] = None,
        images: List[main_models.StartCloudRecordRequestPanesImages] = None,
        pane_crop_mode: int = None,
        pane_id: int = None,
        reserve_pane_for_offline_user: bool = None,
        source: str = None,
        source_type: str = None,
        texts: List[main_models.StartCloudRecordRequestPanesTexts] = None,
        video_order: str = None,
        whiteboard: main_models.StartCloudRecordRequestPanesWhiteboard = None,
    ):
        self.backgrounds = backgrounds
        self.images = images
        self.pane_crop_mode = pane_crop_mode
        # paneId
        # 
        # This parameter is required.
        self.pane_id = pane_id
        self.reserve_pane_for_offline_user = reserve_pane_for_offline_user
        # source
        self.source = source
        # sourceType
        self.source_type = source_type
        self.texts = texts
        self.video_order = video_order
        self.whiteboard = whiteboard

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()
        if self.whiteboard:
            self.whiteboard.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.pane_crop_mode is not None:
            result['PaneCropMode'] = self.pane_crop_mode

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.reserve_pane_for_offline_user is not None:
            result['ReservePaneForOfflineUser'] = self.reserve_pane_for_offline_user

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        if self.video_order is not None:
            result['VideoOrder'] = self.video_order

        if self.whiteboard is not None:
            result['Whiteboard'] = self.whiteboard.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.StartCloudRecordRequestPanesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.StartCloudRecordRequestPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneCropMode') is not None:
            self.pane_crop_mode = m.get('PaneCropMode')

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('ReservePaneForOfflineUser') is not None:
            self.reserve_pane_for_offline_user = m.get('ReservePaneForOfflineUser')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartCloudRecordRequestPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('VideoOrder') is not None:
            self.video_order = m.get('VideoOrder')

        if m.get('Whiteboard') is not None:
            temp_model = main_models.StartCloudRecordRequestPanesWhiteboard()
            self.whiteboard = temp_model.from_map(m.get('Whiteboard'))

        return self

class StartCloudRecordRequestPanesWhiteboard(DaraModel):
    def __init__(
        self,
        whiteboard_id: str = None,
    ):
        self.whiteboard_id = whiteboard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')

        return self

class StartCloudRecordRequestPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordRequestPanesTextsBoxColor = None,
        display: str = None,
        font: int = None,
        font_color: main_models.StartCloudRecordRequestPanesTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.display = display
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.texture = texture
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.display is not None:
            result['Display'] = self.display

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.texture is not None:
            result['Texture'] = self.texture

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordRequestPanesTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordRequestPanesTextsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Texture') is not None:
            self.texture = m.get('Texture')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordRequestPanesTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestPanesTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestPanesImages(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: str = None,
        height: float = None,
        layer: int = None,
        pane_image_crop_mode: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.display = display
        # This parameter is required.
        self.height = height
        self.layer = layer
        self.pane_image_crop_mode = pane_image_crop_mode
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.pane_image_crop_mode is not None:
            result['PaneImageCropMode'] = self.pane_image_crop_mode

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('PaneImageCropMode') is not None:
            self.pane_image_crop_mode = m.get('PaneImageCropMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordRequestPanesBackgrounds(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: str = None,
        height: float = None,
        layer: int = None,
        pane_background_crop_mode: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.display = display
        # This parameter is required.
        self.height = height
        self.layer = layer
        self.pane_background_crop_mode = pane_background_crop_mode
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.pane_background_crop_mode is not None:
            result['PaneBackgroundCropMode'] = self.pane_background_crop_mode

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('PaneBackgroundCropMode') is not None:
            self.pane_background_crop_mode = m.get('PaneBackgroundCropMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordRequestLayoutSpecifiedUsers(DaraModel):
    def __init__(
        self,
        ids: List[str] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.ids = ids
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class StartCloudRecordRequestImages(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        height: float = None,
        image_crop_mode: int = None,
        layer: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        # This parameter is required.
        self.height = height
        self.image_crop_mode = image_crop_mode
        self.layer = layer
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.height is not None:
            result['Height'] = self.height

        if self.image_crop_mode is not None:
            result['ImageCropMode'] = self.image_crop_mode

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageCropMode') is not None:
            self.image_crop_mode = m.get('ImageCropMode')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordRequestClockWidgetsBoxColor = None,
        font: int = None,
        font_color: main_models.StartCloudRecordRequestClockWidgetsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        x: float = None,
        y: float = None,
        zone: int = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y
        self.zone = zone

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordRequestClockWidgetsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordRequestClockWidgetsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class StartCloudRecordRequestClockWidgetsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestClockWidgetsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestBgColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        self.b = b
        self.g = g
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordRequestBackgrounds(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        background_crop_mode: int = None,
        height: float = None,
        layer: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.background_crop_mode = background_crop_mode
        # This parameter is required.
        self.height = height
        self.layer = layer
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.background_crop_mode is not None:
            result['BackgroundCropMode'] = self.background_crop_mode

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BackgroundCropMode') is not None:
            self.background_crop_mode = m.get('BackgroundCropMode')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

