# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartRecordTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        crop_mode: int = None,
        layout_ids: List[int] = None,
        media_encode: int = None,
        mix_mode: int = None,
        owner_id: int = None,
        source_type: str = None,
        stream_type: int = None,
        sub_spec_audio_users: List[str] = None,
        sub_spec_camera_users: List[str] = None,
        sub_spec_share_screen_users: List[str] = None,
        sub_spec_users: List[str] = None,
        task_id: str = None,
        task_profile: str = None,
        template_id: str = None,
        unsub_spec_audio_users: List[str] = None,
        unsub_spec_camera_users: List[str] = None,
        unsub_spec_share_screen_users: List[str] = None,
        user_panes: List[main_models.StartRecordTaskRequestUserPanes] = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. Only a single ID is supported.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The cropping mode of the video. Valid values:
        # 
        # - **1**: crops the video while maintaining the aspect ratio.
        # - **2** (default): adds padding to the video while maintaining the aspect ratio.
        self.crop_mode = crop_mode
        # The list of layout IDs.
        self.layout_ids = layout_ids
        # The encoding option. For more information, see the MediaEncode enum values below.
        self.media_encode = media_encode
        # The recording mode. Valid values:
        # 
        # - **0**: single-stream recording. Task parameters cannot be modified during the recording process. You cannot call the UpdateRecordTask operation to modify task parameters.
        # - **1** (default): mixed-stream recording. Multiple video streams are mixed and output.
        # 
        # > - Valid parameters in single-stream recording mode: StreamType and SourceType.
        # - Valid parameters in mixed-stream recording mode: TaskProfile, MediaEncode, LayoutIds, BackgroundColor, SubSpecUsers, CropMode, UserPanes, Backgrounds, Watermarks, and ClockWidgets.
        self.mix_mode = mix_mode
        self.owner_id = owner_id
        # The video source in single-stream recording mode. Valid values:
        # 
        # - **camera**: the camera.
        # - **shareScreen**: screen sharing.
        # 
        # > If the video source is shareScreen and only the camera stream is ingested, the camera stream is recorded. If both the camera stream and the screen sharing stream are ingested, the screen sharing stream is recorded.
        self.source_type = source_type
        # The single-stream recording mode. Valid values:
        # 
        # - **0** (default): records the original stream.
        # - **1**: records only the audio stream.
        self.stream_type = stream_type
        # Specifies the users whose audio streams are subscribed to in the channel.
        self.sub_spec_audio_users = sub_spec_audio_users
        # Specifies the users whose camera streams are subscribed to in the channel.
        self.sub_spec_camera_users = sub_spec_camera_users
        # Specifies the users whose screen sharing streams are subscribed to in the channel.
        self.sub_spec_share_screen_users = sub_spec_share_screen_users
        # Specifies the list of users to which the task subscribes.
        self.sub_spec_users = sub_spec_users
        # The task ID. Only a single ID is supported and the ID must be unique. The ID must be 1 to 55 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.task_id = task_id
        # The billing configuration of the task. You are charged based on your settings. For more information, see the TaskProfile enum values below.
        # 
        # > - The resolution of the MediaEncode encoding option must be less than or equal to the resolution of TaskProfile.
        # - The maximum number of panes in the layout must be less than or equal to the number of input streams specified by TaskProfile.
        self.task_profile = task_profile
        # The configuration template ID. For more information about how to obtain the template ID, see [AddRecordTemplate](https://help.aliyun.com/document_detail/193625.html).
        # 
        # This parameter is required.
        self.template_id = template_id
        # Specifies the users whose audio streams are not subscribed to in the channel.
        self.unsub_spec_audio_users = unsub_spec_audio_users
        # Specifies the users whose camera streams are not subscribed to in the channel.
        self.unsub_spec_camera_users = unsub_spec_camera_users
        # Specifies the users whose screen sharing streams are not subscribed to in the channel.
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users
        # The list of layout parameters.
        self.user_panes = user_panes

    def validate(self):
        if self.user_panes:
            for v1 in self.user_panes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

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

        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

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

        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')

        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')

        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')

        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.StartRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        return self

class StartRecordTaskRequestUserPanes(DaraModel):
    def __init__(
        self,
        images: List[main_models.StartRecordTaskRequestUserPanesImages] = None,
        pane_id: int = None,
        source_type: str = None,
        texts: List[main_models.StartRecordTaskRequestUserPanesTexts] = None,
        user_id: str = None,
    ):
        # The list of image panes in the current layout.
        self.images = images
        # The pane ID. Valid values: **0** to **15**.
        # 
        # > - If the user specified by PaneId is not found, other streams are displayed by default. The streams are determined based on the order in which users join the channel.
        # - If a parameter related to UserPanes is required, all other related parameters are also required. Otherwise, none of them are required.
        self.pane_id = pane_id
        # The user video input that corresponds to the layout. Valid values:
        # 
        # - **camera** (default): the video stream.
        # - **shareScreen**: the screen sharing stream.
        self.source_type = source_type
        # The list of text panes in the current layout.
        self.texts = texts
        # The ID of the user that corresponds to the layout pane. Valid values of N: **1 to 16**.
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
                temp_model = main_models.StartRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartRecordTaskRequestUserPanesTexts(DaraModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        text: str = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # The text color in RGB format. The calculation formula is R + G × 256 + B × 65536. Valid values of R (red), G (green), and B (blue): **0 to 255**.
        self.font_color = font_color
        # The font size. Valid values: **(0, 72]**.
        self.font_size = font_size
        # The font type. Valid values:
        # 
        # - **0** (default): NOTO_SERIF_CJKSC_REGULAR.
        # - **1**: ALIBABA_PUHUITI_REGULAR.
        # - **2**: ALIBABA_PUHUITI_BOLD.
        # - **3**: ALIBABA_PUHUITI_Heavy.
        # - **4**: ALIBABA_PUHUITI_LIGHT.
        # - **5**: ALIBABA_PUHUITI_MEDIUM.
        self.font_type = font_type
        # The text content.
        self.text = text
        # The X coordinate, represented as a normalized percentage.
        self.x = x
        # The Y coordinate, represented as a normalized percentage.
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

class StartRecordTaskRequestUserPanesImages(DaraModel):
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
        # The display mode of the image. Valid values:
        # 
        # - **0** (None): The image is not displayed.
        # - **1** (Always): The image is always displayed.
        # - **2** (Backup): The image is displayed when the current user has no video stream.
        self.display = display
        # The height of the pane, represented as a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the image.
        self.url = url
        # The width of the pane, represented as a normalized percentage.
        self.width = width
        # The X coordinate, represented as a normalized percentage.
        self.x = x
        # The Y coordinate, represented as a normalized percentage.
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

