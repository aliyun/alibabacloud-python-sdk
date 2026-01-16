# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class PathConfig(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        methods: List[str] = None,
        path: str = None,
        qualifier: str = None,
        rewrite_config: main_models.RewriteConfig = None,
    ):
        # This parameter is required.
        self.function_name = function_name
        self.methods = methods
        # This parameter is required.
        self.path = path
        self.qualifier = qualifier
        self.rewrite_config = rewrite_config

    def validate(self):
        if self.rewrite_config:
            self.rewrite_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.methods is not None:
            result['methods'] = self.methods

        if self.path is not None:
            result['path'] = self.path

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.rewrite_config is not None:
            result['rewriteConfig'] = self.rewrite_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('rewriteConfig') is not None:
            temp_model = main_models.RewriteConfig()
            self.rewrite_config = temp_model.from_map(m.get('rewriteConfig'))

        return self

