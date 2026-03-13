# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, BinaryIO

from darabonba.model import DaraModel

class UploadModuleAdvanceRequest(DaraModel):
    def __init__(
        self,
        code: Dict[str, str] = None,
        module_id: str = None,
        module_name: str = None,
        namespace_name: str = None,
        url_object: BinaryIO = None,
    ):
        self.code = code
        self.module_id = module_id
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.url_object is not None:
            result['url'] = self.url_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('url') is not None:
            self.url_object = m.get('url')

        return self

