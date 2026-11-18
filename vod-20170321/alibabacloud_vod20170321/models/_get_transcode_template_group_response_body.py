# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetTranscodeTemplateGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_template_group: main_models.GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data of the transcoding template group.
        self.transcode_template_group = transcode_template_group

    def validate(self):
        if self.transcode_template_group:
            self.transcode_template_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transcode_template_group is not None:
            result['TranscodeTemplateGroup'] = self.transcode_template_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TranscodeTemplateGroup') is not None:
            temp_model = main_models.GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup()
            self.transcode_template_group = temp_model.from_map(m.get('TranscodeTemplateGroup'))

        return self

class GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        is_default: str = None,
        locked: str = None,
        modify_time: str = None,
        name: str = None,
        transcode_template_group_id: str = None,
        transcode_template_list: List[main_models.GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList] = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the template group was created. The time follows the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Specifies whether the template group is the default template group. Valid values:
        # 
        # - **Default**: The default template group.
        # - **NotDefault**: A non-default template group.
        self.is_default = is_default
        # Specifies whether the template group is locked. Valid values:
        # - **Disabled**: Not locked.
        # - **Enabled**: Locked.
        self.locked = locked
        # The time when the template group was modified. The time follows the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The name of the template group.
        self.name = name
        # The ID of the transcoding template group.
        self.transcode_template_group_id = transcode_template_group_id
        # The list of transcoding template configuration information.
        self.transcode_template_list = transcode_template_list

    def validate(self):
        if self.transcode_template_list:
            for v1 in self.transcode_template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        result['TranscodeTemplateList'] = []
        if self.transcode_template_list is not None:
            for k1 in self.transcode_template_list:
                result['TranscodeTemplateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        self.transcode_template_list = []
        if m.get('TranscodeTemplateList') is not None:
            for k1 in m.get('TranscodeTemplateList'):
                temp_model = main_models.GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList()
                self.transcode_template_list.append(temp_model.from_map(k1))

        return self

class GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList(DaraModel):
    def __init__(
        self,
        audio: str = None,
        clip: str = None,
        container: str = None,
        copyright_mark: str = None,
        definition: str = None,
        encrypt_setting: str = None,
        mux_config: str = None,
        package_setting: str = None,
        rotate: str = None,
        subtitle_list: str = None,
        template_name: str = None,
        trace_mark: str = None,
        trans_config: str = None,
        transcode_file_regular: str = None,
        transcode_template_id: str = None,
        type: str = None,
        video: str = None,
        watermark_ids: List[str] = None,
    ):
        # The transcoding configuration parameters for the audio stream. The value is a JSON string.
        self.audio = audio
        # The video clipping configuration. The value is a JSON string. For example, if you need to extract 5 seconds of content from a video to generate a new video, you can set this parameter.
        self.clip = clip
        # The container format that encapsulates the audio and video streams. The value is a JSON string.
        self.container = container
        # The copyright watermark information.
        self.copyright_mark = copyright_mark
        # The definition tags for standard transcoding templates:
        # 
        # - **LD** (Smooth)
        # - **SD** (Standard definition)
        # - **HD** (High definition)
        # - **FHD** (Full high definition)
        # - **OD** (Original definition, which means container format conversion)
        # - **2K**
        # - **4K**
        # - **SQ** (Standard sound quality)
        # - **HQ** (High sound quality)
        # 
        # The definition tags for built-in Narrowband HD™ 1.0 transcoding templates:
        # 
        # - **LD-NBV1** (Smooth)
        # - **SD-NBV1** (Standard definition)
        # - **HD-NBV1** (High definition)
        # - **FHD-NBV1** (Full high definition)
        # - **2K-NBV1**
        # - **4K-NBV1**
        # 
        # > - You cannot modify the definition tags of transcoding templates.
        # > - The audio and video resolutions, bitrates, and other parameters of Narrowband HD™ 1.0 transcoding templates are built-in and cannot be modified.
        # > - Narrowband HD™ 1.0 transcoding templates support only the FLV, M3U8 (HLS), and MP4 formats.
        self.definition = definition
        # The encryption configuration information for transcoding.
        self.encrypt_setting = encrypt_setting
        # The segment settings for transcoding. This parameter is required for HLS. The value is a JSON string.
        self.mux_config = mux_config
        # The packaging configuration. Only HLS adaptive bitrate streaming packaging and DASH packaging are supported. The value is a JSON string.
        self.package_setting = package_setting
        # The video rotation parameter. This parameter controls the rotation angle of the video image. For example, if you set this parameter to 180, the video image is upside down. Valid values: `[0,360]`.
        self.rotate = rotate
        # The subtitle configuration. The value is a JSON string.
        self.subtitle_list = subtitle_list
        # The name of the transcoding template.
        self.template_name = template_name
        # The tracing watermark information.
        self.trace_mark = trace_mark
        # The conditional transcoding parameters. If you need to make basic logical judgments based on the bitrate and resolution of the source video before outputting the transcoded video, you can set this parameter. The value is a JSON string.
        self.trans_config = trans_config
        # The custom output path for transcoding.
        self.transcode_file_regular = transcode_file_regular
        # The ID of the transcoding template.
        self.transcode_template_id = transcode_template_id
        # The templatetype. Valid values:
        # 
        # - **Normal** (default): A standard transcoding template. You cannot configure the Settings for the PackageSetting parameter for this type of template.
        # - **VideoPackage**: A video stream packaging template. This type of template transcodes the video stream first and then builds an adaptive bitrate stream. You must configure the Settings for the PackageSetting parameter.
        # - **SubtitlePackage**: A subtitle packaging template. This type of template does not transcode the video stream. It only builds the corresponding subtitle information into the adaptive bitrate output file. You must configure the Settings for the PackageSetting parameter. This type of template cannot exist independently in a template group and must be configured together with a VideoPackage template. You can configure only one SubtitlePackage template in a template group.
        self.type = type
        # The transcoding configuration parameters for the video stream. The value is a JSON string.
        self.video = video
        # The IDs of the associated image and text watermark templates.
        self.watermark_ids = watermark_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio

        if self.clip is not None:
            result['Clip'] = self.clip

        if self.container is not None:
            result['Container'] = self.container

        if self.copyright_mark is not None:
            result['CopyrightMark'] = self.copyright_mark

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.encrypt_setting is not None:
            result['EncryptSetting'] = self.encrypt_setting

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config

        if self.package_setting is not None:
            result['PackageSetting'] = self.package_setting

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.subtitle_list is not None:
            result['SubtitleList'] = self.subtitle_list

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trace_mark is not None:
            result['TraceMark'] = self.trace_mark

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config

        if self.transcode_file_regular is not None:
            result['TranscodeFileRegular'] = self.transcode_file_regular

        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id

        if self.type is not None:
            result['Type'] = self.type

        if self.video is not None:
            result['Video'] = self.video

        if self.watermark_ids is not None:
            result['WatermarkIds'] = self.watermark_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('Clip') is not None:
            self.clip = m.get('Clip')

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('CopyrightMark') is not None:
            self.copyright_mark = m.get('CopyrightMark')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('EncryptSetting') is not None:
            self.encrypt_setting = m.get('EncryptSetting')

        if m.get('MuxConfig') is not None:
            self.mux_config = m.get('MuxConfig')

        if m.get('PackageSetting') is not None:
            self.package_setting = m.get('PackageSetting')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('SubtitleList') is not None:
            self.subtitle_list = m.get('SubtitleList')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TraceMark') is not None:
            self.trace_mark = m.get('TraceMark')

        if m.get('TransConfig') is not None:
            self.trans_config = m.get('TransConfig')

        if m.get('TranscodeFileRegular') is not None:
            self.transcode_file_regular = m.get('TranscodeFileRegular')

        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Video') is not None:
            self.video = m.get('Video')

        if m.get('WatermarkIds') is not None:
            self.watermark_ids = m.get('WatermarkIds')

        return self

