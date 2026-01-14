# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAllSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        group_id: int = None,
        namespace: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the lane group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the MSE namespace.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

