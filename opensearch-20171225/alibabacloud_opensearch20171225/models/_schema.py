# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class Schema(DaraModel):
    def __init__(
        self,
        index_sort_config: List[main_models.SchemaIndexSortConfig] = None,
        indexes: main_models.SchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, main_models.SchemaTablesValue] = None,
        ttl_field: main_models.SchemaTtlField = None,
    ):
        self.index_sort_config = index_sort_config
        self.indexes = indexes
        self.name = name
        self.route_field = route_field
        self.route_field_values = route_field_values
        self.second_route_field = second_route_field
        self.tables = tables
        self.ttl_field = ttl_field

    def validate(self):
        if self.index_sort_config:
            for v1 in self.index_sort_config:
                 if v1:
                    v1.validate()
        if self.indexes:
            self.indexes.validate()
        if self.tables:
            for v1 in self.tables.values():
                 if v1:
                    v1.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k1 in self.index_sort_config:
                result['indexSortConfig'].append(k1.to_map() if k1 else None)

        if self.indexes is not None:
            result['indexes'] = self.indexes.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.route_field is not None:
            result['routeField'] = self.route_field

        if self.route_field_values is not None:
            result['routeFieldValues'] = self.route_field_values

        if self.second_route_field is not None:
            result['secondRouteField'] = self.second_route_field

        result['tables'] = {}
        if self.tables is not None:
            for k1, v1 in self.tables.items():
                result['tables'][k1] = v1.to_map() if v1 else None

        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k1 in m.get('indexSortConfig'):
                temp_model = main_models.SchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k1))

        if m.get('indexes') is not None:
            temp_model = main_models.SchemaIndexes()
            self.indexes = temp_model.from_map(m.get('indexes'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')

        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')

        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')

        self.tables = {}
        if m.get('tables') is not None:
            for k1, v1 in m.get('tables').items():
                temp_model = main_models.SchemaTablesValue()
                self.tables[k1] = temp_model.from_map(v1)

        if m.get('ttlField') is not None:
            temp_model = main_models.SchemaTtlField()
            self.ttl_field = temp_model.from_map(m.get('ttlField'))

        return self

class SchemaTtlField(DaraModel):
    def __init__(
        self,
        name: str = None,
        ttl: int = None,
    ):
        self.name = name
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

class SchemaIndexes(DaraModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, main_models.SchemaIndexesSearchFieldsValue] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        if self.search_fields:
            for v1 in self.search_fields.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields

        result['searchFields'] = {}
        if self.search_fields is not None:
            for k1, v1 in self.search_fields.items():
                result['searchFields'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')

        self.search_fields = {}
        if m.get('searchFields') is not None:
            for k1, v1 in m.get('searchFields').items():
                temp_model = main_models.SchemaIndexesSearchFieldsValue()
                self.search_fields[k1] = temp_model.from_map(v1)

        return self

class SchemaIndexSortConfig(DaraModel):
    def __init__(
        self,
        direction: str = None,
        field: str = None,
    ):
        self.direction = direction
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['direction'] = self.direction

        if self.field is not None:
            result['field'] = self.field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('field') is not None:
            self.field = m.get('field')

        return self

