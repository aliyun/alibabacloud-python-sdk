# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateZnodeRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        data: str = None,
        path: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the instance.
        self.cluster_id = cluster_id
        # The data of the node.
        self.data = data
        # The path of the node.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data is not None:
            result['Data'] = self.data

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

