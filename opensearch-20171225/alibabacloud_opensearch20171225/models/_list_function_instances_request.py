# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFunctionInstancesRequest(DaraModel):
    def __init__(
        self,
        function_type: str = None,
        model_type: str = None,
        output: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
    ):
        # The type of the feature.
        self.function_type = function_type
        # The type of the model.
        self.model_type = model_type
        # The richness of the returned information. Valid values:
        # 
        # *   normal: displays information such as createParameters and cron. This is the default value.
        # *   simple: displays only the basic information.
        # *   detail: returns the details of the training task.
        self.output = output
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # How the instance is created. Valid values:
        # 
        # *   builtin: The instance is created by system.
        # *   user: The instance is created by user. This is the default value.
        # *   all: all instances
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.output is not None:
            result['output'] = self.output

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('output') is not None:
            self.output = m.get('output')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

