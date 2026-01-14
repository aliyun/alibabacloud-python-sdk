# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteFlowRulesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        ids: List[int] = None,
        namespace: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The IDs of the rules to be deleted.
        self.ids = ids
        # The microservice namespace to which the application belongs.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

