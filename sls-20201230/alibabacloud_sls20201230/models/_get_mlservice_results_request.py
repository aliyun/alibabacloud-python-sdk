# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetMLServiceResultsRequest(DaraModel):
    def __init__(
        self,
        allow_builtin: bool = None,
        body: main_models.MLServiceAnalysisParam = None,
        version: str = None,
    ):
        self.allow_builtin = allow_builtin
        self.body = body
        # The version of the algorithm. The algorithm varies based on the version.
        self.version = version

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_builtin is not None:
            result['allowBuiltin'] = self.allow_builtin

        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowBuiltin') is not None:
            self.allow_builtin = m.get('allowBuiltin')

        if m.get('body') is not None:
            temp_model = main_models.MLServiceAnalysisParam()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

