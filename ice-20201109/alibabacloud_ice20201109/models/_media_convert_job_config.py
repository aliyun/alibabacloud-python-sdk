# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertJobConfig(DaraModel):
    def __init__(
        self,
        inputs: List[main_models.MediaConvertJobConfigInputs] = None,
        job_name: str = None,
        output_groups: List[main_models.MediaConvertJobConfigOutputGroups] = None,
    ):
        # Inputs.
        self.inputs = inputs
        # The task name.
        # 
        # *   Maximum length: 64 bytes.
        self.job_name = job_name
        # An array of output group configurations.
        self.output_groups = output_groups

    def validate(self):
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()
        if self.output_groups:
            for v1 in self.output_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['Inputs'].append(k1.to_map() if k1 else None)

        if self.job_name is not None:
            result['JobName'] = self.job_name

        result['OutputGroups'] = []
        if self.output_groups is not None:
            for k1 in self.output_groups:
                result['OutputGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inputs = []
        if m.get('Inputs') is not None:
            for k1 in m.get('Inputs'):
                temp_model = main_models.MediaConvertJobConfigInputs()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.output_groups = []
        if m.get('OutputGroups') is not None:
            for k1 in m.get('OutputGroups'):
                temp_model = main_models.MediaConvertJobConfigOutputGroups()
                self.output_groups.append(temp_model.from_map(k1))

        return self

class MediaConvertJobConfigOutputGroups(DaraModel):
    def __init__(
        self,
        group_config: main_models.MediaConvertJobConfigOutputGroupsGroupConfig = None,
        name: str = None,
        outputs: List[main_models.MediaConvertJobConfigOutputGroupsOutputs] = None,
    ):
        # The configuration for this output group.
        self.group_config = group_config
        # The name of the output group.
        self.name = name
        # A list of individual output stream configurations. Each object in this array defines a specific rendition.
        self.outputs = outputs

    def validate(self):
        if self.group_config:
            self.group_config.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_config is not None:
            result['GroupConfig'] = self.group_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupConfig') is not None:
            temp_model = main_models.MediaConvertJobConfigOutputGroupsGroupConfig()
            self.group_config = temp_model.from_map(m.get('GroupConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.MediaConvertJobConfigOutputGroupsOutputs()
                self.outputs.append(temp_model.from_map(k1))

        return self

class MediaConvertJobConfigOutputGroupsOutputs(DaraModel):
    def __init__(
        self,
        features: str = None,
        hls_group_config: main_models.MediaConvertJobConfigOutputGroupsOutputsHlsGroupConfig = None,
        name: str = None,
        output_file_name: str = None,
        override_params: str = None,
        priority: int = None,
        template_id: str = None,
    ):
        # Additional feature parameters. See [MediaConvertJobFeature](https://help.aliyun.com/document_detail/2979993.html) for details.
        self.features = features
        # HLS-specific settings for this stream\\"s behavior in the manifest. Effective only when the group Type is Hls.
        self.hls_group_config = hls_group_config
        # A name to label this output. This is for identification purposes only and does not affect the filename.
        self.name = name
        # The filename for this output. It is used in conjunction with OutputFileBase from the GroupConfig.
        self.output_file_name = output_file_name
        # A JSON string of parameters to override the settings in the specified template.
        self.override_params = override_params
        # The priority of the task, from 1 to 10. A higher value indicates a higher priority. Default: 6.
        self.priority = priority
        # The ID of the transcoding template.
        self.template_id = template_id

    def validate(self):
        if self.hls_group_config:
            self.hls_group_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.features is not None:
            result['Features'] = self.features

        if self.hls_group_config is not None:
            result['HlsGroupConfig'] = self.hls_group_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.output_file_name is not None:
            result['OutputFileName'] = self.output_file_name

        if self.override_params is not None:
            result['OverrideParams'] = self.override_params

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('HlsGroupConfig') is not None:
            temp_model = main_models.MediaConvertJobConfigOutputGroupsOutputsHlsGroupConfig()
            self.hls_group_config = temp_model.from_map(m.get('HlsGroupConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputFileName') is not None:
            self.output_file_name = m.get('OutputFileName')

        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class MediaConvertJobConfigOutputGroupsOutputsHlsGroupConfig(DaraModel):
    def __init__(
        self,
        audio_group: str = None,
        auto_select: str = None,
        forced: str = None,
        group: str = None,
        is_default: str = None,
        language: str = None,
        name: str = None,
        subtitle_group: str = None,
        type: str = None,
    ):
        # The audio group this video stream references. Effective when Type is video.
        # 
        # Default value: audio.
        self.audio_group = audio_group
        # Whether this stream should be automatically selected by the player. Effective when Type is audio or subtitle.
        self.auto_select = auto_select
        # Whether this stream must be played. Effective when Type is audio or subtitle.
        self.forced = forced
        # The GROUP-ID attribute for this stream in the HLS manifest. Effective when Type is audio or subtitle.
        # 
        # Default value: Same as the Type value.
        self.group = group
        # Whether this is the default stream within its group. Effective when Type is audio or subtitle. Only one stream per group can be the default.
        self.is_default = is_default
        # The LANGUAGE attribute for this stream in the HLS manifest (must conform to RFC 5646). Effective when Type is audio or subtitle.
        self.language = language
        # The NAME attribute for this stream in the HLS manifest. **Required** when Type is audio or subtitle.
        self.name = name
        # The subtitle group this video or hybrid stream references. Effective when Type is video or hybrid.
        # 
        # Default value: subtitle.
        self.subtitle_group = subtitle_group
        # Specifies the stream type.
        # 
        # Valid values:
        # 
        # *   video: Video stream.
        # *   audio: Audio stream.
        # *   subtitle: Subtitle stream.
        # *   hybrid: A stream containing both audio and video.
        # 
        # Default value: hybrid.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_group is not None:
            result['AudioGroup'] = self.audio_group

        if self.auto_select is not None:
            result['AutoSelect'] = self.auto_select

        if self.forced is not None:
            result['Forced'] = self.forced

        if self.group is not None:
            result['Group'] = self.group

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.subtitle_group is not None:
            result['SubtitleGroup'] = self.subtitle_group

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioGroup') is not None:
            self.audio_group = m.get('AudioGroup')

        if m.get('AutoSelect') is not None:
            self.auto_select = m.get('AutoSelect')

        if m.get('Forced') is not None:
            self.forced = m.get('Forced')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubtitleGroup') is not None:
            self.subtitle_group = m.get('SubtitleGroup')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MediaConvertJobConfigOutputGroupsGroupConfig(DaraModel):
    def __init__(
        self,
        manifest_extend: main_models.MediaConvertJobConfigOutputGroupsGroupConfigManifestExtend = None,
        manifest_name: str = None,
        output_file_base: main_models.MediaConvertJobConfigOutputGroupsGroupConfigOutputFileBase = None,
        type: str = None,
    ):
        # Configures an extension to an existing manifest file. This allows you to reference an existing manifest and combine it with the results of the current output group to generate a new manifest.
        self.manifest_extend = manifest_extend
        # The name of the manifest file. This parameter is only applicable when Type is set to Hls or Dash.
        self.manifest_name = manifest_name
        # The base output directory. All files generated by this OutputGroup are placed in this directory.
        self.output_file_base = output_file_base
        # The type of the output group. Valid values:
        # 
        # *   File: An individual file.
        # *   Hls: HLS files for adaptive bitrate streaming.
        self.type = type

    def validate(self):
        if self.manifest_extend:
            self.manifest_extend.validate()
        if self.output_file_base:
            self.output_file_base.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.manifest_extend is not None:
            result['ManifestExtend'] = self.manifest_extend.to_map()

        if self.manifest_name is not None:
            result['ManifestName'] = self.manifest_name

        if self.output_file_base is not None:
            result['OutputFileBase'] = self.output_file_base.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManifestExtend') is not None:
            temp_model = main_models.MediaConvertJobConfigOutputGroupsGroupConfigManifestExtend()
            self.manifest_extend = temp_model.from_map(m.get('ManifestExtend'))

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('OutputFileBase') is not None:
            temp_model = main_models.MediaConvertJobConfigOutputGroupsGroupConfigOutputFileBase()
            self.output_file_base = temp_model.from_map(m.get('OutputFileBase'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MediaConvertJobConfigOutputGroupsGroupConfigOutputFileBase(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media asset location.
        # 
        # *   If Type is OSS, this is the destination URL (OSS or HTTP).
        # *   If Type is Media, this is the destination media asset ID.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MediaConvertJobConfigOutputGroupsGroupConfigManifestExtend(DaraModel):
    def __init__(
        self,
        excludes: List[main_models.MediaConvertJobConfigOutputGroupsGroupConfigManifestExtendExcludes] = None,
        input_ref: str = None,
    ):
        # Specifies streams to exclude from the referenced manifest. Multiple conditions within a single exclusion object are combined using AND logic. Multiple exclusion objects in the array are combined using OR logic.
        self.excludes = excludes
        # References the Name of an input that contains the manifest to be extended.
        self.input_ref = input_ref

    def validate(self):
        if self.excludes:
            for v1 in self.excludes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Excludes'] = []
        if self.excludes is not None:
            for k1 in self.excludes:
                result['Excludes'].append(k1.to_map() if k1 else None)

        if self.input_ref is not None:
            result['InputRef'] = self.input_ref

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.excludes = []
        if m.get('Excludes') is not None:
            for k1 in m.get('Excludes'):
                temp_model = main_models.MediaConvertJobConfigOutputGroupsGroupConfigManifestExtendExcludes()
                self.excludes.append(temp_model.from_map(k1))

        if m.get('InputRef') is not None:
            self.input_ref = m.get('InputRef')

        return self

class MediaConvertJobConfigOutputGroupsGroupConfigManifestExtendExcludes(DaraModel):
    def __init__(
        self,
        language: str = None,
        name: str = None,
        type: str = None,
    ):
        # Excludes streams based on their Language field. It must conform to RFC 5646.
        self.language = language
        # Excludes streams based on their Name field.
        self.name = name
        # Excludes streams based on their Type field.
        # 
        # Valid values:
        # 
        # *   Audio
        # *   Subtitle
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MediaConvertJobConfigInputs(DaraModel):
    def __init__(
        self,
        input_file: main_models.MediaConvertJobConfigInputsInputFile = None,
        name: str = None,
    ):
        # The input file.
        self.input_file = input_file
        # The name of the input file. InputRef can reference it in the output configuration.
        self.name = name

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            temp_model = main_models.MediaConvertJobConfigInputsInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class MediaConvertJobConfigInputsInputFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The URL or ID of the media file.
        # 
        # *   If Type is OSS, this is the file URL (OSS or HTTP). Do not use a signed URL, as it may cause authentication failure.
        # *   If Type is Media, this is the media asset ID. The source stream is used by default.
        self.media = media
        # The type of the media file. Valid values:
        # 
        # *   OSS: an OSS object.
        # *   Media: a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

