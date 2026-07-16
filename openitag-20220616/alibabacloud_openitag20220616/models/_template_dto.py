# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TemplateDTO(DaraModel):
    def __init__(
        self,
        classify: str = None,
        description: str = None,
        exif: Dict[str, Any] = None,
        question_configs: List[main_models.QuestionPlugin] = None,
        robot_configs: List[Dict[str, Any]] = None,
        shared_mode: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        view_configs: main_models.TemplateDTOViewConfigs = None,
    ):
        # Template categorization
        self.classify = classify
        # Template description
        self.description = description
        # Template additional information
        self.exif = exif
        # List of question widget configurations
        # 
        # This parameter is required.
        self.question_configs = question_configs
        # List of assisted annotation configurations
        self.robot_configs = robot_configs
        # Template shared mode
        self.shared_mode = shared_mode
        # List of tag information
        self.tags = tags
        # Template ID
        self.template_id = template_id
        # Template Name
        # 
        # This parameter is required.
        self.template_name = template_name
        # View layer configuration
        # 
        # This parameter is required.
        self.view_configs = view_configs

    def validate(self):
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
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.description is not None:
            result['Description'] = self.description

        if self.exif is not None:
            result['Exif'] = self.exif

        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k1 in self.question_configs:
                result['QuestionConfigs'].append(k1.to_map() if k1 else None)

        if self.robot_configs is not None:
            result['RobotConfigs'] = self.robot_configs

        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k1 in m.get('QuestionConfigs'):
                temp_model = main_models.QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k1))

        if m.get('RobotConfigs') is not None:
            self.robot_configs = m.get('RobotConfigs')

        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('ViewConfigs') is not None:
            temp_model = main_models.TemplateDTOViewConfigs()
            self.view_configs = temp_model.from_map(m.get('ViewConfigs'))

        return self

class TemplateDTOViewConfigs(DaraModel):
    def __init__(
        self,
        view_plugins: List[main_models.ViewPlugin] = None,
    ):
        # List of view widgets
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

