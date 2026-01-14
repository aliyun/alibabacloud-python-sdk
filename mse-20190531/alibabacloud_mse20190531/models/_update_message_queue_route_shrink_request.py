# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMessageQueueRouteShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        filter_side: str = None,
        gray_base_tags_shrink: str = None,
        namespace: str = None,
        region: str = None,
        tags_shrink: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        self.app_name = app_name
        # Specifies whether the canary release for messaging feature is enabled for the application. Valid values:
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable = enable
        # The side for message filtering when the canary release for messaging feature is enabled.
        self.filter_side = filter_side
        self.gray_base_tags_shrink = gray_base_tags_shrink
        self.namespace = namespace
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The tag that is negligible for the untagged environment of the application.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.filter_side is not None:
            result['FilterSide'] = self.filter_side

        if self.gray_base_tags_shrink is not None:
            result['GrayBaseTags'] = self.gray_base_tags_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FilterSide') is not None:
            self.filter_side = m.get('FilterSide')

        if m.get('GrayBaseTags') is not None:
            self.gray_base_tags_shrink = m.get('GrayBaseTags')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

