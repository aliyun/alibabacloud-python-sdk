# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QuerySmarttagTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: main_models.QuerySmarttagTemplateListResponseBodyTemplates = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.templates is not None:
            result['Templates'] = self.templates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Templates') is not None:
            temp_model = main_models.QuerySmarttagTemplateListResponseBodyTemplates()
            self.templates = temp_model.from_map(m.get('Templates'))

        return self

class QuerySmarttagTemplateListResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        template: List[main_models.QuerySmarttagTemplateListResponseBodyTemplatesTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.QuerySmarttagTemplateListResponseBodyTemplatesTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class QuerySmarttagTemplateListResponseBodyTemplatesTemplate(DaraModel):
    def __init__(
        self,
        analyse_types: str = None,
        face_category_ids: str = None,
        face_custom_params_config: str = None,
        industry: str = None,
        is_default: bool = None,
        keyword_config: str = None,
        knowledge_config: str = None,
        label_type: str = None,
        label_version: str = None,
        landmark_group_ids: str = None,
        object_group_ids: str = None,
        scene: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.analyse_types = analyse_types
        self.face_category_ids = face_category_ids
        self.face_custom_params_config = face_custom_params_config
        self.industry = industry
        self.is_default = is_default
        self.keyword_config = keyword_config
        self.knowledge_config = knowledge_config
        self.label_type = label_type
        self.label_version = label_version
        self.landmark_group_ids = landmark_group_ids
        self.object_group_ids = object_group_ids
        self.scene = scene
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyse_types is not None:
            result['AnalyseTypes'] = self.analyse_types

        if self.face_category_ids is not None:
            result['FaceCategoryIds'] = self.face_category_ids

        if self.face_custom_params_config is not None:
            result['FaceCustomParamsConfig'] = self.face_custom_params_config

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.keyword_config is not None:
            result['KeywordConfig'] = self.keyword_config

        if self.knowledge_config is not None:
            result['KnowledgeConfig'] = self.knowledge_config

        if self.label_type is not None:
            result['LabelType'] = self.label_type

        if self.label_version is not None:
            result['LabelVersion'] = self.label_version

        if self.landmark_group_ids is not None:
            result['LandmarkGroupIds'] = self.landmark_group_ids

        if self.object_group_ids is not None:
            result['ObjectGroupIds'] = self.object_group_ids

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyseTypes') is not None:
            self.analyse_types = m.get('AnalyseTypes')

        if m.get('FaceCategoryIds') is not None:
            self.face_category_ids = m.get('FaceCategoryIds')

        if m.get('FaceCustomParamsConfig') is not None:
            self.face_custom_params_config = m.get('FaceCustomParamsConfig')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('KeywordConfig') is not None:
            self.keyword_config = m.get('KeywordConfig')

        if m.get('KnowledgeConfig') is not None:
            self.knowledge_config = m.get('KnowledgeConfig')

        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')

        if m.get('LabelVersion') is not None:
            self.label_version = m.get('LabelVersion')

        if m.get('LandmarkGroupIds') is not None:
            self.landmark_group_ids = m.get('LandmarkGroupIds')

        if m.get('ObjectGroupIds') is not None:
            self.object_group_ids = m.get('ObjectGroupIds')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

