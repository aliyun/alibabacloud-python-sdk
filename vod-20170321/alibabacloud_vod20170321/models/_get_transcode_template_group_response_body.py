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
        # The request ID.
        self.request_id = request_id
        # The transcoding template group data.
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
        # The application ID.
        self.app_id = app_id
        # The time when the template group was created. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.creation_time = creation_time
        # Indicates whether the template group is the default one. Valid values:
        # 
        # - **Default**: The template group is the default one.
        # - **NotDefault**: The template group is not the default one.
        self.is_default = is_default
        # Indicates whether the template group is locked. Valid values:
        # - **Disabled**: Not locked.
        # - **Enabled**: Locked.
        self.locked = locked
        # The time when the template group was last modified. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.modify_time = modify_time
        # The name of the template group.
        self.name = name
        # The transcoding template group ID.
        self.transcode_template_group_id = transcode_template_group_id
        # The list of transcoding template configurations.
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
        # The audio stream transcoding configuration parameters (JSON string).
        self.audio = audio
        # The video clipping configuration (JSON string). For example, set this parameter if you want to extract 5 seconds of content from a video to generate a new video.
        self.clip = clip
        # The container format for encapsulating audio and video streams (JSON string).
        self.container = container
        # The copyright watermark information.
        self.copyright_mark = copyright_mark
        # The definition mark for normal transcoding templates:
        # 
        # - **LD** (low definition)
        # - **SD** (standard definition)
        # - **HD** (high definition)
        # - **FHD** (full high definition)
        # - **OD** (original definition, container format conversion)
        # - **2K**
        # - **4K**
        # - **SQ** (standard audio quality)
        # - **HQ** (high audio quality)
        # 
        # The definition mark for Narrowband HD 1.0 built-in transcoding templates:
        # 
        # - **LD-NBV1** (low definition)
        # - **SD-NBV1** (standard definition)
        # - **HD-NBV1** (high definition)
        # - **FHD-NBV1** (full high definition)
        # - **2K-NBV1**
        # - **4K-NBV1**
        # 
        # > - The definition mark of transcoding templates cannot be modified.
        # > - The audio and video resolution, bitrate, and other parameters of Narrowband HD 1.0 transcoding templates are built into the system and cannot be modified.
        # > - Narrowband HD 1.0 transcoding templates can only be created in FLV, M3U8 (HLS), or MP4 format.
        self.definition = definition
        # The transcoding encryption configuration.
        self.encrypt_setting = encrypt_setting
        # The segment setting parameters for transcoding. Required for HLS (JSON string).
        self.mux_config = mux_config
        # The packaging configuration. Only HLS adaptive bitrate streaming packaging and DASH packaging are supported (JSON string).
        self.package_setting = package_setting
        # The video rotation parameter. Controls the rotation angle of the video. For example, if set to 180, the video is flipped upside down. Value range: `[0,360]`.
        self.rotate = rotate
        # The subtitle configuration (JSON string).
        self.subtitle_list = subtitle_list
        # The transcoding template name.
        self.template_name = template_name
        # The tracing watermark information.
        self.trace_mark = trace_mark
        # The conditional transcoding parameters. Set this parameter if you want to perform basic logic checks based on the bitrate or resolution of the source file before outputting the transcoded video (JSON string).
        self.trans_config = trans_config
        # The custom transcoding output path.
        self.transcode_file_regular = transcode_file_regular
        # The transcoding template ID.
        self.transcode_template_id = transcode_template_id
        # The templatetype. Valid values:
        # 
        # - **Normal** (default): a normal transcoding template. The PackageSetting parameter cannot be configured in Settings for this type of template.
        # - **VideoPackage**: a video stream packaging template. This type of template first transcodes and then builds adaptive bitrate streaming. The PackageSetting parameter must be configured in Settings for this type of template.
        # - **SubtitlePackage**: a subtitle packaging template. This type of template does not transcode but only builds the corresponding subtitle information into the adaptive bitrate streaming output file. The PackageSetting parameter must be configured in Settings for this type of template. This type of template cannot exist alone in a template group and must be configured together with a VideoPackage type template. Only one SubtitlePackage template can be configured in a template group.
        self.type = type
        # The video stream transcoding configuration parameters (JSON string).
        self.video = video
        # The IDs of associated image and text watermark templates.
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

