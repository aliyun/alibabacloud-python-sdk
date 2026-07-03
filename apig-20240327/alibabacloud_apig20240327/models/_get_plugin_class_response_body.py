# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetPluginClassResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPluginClassResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetPluginClassResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPluginClassResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        document: str = None,
        name: str = None,
        publish_status: str = None,
        type: str = None,
        wasm_language: str = None,
    ):
        self.alias = alias
        self.description = description
        self.document = document
        self.name = name
        self.publish_status = publish_status
        self.type = type
        self.wasm_language = wasm_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.document is not None:
            result['document'] = self.document

        if self.name is not None:
            result['name'] = self.name

        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status

        if self.type is not None:
            result['type'] = self.type

        if self.wasm_language is not None:
            result['wasmLanguage'] = self.wasm_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('wasmLanguage') is not None:
            self.wasm_language = m.get('wasmLanguage')

        return self

