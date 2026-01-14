# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetTextTemplateResponseBody(DaraModel):
    def __init__(
        self,
        available_industry: main_models.GetTextTemplateResponseBodyAvailableIndustry = None,
        request_id: str = None,
    ):
        self.available_industry = available_industry
        self.request_id = request_id

    def validate(self):
        if self.available_industry:
            self.available_industry.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_industry is not None:
            result['availableIndustry'] = self.available_industry.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableIndustry') is not None:
            temp_model = main_models.GetTextTemplateResponseBodyAvailableIndustry()
            self.available_industry = temp_model.from_map(m.get('availableIndustry'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetTextTemplateResponseBodyAvailableIndustry(DaraModel):
    def __init__(
        self,
        name: str = None,
        text_mode_types: List[main_models.GetTextTemplateResponseBodyAvailableIndustryTextModeTypes] = None,
    ):
        self.name = name
        self.text_mode_types = text_mode_types

    def validate(self):
        if self.text_mode_types:
            for v1 in self.text_mode_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        result['textModeTypes'] = []
        if self.text_mode_types is not None:
            for k1 in self.text_mode_types:
                result['textModeTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        self.text_mode_types = []
        if m.get('textModeTypes') is not None:
            for k1 in m.get('textModeTypes'):
                temp_model = main_models.GetTextTemplateResponseBodyAvailableIndustryTextModeTypes()
                self.text_mode_types.append(temp_model.from_map(k1))

        return self

class GetTextTemplateResponseBodyAvailableIndustryTextModeTypes(DaraModel):
    def __init__(
        self,
        name: str = None,
        text_styles: List[main_models.GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles] = None,
    ):
        self.name = name
        self.text_styles = text_styles

    def validate(self):
        if self.text_styles:
            for v1 in self.text_styles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        result['textStyles'] = []
        if self.text_styles is not None:
            for k1 in self.text_styles:
                result['textStyles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        self.text_styles = []
        if m.get('textStyles') is not None:
            for k1 in m.get('textStyles'):
                temp_model = main_models.GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles()
                self.text_styles.append(temp_model.from_map(k1))

        return self

class GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles(DaraModel):
    def __init__(
        self,
        desc: str = None,
        disabled: bool = None,
        name: str = None,
        template_key: str = None,
    ):
        self.desc = desc
        self.disabled = disabled
        self.name = name
        self.template_key = template_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.disabled is not None:
            result['disabled'] = self.disabled

        if self.name is not None:
            result['name'] = self.name

        if self.template_key is not None:
            result['templateKey'] = self.template_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')

        return self

