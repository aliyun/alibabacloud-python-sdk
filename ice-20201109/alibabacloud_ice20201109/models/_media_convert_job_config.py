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
        self.inputs = inputs
        self.job_name = job_name
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
        self.group_config = group_config
        self.name = name
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
        self.features = features
        self.hls_group_config = hls_group_config
        self.name = name
        self.output_file_name = output_file_name
        self.override_params = override_params
        self.priority = priority
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
        self.audio_group = audio_group
        self.auto_select = auto_select
        self.forced = forced
        self.group = group
        self.is_default = is_default
        self.language = language
        self.name = name
        self.subtitle_group = subtitle_group
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
        self.manifest_extend = manifest_extend
        self.manifest_name = manifest_name
        self.output_file_base = output_file_base
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
        self.media = media
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
        self.excludes = excludes
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
        self.language = language
        self.name = name
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
        self.input_file = input_file
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
        self.media = media
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

