# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateAccessApplicationRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateAccessApplicationRequestBody = None,
    ):
        # The request body for updating the access application.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateAccessApplicationRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateAccessApplicationRequestBody(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        redirect_uris: List[str] = None,
    ):
        # The name of the access application.
        self.application_name = application_name
        # The list of redirect URIs.
        self.redirect_uris = redirect_uris

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.redirect_uris is not None:
            result['redirectUris'] = self.redirect_uris

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('redirectUris') is not None:
            self.redirect_uris = m.get('redirectUris')

        return self

