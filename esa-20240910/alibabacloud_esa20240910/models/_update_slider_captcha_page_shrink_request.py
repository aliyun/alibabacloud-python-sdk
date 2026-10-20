# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSliderCaptchaPageShrinkRequest(DaraModel):
    def __init__(
        self,
        configs_shrink: str = None,
        custom_content: str = None,
        force_language: str = None,
        id: int = None,
        name: str = None,
        site_ids_shrink: str = None,
    ):
        # The predefined configurations of the custom slider page.
        self.configs_shrink = configs_shrink
        # The custom slider configuration.
        self.custom_content = custom_content
        # The forced language.
        self.force_language = force_language
        # The ID of the custom slider page.
        # 
        # This parameter is required.
        self.id = id
        # The name of the custom slider page.
        self.name = name
        # The list of bound site IDs.
        self.site_ids_shrink = site_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.force_language is not None:
            result['ForceLanguage'] = self.force_language

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids_shrink is not None:
            result['SiteIds'] = self.site_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('ForceLanguage') is not None:
            self.force_language = m.get('ForceLanguage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids_shrink = m.get('SiteIds')

        return self

