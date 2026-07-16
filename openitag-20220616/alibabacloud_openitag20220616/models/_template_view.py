# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TemplateView(DaraModel):
    def __init__(
        self,
        fields: List[main_models.TemplateViewFields] = None,
    ):
        # View List
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.TemplateViewFields()
                self.fields.append(temp_model.from_map(k1))

        return self

class TemplateViewFields(DaraModel):
    def __init__(
        self,
        display_ori_img: bool = None,
        field_name: str = None,
        type: str = None,
        visit_info: main_models.TemplateViewFieldsVisitInfo = None,
    ):
        # Whether to Display Original Image
        self.display_ori_img = display_ori_img
        # Associated Column Name
        self.field_name = field_name
        # View Type
        self.type = type
        # Access Information
        self.visit_info = visit_info

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.type is not None:
            result['Type'] = self.type

        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VisitInfo') is not None:
            temp_model = main_models.TemplateViewFieldsVisitInfo()
            self.visit_info = temp_model.from_map(m.get('VisitInfo'))

        return self

class TemplateViewFieldsVisitInfo(DaraModel):
    def __init__(
        self,
        afts_conf: Dict[str, Any] = None,
        oss_conf: Dict[str, Any] = None,
    ):
        # Afts Configuration
        self.afts_conf = afts_conf
        # OSS Configuration
        self.oss_conf = oss_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.afts_conf is not None:
            result['AftsConf'] = self.afts_conf

        if self.oss_conf is not None:
            result['OssConf'] = self.oss_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AftsConf') is not None:
            self.afts_conf = m.get('AftsConf')

        if m.get('OssConf') is not None:
            self.oss_conf = m.get('OssConf')

        return self

