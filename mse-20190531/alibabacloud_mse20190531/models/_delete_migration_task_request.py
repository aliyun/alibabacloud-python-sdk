# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMigrationTaskRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the task.
        self.id = id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.id is not None:
            result['Id'] = self.id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

