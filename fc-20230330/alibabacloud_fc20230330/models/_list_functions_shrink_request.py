# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFunctionsShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        fc_version: str = None,
        function_name: str = None,
        gpu_type: str = None,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        resource_group_id: str = None,
        runtime: str = None,
        tags_shrink: str = None,
    ):
        # The description of the functions to retrieve.
        self.description = description
        # The version of Function Compute to which the functions belong.
        # 
        # *   v3: Only lists functions of Function Compute 3.0.
        # *   v2: Only lists functions of Function Compute 2.0.
        # 
        # By default, this parameter is left empty and functions in both Function Compute 3.0 and Function Compute 2.0 are listed.
        self.fc_version = fc_version
        self.function_name = function_name
        # The GPU type of the functions to retrieve.
        self.gpu_type = gpu_type
        # The number of functions to return. The minimum value is 1 and the maximum value is 100.
        self.limit = limit
        # The pagination token.
        self.next_token = next_token
        # The prefix of the function name.
        self.prefix = prefix
        self.resource_group_id = resource_group_id
        # The runtime of the functions to retrieve.
        self.runtime = runtime
        # The tag of the functions to retrieve.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.fc_version is not None:
            result['fcVersion'] = self.fc_version

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type

        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fcVersion') is not None:
            self.fc_version = m.get('fcVersion')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

