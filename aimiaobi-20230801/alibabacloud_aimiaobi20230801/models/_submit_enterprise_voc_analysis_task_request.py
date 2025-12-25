# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitEnterpriseVocAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        content_tags: List[main_models.SubmitEnterpriseVocAnalysisTaskRequestContentTags] = None,
        contents: List[main_models.SubmitEnterpriseVocAnalysisTaskRequestContents] = None,
        file_key: str = None,
        filter_tags: List[main_models.SubmitEnterpriseVocAnalysisTaskRequestFilterTags] = None,
        material_type: str = None,
        model_id: str = None,
        positive_sample: str = None,
        positive_sample_file_key: str = None,
        task_type: str = None,
        workspace_id: str = None,
    ):
        self.api_key = api_key
        # This parameter is required.
        self.content_tags = content_tags
        self.contents = contents
        self.file_key = file_key
        self.filter_tags = filter_tags
        self.material_type = material_type
        # This parameter is required.
        self.model_id = model_id
        self.positive_sample = positive_sample
        self.positive_sample_file_key = positive_sample_file_key
        self.task_type = task_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.content_tags:
            for v1 in self.content_tags:
                 if v1:
                    v1.validate()
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()
        if self.filter_tags:
            for v1 in self.filter_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        result['ContentTags'] = []
        if self.content_tags is not None:
            for k1 in self.content_tags:
                result['ContentTags'].append(k1.to_map() if k1 else None)

        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        result['FilterTags'] = []
        if self.filter_tags is not None:
            for k1 in self.filter_tags:
                result['FilterTags'].append(k1.to_map() if k1 else None)

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.positive_sample is not None:
            result['PositiveSample'] = self.positive_sample

        if self.positive_sample_file_key is not None:
            result['PositiveSampleFileKey'] = self.positive_sample_file_key

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        self.content_tags = []
        if m.get('ContentTags') is not None:
            for k1 in m.get('ContentTags'):
                temp_model = main_models.SubmitEnterpriseVocAnalysisTaskRequestContentTags()
                self.content_tags.append(temp_model.from_map(k1))

        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.SubmitEnterpriseVocAnalysisTaskRequestContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        self.filter_tags = []
        if m.get('FilterTags') is not None:
            for k1 in m.get('FilterTags'):
                temp_model = main_models.SubmitEnterpriseVocAnalysisTaskRequestFilterTags()
                self.filter_tags.append(temp_model.from_map(k1))

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('PositiveSample') is not None:
            self.positive_sample = m.get('PositiveSample')

        if m.get('PositiveSampleFileKey') is not None:
            self.positive_sample_file_key = m.get('PositiveSampleFileKey')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SubmitEnterpriseVocAnalysisTaskRequestFilterTags(DaraModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
        tag_type: str = None,
        tag_value_define_prompt: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name
        self.tag_type = tag_type
        self.tag_value_define_prompt = tag_value_define_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_define_prompt is not None:
            result['TagDefinePrompt'] = self.tag_define_prompt

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tag_type is not None:
            result['TagType'] = self.tag_type

        if self.tag_value_define_prompt is not None:
            result['TagValueDefinePrompt'] = self.tag_value_define_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('TagDefinePrompt')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')

        if m.get('TagValueDefinePrompt') is not None:
            self.tag_value_define_prompt = m.get('TagValueDefinePrompt')

        return self

class SubmitEnterpriseVocAnalysisTaskRequestContents(DaraModel):
    def __init__(
        self,
        extra_info: str = None,
        text: str = None,
    ):
        self.extra_info = extra_info
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class SubmitEnterpriseVocAnalysisTaskRequestContentTags(DaraModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
        tag_task_type: str = None,
        tag_value_define_prompt: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name
        self.tag_task_type = tag_task_type
        self.tag_value_define_prompt = tag_value_define_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_define_prompt is not None:
            result['TagDefinePrompt'] = self.tag_define_prompt

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tag_task_type is not None:
            result['TagTaskType'] = self.tag_task_type

        if self.tag_value_define_prompt is not None:
            result['TagValueDefinePrompt'] = self.tag_value_define_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('TagDefinePrompt')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TagTaskType') is not None:
            self.tag_task_type = m.get('TagTaskType')

        if m.get('TagValueDefinePrompt') is not None:
            self.tag_value_define_prompt = m.get('TagValueDefinePrompt')

        return self

