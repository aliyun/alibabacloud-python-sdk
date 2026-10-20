# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateSliderCaptchaPageRequest(DaraModel):
    def __init__(
        self,
        configs: main_models.CreateSliderCaptchaPageRequestConfigs = None,
        custom_content: str = None,
        force_language: str = None,
        name: str = None,
        site_ids: List[int] = None,
    ):
        # The predefined configurations for the custom slider page.
        self.configs = configs
        # The custom slider configurations. The value is a JSON string.
        self.custom_content = custom_content
        # The forced language.
        self.force_language = force_language
        # The name of the custom slider page.
        # 
        # This parameter is required.
        self.name = name
        # The list of bound site IDs.
        self.site_ids = site_ids

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.force_language is not None:
            result['ForceLanguage'] = self.force_language

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = main_models.CreateSliderCaptchaPageRequestConfigs()
            self.configs = temp_model.from_map(m.get('Configs'))

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('ForceLanguage') is not None:
            self.force_language = m.get('ForceLanguage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        return self

class CreateSliderCaptchaPageRequestConfigs(DaraModel):
    def __init__(
        self,
        en: main_models.CreateSliderCaptchaPageRequestConfigsEn = None,
        zh: main_models.CreateSliderCaptchaPageRequestConfigsZh = None,
    ):
        # The predefined English style.
        self.en = en
        # The predefined Chinese style.
        self.zh = zh

    def validate(self):
        if self.en:
            self.en.validate()
        if self.zh:
            self.zh.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en is not None:
            result['En'] = self.en.to_map()

        if self.zh is not None:
            result['Zh'] = self.zh.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('En') is not None:
            temp_model = main_models.CreateSliderCaptchaPageRequestConfigsEn()
            self.en = temp_model.from_map(m.get('En'))

        if m.get('Zh') is not None:
            temp_model = main_models.CreateSliderCaptchaPageRequestConfigsZh()
            self.zh = temp_model.from_map(m.get('Zh'))

        return self

class CreateSliderCaptchaPageRequestConfigsZh(DaraModel):
    def __init__(
        self,
        show_footer: bool = None,
        show_request_id: bool = None,
        slider_color: str = None,
        title: str = None,
    ):
        # Specifies whether to show the footer.
        # 
        # This parameter is required.
        self.show_footer = show_footer
        # Specifies whether to show the request ID.
        # 
        # This parameter is required.
        self.show_request_id = show_request_id
        # The color of the slider.
        # 
        # This parameter is required.
        self.slider_color = slider_color
        # The title.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_footer is not None:
            result['ShowFooter'] = self.show_footer

        if self.show_request_id is not None:
            result['ShowRequestId'] = self.show_request_id

        if self.slider_color is not None:
            result['SliderColor'] = self.slider_color

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowFooter') is not None:
            self.show_footer = m.get('ShowFooter')

        if m.get('ShowRequestId') is not None:
            self.show_request_id = m.get('ShowRequestId')

        if m.get('SliderColor') is not None:
            self.slider_color = m.get('SliderColor')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CreateSliderCaptchaPageRequestConfigsEn(DaraModel):
    def __init__(
        self,
        show_footer: bool = None,
        show_request_id: bool = None,
        slider_color: str = None,
        title: str = None,
    ):
        # Specifies whether to show the footer.
        # 
        # This parameter is required.
        self.show_footer = show_footer
        # Specifies whether to show the request ID.
        self.show_request_id = show_request_id
        # The color of the slider.
        # 
        # This parameter is required.
        self.slider_color = slider_color
        # The title.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_footer is not None:
            result['ShowFooter'] = self.show_footer

        if self.show_request_id is not None:
            result['ShowRequestId'] = self.show_request_id

        if self.slider_color is not None:
            result['SliderColor'] = self.slider_color

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowFooter') is not None:
            self.show_footer = m.get('ShowFooter')

        if m.get('ShowRequestId') is not None:
            self.show_request_id = m.get('ShowRequestId')

        if m.get('SliderColor') is not None:
            self.slider_color = m.get('SliderColor')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

