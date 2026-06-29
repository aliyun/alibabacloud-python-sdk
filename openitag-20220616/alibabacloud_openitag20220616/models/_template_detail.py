# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TemplateDetail(DaraModel):
    def __init__(
        self,
        abandon_reasons: List[str] = None,
        classify: str = None,
        creator: main_models.SimpleUser = None,
        description: str = None,
        exif: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier: main_models.SimpleUser = None,
        question_configs: List[main_models.QuestionPlugin] = None,
        shared_mode: str = None,
        status: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        type: str = None,
        view_configs: main_models.TemplateDetailViewConfigs = None,
    ):
        # Reasons for deprecation.
        self.abandon_reasons = abandon_reasons
        # Template categorization.
        self.classify = classify
        # Creator.
        self.creator = creator
        # Template description.
        self.description = description
        # Additional template information.
        self.exif = exif
        # Creation Time.
        self.gmt_create_time = gmt_create_time
        # Updated At.
        self.gmt_modified_time = gmt_modified_time
        # Modifier.
        self.modifier = modifier
        # Question widget configuration.
        self.question_configs = question_configs
        # Template shared mode.
        self.shared_mode = shared_mode
        # Template status.
        self.status = status
        # Label information.
        self.tags = tags
        # Template ID.
        self.template_id = template_id
        # Template Name.
        self.template_name = template_name
        # Tenant where the template resides.
        self.tenant_id = tenant_id
        # Template type.
        self.type = type
        # View layer configuration.
        self.view_configs = view_configs

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.question_configs:
            for v1 in self.question_configs:
                 if v1:
                    v1.validate()
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k1 in self.question_configs:
                result['QuestionConfigs'].append(k1.to_map() if k1 else None)

        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Creator') is not None:
            temp_model = main_models.SimpleUser()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Modifier') is not None:
            temp_model = main_models.SimpleUser()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k1 in m.get('QuestionConfigs'):
                temp_model = main_models.QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k1))

        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ViewConfigs') is not None:
            temp_model = main_models.TemplateDetailViewConfigs()
            self.view_configs = temp_model.from_map(m.get('ViewConfigs'))

        return self

class TemplateDetailViewConfigs(DaraModel):
    def __init__(
        self,
        view_plugins: List[main_models.ViewPlugin] = None,
    ):
        # View widgets.
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for v1 in self.view_plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k1 in self.view_plugins:
                result['ViewPlugins'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k1 in m.get('ViewPlugins'):
                temp_model = main_models.ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k1))

        return self

