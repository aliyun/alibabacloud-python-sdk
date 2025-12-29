# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParametersByPathRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        # 
        # This parameter is required.
        self.path = path
        # Specifies whether to recursively query encryption parameters from all levels of directories in the specified path. Valid values: true and false. For example, if you want to query the /secretParameter/mySecretParameter and /secretParameter/secretParameter 1/mySecretParameter parameters, the valid values specify the parameters to be returned.
        # 
        # *   true: returns both of the /secretParameter/mySecretParameter and /secretParameter/secretParameter1/mySecretParameter parameters.
        # *   false: returns only the /secretParameter/mySecretParameter parameter.
        self.recursive = recursive
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.path is not None:
            result['Path'] = self.path

        if self.recursive is not None:
            result['Recursive'] = self.recursive

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

