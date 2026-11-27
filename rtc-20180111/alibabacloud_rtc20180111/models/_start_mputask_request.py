# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartMPUTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        background_color: int = None,
        backgrounds: List[main_models.StartMPUTaskRequestBackgrounds] = None,
        channel_id: str = None,
        clock_widgets: List[main_models.StartMPUTaskRequestClockWidgets] = None,
        crop_mode: int = None,
        enhanced_param: main_models.StartMPUTaskRequestEnhancedParam = None,
        layout_ids: List[int] = None,
        media_encode: int = None,
        mix_mode: int = None,
        owner_id: int = None,
        payload_type: int = None,
        report_vad: int = None,
        rtp_ext_info: int = None,
        source_type: str = None,
        stream_type: int = None,
        stream_url: str = None,
        sub_spec_audio_users: List[str] = None,
        sub_spec_camera_users: List[str] = None,
        sub_spec_share_screen_users: List[str] = None,
        sub_spec_users: List[str] = None,
        task_id: str = None,
        task_type: int = None,
        time_stamp_ref: int = None,
        unsub_spec_audio_users: List[str] = None,
        unsub_spec_camera_users: List[str] = None,
        unsub_spec_share_screen_users: List[str] = None,
        user_panes: List[main_models.StartMPUTaskRequestUserPanes] = None,
        vad_interval: int = None,
        watermarks: List[main_models.StartMPUTaskRequestWatermarks] = None,
    ):
        # The application ID. Only a single ID is supported.
        # 
        # You can create and query it in the console.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The RGB value of the background color. Default value: **0** (black).
        # 
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): 0 to 255.
        self.background_color = background_color
        # The canvas background image panes.
        self.backgrounds = backgrounds
        # The channel ID. Only a single ID is supported.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The clock widgets.
        self.clock_widgets = clock_widgets
        # The video cropping mode. Valid values:
        # 
        # - **1**: crop while keeping the aspect ratio.
        # 
        # - **2**: keep the aspect ratio and add padding (default).
        self.crop_mode = crop_mode
        # The enhanced parameters.
        self.enhanced_param = enhanced_param
        # The layout IDs.
        self.layout_ids = layout_ids
        # The encoding options. For more information, see the MediaEncode enum values below.
        self.media_encode = media_encode
        # The mixed streaming mode. Valid values:
        # 
        # - **0**: single-stream relay. The original single stream is relayed without mixed-stream transcoding. You do not need to configure mixed-stream transcoding parameters.
        # - **1**: mixed-stream transcoding (default). Mixed-stream transcoding output is supported.
        # 
        # > - Valid parameters in single-stream relay mode: **StreamType**, **SourceType**, and **SubSpecUsers**.
        # - Valid parameters in mixed-stream transcoding mode: **MediaEncode**, **LayoutIds**, **BackgroundColor**, **SubSpecUsers**, **CropMode**, **UserPanes**, **Backgrounds**, and **Watermarks**.
        self.mix_mode = mix_mode
        self.owner_id = owner_id
        # The payload type. Valid values:
        # - **0**: do not use a payload.
        # - **1**: use VideoSEI.
        self.payload_type = payload_type
        # The voice activity detection (VAD) flag. Valid values:
        # - **0**: do not pass VAD information.
        # - **1**: pass VAD information.
        self.report_vad = report_vad
        # The RTP extension header information. Valid values:
        # - **0**: do not pass.
        # - **1**: pass.
        self.rtp_ext_info = rtp_ext_info
        # The user video input stream in single-stream relay mode. Valid values:
        # 
        # - **camera**: camera.
        # - **shareScreen**: screen sharing.
        self.source_type = source_type
        # The stream type to relay in single-stream relay mode. Valid values:
        # 
        # - **0**: relay the original stream.
        # - **1**: relay only the audio stream.
        # - **2**: relay only the video stream.
        # 
        # By default, the original stream is relayed.
        self.stream_type = stream_type
        # The live streaming ingest URL. Only a single URL is supported. For more information about the generation rules, see [Ingest and streaming URLs](https://help.aliyun.com/document_detail/199339.html).
        # 
        # >- For domain names with hotlink protection authentication enabled, the ingest URL must include an authentication string.
        # - The same StreamURL cannot be used simultaneously in different tasks.
        # - The same StreamURL cannot be used within 10 seconds after a task is stopped.
        self.stream_url = stream_url
        # Specifies the users whose audio streams are subscribed to in the channel.
        self.sub_spec_audio_users = sub_spec_audio_users
        # Specifies the users whose camera video streams are subscribed to in the channel.
        self.sub_spec_camera_users = sub_spec_camera_users
        # Specifies the users whose screen sharing video streams are subscribed to in the channel.
        self.sub_spec_share_screen_users = sub_spec_share_screen_users
        # Specifies the list of users to which the task subscribes.
        self.sub_spec_users = sub_spec_users
        # The task ID. Only a single ID is supported. The ID can contain letters, digits, underscores (_), and hyphens (-), and can be up to 55 bytes in length.
        # 
        # > This ID identifies the bypass live streaming task and must be unique.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The media processing type. Valid values:
        # 
        # - **0**: bypass live streaming task.
        # - **1**: MCU mixed-stream low-latency distribution task.
        self.task_type = task_type
        # The timestamp.
        self.time_stamp_ref = time_stamp_ref
        # Specifies the users whose audio streams are not subscribed to in the channel.
        self.unsub_spec_audio_users = unsub_spec_audio_users
        # Specifies the users whose camera video streams are not subscribed to in the channel.
        self.unsub_spec_camera_users = unsub_spec_camera_users
        # Specifies the users whose screen sharing video streams are not subscribed to in the channel.
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users
        # The layout parameters.
        self.user_panes = user_panes
        # The callback interval for voice activity detection.
        self.vad_interval = vad_interval
        # The watermark image panes.
        self.watermarks = watermarks

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.clock_widgets:
            for v1 in self.clock_widgets:
                 if v1:
                    v1.validate()
        if self.enhanced_param:
            self.enhanced_param.validate()
        if self.user_panes:
            for v1 in self.user_panes:
                 if v1:
                    v1.validate()
        if self.watermarks:
            for v1 in self.watermarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color

        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k1 in self.clock_widgets:
                result['ClockWidgets'].append(k1.to_map() if k1 else None)

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        if self.enhanced_param is not None:
            result['EnhancedParam'] = self.enhanced_param.to_map()

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type

        if self.report_vad is not None:
            result['ReportVad'] = self.report_vad

        if self.rtp_ext_info is not None:
            result['RtpExtInfo'] = self.rtp_ext_info

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users

        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users

        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users

        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.time_stamp_ref is not None:
            result['TimeStampRef'] = self.time_stamp_ref

        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users

        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users

        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users

        result['UserPanes'] = []
        if self.user_panes is not None:
            for k1 in self.user_panes:
                result['UserPanes'].append(k1.to_map() if k1 else None)

        if self.vad_interval is not None:
            result['VadInterval'] = self.vad_interval

        result['Watermarks'] = []
        if self.watermarks is not None:
            for k1 in self.watermarks:
                result['Watermarks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.StartMPUTaskRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.StartMPUTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        if m.get('EnhancedParam') is not None:
            temp_model = main_models.StartMPUTaskRequestEnhancedParam()
            self.enhanced_param = temp_model.from_map(m.get('EnhancedParam'))

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')

        if m.get('ReportVad') is not None:
            self.report_vad = m.get('ReportVad')

        if m.get('RtpExtInfo') is not None:
            self.rtp_ext_info = m.get('RtpExtInfo')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')

        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')

        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')

        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TimeStampRef') is not None:
            self.time_stamp_ref = m.get('TimeStampRef')

        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')

        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')

        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')

        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.StartMPUTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        if m.get('VadInterval') is not None:
            self.vad_interval = m.get('VadInterval')

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.StartMPUTaskRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class StartMPUTaskRequestWatermarks(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # The transparency. A value of 0.0 indicates fully transparent, and 1.0 indicates fully opaque.
        self.alpha = alpha
        # Specifies whether to display the image. Valid values:
        # 
        # - **0 (None)**: not displayed.
        # - **1 (Always)**: always displayed.
        self.display = display
        # The height of the pane, as a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the image.
        self.url = url
        # The width of the pane, as a normalized percentage.
        self.width = width
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 indicates the bottom layer, 1 indicates the layer above 0, and so on.
        self.zorder = zorder

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

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartMPUTaskRequestUserPanes(DaraModel):
    def __init__(
        self,
        images: List[main_models.StartMPUTaskRequestUserPanesImages] = None,
        pane_id: int = None,
        segment_type: int = None,
        source_type: str = None,
        texts: List[main_models.StartMPUTaskRequestUserPanesTexts] = None,
        user_id: str = None,
    ):
        # The image panes in the current layout.
        self.images = images
        # The pane ID. Valid values: **0** to **15**.
        # >If the user specified by PaneId is not found, the system displays other streams by default. The streams are determined based on the order in which users join the channel.
        self.pane_id = pane_id
        # The portrait segmentation type. Valid values:
        # 
        # - **0**: no portrait segmentation (default).
        # 
        # - **1**: portrait segmentation. This value takes effect only after the portrait segmentation feature is enabled.
        self.segment_type = segment_type
        # The user video input corresponding to the layout. Valid values:
        # 
        # - **camera**: video stream (default).
        # - **shareScreen**: screen sharing stream.
        self.source_type = source_type
        # The text panes in the current layout.
        self.texts = texts
        # The ID of the user corresponding to the layout pane. Valid values: **1** to **16**.
        self.user_id = user_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.StartMPUTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartMPUTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartMPUTaskRequestUserPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        border_color: int = None,
        border_width: int = None,
        box: bool = None,
        box_border_width: int = None,
        box_color: int = None,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        text: str = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # The transparency of the text box and text. A value of 0.0 indicates fully transparent, and 1.0 indicates fully opaque.
        self.alpha = alpha
        # The text stroke color in RGB format.
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.border_color = border_color
        # The text stroke width, in pixels. Default value: 0.
        self.border_width = border_width
        # Specifies whether to display the text box. Valid values:
        # 
        # - false (default): not displayed.
        # - true: displayed.
        self.box = box
        # The text box border width, in pixels. Default value: 0.
        self.box_border_width = box_border_width
        # The text box color in RGB format.
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.box_color = box_color
        # The text color in RGB format.
        # 
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.font_color = font_color
        # The font size. Valid values: **0** to **72**.
        self.font_size = font_size
        # The font type. Valid values:
        # 
        # - **0**: NOTO_SERIF_CJKSC_REGULAR (default).
        # - **1**: ALIBABA_PUHUITI_REGULAR.
        # - **2**: ALIBABA_PUHUITI_BOLD.
        # - **3**: ALIBABA_PUHUITI_Heavy.
        # - **4**: ALIBABA_PUHUITI_LIGHT.
        # - **5**: ALIBABA_PUHUITI_MEDIUM.
        self.font_type = font_type
        # The text content.
        self.text = text
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 indicates the bottom layer, 1 indicates the layer above 0, and so on.
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.box is not None:
            result['Box'] = self.box

        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width

        if self.box_color is not None:
            result['BoxColor'] = self.box_color

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.font_type is not None:
            result['FontType'] = self.font_type

        if self.text is not None:
            result['Text'] = self.text

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Box') is not None:
            self.box = m.get('Box')

        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')

        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartMPUTaskRequestUserPanesImages(DaraModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # Specifies whether to display the image. Valid values:
        # 
        # - **0 (None)**: not displayed.
        # - **1 (Always)**: always displayed.
        # - **2 (Backup)**: displayed when the current user has no video stream.
        self.display = display
        # The height of the pane, as a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the image.
        self.url = url
        # The width of the pane, as a normalized percentage.
        self.width = width
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 indicates the bottom layer, 1 indicates the layer above 0, and so on.
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartMPUTaskRequestEnhancedParam(DaraModel):
    def __init__(
        self,
        enable_portrait_segmentation: bool = None,
    ):
        # Specifies whether to enable the portrait segmentation feature (in closed beta). Valid values:
        # 
        # - **true**: enabled.
        # - **false** (default): disabled.
        self.enable_portrait_segmentation = enable_portrait_segmentation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_portrait_segmentation is not None:
            result['EnablePortraitSegmentation'] = self.enable_portrait_segmentation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePortraitSegmentation') is not None:
            self.enable_portrait_segmentation = m.get('EnablePortraitSegmentation')

        return self

class StartMPUTaskRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        border_color: int = None,
        border_width: int = None,
        box: bool = None,
        box_border_width: int = None,
        box_color: int = None,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # The transparency of the text box and text. A value of 0.0 indicates fully transparent, and 1.0 indicates fully opaque.
        self.alpha = alpha
        # The text stroke color in RGB format.
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.border_color = border_color
        # The text stroke width, in pixels. Default value: 0.
        self.border_width = border_width
        # Specifies whether to display the text box. Valid values:
        # 
        # - false (default): not displayed.
        # - true: displayed.
        self.box = box
        # The text box border width, in pixels. Default value: 0.
        self.box_border_width = box_border_width
        # The text box color in RGB format.
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.box_color = box_color
        # The text color in RGB format.
        # 
        # The formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.font_color = font_color
        # The font size. Valid values: **0** to **72**.
        self.font_size = font_size
        # The font type. Valid values:
        # 
        # - **0**: NOTO_SERIF_CJKSC_REGULAR (default).
        # - **1**: ALIBABA_PUHUITI_REGULAR.
        # - **2**: ALIBABA_PUHUITI_BOLD.
        # - **3**: ALIBABA_PUHUITI_Heavy.
        # - **4**: ALIBABA_PUHUITI_LIGHT.
        # - **5**: ALIBABA_PUHUITI_MEDIUM.
        self.font_type = font_type
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 indicates the bottom layer, 1 indicates the layer above 0, and so on.
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.box is not None:
            result['Box'] = self.box

        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width

        if self.box_color is not None:
            result['BoxColor'] = self.box_color

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.font_type is not None:
            result['FontType'] = self.font_type

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Box') is not None:
            self.box = m.get('Box')

        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')

        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartMPUTaskRequestBackgrounds(DaraModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # Specifies whether to display the image. Valid values:
        # 
        # - **0 (None)**: not displayed.
        # - **1 (Always)**: always displayed.
        self.display = display
        # The height of the pane, as a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the image.
        self.url = url
        # The width of the pane, as a normalized percentage.
        self.width = width
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 indicates the bottom layer, 1 indicates the layer above 0, and so on.
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

