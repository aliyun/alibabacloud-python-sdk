# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class FunctionDefinition(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        definition: str = None,
        file_resources: List[main_models.FunctionFileResource] = None,
        function_name: str = None,
        language: str = None,
        type: str = None,
    ):
        # required in FileFunctionDefinition
        self.class_name = class_name
        # required in SQLFunctionDefinition/LambdaFunctionDefinition
        self.definition = definition
        # required in FileFunctionDefinition
        self.file_resources = file_resources
        # required in FileFunctionDefinition
        self.function_name = function_name
        # required in LambdaFunctionDefinition/FileFunctionDefinition
        self.language = language
        self.type = type

    def validate(self):
        if self.file_resources:
            for v1 in self.file_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['className'] = self.class_name

        if self.definition is not None:
            result['definition'] = self.definition

        result['fileResources'] = []
        if self.file_resources is not None:
            for k1 in self.file_resources:
                result['fileResources'].append(k1.to_map() if k1 else None)

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.language is not None:
            result['language'] = self.language

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('definition') is not None:
            self.definition = m.get('definition')

        self.file_resources = []
        if m.get('fileResources') is not None:
            for k1 in m.get('fileResources'):
                temp_model = main_models.FunctionFileResource()
                self.file_resources.append(temp_model.from_map(k1))

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

