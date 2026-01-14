# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIsolationRulesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        namespace: str = None,
        page_index: int = None,
        page_size: int = None,
        resource: str = None,
        resource_search_key: str = None,
    ):
        self.accept_language = accept_language
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        self.resource = resource
        self.resource_search_key = resource_search_key

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

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_search_key is not None:
            result['ResourceSearchKey'] = self.resource_search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceSearchKey') is not None:
            self.resource_search_key = m.get('ResourceSearchKey')

        return self

