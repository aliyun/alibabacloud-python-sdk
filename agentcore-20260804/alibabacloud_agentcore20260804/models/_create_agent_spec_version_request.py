# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateAgentSpecVersionRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateAgentSpecVersionRequestBody = None,
    ):
        # The request body.
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
            temp_model = main_models.CreateAgentSpecVersionRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class CreateAgentSpecVersionRequestBody(DaraModel):
    def __init__(
        self,
        based_on_version: str = None,
        target_version: str = None,
    ):
        # The existing version on which to base the draft.
        self.based_on_version = based_on_version
        # The version number for the draft. If not specified, the version number is automatically incremented.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.based_on_version is not None:
            result['basedOnVersion'] = self.based_on_version

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basedOnVersion') is not None:
            self.based_on_version = m.get('basedOnVersion')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

