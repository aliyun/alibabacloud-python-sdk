# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCloudGtmMonitorTemplateRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        template_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US (default): English.
        self.accept_language = accept_language
        # A client-generated token that is used to ensure the idempotence of the request. This token must be unique for each request and can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The unique ID of the health check template.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

