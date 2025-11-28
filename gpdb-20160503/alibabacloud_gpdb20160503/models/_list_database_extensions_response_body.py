# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListDatabaseExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        extensions: List[main_models.ListDatabaseExtensionsResponseBodyExtensions] = None,
        request_id: str = None,
    ):
        self.extensions = extensions
        self.request_id = request_id

    def validate(self):
        if self.extensions:
            for v1 in self.extensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Extensions'] = []
        if self.extensions is not None:
            for k1 in self.extensions:
                result['Extensions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extensions = []
        if m.get('Extensions') is not None:
            for k1 in m.get('Extensions'):
                temp_model = main_models.ListDatabaseExtensionsResponseBodyExtensions()
                self.extensions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDatabaseExtensionsResponseBodyExtensions(DaraModel):
    def __init__(
        self,
        description: str = None,
        extension_name: str = None,
        status: str = None,
    ):
        self.description = description
        self.extension_name = extension_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

