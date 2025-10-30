# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryCollectionDataResponseBody(DaraModel):
    def __init__(
        self,
        matches: main_models.QueryCollectionDataResponseBodyMatches = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        total: int = None,
    ):
        # Data list.
        self.matches = matches
        # Detailed information when the request fails.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Status, with the following values:
        # - **success**: Success.
        # - **fail**: Failure.
        self.status = status
        # Only returned when the Offset is not 0, this value represents the total number of hits for the search criteria.
        self.total = total

    def validate(self):
        if self.matches:
            self.matches.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.matches is not None:
            result['Matches'] = self.matches.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Matches') is not None:
            temp_model = main_models.QueryCollectionDataResponseBodyMatches()
            self.matches = temp_model.from_map(m.get('Matches'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryCollectionDataResponseBodyMatches(DaraModel):
    def __init__(
        self,
        match: List[main_models.QueryCollectionDataResponseBodyMatchesMatch] = None,
    ):
        self.match = match

    def validate(self):
        if self.match:
            for v1 in self.match:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['match'] = []
        if self.match is not None:
            for k1 in self.match:
                result['match'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match = []
        if m.get('match') is not None:
            for k1 in m.get('match'):
                temp_model = main_models.QueryCollectionDataResponseBodyMatchesMatch()
                self.match.append(temp_model.from_map(k1))

        return self

class QueryCollectionDataResponseBodyMatchesMatch(DaraModel):
    def __init__(
        self,
        id: str = None,
        metadata: Dict[str, str] = None,
        metadata_v2: Dict[str, Any] = None,
        score: float = None,
        sparse_values: main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValues = None,
        values: main_models.QueryCollectionDataResponseBodyMatchesMatchValues = None,
    ):
        # The unique ID of the vector data.
        self.id = id
        # Metadata.
        self.metadata = metadata
        self.metadata_v2 = metadata_v2
        # The similarity score of this data, which is related to the algorithm `(l2/ip/cosine)` specified when creating the index.
        self.score = score
        self.sparse_values = sparse_values
        # List of vector data.
        self.values = values

    def validate(self):
        if self.sparse_values:
            self.sparse_values.validate()
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.metadata_v2 is not None:
            result['MetadataV2'] = self.metadata_v2

        if self.score is not None:
            result['Score'] = self.score

        if self.sparse_values is not None:
            result['SparseValues'] = self.sparse_values.to_map()

        if self.values is not None:
            result['Values'] = self.values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('MetadataV2') is not None:
            self.metadata_v2 = m.get('MetadataV2')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SparseValues') is not None:
            temp_model = main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValues()
            self.sparse_values = temp_model.from_map(m.get('SparseValues'))

        if m.get('Values') is not None:
            temp_model = main_models.QueryCollectionDataResponseBodyMatchesMatchValues()
            self.values = temp_model.from_map(m.get('Values'))

        return self

class QueryCollectionDataResponseBodyMatchesMatchValues(DaraModel):
    def __init__(
        self,
        value: List[float] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class QueryCollectionDataResponseBodyMatchesMatchSparseValues(DaraModel):
    def __init__(
        self,
        indices: main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValuesIndices = None,
        values: main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValuesValues = None,
    ):
        self.indices = indices
        self.values = values

    def validate(self):
        if self.indices:
            self.indices.validate()
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.indices is not None:
            result['Indices'] = self.indices.to_map()

        if self.values is not None:
            result['Values'] = self.values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Indices') is not None:
            temp_model = main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValuesIndices()
            self.indices = temp_model.from_map(m.get('Indices'))

        if m.get('Values') is not None:
            temp_model = main_models.QueryCollectionDataResponseBodyMatchesMatchSparseValuesValues()
            self.values = temp_model.from_map(m.get('Values'))

        return self

class QueryCollectionDataResponseBodyMatchesMatchSparseValuesValues(DaraModel):
    def __init__(
        self,
        value: List[float] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryCollectionDataResponseBodyMatchesMatchSparseValuesIndices(DaraModel):
    def __init__(
        self,
        indice: List[int] = None,
    ):
        self.indice = indice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.indice is not None:
            result['Indice'] = self.indice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Indice') is not None:
            self.indice = m.get('Indice')

        return self

