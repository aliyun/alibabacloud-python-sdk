# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateSortScriptResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateSortScriptResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.CreateSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateSortScriptResponseBodyResult(DaraModel):
    def __init__(
        self,
        scope: str = None,
        script_name: str = None,
        type: str = None,
    ):
        # The sort phase to which the script applies.
        self.scope = scope
        # The script name.
        self.script_name = script_name
        # The script type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope is not None:
            result['scope'] = self.scope

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

