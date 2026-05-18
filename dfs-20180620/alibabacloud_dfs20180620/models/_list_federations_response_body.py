# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListFederationsResponseBody(DaraModel):
    def __init__(
        self,
        federations: List[main_models.ListFederationsResponseBodyFederations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.federations = federations
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.federations:
            for v1 in self.federations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Federations'] = []
        if self.federations is not None:
            for k1 in self.federations:
                result['Federations'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.federations = []
        if m.get('Federations') is not None:
            for k1 in m.get('Federations'):
                temp_model = main_models.ListFederationsResponseBodyFederations()
                self.federations.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFederationsResponseBodyFederations(DaraModel):
    def __init__(
        self,
        federation_id: str = None,
        file_system_ids: str = None,
    ):
        self.federation_id = federation_id
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.federation_id is not None:
            result['FederationId'] = self.federation_id

        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FederationId') is not None:
            self.federation_id = m.get('FederationId')

        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')

        return self

