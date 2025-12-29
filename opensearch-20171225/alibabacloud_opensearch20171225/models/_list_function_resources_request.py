# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFunctionResourcesRequest(DaraModel):
    def __init__(
        self,
        output: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
    ):
        # The output level.
        # 
        # Valid values:
        # 
        # *   simple
        # *   normal
        # *   detail
        self.output = output
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The type of the resource.
        # 
        # Valid values:
        # 
        # *   feature_generator
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   raw_file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['output'] = self.output

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

