# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmarttagTemplateRequest(DaraModel):
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
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene: str = None,
        template_config: str = None,
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
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene = scene
        self.template_config = template_config
        # This parameter is required.
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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

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

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

