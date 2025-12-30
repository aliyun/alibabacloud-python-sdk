# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListUserClusterTypesResponseBody(DaraModel):
    def __init__(
        self,
        cluster_types: List[main_models.ListUserClusterTypesResponseBodyClusterTypes] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of cluster types. Number of elements in the array: 1 to 100.
        self.cluster_types = cluster_types
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.cluster_types:
            for v1 in self.cluster_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterTypes'] = []
        if self.cluster_types is not None:
            for k1 in self.cluster_types:
                result['ClusterTypes'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_types = []
        if m.get('ClusterTypes') is not None:
            for k1 in m.get('ClusterTypes'):
                temp_model = main_models.ListUserClusterTypesResponseBodyClusterTypes()
                self.cluster_types.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUserClusterTypesResponseBodyClusterTypes(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        type_name: str = None,
    ):
        # The access type of cluster type
        self.access_type = access_type
        # The name of cluster type
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

