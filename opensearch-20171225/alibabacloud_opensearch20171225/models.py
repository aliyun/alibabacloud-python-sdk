# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ABTestExperiment(TeaModel):
    def __init__(
        self,
        name: str = None,
        online: bool = None,
        params: Dict[str, str] = None,
        serial_number: int = None,
        traffic: int = None,
    ):
        self.name = name
        self.online = online
        self.params = params
        self.serial_number = serial_number
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.traffic is not None:
            result['traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        return self


class ABTestGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: int = None,
    ):
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ABTestScene(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: int = None,
        values: List[str] = None,
    ):
        self.name = name
        self.status = status
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class AppCluster(TeaModel):
    def __init__(
        self,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
    ):
        self.max_query_clause_length = max_query_clause_length
        self.max_timeout_ms = max_timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class DataSourcePluginsValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        from_fields: str = None,
        parameters: Dict[str, str] = None,
    ):
        self.name = name
        self.from_fields = from_fields
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.from_fields is not None:
            result['fromFields'] = self.from_fields
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fromFields') is not None:
            self.from_fields = m.get('fromFields')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class DataSource(TeaModel):
    def __init__(
        self,
        fields: List[Dict[str, str]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, DataSourcePluginsValue] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        if self.plugins:
            for v in self.plugins.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        result['plugins'] = {}
        if self.plugins is not None:
            for k, v in self.plugins.items():
                result['plugins'][k] = v.to_map()
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        self.plugins = {}
        if m.get('plugins') is not None:
            for k, v in m.get('plugins').items():
                temp_model = DataSourcePluginsValue()
                self.plugins[k] = temp_model.from_map(v)
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Domain(TeaModel):
    def __init__(
        self,
        category: str = None,
        functions: Dict[str, List[str]] = None,
        name: str = None,
    ):
        self.category = category
        self.functions = functions
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            self.functions = m.get('functions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class FirstRank(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryProcessor(TeaModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class Quota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        order_type: str = None,
        spec: str = None,
    ):
        self.compute_resource = compute_resource
        self.doc_size = doc_size
        self.order_type = order_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class SchemaTablesValueFieldsValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        primary_key: bool = None,
        type: str = None,
        join_with: List[str] = None,
        label: str = None,
    ):
        self.name = name
        self.primary_key = primary_key
        self.type = type
        self.join_with = join_with
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.type is not None:
            result['type'] = self.type
        if self.join_with is not None:
            result['joinWith'] = self.join_with
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('joinWith') is not None:
            self.join_with = m.get('joinWith')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class SchemaTablesValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        primary_table: bool = None,
        fields: Dict[str, SchemaTablesValueFieldsValue] = None,
    ):
        self.name = name
        self.primary_table = primary_table
        self.fields = fields

    def validate(self):
        if self.fields:
            for v in self.fields.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.primary_table is not None:
            result['primaryTable'] = self.primary_table
        result['fields'] = {}
        if self.fields is not None:
            for k, v in self.fields.items():
                result['fields'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryTable') is not None:
            self.primary_table = m.get('primaryTable')
        self.fields = {}
        if m.get('fields') is not None:
            for k, v in m.get('fields').items():
                temp_model = SchemaTablesValueFieldsValue()
                self.fields[k] = temp_model.from_map(v)
        return self


class SchemaIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SchemaIndexesSearchFieldsValue(TeaModel):
    def __init__(
        self,
        analyzer: str = None,
        analyzer_type: str = None,
        analyzer_generation: str = None,
        fields: List[str] = None,
        label: str = None,
    ):
        self.analyzer = analyzer
        self.analyzer_type = analyzer_type
        self.analyzer_generation = analyzer_generation
        self.fields = fields
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.analyzer_generation is not None:
            result['analyzerGeneration'] = self.analyzer_generation
        if self.fields is not None:
            result['fields'] = self.fields
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('analyzerGeneration') is not None:
            self.analyzer_generation = m.get('analyzerGeneration')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class SchemaIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, SchemaIndexesSearchFieldsValue] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        if self.search_fields:
            for v in self.search_fields.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        result['searchFields'] = {}
        if self.search_fields is not None:
            for k, v in self.search_fields.items():
                result['searchFields'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        self.search_fields = {}
        if m.get('searchFields') is not None:
            for k, v in m.get('searchFields').items():
                temp_model = SchemaIndexesSearchFieldsValue()
                self.search_fields[k] = temp_model.from_map(v)
        return self


class SchemaTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class Schema(TeaModel):
    def __init__(
        self,
        index_sort_config: List[SchemaIndexSortConfig] = None,
        indexes: SchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, SchemaTablesValue] = None,
        ttl_field: SchemaTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.tables:
            for v in self.tables.values():
                if v:
                    v.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
            for k, v in self.tables.items():
                result['tables'][k] = v.to_map()
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = SchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = SchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
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
            for k, v in m.get('tables').items():
                temp_model = SchemaTablesValue()
                self.tables[k] = temp_model.from_map(v)
        if m.get('ttlField') is not None:
            temp_model = SchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class SecondRank(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SummaryMeta(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class Summary(TeaModel):
    def __init__(
        self,
        active: bool = None,
        meta: SummaryMeta = None,
        name: str = None,
    ):
        self.active = active
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('meta') is not None:
            temp_model = SummaryMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class App(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: AppCluster = None,
        data_sources: List[DataSource] = None,
        description: str = None,
        domain: Domain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[FirstRank] = None,
        network_type: str = None,
        query_processors: List[QueryProcessor] = None,
        quota: Quota = None,
        realtime_shared: bool = None,
        schema: Schema = None,
        schemas: List[Schema] = None,
        second_ranks: List[SecondRank] = None,
        summaries: List[Summary] = None,
        type: str = None,
    ):
        self.auto_switch = auto_switch
        self.cluster = cluster
        self.data_sources = data_sources
        self.description = description
        self.domain = domain
        self.fetch_fields = fetch_fields
        self.first_ranks = first_ranks
        self.network_type = network_type
        self.query_processors = query_processors
        self.quota = quota
        self.realtime_shared = realtime_shared
        self.schema = schema
        self.schemas = schemas
        self.second_ranks = second_ranks
        self.summaries = summaries
        self.type = type

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.quota:
            self.quota.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.network_type is not None:
            result['networkType'] = self.network_type
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.realtime_shared is not None:
            result['realtimeShared'] = self.realtime_shared
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = AppCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = DataSource()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = Domain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = FirstRank()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = QueryProcessor()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('quota') is not None:
            temp_model = Quota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('realtimeShared') is not None:
            self.realtime_shared = m.get('realtimeShared')
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = Schema()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = SecondRank()
                self.second_ranks.append(temp_model.from_map(k))
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = Summary()
                self.summaries.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AppGroupOrder(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class AppGroup(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        description: str = None,
        domain: str = None,
        name: str = None,
        order: AppGroupOrder = None,
        quota: Quota = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.description = description
        self.domain = domain
        self.name = name
        self.order = order
        self.quota = quota
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        if self.order:
            self.order.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.order is not None:
            result['order'] = self.order.to_map()
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order') is not None:
            temp_model = AppGroupOrder()
            self.order = temp_model.from_map(m['order'])
        if m.get('quota') is not None:
            temp_model = Quota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PrepayOrderInfo(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class ScheduledTaskFilter(TeaModel):
    def __init__(
        self,
        days: int = None,
        expression: str = None,
        field: str = None,
        unit: str = None,
    ):
        self.days = days
        self.expression = expression
        self.field = field
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['days'] = self.days
        if self.expression is not None:
            result['expression'] = self.expression
        if self.field is not None:
            result['field'] = self.field
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class ScheduledTask(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cron: str = None,
        enabled: bool = None,
        filter: ScheduledTaskFilter = None,
        forked_app_id: str = None,
        permanent: bool = None,
        run_now: bool = None,
        type: str = None,
        version: str = None,
    ):
        self.auto_switch = auto_switch
        self.cron = cron
        self.enabled = enabled
        self.filter = filter
        self.forked_app_id = forked_app_id
        self.permanent = permanent
        self.run_now = run_now
        self.type = type
        self.version = version

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cron is not None:
            result['cron'] = self.cron
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        if self.forked_app_id is not None:
            result['forkedAppId'] = self.forked_app_id
        if self.permanent is not None:
            result['permanent'] = self.permanent
        if self.run_now is not None:
            result['runNow'] = self.run_now
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('filter') is not None:
            temp_model = ScheduledTaskFilter()
            self.filter = temp_model.from_map(m['filter'])
        if m.get('forkedAppId') is not None:
            self.forked_app_id = m.get('forkedAppId')
        if m.get('permanent') is not None:
            self.permanent = m.get('permanent')
        if m.get('runNow') is not None:
            self.run_now = m.get('runNow')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class SearchStrategyMergeConfig(TeaModel):
    def __init__(
        self,
        doc_count: int = None,
        rank_name: str = None,
    ):
        self.doc_count = doc_count
        self.rank_name = rank_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_count is not None:
            result['docCount'] = self.doc_count
        if self.rank_name is not None:
            result['rankName'] = self.rank_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docCount') is not None:
            self.doc_count = m.get('docCount')
        if m.get('rankName') is not None:
            self.rank_name = m.get('rankName')
        return self


class SearchStrategySearchConfigs(TeaModel):
    def __init__(
        self,
        first_rank_name: str = None,
        merge_proportion: int = None,
        query_type: str = None,
        second_rank_name: str = None,
    ):
        self.first_rank_name = first_rank_name
        self.merge_proportion = merge_proportion
        self.query_type = query_type
        self.second_rank_name = second_rank_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_rank_name is not None:
            result['firstRankName'] = self.first_rank_name
        if self.merge_proportion is not None:
            result['mergeProportion'] = self.merge_proportion
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.second_rank_name is not None:
            result['secondRankName'] = self.second_rank_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstRankName') is not None:
            self.first_rank_name = m.get('firstRankName')
        if m.get('mergeProportion') is not None:
            self.merge_proportion = m.get('mergeProportion')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('secondRankName') is not None:
            self.second_rank_name = m.get('secondRankName')
        return self


class SearchStrategy(TeaModel):
    def __init__(
        self,
        description: str = None,
        is_default: bool = None,
        merge_config: SearchStrategyMergeConfig = None,
        name: str = None,
        search_configs: List[SearchStrategySearchConfigs] = None,
    ):
        self.description = description
        self.is_default = is_default
        self.merge_config = merge_config
        self.name = name
        self.search_configs = search_configs

    def validate(self):
        if self.merge_config:
            self.merge_config.validate()
        if self.search_configs:
            for k in self.search_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.merge_config is not None:
            result['mergeConfig'] = self.merge_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['searchConfigs'] = []
        if self.search_configs is not None:
            for k in self.search_configs:
                result['searchConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('mergeConfig') is not None:
            temp_model = SearchStrategyMergeConfig()
            self.merge_config = temp_model.from_map(m['mergeConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.search_configs = []
        if m.get('searchConfigs') is not None:
            for k in m.get('searchConfigs'):
                temp_model = SearchStrategySearchConfigs()
                self.search_configs.append(temp_model.from_map(k))
        return self


class BindESUserAnalyzerRequest(TeaModel):
    def __init__(
        self,
        body: Any = None,
    ):
        # The request parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class BindESUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The custom analyzer.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BindESUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindESUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEsInstanceRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The body of the request.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class BindEsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BindEsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindEsInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompileSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CompileSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompileSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CompileSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestExperimentRequest(TeaModel):
    def __init__(
        self,
        body: ABTestExperiment = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestExperiment()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the experiment was created.
        self.created = created
        # The experiment ID.
        self.id = id
        # The experiment alias.
        self.name = name
        # Indicates whether the experiment is in effect. Valid values:
        # 
        # *   true
        # *   false
        self.online = online
        # The experiment parameters.
        self.params = params
        # The percentage of traffic that is routed to the experiment.
        self.traffic = traffic
        # The time when the experiment was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateABTestExperimentResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The experiment details.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestGroupRequest(TeaModel):
    def __init__(
        self,
        body: ABTestGroup = None,
        dry_run: bool = None,
    ):
        # The request body. For more information, see [ABTestGroup](https://help.aliyun.com/document_detail/178935.html).
        self.body = body
        # Specifies whether to check the validity of input parameters. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**: checks only the validity of input parameters.
        # *   **false**: checks the validity of input parameters and creates an attribution configuration.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestGroup()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
    ):
        # The time when the test group was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The alias of the test group.
        self.name = name
        # The status of the test group.
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test group was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateABTestGroupResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestSceneRequest(TeaModel):
    def __init__(
        self,
        body: ABTestScene = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestScene()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
        values: List[str] = None,
    ):
        # The time when the test scenario was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The name of the test group.
        self.name = name
        # The status of the test scenario. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test scenario was last modified.
        self.updated = updated
        # The tag of the test scenario.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateABTestSceneResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestCluster(TeaModel):
    def __init__(
        self,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
    ):
        self.max_query_clause_length = max_query_clause_length
        self.max_timeout_ms = max_timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class CreateAppRequestDataSources(TeaModel):
    def __init__(
        self,
        fields: List[Dict[str, Any]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, Any] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.plugins is not None:
            result['plugins'] = self.plugins
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('plugins') is not None:
            self.plugins = m.get('plugins')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppRequestDomain(TeaModel):
    def __init__(
        self,
        category: str = None,
        functions: Dict[str, Any] = None,
        name: str = None,
    ):
        self.category = category
        self.functions = functions
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            self.functions = m.get('functions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppRequestFirstRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppRequestQueryProcessors(TeaModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class CreateAppRequestSchemaIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppRequestSchemaIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class CreateAppRequestSchemaTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppRequestSchema(TeaModel):
    def __init__(
        self,
        index_sort_config: List[CreateAppRequestSchemaIndexSortConfig] = None,
        indexes: CreateAppRequestSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: CreateAppRequestSchemaTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = CreateAppRequestSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = CreateAppRequestSchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = CreateAppRequestSchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class CreateAppRequestSchemasIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppRequestSchemasIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class CreateAppRequestSchemasTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppRequestSchemas(TeaModel):
    def __init__(
        self,
        index_sort_config: List[CreateAppRequestSchemasIndexSortConfig] = None,
        indexes: CreateAppRequestSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: CreateAppRequestSchemasTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = CreateAppRequestSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = CreateAppRequestSchemasIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = CreateAppRequestSchemasTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class CreateAppRequestSecondRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppRequestSummariesMeta(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class CreateAppRequestSummaries(TeaModel):
    def __init__(
        self,
        meta: List[CreateAppRequestSummariesMeta] = None,
        name: str = None,
    ):
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = CreateAppRequestSummariesMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: CreateAppRequestCluster = None,
        data_sources: List[CreateAppRequestDataSources] = None,
        description: str = None,
        domain: CreateAppRequestDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[CreateAppRequestFirstRanks] = None,
        network_type: str = None,
        query_processors: List[CreateAppRequestQueryProcessors] = None,
        schema: CreateAppRequestSchema = None,
        schemas: List[CreateAppRequestSchemas] = None,
        second_ranks: List[CreateAppRequestSecondRanks] = None,
        summaries: List[CreateAppRequestSummaries] = None,
        dry_run: bool = None,
    ):
        self.auto_switch = auto_switch
        self.cluster = cluster
        self.data_sources = data_sources
        self.description = description
        self.domain = domain
        self.fetch_fields = fetch_fields
        self.first_ranks = first_ranks
        self.network_type = network_type
        self.query_processors = query_processors
        self.schema = schema
        self.schemas = schemas
        self.second_ranks = second_ranks
        self.summaries = summaries
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.network_type is not None:
            result['networkType'] = self.network_type
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = CreateAppRequestCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = CreateAppRequestDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = CreateAppRequestDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = CreateAppRequestFirstRanks()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = CreateAppRequestQueryProcessors()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('schema') is not None:
            temp_model = CreateAppRequestSchema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = CreateAppRequestSchemas()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = CreateAppRequestSecondRanks()
                self.second_ranks.append(temp_model.from_map(k))
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = CreateAppRequestSummaries()
                self.summaries.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppResponseBodyResultCluster(TeaModel):
    def __init__(
        self,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
    ):
        self.max_query_clause_length = max_query_clause_length
        self.max_timeout_ms = max_timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class CreateAppResponseBodyResultDataSources(TeaModel):
    def __init__(
        self,
        fields: List[Dict[str, Any]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, Any] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.plugins is not None:
            result['plugins'] = self.plugins
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('plugins') is not None:
            self.plugins = m.get('plugins')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppResponseBodyResultDomainFunctions(TeaModel):
    def __init__(
        self,
        algo: List[str] = None,
        qp: List[str] = None,
        service: List[str] = None,
    ):
        self.algo = algo
        self.qp = qp
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo is not None:
            result['algo'] = self.algo
        if self.qp is not None:
            result['qp'] = self.qp
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algo') is not None:
            self.algo = m.get('algo')
        if m.get('qp') is not None:
            self.qp = m.get('qp')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class CreateAppResponseBodyResultDomain(TeaModel):
    def __init__(
        self,
        category: str = None,
        functions: CreateAppResponseBodyResultDomainFunctions = None,
        name: str = None,
    ):
        self.category = category
        self.functions = functions
        self.name = name

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            temp_model = CreateAppResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m['functions'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppResponseBodyResultFirstRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppResponseBodyResultQueryProcessors(TeaModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class CreateAppResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        qps: int = None,
        spec: str = None,
    ):
        self.compute_resource = compute_resource
        self.doc_size = doc_size
        self.qps = qps
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.qps is not None:
            result['qps'] = self.qps
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class CreateAppResponseBodyResultSchemaIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppResponseBodyResultSchemaIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class CreateAppResponseBodyResultSchemaTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppResponseBodyResultSchema(TeaModel):
    def __init__(
        self,
        index_sort_config: List[CreateAppResponseBodyResultSchemaIndexSortConfig] = None,
        indexes: CreateAppResponseBodyResultSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: CreateAppResponseBodyResultSchemaTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = CreateAppResponseBodyResultSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = CreateAppResponseBodyResultSchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = CreateAppResponseBodyResultSchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class CreateAppResponseBodyResultSchemasIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppResponseBodyResultSchemasIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class CreateAppResponseBodyResultSchemasTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAppResponseBodyResultSchemas(TeaModel):
    def __init__(
        self,
        index_sort_config: List[CreateAppResponseBodyResultSchemasIndexSortConfig] = None,
        indexes: CreateAppResponseBodyResultSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: CreateAppResponseBodyResultSchemasTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = CreateAppResponseBodyResultSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = CreateAppResponseBodyResultSchemasIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = CreateAppResponseBodyResultSchemasTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class CreateAppResponseBodyResultSecondRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppResponseBodyResultSummariesMeta(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class CreateAppResponseBodyResultSummaries(TeaModel):
    def __init__(
        self,
        meta: List[CreateAppResponseBodyResultSummariesMeta] = None,
        name: str = None,
    ):
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = CreateAppResponseBodyResultSummariesMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: CreateAppResponseBodyResultCluster = None,
        cluster_name: str = None,
        data_sources: List[CreateAppResponseBodyResultDataSources] = None,
        description: str = None,
        domain: CreateAppResponseBodyResultDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[CreateAppResponseBodyResultFirstRanks] = None,
        id: str = None,
        interpretations: Dict[str, Any] = None,
        is_current: bool = None,
        progress_percent: int = None,
        prompts: List[Dict[str, Any]] = None,
        query_processors: List[CreateAppResponseBodyResultQueryProcessors] = None,
        quota: CreateAppResponseBodyResultQuota = None,
        schema: CreateAppResponseBodyResultSchema = None,
        schemas: List[CreateAppResponseBodyResultSchemas] = None,
        second_ranks: List[CreateAppResponseBodyResultSecondRanks] = None,
        status: str = None,
        summaries: List[CreateAppResponseBodyResultSummaries] = None,
        type: str = None,
    ):
        self.auto_switch = auto_switch
        self.cluster = cluster
        self.cluster_name = cluster_name
        self.data_sources = data_sources
        self.description = description
        self.domain = domain
        self.fetch_fields = fetch_fields
        self.first_ranks = first_ranks
        self.id = id
        self.interpretations = interpretations
        self.is_current = is_current
        self.progress_percent = progress_percent
        self.prompts = prompts
        self.query_processors = query_processors
        self.quota = quota
        self.schema = schema
        self.schemas = schemas
        self.second_ranks = second_ranks
        self.status = status
        self.summaries = summaries
        self.type = type

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.quota:
            self.quota.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.interpretations is not None:
            result['interpretations'] = self.interpretations
        if self.is_current is not None:
            result['isCurrent'] = self.is_current
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.prompts is not None:
            result['prompts'] = self.prompts
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = CreateAppResponseBodyResultCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = CreateAppResponseBodyResultDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = CreateAppResponseBodyResultDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = CreateAppResponseBodyResultFirstRanks()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('interpretations') is not None:
            self.interpretations = m.get('interpretations')
        if m.get('isCurrent') is not None:
            self.is_current = m.get('isCurrent')
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('prompts') is not None:
            self.prompts = m.get('prompts')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = CreateAppResponseBodyResultQueryProcessors()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('quota') is not None:
            temp_model = CreateAppResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('schema') is not None:
            temp_model = CreateAppResponseBodyResultSchema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = CreateAppResponseBodyResultSchemas()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = CreateAppResponseBodyResultSecondRanks()
                self.second_ranks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = CreateAppResponseBodyResultSummaries()
                self.summaries.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupRequestQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        self.compute_resource = compute_resource
        self.doc_size = doc_size
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class CreateAppGroupRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        name: str = None,
        quota: CreateAppGroupRequestQuota = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.name = name
        self.quota = quota
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = CreateAppGroupRequestQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class CreateAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        engine_type: str = None,
        expire_on: str = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        produced: int = None,
        project_id: str = None,
        quota: CreateAppGroupResponseBodyResultQuota = None,
        status: str = None,
        switched_time: int = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The type of the industry. Valid values:
        # 
        # *   GENERAL: general.
        # *   ECOMMERCE: e-commerce.
        # *   IT_CONTENT: IT content.
        self.domain = domain
        self.engine_type = engine_type
        # The expiration time.
        self.expire_on = expire_on
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The ID of the application.
        self.id = id
        # The ID of the instance.
        self.instance_id = instance_id
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # The name of the application.
        self.name = name
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application.
        self.quota = quota
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = CreateAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppGroupResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupCredentialsRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        dry_run: bool = None,
    ):
        self.type = type
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppGroupCredentialsResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_group_id: int = None,
        enabled: bool = None,
        token: str = None,
        type: str = None,
    ):
        self.app_group_id = app_group_id
        self.enabled = enabled
        self.token = token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.token is not None:
            result['token'] = self.token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppGroupCredentialsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppGroupCredentialsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateAppGroupCredentialsResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateAppGroupCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppGroupCredentialsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppGroupCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFirstRankRequest(TeaModel):
    def __init__(
        self,
        body: FirstRank = None,
        dry_run: bool = None,
    ):
        # The request body that contains the parameters of the rough sort expression.
        self.body = body
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = FirstRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression.
        self.arg = arg
        # The attribute, feature functions, or field to be searched for.
        self.attribute = attribute
        # The weight. Valid values: [-100000,100000]. The value cannot be 0.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreateFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        meta: List[CreateFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The content of the expression.
        self.meta = meta
        # The name of the expression.
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = CreateFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateFirstRankResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateFunctionInstanceRequestUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateFunctionInstanceRequest(TeaModel):
    def __init__(
        self,
        create_parameters: List[CreateFunctionInstanceRequestCreateParameters] = None,
        cron: str = None,
        description: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        usage_parameters: List[CreateFunctionInstanceRequestUsageParameters] = None,
    ):
        # The parameters used to create the instance.
        self.create_parameters = create_parameters
        # The CRON expression used to schedule periodic training, in the format of Minutes Hours DayofMonth Month DayofWeek. The default value is empty, which specifies that no periodic training is performed. A value of 0 for DayofWeek specifies Sunday.
        self.cron = cron
        # The description.
        self.description = description
        # The feature type.
        # 
        # *   Default value: PAAS. Training is required before you can use the feature.
        self.function_type = function_type
        # The instance name. The name must be 1 to 30 characters in length and can contain letters, digits, and underscores (_). The name is case-sensitive and must start with a letter.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The model type. The value varies based on the model.
        # 
        # *   Click-through rate (CTR) model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Hint model: offline_inference
        # *   Hotword model for real-time top searches: near_realtime
        # *   Personalized hint model: near_realtime
        # *   Drop-down suggestion model: offline_inference
        # *   Tokenization model: text
        # *   Term weight model: tf_checkpoint
        # *   Synonym model: offline_inference
        # 
        # This parameter is required.
        self.model_type = model_type
        # The parameters used to use the instance.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['createParameters'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.model_type is not None:
            result['modelType'] = self.model_type
        result['usageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['usageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k in m.get('createParameters'):
                temp_model = CreateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k in m.get('usageParameters'):
                temp_model = CreateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class CreateFunctionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message. If no error occurs, this parameter is left empty.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFunctionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionResourceRequestDataGeneratorsInputFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        # 
        # Valid values:
        # 
        # *   item
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   user
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFunctionResourceRequestDataGeneratorsInput(TeaModel):
    def __init__(
        self,
        features: List[CreateFunctionResourceRequestDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = CreateFunctionResourceRequestDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class CreateFunctionResourceRequestDataGenerators(TeaModel):
    def __init__(
        self,
        generator: str = None,
        input: CreateFunctionResourceRequestDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        # 
        # Valid values:
        # 
        # *   lookup
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   sequence
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   overlap
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   raw
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   combo
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   id
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = CreateFunctionResourceRequestDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class CreateFunctionResourceRequestData(TeaModel):
    def __init__(
        self,
        content: str = None,
        generators: List[CreateFunctionResourceRequestDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = CreateFunctionResourceRequestDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class CreateFunctionResourceRequest(TeaModel):
    def __init__(
        self,
        data: CreateFunctionResourceRequestData = None,
        description: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description
        # The name of the resource.
        self.resource_name = resource_name
        # The resource type.
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
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateFunctionResourceRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateFunctionResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The time consumed for the request. Unit: milliseconds.
        self.latency = latency
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code. Valid values:
        # 
        # *   OK
        # *   FAIL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFunctionResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFunctionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInterventionDictionaryRequest(TeaModel):
    def __init__(
        self,
        analyzer_type: str = None,
        name: str = None,
        type: str = None,
        dry_run: bool = None,
    ):
        # The type of the analyzer. Valid values:
        # 
        # *   MODEL: model-based custom analyzer.
        # *   SYSTEM: system analyzer.
        # *   USER: custom analyzer.
        self.analyzer_type = analyzer_type
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering.
        # *   synonym: an intervention dictionary for synonym configuration.
        # *   correction: an intervention dictionary for spelling correction.
        # *   category_prediction: an intervention dictionary for category prediction.
        # *   ner: an intervention dictionary for named entity recognition (NER).
        # *   term_weighting: an intervention dictionary for term weight analysis.
        # *   suggest_allowlist: a drop-down suggestion whitelist.
        # *   suggest_denylist: a drop-down suggestion blacklist.
        # *   hot_allowlist: a top search whitelist.
        # *   hot_denylist: a top search blacklist.
        # *   hint_allowlist: a hint whitelist.
        # *   hint_denylist: a hint blacklist.
        self.type = type
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        analyzer: str = None,
        created: str = None,
        name: str = None,
        type: str = None,
        updated: str = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the test scenario was created.
        self.created = created
        # The name of the test group.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type
        # The time when the intervention dictionary was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateInterventionDictionaryResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueryProcessorRequest(TeaModel):
    def __init__(
        self,
        body: Any = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
    ):
        # Indicates whether the query analysis rule is the default one.
        self.active = active
        # The time when the query analysis rule was created.
        self.created = created
        # The type of the industry to which the query analysis rule was applied. Valid values:
        # 
        # *   GENERAL: general.
        # *   ECOMMERCE: e-commerce.
        # *   IT_CONTENT: IT content.
        self.domain = domain
        # The indexes to which the query analysis rule was applied.
        self.indexes = indexes
        # The name of the query analysis rule.
        self.name = name
        # The features that are used in the query analysis rule.
        # 
        # For more information, see [QueryProcessor](https://help.aliyun.com/document_detail/170014.html).
        self.processors = processors
        # The time when the query analysis rule was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateQueryProcessorResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the query analysis rule.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        body: ScheduledTask = None,
    ):
        # 请求体
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ScheduledTask()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the scheduled task.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSearchStrategyRequest(TeaModel):
    def __init__(
        self,
        body: SearchStrategy = None,
    ):
        # The query policy.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SearchStrategy()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSearchStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSearchStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSearchStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecondRankRequest(TeaModel):
    def __init__(
        self,
        body: SecondRank = None,
        dry_run: bool = None,
    ):
        # The request body. For more information, see [SecondRank](https://help.aliyun.com/document_detail/170008.html).
        self.body = body
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SecondRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the fine sort expression.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSortScriptRequest(TeaModel):
    def __init__(
        self,
        scope: str = None,
        script_name: str = None,
        type: str = None,
    ):
        # The sort phase to which the script applies.
        self.scope = scope
        # The script name.
        self.script_name = script_name
        # The script type. Set the value to cava_script.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSortScriptResponseBodyResult(TeaModel):
    def __init__(
        self,
        scope: str = None,
        script_name: str = None,
        type: str = None,
    ):
        # The sort phase to which the script applies.
        self.scope = scope
        # The script name.
        self.script_name = script_name
        # The script type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateSortScriptResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAnalyzerRequest(TeaModel):
    def __init__(
        self,
        business: str = None,
        business_app_group_id: str = None,
        business_type: str = None,
        name: str = None,
        type: str = None,
        dry_run: bool = None,
    ):
        # The basic analyzer.
        self.business = business
        # The application ID of the custom analyzer.
        self.business_app_group_id = business_app_group_id
        # The basic analyzer type. Valid values: AUTO, MODEL, SYSTEM, and USER.
        self.business_type = business_type
        # The analyzer name.
        self.name = name
        # The engine type. Valid values: HA3 and ES.
        self.type = type
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['business'] = self.business
        if self.business_app_group_id is not None:
            result['businessAppGroupId'] = self.business_app_group_id
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business') is not None:
            self.business = m.get('business')
        if m.get('businessAppGroupId') is not None:
            self.business_app_group_id = m.get('businessAppGroupId')
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The custom analyzer.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result that was returned.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message. If no error occurs, this parameter is left empty.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request. Valid values:
        # 
        # *   OK: The request is successful.
        # *   FAIL: The request fails.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteFunctionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code returned. If no error occurs, this value is empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The time consumed for the request. Unit: milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code. Valid values:
        # 
        # *   OK
        # *   FAIL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteFunctionResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteFunctionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestExperimentResponseBodyResultParams(TeaModel):
    def __init__(
        self,
        first_formula_name: str = None,
    ):
        # The name of the rough sort policy.
        self.first_formula_name = first_formula_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_formula_name is not None:
            result['first_formula_name'] = self.first_formula_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('first_formula_name') is not None:
            self.first_formula_name = m.get('first_formula_name')
        return self


class DescribeABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: DescribeABTestExperimentResponseBodyResultParams = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the test was created.
        self.created = created
        # The ID of the test.
        self.id = id
        # The name of the test.
        self.name = name
        # The status of the test. Valid values:
        # 
        # *   true: in effect
        # *   false: not in effect
        self.online = online
        # The parameters of the test.
        self.params = params
        # The percentage of traffic that is routed to the test.
        self.traffic = traffic
        # The time when the test was last modified.
        self.updated = updated

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResultParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeABTestExperimentResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the test.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
    ):
        # The time when the test group was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The name of the test group.
        self.name = name
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test group was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeABTestGroupResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the test group.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
        values: List[str] = None,
    ):
        # The time when the test scenario was created.
        self.created = created
        # The ID of the test scenario.
        self.id = id
        # The name of the test scenario.
        self.name = name
        # The status of the test scenario. Valid values:
        # 
        # *   0: The test is stopped.
        # *   1: The test is started.
        self.status = status
        # The time when the test was last modified.
        self.updated = updated
        # The indicators of the test scenarios.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class DescribeABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeABTestSceneResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the test scenario.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppResponseBodyResultCluster(TeaModel):
    def __init__(
        self,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
    ):
        self.max_query_clause_length = max_query_clause_length
        self.max_timeout_ms = max_timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class DescribeAppResponseBodyResultDataSources(TeaModel):
    def __init__(
        self,
        fields: List[Dict[str, Any]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, Any] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.plugins is not None:
            result['plugins'] = self.plugins
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('plugins') is not None:
            self.plugins = m.get('plugins')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppResponseBodyResultDomainFunctions(TeaModel):
    def __init__(
        self,
        algo: List[str] = None,
        qp: List[str] = None,
        service: List[str] = None,
    ):
        # Algorithm structure
        self.algo = algo
        # Queryprocessor description
        self.qp = qp
        # Function description
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo is not None:
            result['algo'] = self.algo
        if self.qp is not None:
            result['qp'] = self.qp
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algo') is not None:
            self.algo = m.get('algo')
        if m.get('qp') is not None:
            self.qp = m.get('qp')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class DescribeAppResponseBodyResultDomain(TeaModel):
    def __init__(
        self,
        category: str = None,
        functions: DescribeAppResponseBodyResultDomainFunctions = None,
        name: str = None,
    ):
        # The category. By default, this parameter is left empty.
        self.category = category
        # search functions
        self.functions = functions
        # The name
        self.name = name

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            temp_model = DescribeAppResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m['functions'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppResponseBodyResultFirstRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppResponseBodyResultQueryProcessors(TeaModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class DescribeAppResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        qps: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The number of search requests per second. You are charged based on the number of search requests per second in the earlier billing model.
        self.qps = qps
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.qps is not None:
            result['qps'] = self.qps
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeAppResponseBodyResultSchemaIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppResponseBodyResultSchemaIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class DescribeAppResponseBodyResultSchemaTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppResponseBodyResultSchema(TeaModel):
    def __init__(
        self,
        index_sort_config: List[DescribeAppResponseBodyResultSchemaIndexSortConfig] = None,
        indexes: DescribeAppResponseBodyResultSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: DescribeAppResponseBodyResultSchemaTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = DescribeAppResponseBodyResultSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = DescribeAppResponseBodyResultSchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = DescribeAppResponseBodyResultSchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class DescribeAppResponseBodyResultSchemasIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppResponseBodyResultSchemasIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class DescribeAppResponseBodyResultSchemasTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppResponseBodyResultSchemas(TeaModel):
    def __init__(
        self,
        index_sort_config: List[DescribeAppResponseBodyResultSchemasIndexSortConfig] = None,
        indexes: DescribeAppResponseBodyResultSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: DescribeAppResponseBodyResultSchemasTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = DescribeAppResponseBodyResultSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = DescribeAppResponseBodyResultSchemasIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = DescribeAppResponseBodyResultSchemasTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class DescribeAppResponseBodyResultSecondRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppResponseBodyResultSummariesMeta(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class DescribeAppResponseBodyResultSummaries(TeaModel):
    def __init__(
        self,
        meta: List[DescribeAppResponseBodyResultSummariesMeta] = None,
        name: str = None,
    ):
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = DescribeAppResponseBodyResultSummariesMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: DescribeAppResponseBodyResultCluster = None,
        cluster_name: str = None,
        data_sources: List[DescribeAppResponseBodyResultDataSources] = None,
        description: str = None,
        domain: DescribeAppResponseBodyResultDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[DescribeAppResponseBodyResultFirstRanks] = None,
        id: str = None,
        interpretations: Dict[str, Any] = None,
        is_current: bool = None,
        progress_percent: int = None,
        prompts: List[Dict[str, Any]] = None,
        query_processors: List[DescribeAppResponseBodyResultQueryProcessors] = None,
        quota: DescribeAppResponseBodyResultQuota = None,
        schema: DescribeAppResponseBodyResultSchema = None,
        schemas: List[DescribeAppResponseBodyResultSchemas] = None,
        second_ranks: List[DescribeAppResponseBodyResultSecondRanks] = None,
        status: str = None,
        summaries: List[DescribeAppResponseBodyResultSummaries] = None,
        type: str = None,
    ):
        # Indicates whether the version is automatically published to the online environment.
        self.auto_switch = auto_switch
        self.cluster = cluster
        # The name of the cluster.
        self.cluster_name = cluster_name
        self.data_sources = data_sources
        # The description of the version.
        self.description = description
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The default display fields.
        self.fetch_fields = fetch_fields
        self.first_ranks = first_ranks
        # The ID of the version.
        self.id = id
        self.interpretations = interpretations
        self.is_current = is_current
        # The progress of data import, in percentage. For example, a value of 83 indicates 83%.
        self.progress_percent = progress_percent
        self.prompts = prompts
        self.query_processors = query_processors
        # The quota information about the version.
        self.quota = quota
        # The application schema.
        self.schema = schema
        self.schemas = schemas
        self.second_ranks = second_ranks
        # The status of the version. Valid values:
        # 
        # *   ok
        # *   stopped
        # *   frozen
        # *   initializing
        # *   unavailable
        # *   data_waiting
        # *   data_preparing
        self.status = status
        self.summaries = summaries
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.quota:
            self.quota.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.interpretations is not None:
            result['interpretations'] = self.interpretations
        if self.is_current is not None:
            result['isCurrent'] = self.is_current
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.prompts is not None:
            result['prompts'] = self.prompts
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = DescribeAppResponseBodyResultCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = DescribeAppResponseBodyResultDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = DescribeAppResponseBodyResultDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = DescribeAppResponseBodyResultFirstRanks()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('interpretations') is not None:
            self.interpretations = m.get('interpretations')
        if m.get('isCurrent') is not None:
            self.is_current = m.get('isCurrent')
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('prompts') is not None:
            self.prompts = m.get('prompts')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = DescribeAppResponseBodyResultQueryProcessors()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('quota') is not None:
            temp_model = DescribeAppResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('schema') is not None:
            temp_model = DescribeAppResponseBodyResultSchema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = DescribeAppResponseBodyResultSchemas()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = DescribeAppResponseBodyResultSecondRanks()
                self.second_ranks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = DescribeAppResponseBodyResultSummaries()
                self.summaries.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAppResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the version.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic.
        # *   opensearch.share.common: shared general-purpose.
        # *   opensearch.share.compute: shared computing.
        # *   opensearch.share.storage: shared storage.
        # *   opensearch.private.common: exclusive general-purpose.
        # *   opensearch.private.compute: exclusive computing.
        # *   opensearch.private.storage: exclusive storage.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeAppGroupResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        engine_type: str = None,
        expire_on: str = None,
        first_rank_algo_deployment_id: int = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        locked_by_expiration: int = None,
        name: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        processing_order_id: str = None,
        produced: int = None,
        project_id: str = None,
        quota: DescribeAppGroupResponseBodyResultQuota = None,
        resource_group_id: str = None,
        second_rank_algo_deployment_id: int = None,
        status: str = None,
        switched_time: int = None,
        tags: List[DescribeAppGroupResponseBodyResultTags] = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billable item. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way
        # The commodity code.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The industry of the application.
        self.domain = domain
        self.engine_type = engine_type
        # The expiration time.
        self.expire_on = expire_on
        # The ID of the created rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The application is in service.
        # *   1: The quotas are being reviewed.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration
        # The application name.
        self.name = name
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        # The ID of the order that is not complete.
        self.processing_order_id = processing_order_id
        # Indicates whether the application is created. Valid values:
        # 
        # *   0: The application is being created.
        # *   1: The application is created.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application.
        self.quota = quota
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the created fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        # The state of the application. Valid values:
        # 
        # *   producing: The application is being created.
        # *   review_pending: The application is being reviewed.
        # *   config_pending: The application is to be configured.
        # *   normal: The application is in service.
        # *   frozen: The application is frozen.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The application tags.
        self.tags = tags
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *\
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = DescribeAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeAppGroupResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAppGroupResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the application.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The statistics.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeAppStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsResponseBodyResultCluster(TeaModel):
    def __init__(
        self,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
    ):
        self.max_query_clause_length = max_query_clause_length
        self.max_timeout_ms = max_timeout_ms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class DescribeAppsResponseBodyResultDataSources(TeaModel):
    def __init__(
        self,
        fields: List[Dict[str, Any]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, Any] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.plugins is not None:
            result['plugins'] = self.plugins
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('plugins') is not None:
            self.plugins = m.get('plugins')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppsResponseBodyResultDomainFunctions(TeaModel):
    def __init__(
        self,
        algo: List[str] = None,
        qp: List[str] = None,
        service: List[str] = None,
    ):
        self.algo = algo
        self.qp = qp
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo is not None:
            result['algo'] = self.algo
        if self.qp is not None:
            result['qp'] = self.qp
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algo') is not None:
            self.algo = m.get('algo')
        if m.get('qp') is not None:
            self.qp = m.get('qp')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class DescribeAppsResponseBodyResultDomain(TeaModel):
    def __init__(
        self,
        category: str = None,
        functions: DescribeAppsResponseBodyResultDomainFunctions = None,
        name: str = None,
    ):
        self.category = category
        self.functions = functions
        self.name = name

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            temp_model = DescribeAppsResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m['functions'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppsResponseBodyResultFirstRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppsResponseBodyResultQueryProcessors(TeaModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.active = active
        self.category = category
        self.domain = domain
        self.indexes = indexes
        self.name = name
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class DescribeAppsResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        qps: int = None,
        spec: str = None,
    ):
        self.compute_resource = compute_resource
        self.doc_size = doc_size
        self.qps = qps
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.qps is not None:
            result['qps'] = self.qps
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeAppsResponseBodyResultSchemaIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppsResponseBodyResultSchemaIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class DescribeAppsResponseBodyResultSchemaTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppsResponseBodyResultSchema(TeaModel):
    def __init__(
        self,
        index_sort_config: List[DescribeAppsResponseBodyResultSchemaIndexSortConfig] = None,
        indexes: DescribeAppsResponseBodyResultSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: DescribeAppsResponseBodyResultSchemaTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = DescribeAppsResponseBodyResultSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = DescribeAppsResponseBodyResultSchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = DescribeAppsResponseBodyResultSchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class DescribeAppsResponseBodyResultSchemasIndexSortConfig(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppsResponseBodyResultSchemasIndexes(TeaModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        self.filter_fields = filter_fields
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        if self.search_fields is not None:
            result['searchFields'] = self.search_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        if m.get('searchFields') is not None:
            self.search_fields = m.get('searchFields')
        return self


class DescribeAppsResponseBodyResultSchemasTtlField(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeAppsResponseBodyResultSchemas(TeaModel):
    def __init__(
        self,
        index_sort_config: List[DescribeAppsResponseBodyResultSchemasIndexSortConfig] = None,
        indexes: DescribeAppsResponseBodyResultSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: DescribeAppsResponseBodyResultSchemasTtlField = None,
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
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
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
        if self.tables is not None:
            result['tables'] = self.tables
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = DescribeAppsResponseBodyResultSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = DescribeAppsResponseBodyResultSchemasIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('ttlField') is not None:
            temp_model = DescribeAppsResponseBodyResultSchemasTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class DescribeAppsResponseBodyResultSecondRanks(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppsResponseBodyResultSummariesMeta(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class DescribeAppsResponseBodyResultSummaries(TeaModel):
    def __init__(
        self,
        meta: List[DescribeAppsResponseBodyResultSummariesMeta] = None,
        name: str = None,
    ):
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = DescribeAppsResponseBodyResultSummariesMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppsResponseBodyResult(TeaModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: DescribeAppsResponseBodyResultCluster = None,
        cluster_name: str = None,
        data_sources: List[DescribeAppsResponseBodyResultDataSources] = None,
        description: str = None,
        domain: DescribeAppsResponseBodyResultDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[DescribeAppsResponseBodyResultFirstRanks] = None,
        id: str = None,
        interpretations: Dict[str, Any] = None,
        is_current: bool = None,
        progress_percent: int = None,
        prompts: List[Dict[str, Any]] = None,
        query_processors: List[DescribeAppsResponseBodyResultQueryProcessors] = None,
        quota: DescribeAppsResponseBodyResultQuota = None,
        schema: DescribeAppsResponseBodyResultSchema = None,
        schemas: List[DescribeAppsResponseBodyResultSchemas] = None,
        second_ranks: List[DescribeAppsResponseBodyResultSecondRanks] = None,
        status: str = None,
        summaries: List[DescribeAppsResponseBodyResultSummaries] = None,
        type: str = None,
    ):
        self.auto_switch = auto_switch
        self.cluster = cluster
        self.cluster_name = cluster_name
        self.data_sources = data_sources
        self.description = description
        self.domain = domain
        self.fetch_fields = fetch_fields
        self.first_ranks = first_ranks
        self.id = id
        self.interpretations = interpretations
        self.is_current = is_current
        self.progress_percent = progress_percent
        self.prompts = prompts
        self.query_processors = query_processors
        self.quota = quota
        self.schema = schema
        self.schemas = schemas
        self.second_ranks = second_ranks
        self.status = status
        self.summaries = summaries
        self.type = type

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.quota:
            self.quota.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.interpretations is not None:
            result['interpretations'] = self.interpretations
        if self.is_current is not None:
            result['isCurrent'] = self.is_current
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.prompts is not None:
            result['prompts'] = self.prompts
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = DescribeAppsResponseBodyResultCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = DescribeAppsResponseBodyResultDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = DescribeAppsResponseBodyResultDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = DescribeAppsResponseBodyResultFirstRanks()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('interpretations') is not None:
            self.interpretations = m.get('interpretations')
        if m.get('isCurrent') is not None:
            self.is_current = m.get('isCurrent')
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('prompts') is not None:
            self.prompts = m.get('prompts')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = DescribeAppsResponseBodyResultQueryProcessors()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('quota') is not None:
            temp_model = DescribeAppsResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('schema') is not None:
            temp_model = DescribeAppsResponseBodyResultSchema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = DescribeAppsResponseBodyResultSchemas()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = DescribeAppsResponseBodyResultSecondRanks()
                self.second_ranks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = DescribeAppsResponseBodyResultSummaries()
                self.summaries.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeAppsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each version.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeAppsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCollctionResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        id: str = None,
        industry_name: str = None,
        name: str = None,
        status: int = None,
        sundial_id: str = None,
        type: str = None,
        updated: int = None,
    ):
        # The time when the task was created.
        self.created = created
        # The type of data collected. Valid values:
        # 
        # *   behavior: behavioral data.
        # *   item_info: project information.
        # *   industry_specific: industry-specific data.
        self.data_collection_type = data_collection_type
        # The ID of the data collection task.
        self.id = id
        # The industry name. Valid values:
        # 
        # *   general
        # *   ecommerce
        self.industry_name = industry_name
        # The name of the data collection task.
        self.name = name
        # The status of the data collection feature. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is being enabled.
        # *   2: The feature is enabled.
        # *   3: The feature failed to be enabled.
        self.status = status
        # The sundial ID.
        self.sundial_id = sundial_id
        # The type of the source from which data was collected. Valid values:
        # 
        # *   server
        # *   web
        # *   app Note: Only server is supported.
        self.type = type
        # The time when the data collection task was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.id is not None:
            result['id'] = self.id
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeDataCollctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDataCollctionResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the data collection task.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeDataCollctionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeDataCollctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataCollctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataCollctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression.
        self.arg = arg
        # The attribute, feature function, or field to be searched for.
        self.attribute = attribute
        # The weight.
        # 
        # Valid values: [-100000,100000] (excluding 0).
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class DescribeFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: List[DescribeFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The description of the expression.
        self.description = description
        # The content of the expression.
        self.meta = meta
        # The name of the expression.
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = DescribeFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeFirstRankResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the rough sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        analyzer: str = None,
        created: str = None,
        name: str = None,
        type: str = None,
        updated: str = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the intervention dictionary was created.
        self.created = created
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type
        # The time when the intervention dictionary was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeInterventionDictionaryResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information the intervention dictionary.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
    ):
        # Indicates whether the query analysis rule is the default one.
        self.active = active
        # The time when the query analysis rule was created.
        self.created = created
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The indexes to which the query analysis rule applies.
        self.indexes = indexes
        # The name of the query analysis rule.
        self.name = name
        # The features that are used in the query analysis rule.
        self.processors = processors
        # The time when the query analysis rule was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeQueryProcessorResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the query analysis rule.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        console_url: str = None,
        endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        # The console URL.
        self.console_url = console_url
        # The endpoint.
        self.endpoint = endpoint
        # The region name.
        self.local_name = local_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeRegionsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The results returned.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the scheduled task.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecondRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        id: str = None,
        is_default: str = None,
        is_sys: str = None,
        meta: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The time when the expression was created.
        self.created = created
        # The description of the expression.
        self.description = description
        # The ID of the expression. This parameter appears only in the response.
        self.id = id
        # Indicates whether the expression is the default one. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default
        # Indicates whether the expression is a system expression. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_sys = is_sys
        # The content of the fine sort expression.
        # 
        # You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta
        # The name of the expression.
        self.name = name
        # The time when the expression was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSecondRankResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the fine sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_group_id: str = None,
        region: str = None,
        status: str = None,
    ):
        # The ID of the application.
        self.app_group_id = app_group_id
        # The network type of the slow query optimization service. Valid values:
        # 
        # *   outer: the Internet
        # *   internal: the internal network
        self.region = region
        # The status of the slow query optimization service. Valid values:
        # 
        # *   enabled
        # *   disabled
        # *   n/a
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeSlowQueryStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSlowQueryStatusResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSlowQueryStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSlowQueryStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowQueryStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowQueryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAnalyzerRequest(TeaModel):
    def __init__(
        self,
        with_: str = None,
    ):
        # The Associated information,output properties based on hierarchy.
        # * **all**: Outputs associated app information
        self.with_ = with_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_ is not None:
            result['with'] = self.with_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('with') is not None:
            self.with_ = m.get('with')
        return self


class DescribeUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the custom analyzer.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSlowQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DisableSlowQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableSlowQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSlowQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class EnableSlowQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableSlowQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateMergedTableRequest(TeaModel):
    def __init__(
        self,
        body: Schema = None,
        spec: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The specifications of the OpenSearch instance. This parameter is used to check whether the OpenSearch instance meets the special limits on an exclusive instance.
        # 
        # Default value: opensearch.share.common.
        # 
        # For more information, see the description of the spec field in the Quota topic.
        self.spec = spec

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Schema()
            self.body = temp_model.from_map(m['body'])
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class GenerateMergedTableResponseBodyResult(TeaModel):
    def __init__(
        self,
        from_table: Dict[str, Any] = None,
        merge_table: Dict[str, Any] = None,
        primary_key: str = None,
    ):
        # The tables on which the JOIN operation is performed.
        self.from_table = from_table
        # The wide table that is generated after the JOIN operation is performed on multiple tables.
        self.merge_table = merge_table
        # The primary key.
        self.primary_key = primary_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_table is not None:
            result['fromTable'] = self.from_table
        if self.merge_table is not None:
            result['mergeTable'] = self.merge_table
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTable') is not None:
            self.from_table = m.get('fromTable')
        if m.get('mergeTable') is not None:
            self.merge_table = m.get('mergeTable')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        return self


class GenerateMergedTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GenerateMergedTableResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GenerateMergedTableResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GenerateMergedTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateMergedTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateMergedTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(
        self,
        app_group_identity: str = None,
    ):
        # The name or ID of the application.
        # 
        # This parameter is required.
        self.app_group_identity = app_group_identity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_identity is not None:
            result['appGroupIdentity'] = self.app_group_identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupIdentity') is not None:
            self.app_group_identity = m.get('appGroupIdentity')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCurrentVersionRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        function_type: str = None,
        model_type: str = None,
    ):
        # The category. By default, this parameter is left empty.
        self.category = category
        # The industry. By default, this parameter is left empty, which indicates General-purpose Edition.
        self.domain = domain
        # The type of the feature. Valid values:
        # 
        # *   PAAS. This is the default value.
        # *   SAAS.
        self.function_type = function_type
        # The type of the model. The following features correspond to different model types:
        # 
        # *   CTR model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Shading model: offline_inference
        # *   Drop-down suggestion model: offline_inference
        # *   Word segmentation model: text
        # *   Word weight model: tf_checkpoint
        # 
        # This parameter is required.
        self.model_type = model_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.model_type is not None:
            result['modelType'] = self.model_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends(TeaModel):
    def __init__(
        self,
        condition: str = None,
        dependency: str = None,
        description: str = None,
    ):
        # The condition.
        self.condition = condition
        # The dependency.
        self.dependency = dependency
        # The description.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.dependency is not None:
            result['Dependency'] = self.dependency
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Dependency') is not None:
            self.dependency = m.get('Dependency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfig(TeaModel):
    def __init__(
        self,
        create_parameters: List[GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters] = None,
        depends: List[GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends] = None,
        usage_parameters: List[GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters] = None,
    ):
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The dependencies of the instance.
        self.depends = depends
        # The parameters that are used to use the instance online.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.depends:
            for k in self.depends:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        result['Depends'] = []
        if self.depends is not None:
            for k in self.depends:
                result['Depends'].append(k.to_map() if k else None)
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        self.depends = []
        if m.get('Depends') is not None:
            for k in m.get('Depends'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends()
                self.depends.append(temp_model.from_map(k))
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class GetFunctionCurrentVersionResponseBodyResult(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        function_type: str = None,
        model_type: str = None,
        version_config: GetFunctionCurrentVersionResponseBodyResultVersionConfig = None,
        version_id: int = None,
        version_name: str = None,
    ):
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature. Valid values:
        # 
        # *   PAAS
        # *   SAAS
        self.function_type = function_type
        # The type of the model.
        self.model_type = model_type
        # The configuration information about the instance.
        self.version_config = version_config
        # The ID of the version.
        self.version_id = version_id
        # The name of the version.
        self.version_name = version_name

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('VersionConfig') is not None:
            temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfig()
            self.version_config = temp_model.from_map(m['VersionConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetFunctionCurrentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionCurrentVersionResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the request.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionCurrentVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionCurrentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionCurrentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionCurrentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionDefaultInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The default instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class GetFunctionDefaultInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        function_name: str = None,
        http_code: int = None,
        instance_name: str = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionDefaultInstanceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The name of the feature.
        self.function_name = function_name
        # The HTTP status code.
        self.http_code = http_code
        # The name of the instance.
        self.instance_name = instance_name
        # The default running time.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the request.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionDefaultInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionDefaultInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionDefaultInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionInstanceRequest(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # Specifies the richness of returned information. Valid values:
        # 
        # *   simple: displays only the basic information.
        # *   normal: displays information such as createParameters and cron. This is the default value.
        # *   detail: returns the details of the training task.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        return self


class GetFunctionInstanceResponseBodyResultBelongs(TeaModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        language: str = None,
    ):
        # The category.
        self.category = category
        # The industry.
        self.domain = domain
        # The abbreviation of the language that applies.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetFunctionInstanceResponseBodyResultCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetFunctionInstanceResponseBodyResultTask(TeaModel):
    def __init__(
        self,
        dag_status: str = None,
        last_run_time: int = None,
    ):
        # The status of the task. Valid values:
        # 
        # *   success: succeeded
        # *   failed: failed
        # *   untrained: to be trained
        # *   pending: being scheduled
        # *   running: being trained
        self.dag_status = dag_status
        # The time consumed for the most recent run, in milliseconds.
        self.last_run_time = last_run_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_status is not None:
            result['DagStatus'] = self.dag_status
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagStatus') is not None:
            self.dag_status = m.get('DagStatus')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        return self


class GetFunctionInstanceResponseBodyResultUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetFunctionInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        belongs: GetFunctionInstanceResponseBodyResultBelongs = None,
        create_parameters: List[GetFunctionInstanceResponseBodyResultCreateParameters] = None,
        create_time: int = None,
        cron: str = None,
        description: str = None,
        extend_info: str = None,
        function_name: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        source: str = None,
        status: str = None,
        task: GetFunctionInstanceResponseBodyResultTask = None,
        usage_parameters: List[GetFunctionInstanceResponseBodyResultUsageParameters] = None,
        version_id: int = None,
    ):
        # The information about the instance.
        self.belongs = belongs
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The time when the task was created. Unit: milliseconds.
        self.create_time = create_time
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron
        # The description of the instance.
        self.description = description
        # The extended information, which is a JSON string.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature.
        self.function_type = function_type
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the model.
        self.model_type = model_type
        # How the instance is created. Valid values:
        # 
        # *   user: The instance is created by user.
        # *   builtin: The instance is created by the system.
        self.source = source
        # The status of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status
        # The information about the training task. This parameter is not displayed if no task is available.
        self.task = task
        # The parameters that are used.
        self.usage_parameters = usage_parameters
        # The ID of the version.
        self.version_id = version_id

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.task:
            self.task.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belongs is not None:
            result['Belongs'] = self.belongs.to_map()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.description is not None:
            result['Description'] = self.description
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task is not None:
            result['Task'] = self.task.to_map()
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Belongs') is not None:
            temp_model = GetFunctionInstanceResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m['Belongs'])
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionInstanceResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Task') is not None:
            temp_model = GetFunctionInstanceResponseBodyResultTask()
            self.task = temp_model.from_map(m['Task'])
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionInstanceResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetFunctionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionInstanceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details of the instance.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionResourceRequest(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output level.
        # 
        # Valid values:
        # 
        # *   simple
        # *   normal
        # *   detail
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        return self


class GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFunctionResourceResponseBodyResultDataGeneratorsInput(TeaModel):
    def __init__(
        self,
        features: List[GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class GetFunctionResourceResponseBodyResultDataGenerators(TeaModel):
    def __init__(
        self,
        generator: str = None,
        input: GetFunctionResourceResponseBodyResultDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = GetFunctionResourceResponseBodyResultDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class GetFunctionResourceResponseBodyResultData(TeaModel):
    def __init__(
        self,
        content: str = None,
        generators: List[GetFunctionResourceResponseBodyResultDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = GetFunctionResourceResponseBodyResultDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class GetFunctionResourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data: GetFunctionResourceResponseBodyResultData = None,
        description: str = None,
        function_name: str = None,
        modify_time: int = None,
        referenced_instances: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The time when the resource was created. Unit: milliseconds.
        self.create_time = create_time
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description
        # The name of the feature.
        self.function_name = function_name
        # The time when the resource was modified. Unit: milliseconds.
        self.modify_time = modify_time
        # The algorithm instances that are referenced.
        self.referenced_instances = referenced_instances
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.referenced_instances is not None:
            result['ReferencedInstances'] = self.referenced_instances
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = GetFunctionResourceResponseBodyResultData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ReferencedInstances') is not None:
            self.referenced_instances = m.get('ReferencedInstances')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetFunctionResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionResourceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code returned. If no error occurs, this value is empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The time consumed for the API request. Unit: milliseconds.
        self.latency = latency
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result
        # The HTTP status code. Valid values:
        # 
        # *   OK
        # *   FAIL
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionResourceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        extend_info: str = None,
        function_name: str = None,
        generation: str = None,
        progress: int = None,
        run_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The timestamp that indicates the end time of the task. Unit: milliseconds.
        self.end_time = end_time
        # The extended information, which is a JSON string.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The number of iterations.
        self.generation = generation
        # The progress. 90 indicates 90%.
        self.progress = progress
        # The ID of the task.
        self.run_id = run_id
        # The timestamp that indicates the start time of the task. Unit: milliseconds.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionTaskResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the request.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionTaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionVersionResponseBodyResultVersionConfigCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionVersionResponseBodyResultVersionConfigDepends(TeaModel):
    def __init__(
        self,
        condition: str = None,
        dependency: str = None,
        description: str = None,
    ):
        # The condition.
        self.condition = condition
        # The dependency.
        self.dependency = dependency
        # The description.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.dependency is not None:
            result['Dependency'] = self.dependency
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Dependency') is not None:
            self.dependency = m.get('Dependency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetFunctionVersionResponseBodyResultVersionConfigUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: str = None,
    ):
        # The name of the instance.
        self.name = name
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionVersionResponseBodyResultVersionConfig(TeaModel):
    def __init__(
        self,
        create_parameters: List[GetFunctionVersionResponseBodyResultVersionConfigCreateParameters] = None,
        depends: List[GetFunctionVersionResponseBodyResultVersionConfigDepends] = None,
        usage_parameters: List[GetFunctionVersionResponseBodyResultVersionConfigUsageParameters] = None,
    ):
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The dependencies of the instance.
        self.depends = depends
        # The parameters that are used during online use of the instance.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.depends:
            for k in self.depends:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        result['Depends'] = []
        if self.depends is not None:
            for k in self.depends:
                result['Depends'].append(k.to_map() if k else None)
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        self.depends = []
        if m.get('Depends') is not None:
            for k in m.get('Depends'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigDepends()
                self.depends.append(temp_model.from_map(k))
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class GetFunctionVersionResponseBodyResult(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        function_type: str = None,
        model_type: str = None,
        version_config: GetFunctionVersionResponseBodyResultVersionConfig = None,
        version_id: int = None,
        version_name: str = None,
    ):
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature. Valid values:
        # 
        # *   PAAS
        # *   SAAS
        self.function_type = function_type
        # The type of the model.
        self.model_type = model_type
        # The configuration information.
        self.version_config = version_config
        # The ID of the version.
        self.version_id = version_id
        # The name of the version.
        self.version_name = version_name

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('VersionConfig') is not None:
            temp_model = GetFunctionVersionResponseBodyResultVersionConfig()
            self.version_config = temp_model.from_map(m['VersionConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetFunctionVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: GetFunctionVersionResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The maximum duration for which a task can be executed.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result body.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScriptFileNamesResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        file_name: str = None,
        modify_time: str = None,
        path_name: str = None,
    ):
        # The time when the script file was created.
        self.create_time = create_time
        # The name of the script file.
        self.file_name = file_name
        # The time when the script file was last modified.
        self.modify_time = modify_time
        # The path name of the script file.
        self.path_name = path_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.path_name is not None:
            result['pathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('pathName') is not None:
            self.path_name = m.get('pathName')
        return self


class GetScriptFileNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetScriptFileNamesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The files of the script.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetScriptFileNamesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetScriptFileNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScriptFileNamesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScriptFileNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSearchStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSearchStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSearchStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        scope: str = None,
        script_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the script was created.
        self.create_time = create_time
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The sort phase to which the script applies.
        self.scope = scope
        # The name of the script.
        self.script_name = script_name
        # The status of the script. For more information, see the description of the status response parameter in the ListSortScripts topic.
        self.status = status
        # The type of the script.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetSortScriptResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the script.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        modify_time: str = None,
        version: int = None,
    ):
        # The script content that is encoded in the Base64 format.
        self.content = content
        # The time when the script was created.
        self.create_time = create_time
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The version of the script content.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetSortScriptFileResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The content of the sort script.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetSortScriptFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestExperimentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the experiment was created.
        self.created = created
        # The experiment ID.
        self.id = id
        # The group alias.
        self.name = name
        # Indicates whether the experiment is in effect. Valid values:
        # 
        # *   true
        # *   false
        self.online = online
        # The experiment parameters.
        self.params = params
        # The percentage of traffic that is routed to the experiment.
        # 
        # Valid values: [0,100]
        self.traffic = traffic
        # The time when the experiment was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListABTestExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListABTestExperimentsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The experiment details.\\
        # For more information, see [ABTestExperiment](https://help.aliyun.com/document_detail/173617.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestExperimentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABTestExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The queried whitelists.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListABTestFixedFlowDividersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABTestFixedFlowDividersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestGroupsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
    ):
        # The time when the test group was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The name of the test group.
        self.name = name
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test group was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListABTestGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListABTestGroupsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The test groups.
        # 
        # For more information, see [ABTestGroup](https://help.aliyun.com/document_detail/178935.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABTestGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestScenesResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
        values: List[str] = None,
    ):
        # The time when the test scenario was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The name of the test group.
        self.name = name
        # The status of the test scenario. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test scenario was last modified.
        self.updated = updated
        # The name of the test scenario.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListABTestScenesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListABTestScenesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the test scenarios.
        # 
        # For more information, see [ABTestScene](https://help.aliyun.com/document_detail/173618.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListABTestScenesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupsRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListAppGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: int = None,
        tags: List[ListAppGroupsRequestTags] = None,
        type: str = None,
    ):
        # The ID of the instance. Exact match is used.
        self.instance_id = instance_id
        # The name of the application.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The method based on which applications are sorted. Valid values:
        # 
        # *   0: sorts applications in descending order by creation time.
        # *   1: sorts applications in descending order by modification time.
        # 
        # Default value: 0.
        self.sort_by = sort_by
        # The tags.
        self.tags = tags
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListAppGroupsRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAppGroupsShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: int = None,
        tags_shrink: str = None,
        type: str = None,
    ):
        # The ID of the instance. Exact match is used.
        self.instance_id = instance_id
        # The name of the application.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The method based on which applications are sorted. Valid values:
        # 
        # *   0: sorts applications in descending order by creation time.
        # *   1: sorts applications in descending order by modification time.
        # 
        # Default value: 0.
        self.sort_by = sort_by
        # The tags.
        self.tags_shrink = tags_shrink
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAppGroupsResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic.
        # *   opensearch.share.common: shared general-purpose.
        # *   opensearch.share.compute: shared computing.
        # *   opensearch.share.storage: shared storage.
        # *   opensearch.private.common: exclusive general-purpose.
        # *   opensearch.private.compute: exclusive computing.
        # *   opensearch.private.storage: exclusive storage.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListAppGroupsResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListAppGroupsResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        engine_type: str = None,
        expire_on: str = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        locked_by_expiration: int = None,
        name: str = None,
        produced: int = None,
        project_id: str = None,
        quota: ListAppGroupsResponseBodyResultQuota = None,
        status: str = None,
        switched_time: int = None,
        tags: List[ListAppGroupsResponseBodyResultTags] = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billable item. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way
        # The commodity code.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The industry of the application.
        self.domain = domain
        self.engine_type = engine_type
        # The time when the application expired.
        self.expire_on = expire_on
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The application is in service.
        # *   1: The quotas are being reviewed.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration
        # The application name.
        self.name = name
        # Indicates whether the application is created. Valid values:
        # 
        # *   0: The application is being created.
        # *   1: The application is created.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application. For more information, see [Quota](https://help.aliyun.com/document_detail/170001.html).
        self.quota = quota
        # The state of the application. Valid values:
        # 
        # *   producing: The application is being created.
        # *   review_pending: The application is being reviewed.
        # *   config_pending: The application is to be configured.
        # *   normal: The application is in service.
        # *   frozen: The application is frozen.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The application tags.
        self.tags = tags
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *\
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ListAppGroupsResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListAppGroupsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListAppGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAppGroupsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the application.
        # 
        # For more information, see [AppGroup](https://help.aliyun.com/document_detail/170000.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAppGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataCollectionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 1
        self.page_number = page_number
        # 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDataCollectionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        data_collection_type: str = None,
        id: str = None,
        industry_name: str = None,
        name: str = None,
        status: int = None,
        sundial_id: str = None,
        type: str = None,
        updated: int = None,
    ):
        # The time when the data collection task was created.
        self.created = created
        # The type of the data that is collected by the task. Valid values:
        # 
        # *   behavior: behavioral data
        # *   item_info: project data
        # *   industry_specific: industry-specific data
        self.data_collection_type = data_collection_type
        # The ID of the data collection task.
        self.id = id
        # The industry to which the data collection task applies. Valid values:
        # 
        # *   general
        # *   ecommerce
        self.industry_name = industry_name
        # The name of the data collection task.
        self.name = name
        # The status of the data collection task. Valid values:
        # 
        # *   0: disabled
        # *   1: being enabled
        # *   2: enabled
        # *   3: failed to be enabled
        self.status = status
        # The ID of the sundial.
        self.sundial_id = sundial_id
        # The type of the data source. Valid values:
        # 
        # *   server
        # *   web
        # *   app
        # 
        # Note: Only server is supported.
        self.type = type
        # The time when the data collection task was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.id is not None:
            result['id'] = self.id
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListDataCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataCollectionsResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the data collection tasks.
        # 
        # For more information, see [DataCollection](https://help.aliyun.com/document_detail/173605.html).
        self.result = result
        # The total number of the returned data collection tasks.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataCollectionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTableFieldsRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        raw_type: bool = None,
    ):
        # The parameters of the data source. The value of the params parameter is a JSON string. The value must be URL-encoded.
        # 
        # Different types of data sources use different parameters. For more information, see the following sections of the "DataSource" topic:
        # 
        # *   [rds](https://help.aliyun.com/document_detail/170005.html)
        # *   [polardb](https://help.aliyun.com/document_detail/170005.html)
        # *   [odps](https://help.aliyun.com/document_detail/170005.html)
        # *   [mysql](https://help.aliyun.com/document_detail/173627.html)
        # *   [drds](https://help.aliyun.com/document_detail/173627.html)
        # 
        # This parameter is required.
        self.params = params
        # Specifies whether to return the original field types of the data source.
        self.raw_type = raw_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.raw_type is not None:
            result['rawType'] = self.raw_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('rawType') is not None:
            self.raw_type = m.get('rawType')
        return self


class ListDataSourceTableFieldsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataSourceTableFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceTableFieldsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTableFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTablesRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
    ):
        # N/A
        # 
        # This parameter is required.
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        return self


class ListDataSourceTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data tables.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataSourceTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFirstRanksResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: int = None,
    ):
        # The parameters that are used by a function in the expression.
        # 
        # For more information, see [Rough sort functions](https://help.aliyun.com/document_detail/180765.html).
        self.arg = arg
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see [Rough sort functions](https://help.aliyun.com/document_detail/180765.html).
        self.attribute = attribute
        # The weight.
        # 
        # Valid values: [-100000,100000] (excluding 0).
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ListFirstRanksResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        meta: List[ListFirstRanksResponseBodyResultMeta] = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The time when the cluster was created.
        self.created = created
        # The description of the expression.
        self.description = description
        # The content of the expression.
        self.meta = meta
        # The name of the expression.
        self.name = name
        # The time when the cluster was updated.
        self.updated = updated

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ListFirstRanksResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListFirstRanksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListFirstRanksResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each rough sort expression.
        # 
        # For more information, see [FirstRank](https://help.aliyun.com/document_detail/170007.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFirstRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListFirstRanksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFirstRanksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFirstRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionInstancesRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListFunctionInstancesResponseBodyResultBelongs(TeaModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        language: str = None,
    ):
        # The category.
        self.category = category
        # The industry.
        self.domain = domain
        # The abbreviation of the language that applies.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListFunctionInstancesResponseBodyResultCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFunctionInstancesResponseBodyResultUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFunctionInstancesResponseBodyResult(TeaModel):
    def __init__(
        self,
        belongs: ListFunctionInstancesResponseBodyResultBelongs = None,
        create_parameters: List[ListFunctionInstancesResponseBodyResultCreateParameters] = None,
        create_time: int = None,
        cron: str = None,
        description: str = None,
        extend_info: str = None,
        function_name: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        source: str = None,
        status: str = None,
        usage_parameters: List[ListFunctionInstancesResponseBodyResultUsageParameters] = None,
        version_id: int = None,
    ):
        # The information about the instance.
        self.belongs = belongs
        # The parameters of the instance.
        self.create_parameters = create_parameters
        # The time when the instance was created.
        self.create_time = create_time
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron
        # The description.
        self.description = description
        # The extended information, which is a JSON string. It includes model evaluation information and error information.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The type of the feature.
        self.function_type = function_type
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the model.
        self.model_type = model_type
        # How the instance is created. Valid values:
        # 
        # *   user: The instance is created by user.
        # *   builtin: The instance is created by system.
        self.source = source
        # The state of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status
        # The parameters that are used.
        self.usage_parameters = usage_parameters
        # The ID of the version.
        self.version_id = version_id

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belongs is not None:
            result['Belongs'] = self.belongs.to_map()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.description is not None:
            result['Description'] = self.description
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Belongs') is not None:
            temp_model = ListFunctionInstancesResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m['Belongs'])
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = ListFunctionInstancesResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = ListFunctionInstancesResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListFunctionInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListFunctionInstancesResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code. If no error occurs, the parameter is left empty.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message. If no error occurs, the parameter is left empty.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The information about the instances.
        self.result = result
        # The status of the request.
        self.status = status
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListFunctionInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionResourcesRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        # 
        # Valid values:
        # 
        # *   item
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   user
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFunctionResourcesResponseBodyResultDataGeneratorsInput(TeaModel):
    def __init__(
        self,
        features: List[ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class ListFunctionResourcesResponseBodyResultDataGenerators(TeaModel):
    def __init__(
        self,
        generator: str = None,
        input: ListFunctionResourcesResponseBodyResultDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = ListFunctionResourcesResponseBodyResultDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListFunctionResourcesResponseBodyResultData(TeaModel):
    def __init__(
        self,
        content: str = None,
        generators: List[ListFunctionResourcesResponseBodyResultDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = ListFunctionResourcesResponseBodyResultDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class ListFunctionResourcesResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data: ListFunctionResourcesResponseBodyResultData = None,
        description: str = None,
        function_name: str = None,
        modify_time: int = None,
        referenced_instances: List[str] = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The time when the resource was created. Unit: milliseconds.
        self.create_time = create_time
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description
        # The name of the feature.
        self.function_name = function_name
        # The time when the resource was modified. Unit: milliseconds.
        self.modify_time = modify_time
        # The algorithm instances that are referenced.
        self.referenced_instances = referenced_instances
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.referenced_instances is not None:
            result['ReferencedInstances'] = self.referenced_instances
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = ListFunctionResourcesResponseBodyResultData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ReferencedInstances') is not None:
            self.referenced_instances = m.get('ReferencedInstances')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListFunctionResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        result: List[ListFunctionResourcesResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code returned. If no error occurs, this value is empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The amount of time consumed for the request. Unit: milliseconds.
        self.latency = latency
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The results returned.
        self.result = result
        # The status of the request. Valid values: OK and FAIL.
        self.status = status
        # The total number of records that meet the requirements.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListFunctionResourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionTasksRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The end time is less than the specified time. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 1.
        self.page_size = page_size
        # The start time is greater than the specified time. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListFunctionTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        extend_info: str = None,
        function_name: str = None,
        generation: str = None,
        progress: int = None,
        run_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The timestamp that indicates the end time. Unit: milliseconds. 0 indicates that the task has not ended.
        self.end_time = end_time
        # The value is a JSON string. It includes model evaluation information and training error information.
        self.extend_info = extend_info
        # The name of the feature.
        self.function_name = function_name
        # The number of iterations.
        self.generation = generation
        # The progress. 90 indicates 90%.
        self.progress = progress
        # The ID of the task.
        self.run_id = run_id
        # The timestamp that indicates the start time. Unit: milliseconds.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListFunctionTasksResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The status of the request.
        self.status = status
        # The total number of records that meet the requirements.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListFunctionTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionariesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        types: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListInterventionDictionariesResponseBodyResult(TeaModel):
    def __init__(
        self,
        analyzer: str = None,
        created: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
        updated: int = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the intervention dictionary was created.
        self.created = created
        # The ID of the intervention dictionary.
        self.id = id
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type
        # The time when the intervention dictionary was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListInterventionDictionariesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListInterventionDictionariesResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each intervention dictionary.
        # 
        # For more information, see [InterventionDictionary](https://help.aliyun.com/document_detail/173608.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionariesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterventionDictionariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        word: str = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Default value: 10.
        self.page_size = page_size
        # The intervention entry.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListInterventionDictionaryEntriesResponseBodyResultTokens(TeaModel):
    def __init__(
        self,
        order: int = None,
        tag: str = None,
        tag_label: str = None,
        token: str = None,
    ):
        # The sequence number.
        self.order = order
        # The internal name of the identified entity type. Valid values:
        # 
        # *   brand
        # *   category
        # *   material
        # *   element
        # *   style
        # *   color
        # *   function
        # *   scenario
        # *   people
        # *   season
        # *   model
        # *   region
        # *   name
        # *   adjective
        # *   category-modifier
        # *   size
        # *   quality
        # *   suit
        # *   new-release
        # *   series
        # *   marketing
        # *   entertainment
        # *   organization
        # *   movie
        # *   game
        # *   number
        # *   unit
        # *   common
        # *   new-word
        # *   proper-noun
        # *   symbol
        # *   prefix
        # *   suffix
        # *   gift
        # *   negative
        # *   agent
        self.tag = tag
        # The description of the internal name of the identified entity type.
        self.tag_label = tag_label
        # The entity.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ListInterventionDictionaryEntriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        created: int = None,
        relevance: Dict[str, Any] = None,
        status: str = None,
        tokens: List[ListInterventionDictionaryEntriesResponseBodyResultTokens] = None,
        updated: int = None,
        word: str = None,
    ):
        # The command. Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd
        # The timestamp when the intervention entry was created.
        self.created = created
        # The content of an intervention entry for category prediction. The field value consists of key-value pairs. The key in a key-value pair indicates the ID of the category. The value in a key-value pair indicates the relevance to the category. A value of 0 indicates irrelevant. A value of 1 indicates slightly relevant. A value of 2 indicates relevant. Example: {"2":1, "100":0}
        self.relevance = relevance
        # The status of the intervention entry. Valid value:
        # 
        # *   ACTIVE: The intervention entry takes effect.
        self.status = status
        # The content of the intervention entry for term weight analysis.
        self.tokens = tokens
        # The timestamp when the intervention entry was last updated.
        self.updated = updated
        # The intervention entry.
        self.word = word

    def validate(self):
        if self.tokens:
            for k in self.tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.created is not None:
            result['created'] = self.created
        if self.relevance is not None:
            result['relevance'] = self.relevance
        if self.status is not None:
            result['status'] = self.status
        result['tokens'] = []
        if self.tokens is not None:
            for k in self.tokens:
                result['tokens'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('relevance') is not None:
            self.relevance = m.get('relevance')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tokens = []
        if m.get('tokens') is not None:
            for k in m.get('tokens'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResultTokens()
                self.tokens.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListInterventionDictionaryEntriesResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about intervention entries.
        # 
        # For more information, see [InterventionDictionaryEntry](https://help.aliyun.com/document_detail/173606.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterventionDictionaryEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryNerResultsRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
    ):
        # Query keywords.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class ListInterventionDictionaryNerResultsResponseBodyResult(TeaModel):
    def __init__(
        self,
        order: int = None,
        tag: str = None,
        tag_label: str = None,
        token: str = None,
    ):
        # The sequence number.
        self.order = order
        # The internal name of the identified entity type. Valid values:
        # 
        # *   brand
        # *   category
        # *   material
        # *   element
        # *   style
        # *   color
        # *   function
        # *   scenario
        # *   people
        # *   season
        # *   model
        # *   region
        # *   name
        # *   adjective
        # *   category-modifier
        # *   size
        # *   quality
        # *   suit
        # *   new-release
        # *   series
        # *   marketing
        # *   entertainment
        # *   organization
        # *   movie
        # *   game
        # *   number
        # *   unit
        # *   common
        # *   new-word
        # *   proper-noun
        # *   symbol
        # *   prefix
        # *   suffix
        # *   gift
        # *   negative
        # *   agent
        self.tag = tag
        # The description of the internal name of the identified entity type.
        self.tag_label = tag_label
        # The entity.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ListInterventionDictionaryNerResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListInterventionDictionaryNerResultsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The NER result.
        # 
        # For more information, see [InterventionDictionaryEntry](https://help.aliyun.com/document_detail/173606.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryNerResultsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInterventionDictionaryNerResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterventionDictionaryNerResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryNerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryRelatedEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each application and each query analysis rule. If no query analysis rule references the intervention dictionary, the value of the result parameter is an empty list.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListInterventionDictionaryRelatedEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterventionDictionaryRelatedEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryRelatedEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProceedingsRequest(TeaModel):
    def __init__(
        self,
        filter_finished: bool = None,
    ):
        # Specifies whether the filtering is complete.
        self.filter_finished = filter_finished

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_finished is not None:
            result['filterFinished'] = self.filter_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFinished') is not None:
            self.filter_finished = m.get('filterFinished')
        return self


class ListProceedingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProceedingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProceedingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProceedingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorAnalyzerResultsRequest(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        # The text to be tested.
        # 
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class ListQueryProcessorAnalyzerResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data returned.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListQueryProcessorAnalyzerResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueryProcessorAnalyzerResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorAnalyzerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorNersRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # The type of the industry.
        # 
        # *   ECOMMERCE
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ListQueryProcessorNersResponseBodyResult(TeaModel):
    def __init__(
        self,
        label: str = None,
        order: int = None,
        priority: str = None,
        tag: str = None,
    ):
        # The name of the entity type.
        self.label = label
        # The priority of an entity type among entity types that have the same priority level. A smaller value indicates a higher priority. Default value: 0.
        self.order = order
        # The priority level of the entity type. Valid values:
        # 
        # *   HIGH
        # *   MIDDLE
        # *   LOW
        self.priority = priority
        # The internal name of the entity type.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.order is not None:
            result['order'] = self.order
        if self.priority is not None:
            result['priority'] = self.priority
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class ListQueryProcessorNersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListQueryProcessorNersResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The priority settings of entity types.
        # 
        # For more information, see [Priority settings of entity types](https://help.aliyun.com/document_detail/173616.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorNersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListQueryProcessorNersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueryProcessorNersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorNersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorsRequest(TeaModel):
    def __init__(
        self,
        is_active: int = None,
    ):
        # The scope of query analysis rules to be queried. Default value: 0. Valid values:
        # 
        # *   0: queries all query analysis rules.
        # *   1: queries the default query analysis rules.
        # *   2: queries the query analysis rules that are not the default rules.
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_active is not None:
            result['isActive'] = self.is_active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')
        return self


class ListQueryProcessorsResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
    ):
        # Indicates whether the query analysis rule is a default rule.
        self.active = active
        # The time when the query analysis rule was created.
        self.created = created
        # The type of the industry to which the query analysis rule is applied. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The indexes to which the query analysis rule is applied.
        self.indexes = indexes
        # The name of the query analysis rule.
        self.name = name
        # The features that are used in the query analysis rule.
        self.processors = processors
        # The time when the query analysis rule was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListQueryProcessorsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListQueryProcessorsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the query analysis rule.
        # 
        # For more information, see [QueryProcessor](https://help.aliyun.com/document_detail/170014.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListQueryProcessorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueryProcessorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaReviewTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListQuotaReviewTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_group_name: str = None,
        app_group_type: str = None,
        approved: bool = None,
        available: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        memo: str = None,
        new_compute_resource: int = None,
        new_soc_size: int = None,
        new_spec: str = None,
        old_compute_resource: int = None,
        old_doc_size: int = None,
        old_spec: str = None,
        pending: bool = None,
    ):
        # The application ID.
        self.app_group_id = app_group_id
        # The application name.
        self.app_group_name = app_group_name
        # The application type.
        self.app_group_type = app_group_type
        # Indicates whether the ticket is approved.
        self.approved = approved
        # Indicates whether the application is available.
        self.available = available
        # The time when the ticket was created.
        self.gmt_create = gmt_create
        # The time when the ticket was last updated.
        self.gmt_modified = gmt_modified
        # The ticket ID.
        self.id = id
        # The remarks.
        self.memo = memo
        # The computing resource quota that is applied for.
        self.new_compute_resource = new_compute_resource
        # The storage capacity quota that is applied for.
        self.new_soc_size = new_soc_size
        # The application specifications that are applied for.
        self.new_spec = new_spec
        # The original quota of computing resources.
        self.old_compute_resource = old_compute_resource
        # The original quota of storage capacity.
        self.old_doc_size = old_doc_size
        # The original specifications of the application.
        self.old_spec = old_spec
        # Indicates whether the ticket is pending.
        self.pending = pending

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        if self.app_group_name is not None:
            result['appGroupName'] = self.app_group_name
        if self.app_group_type is not None:
            result['appGroupType'] = self.app_group_type
        if self.approved is not None:
            result['approved'] = self.approved
        if self.available is not None:
            result['available'] = self.available
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.memo is not None:
            result['memo'] = self.memo
        if self.new_compute_resource is not None:
            result['newComputeResource'] = self.new_compute_resource
        if self.new_soc_size is not None:
            result['newSocSize'] = self.new_soc_size
        if self.new_spec is not None:
            result['newSpec'] = self.new_spec
        if self.old_compute_resource is not None:
            result['oldComputeResource'] = self.old_compute_resource
        if self.old_doc_size is not None:
            result['oldDocSize'] = self.old_doc_size
        if self.old_spec is not None:
            result['oldSpec'] = self.old_spec
        if self.pending is not None:
            result['pending'] = self.pending
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        if m.get('appGroupName') is not None:
            self.app_group_name = m.get('appGroupName')
        if m.get('appGroupType') is not None:
            self.app_group_type = m.get('appGroupType')
        if m.get('approved') is not None:
            self.approved = m.get('approved')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('newComputeResource') is not None:
            self.new_compute_resource = m.get('newComputeResource')
        if m.get('newSocSize') is not None:
            self.new_soc_size = m.get('newSocSize')
        if m.get('newSpec') is not None:
            self.new_spec = m.get('newSpec')
        if m.get('oldComputeResource') is not None:
            self.old_compute_resource = m.get('oldComputeResource')
        if m.get('oldDocSize') is not None:
            self.old_doc_size = m.get('oldDocSize')
        if m.get('oldSpec') is not None:
            self.old_spec = m.get('oldSpec')
        if m.get('pending') is not None:
            self.pending = m.get('pending')
        return self


class ListQuotaReviewTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListQuotaReviewTasksResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the tickets. For more information, see [QuotaReviewTask](https://help.aliyun.com/document_detail/173609.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQuotaReviewTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListQuotaReviewTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaReviewTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaReviewTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The scheduled task type. Valid values:
        # 
        # *   wipe: data cleaning.
        # *   fork: reindexing.
        # *   check-status: application status check.
        # *   index: reindexing.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListScheduledTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListScheduledTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchStrategiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSearchStrategiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSearchStrategiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSearchStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecondRanksResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        id: str = None,
        is_default: str = None,
        is_sys: str = None,
        meta: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The time when the expression was created.
        self.created = created
        # The description of the expression.
        self.description = description
        # The ID of the expression. This parameter appears only in the response.
        self.id = id
        # Indicates whether the expression is the default one. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default
        # Indicates whether the expression is a system expression. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_sys = is_sys
        # The content of the fine sort expression.
        # 
        # You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta
        # The name of the expression.
        self.name = name
        # The time when the expression was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListSecondRanksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListSecondRanksResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each fine sort expression.
        # 
        # For more information, see [SecondRank](https://help.aliyun.com/document_detail/170008.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSecondRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSecondRanksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecondRanksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSecondRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryCategoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        analyze_status: str = None,
        end: int = None,
        start: int = None,
    ):
        # The status of the analysis. Valid values:
        # 
        # *   PENDING: preparing
        # *   SUCCESS: succeeded
        # *   RUNNING: running
        # *   FAILED: failed
        # *   N/A: unknown
        self.analyze_status = analyze_status
        # The timestamp that indicates the end of the time range to query.
        self.end = end
        # The timestamp that indicates the beginning of the time range to query.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyze_status is not None:
            result['analyzeStatus'] = self.analyze_status
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzeStatus') is not None:
            self.analyze_status = m.get('analyzeStatus')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListSlowQueryCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListSlowQueryCategoriesResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSlowQueryCategoriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSlowQueryCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSlowQueryCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlowQueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryQueriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_query: str = None,
        end: int = None,
        index: int = None,
        start: int = None,
    ):
        # The content of the optimization suggestion for the query.
        self.app_query = app_query
        # The end of the time range that was queried.
        self.end = end
        # The ID of the optimization suggestion.
        self.index = index
        # The beginning of the time range that was queried.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_query is not None:
            result['appQuery'] = self.app_query
        if self.end is not None:
            result['end'] = self.end
        if self.index is not None:
            result['index'] = self.index
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appQuery') is not None:
            self.app_query = m.get('appQuery')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListSlowQueryQueriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListSlowQueryQueriesResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSlowQueryQueriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSlowQueryQueriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSlowQueryQueriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlowQueryQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortExpressionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The timestamp when the sort expression was created.
        self.created = created
        # The description of the sort expression.
        self.description = description
        # The name of the sort expression.
        self.name = name
        # The timestamp when the sort expression was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListSortExpressionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListSortExpressionsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort or fine sort expressions that are returned.
        # 
        # For more information, see [FirstRank](https://help.aliyun.com/document_detail/170007.html) and [SecondRank](https://help.aliyun.com/document_detail/170008.html).
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortExpressionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSortExpressionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSortExpressionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSortExpressionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortScriptsResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        scope: str = None,
        script_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the script was created.
        self.create_time = create_time
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The sort phase to which the script applies.
        self.scope = scope
        # The name of the script.
        self.script_name = script_name
        # The status of the script. Valid values:
        # 
        # *   configurable: The script is created, but no script files are uploaded.
        # *   not compiled: The script is not compiled.
        # *   compile failed: The compilation of the script failed.
        # *   compile successful: The script is compiled.
        # *   released: The script is published.
        self.status = status
        # The type of the script.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSortScriptsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListSortScriptsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The scripts.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortScriptsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSortScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSortScriptsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSortScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticLogsRequest(TeaModel):
    def __init__(
        self,
        columns: str = None,
        distinct: bool = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        start_time: int = None,
        stop_time: int = None,
    ):
        # The fields to query. Format: columns=wordsTopPv.
        # 
        # For more information, see [Metrics in statistical reports](https://help.aliyun.com/document_detail/187665.html).
        self.columns = columns
        # Specifies whether to use the distinct clause.
        self.distinct = distinct
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The content of the query clause.
        self.query = query
        # The content of the sort clause.
        self.sort_by = sort_by
        # The beginning of the time range to query. The default value is the timestamp of 00:00:00 on the current day.
        self.start_time = start_time
        # The end of the time range to query. The default value is the timestamp of 24:00:00 on the current day.
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.distinct is not None:
            result['distinct'] = self.distinct
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('distinct') is not None:
            self.distinct = m.get('distinct')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        return self


class ListStatisticLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result. For more information, see
        # 
        # *   [Parameters of hotwords rankings](https://help.aliyun.com/document_detail/421248.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatisticLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatisticLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticReportRequest(TeaModel):
    def __init__(
        self,
        columns: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        start_time: int = None,
    ):
        # pv,uv
        self.columns = columns
        # 1582646399
        self.end_time = end_time
        # 1
        self.page_number = page_number
        # 10
        self.page_size = page_size
        # bizType:test,sceneTag:myTag
        self.query = query
        # 1582214400
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListStatisticReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The queried reports. Valid values:
        # 
        # For more information about the metrics in data quality reports, see the Upload behavioral data section of [Data collection 2.0](https://help.aliyun.com/document_detail/131547.html).
        # 
        # For more information about the metrics in application and A/B test reports, see the Core metrics section of [Metrics of statistical reports](https://help.aliyun.com/document_detail/187654.html).
        # 
        # For more information about the metrics in query analysis reports, see the Query analysis metrics section of [Metrics of statistical reports](https://help.aliyun.com/document_detail/187654.html).
        self.result = result
        # The total number of the queried reports.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatisticReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatisticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. You can specify a maximum number of 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. You can specify a maximum number of 20 tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListTagResourcesResponseBodyResult(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        result: List[ListTagResourcesResponseBodyResult] = None,
    ):
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The resources.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTagResourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzerEntriesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        word: str = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The key to be used to query entries.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The entries of the custom analyzer. For more information, see [UserAnalyzerEntry](https://www.alibabacloud.com/help/en/open-search/industry-algorithm-edition/useranalyzerentry).
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListUserAnalyzerEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserAnalyzerEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUserAnalyzersResponseBodyResultDicts(TeaModel):
    def __init__(
        self,
        available: bool = None,
        created: int = None,
        entries_count: int = None,
        entries_limit: int = None,
        id: str = None,
        type: str = None,
        updated: int = None,
    ):
        # Indicates whether the application is available.
        self.available = available
        # The timestamp when the application was created.
        self.created = created
        # The number of intervention entries.
        self.entries_count = entries_count
        # The maximum number of intervention entries that can be created in the dictionary.
        self.entries_limit = entries_limit
        # The ID of the dictionary.
        self.id = id
        # The type. Valid value:
        # 
        # *   segment
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['available'] = self.available
        if self.created is not None:
            result['created'] = self.created
        if self.entries_count is not None:
            result['entriesCount'] = self.entries_count
        if self.entries_limit is not None:
            result['entriesLimit'] = self.entries_limit
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('entriesCount') is not None:
            self.entries_count = m.get('entriesCount')
        if m.get('entriesLimit') is not None:
            self.entries_limit = m.get('entriesLimit')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListUserAnalyzersResponseBodyResult(TeaModel):
    def __init__(
        self,
        available: bool = None,
        business: str = None,
        created: int = None,
        dicts: List[ListUserAnalyzersResponseBodyResultDicts] = None,
        id: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the application is available.
        self.available = available
        # The basic analyzer. Valid values:
        # 
        # *   chn_standard: [a common analyzer in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   chn_scene_name: an analyzer for person names in Chinese
        # *   chn_ecommerce: [an analyzer for E-commerce in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   chn_it_content: [an analyzer for IT content in Chinese](https://help.aliyun.com/document_detail/179424.html)
        # *   en_min: a small-granularity analyzer in English
        # *   th_standard: a common analyzer in Thai
        # *   th_ecommerce: an analyzer for E-commerce in Thai
        # *   vn_standard: a common analyzer in Vietnamese
        # *   chn_community_it: an analyzer for IT community content in Chinese
        # *   chn_ecommerce_general: a common analyzer for the E-commerce industry in Chinese
        # *   chn_esports_general: a common analyzer for the gaming industry in Chinese
        # *   chn_edu_question: an analyzer for question search of the education industry in Chinese
        self.business = business
        # The timestamp when the application was created.
        self.created = created
        # The dictionaries that are used by the custom analyzer.
        # 
        # For more information, see [UserDict](https://help.aliyun.com/document_detail/178933.html).
        self.dicts = dicts
        # The ID of the custom analyzer.
        self.id = id
        # The name of the custom analyzer.
        self.name = name
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.dicts:
            for k in self.dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['available'] = self.available
        if self.business is not None:
            result['business'] = self.business
        if self.created is not None:
            result['created'] = self.created
        result['dicts'] = []
        if self.dicts is not None:
            for k in self.dicts:
                result['dicts'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('business') is not None:
            self.business = m.get('business')
        if m.get('created') is not None:
            self.created = m.get('created')
        self.dicts = []
        if m.get('dicts') is not None:
            for k in m.get('dicts'):
                temp_model = ListUserAnalyzersResponseBodyResultDicts()
                self.dicts.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListUserAnalyzersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListUserAnalyzersResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The custom analyzer.
        # 
        # For more information, see [UserAnalyzer](https://help.aliyun.com/document_detail/178934.html).
        self.result = result
        # The total number.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUserAnalyzersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListUserAnalyzersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserAnalyzersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupRequest(TeaModel):
    def __init__(
        self,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        resource_group_id: str = None,
        dry_run: bool = None,
    ):
        # The online version of the application.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The type of the industry. Valid values:
        # 
        # *   general: general.
        # *   ecommerce: e-commerce.
        # *   education: education.
        # *   esports: electronic sports.
        # *   community: content community.
        self.domain = domain
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # Specifies whether to verify the application before modification. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic.
        # *   opensearch.share.common: shared general-purpose.
        # *   opensearch.share.compute: shared computing.
        # *   opensearch.share.storage: shared storage.
        # *   opensearch.private.common: exclusive general-purpose.
        # *   opensearch.private.compute: exclusive computing.
        # *   opensearch.private.storage: exclusive storage.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ModifyAppGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        engine_type: str = None,
        expire_on: str = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        produced: int = None,
        project_id: str = None,
        quota: ModifyAppGroupResponseBodyResultQuota = None,
        resource_group_id: str = None,
        status: str = None,
        switched_time: int = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billable item. Valid values:
        # 
        # *   1: computing resources.
        # *   2: QPS.
        self.charging_way = charging_way
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The type of the industry. Valid values:
        # 
        # *   GENERAL: general.
        # *   ECOMMERCE: e-commerce.
        # *   IT_CONTENT: IT content.
        self.domain = domain
        self.engine_type = engine_type
        # The time when the application expired.
        self.expire_on = expire_on
        # The approval status of the quotas. Valid values:
        # 
        # *   0: normal.
        # *   1: being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock status. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # The name of the application.
        self.name = name
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application.
        self.quota = quota
        self.resource_group_id = resource_group_id
        # The state of the application. Valid values:
        # 
        # *   producing: being produced.
        # *   review_pending: being approved.
        # *   config_pending: to be configured.
        # *   normal: normal.
        # *   frozen: frozen.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The type of the application. Valid values:
        # 
        # *   standard: a standard edition application.
        # *   advance: an advanced edition application of an old version. New versions are not supported for this edition.
        # *   enhanced: an advanced edition application of a new version.
        self.type = type
        # The timestamp when the application was last modified.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyAppGroupResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned data.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupQuotaRequest(TeaModel):
    def __init__(
        self,
        body: Quota = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to verify the application before modification. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Quota()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyAppGroupQuotaResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ModifyAppGroupQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        engine_type: str = None,
        expire_on: str = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        name: str = None,
        produced: int = None,
        project_id: str = None,
        quota: ModifyAppGroupQuotaResponseBodyResultQuota = None,
        resource_group_id: str = None,
        status: str = None,
        switched_time: int = None,
        type: str = None,
        updated: int = None,
    ):
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        self.engine_type = engine_type
        # The expiration time.
        self.expire_on = expire_on
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The ID of the application.
        self.id = id
        # The ID of the instance.
        self.instance_id = instance_id
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # The name of the application.
        self.name = name
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The information about the quotas of the application.
        self.quota = quota
        self.resource_group_id = resource_group_id
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type
        # The timestamp when the application was last updated.
        self.updated = updated

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.name is not None:
            result['name'] = self.name
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyAppGroupQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyAppGroupQuotaResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the application.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyAppGroupQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppGroupQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirstRankRequest(TeaModel):
    def __init__(
        self,
        body: FirstRank = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether the request is a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = FirstRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression.
        self.arg = arg
        # The attribute, feature function, or field to be searched for.
        self.attribute = attribute
        # The weight. Valid values: -100000 to 100000. The value cannot be 0.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ModifyFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: List[ModifyFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The description of the rough sort expression.
        self.description = description
        # The information about the expression.
        self.meta = meta
        # The name of the expression.
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ModifyFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyFirstRankResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQueryProcessorRequest(TeaModel):
    def __init__(
        self,
        body: Any = None,
        dry_run: bool = None,
    ):
        # The request parameters.
        self.body = body
        # Specifies whether the request is a dry run.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyQueryProcessorResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
    ):
        # Indicates whether the query analysis rule is a default rule.
        self.active = active
        # The time when the rule was created.
        self.created = created
        # The type of the industry to which the query analysis rule is applied. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The indexes to which the query analysis rule is applied.
        self.indexes = indexes
        # The name of the query analysis rule.
        self.name = name
        # The analysis rule.
        self.processors = processors
        # The time when the rule was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyQueryProcessorResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the query analysis rule.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        body: Any = None,
    ):
        # The request parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the scheduled task.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecondRankRequest(TeaModel):
    def __init__(
        self,
        body: SecondRank = None,
        dry_run: bool = None,
    ):
        # The request parameters.
        self.body = body
        # Specifies whether the request is a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SecondRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifySecondRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        id: str = None,
        is_default: str = None,
        is_sys: str = None,
        meta: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The time when the expression was created.
        self.created = created
        # The description of the expression.
        self.description = description
        # The expression ID. This parameter is displayed only in the response.
        self.id = id
        # Indicates whether the expression is the default one. This parameter is displayed only in the response. Valid values:
        # 
        # *   true: the expression is the default one.
        # *   false: the expression is not the default one.
        self.is_default = is_default
        # Indicates whether the expression is a system expression. This parameter is displayed only in the response. Valid values:
        # 
        # *   true: The expression is a system expression.
        # *   false:The expression is not a system expression
        self.is_sys = is_sys
        # The content of the fine sort expression. You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta
        # The expression name.
        self.name = name
        # The time when the expression was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifySecondRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifySecondRankResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the fine sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifySecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifySecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecondRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(
        self,
        body: List[Dict[str, Any]] = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to check the validity of input parameters. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**: checks only the validity of input parameters.
        # *   **false**: checks the validity of input parameters and creates an attribution configuration.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class PushInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushInterventionDictionaryEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushUserAnalyzerEntriesRequestEntries(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        key: str = None,
        split_enabled: bool = None,
        value: str = None,
    ):
        # The operation to be performed on the entries.
        # 
        # Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd
        # The key to be used to query entries.
        self.key = key
        # Specifies whether to further analyze the terms that are generated after the search query is analyzed.
        # 
        # Default value: true.
        self.split_enabled = split_enabled
        # The analysis result.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.key is not None:
            result['key'] = self.key
        if self.split_enabled is not None:
            result['splitEnabled'] = self.split_enabled
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('splitEnabled') is not None:
            self.split_enabled = m.get('splitEnabled')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PushUserAnalyzerEntriesRequest(TeaModel):
    def __init__(
        self,
        entries: List[PushUserAnalyzerEntriesRequestEntries] = None,
        dry_run: bool = None,
    ):
        # The entries of the custom analyzer.
        self.entries = entries
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['entries'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('entries') is not None:
            for k in m.get('entries'):
                temp_model = PushUserAnalyzerEntriesRequestEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class PushUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result returned.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushUserAnalyzerEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushUserAnalyzerEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReleaseSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[int] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The return result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[int] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataCollectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # —
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveDataCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveDataCollectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression.
        # 
        # For more information, see Rough sort functions.
        self.arg = arg
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see Rough sort functions.
        self.attribute = attribute
        # The weight.
        # 
        # Valid values: [-100000,100000] (excluding 0).
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RemoveFirstRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: List[RemoveFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The description of the expression.
        self.description = description
        # The content of the expression.
        self.meta = meta
        # The name of the expression.
        self.name = name

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = RemoveFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RemoveFirstRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RemoveFirstRankResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the rough sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RemoveFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class RemoveFirstRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveFirstRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(
        self,
        analyzer: str = None,
        created: str = None,
        name: str = None,
        type: str = None,
        updated: str = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the intervention dictionary was created.
        self.created = created
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type
        # The time when the intervention dictionary was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class RemoveInterventionDictionaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RemoveInterventionDictionaryResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the intervention dictionary.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RemoveInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class RemoveInterventionDictionaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveInterventionDictionaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveQueryProcessorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveQueryProcessorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveQueryProcessorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[int] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSearchStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveSearchStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSearchStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSecondRankResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveSecondRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSecondRankResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppGroupRequest(TeaModel):
    def __init__(
        self,
        body: PrepayOrderInfo = None,
        client_token: str = None,
    ):
        # The renewal request body.
        self.body = body
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PrepayOrderInfo()
            self.body = temp_model.from_map(m['body'])
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewAppGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the application was renewed.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RenewAppGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAppGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResultQuota(TeaModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The number of computing resources configured.
        self.compute_resource = compute_resource
        # The storage capacity.
        self.doc_size = doc_size
        # The specifications configured.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        expire_on: str = None,
        first_rank_algo_deployment_id: int = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        locked_by_expiration: int = None,
        name: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        processing_order_id: str = None,
        produced: int = None,
        project_id: str = None,
        quota: ReplaceAppGroupCommodityCodeResponseBodyResultQuota = None,
        second_rank_algo_deployment_id: int = None,
        status: str = None,
        switched_time: int = None,
        type: str = None,
        updated: int = None,
        versions: List[str] = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billing type. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The expiration time.
        self.expire_on = expire_on
        # The ID of the rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The approval status is normal.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # Indicates whether the instance is automatically locked after it expires. Valid values:
        # 
        # *   0: The instance is not automatically locked after it expires.
        # *   1: The instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration
        # The name of the order.
        self.name = name
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        # The ID of the order that is in progress.
        self.processing_order_id = processing_order_id
        # Indicates whether the order is produced.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The configuration information.
        self.quota = quota
        # The ID of the fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        # The status of the application.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The type of the application.
        self.type = type
        # The timestamp when the application was updated.
        self.updated = updated
        # The versions.
        self.versions = versions

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        if self.versions is not None:
            result['versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        return self


class ReplaceAppGroupCommodityCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ReplaceAppGroupCommodityCodeResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ReplaceAppGroupCommodityCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplaceAppGroupCommodityCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSortScriptFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        version: int = None,
    ):
        # The script content that is encoded in the Base64 format.
        self.content = content
        # The version number of the script content.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class SaveSortScriptFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SaveSortScriptFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSortScriptFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSlowQueryAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # N/A
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StartSlowQueryAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSlowQueryAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartSlowQueryAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. You can specify a maximum number of 20 tags.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindESUserAnalyzerRequest(TeaModel):
    def __init__(
        self,
        body: Any = None,
    ):
        # The request parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UnbindESUserAnalyzerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The custom analyzer.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UnbindESUserAnalyzerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindESUserAnalyzerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data returned.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UnbindEsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindEsInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified one or more resources. This parameter takes effect only if the tagKey parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all
        # The resource IDs. You can specify a maximum number of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags. You can specify a maximum number of 20 keys.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        # Specifies whether to remove all tags from the specified one or more resources. This parameter takes effect only if the tagKey parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all
        # The resource IDs. You can specify a maximum number of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags. You can specify a maximum number of 20 keys.
        self.tag_key_shrink = tag_key_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['tagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key_shrink = m.get('tagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        tequest_id: str = None,
    ):
        # The ID of the request.
        self.tequest_id = tequest_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tequest_id is not None:
            result['tequestId'] = self.tequest_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tequestId') is not None:
            self.tequest_id = m.get('tequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestExperimentRequest(TeaModel):
    def __init__(
        self,
        body: ABTestExperiment = None,
        dry_run: bool = None,
    ):
        # The request body. For more information, see [ABTestExperiment](https://help.aliyun.com/document_detail/173617.html).
        self.body = body
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. No endpoint is created. The system checks whether your AccessKey is valid, whether Resource Access Management (RAM) users are authorized, and whether the required parameters are set.
        # *   false (default): creates an endpoint immediately.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestExperiment()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the test was created.
        self.created = created
        # The test ID.
        self.id = id
        # The alias of the test.
        self.name = name
        # Indicates whether the test is in effect. Valid values:
        # 
        # *   true
        # *   false
        self.online = online
        # The test parameters.
        self.params = params
        # The percentage of traffic that is routed to the test. Valid values: [0,100]
        self.traffic = traffic
        # The time when the test was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateABTestExperimentResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the test.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABTestExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestFixedFlowDividersRequest(TeaModel):
    def __init__(
        self,
        body: List[str] = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateABTestFixedFlowDividersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABTestFixedFlowDividersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestGroupRequest(TeaModel):
    def __init__(
        self,
        body: ABTestGroup = None,
        dry_run: bool = None,
    ):
        # The request body. For more information, see [ABTestGroup](https://help.aliyun.com/document_detail/178935.html).
        self.body = body
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. No endpoint is created. The system checks whether your AccessKey is valid, whether Resource Access Management (RAM) users are authorized, and whether the required parameters are set.
        # *   false (default): creates an endpoint immediately.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestGroup()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
    ):
        # The time when the test group was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The alias of the test group.
        self.name = name
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test group was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateABTestGroupResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the test group.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABTestGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestSceneRequest(TeaModel):
    def __init__(
        self,
        body: ABTestScene = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestScene()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: Dict[str, Any] = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the test scenario was created.
        self.created = created
        # The ID of the test scenario.
        self.id = id
        # The name of the test scenario.
        self.name = name
        # The status of the test. Valid values:
        # 
        # *   true: The test is started.
        # *   false: The test is stopped.
        self.online = online
        # The parameters of the A/B test.
        self.params = params
        # The percentage of traffic that is allocated to the A/B test. Valid values: 0 to 100.
        self.traffic = traffic
        # The time when the test scenario was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateABTestSceneResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the test scenario. For more information, see [ABTestScene](https://help.aliyun.com/document_detail/173618.html).
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateABTestSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFetchFieldsRequest(TeaModel):
    def __init__(
        self,
        body: List[str] = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # true
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateFetchFieldsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateFetchFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFetchFieldsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFetchFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionDefaultInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The name of the instance.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self


class UpdateFunctionDefaultInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFunctionDefaultInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionDefaultInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateFunctionInstanceRequestUsageParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateFunctionInstanceRequest(TeaModel):
    def __init__(
        self,
        create_parameters: List[UpdateFunctionInstanceRequestCreateParameters] = None,
        cron: str = None,
        description: str = None,
        usage_parameters: List[UpdateFunctionInstanceRequestUsageParameters] = None,
    ):
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The cron expression used to schedule periodic training, in the format of (Minutes Hours DayofMonth Month DayofWeek). The default value is empty, which indicates that no periodic training is performed. DayofWeek 0 indicates Sunday.
        self.cron = cron
        # The description of the instance.
        self.description = description
        # The parameters that are used.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['createParameters'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        result['usageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['usageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k in m.get('createParameters'):
                temp_model = UpdateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k in m.get('usageParameters'):
                temp_model = UpdateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class UpdateFunctionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed for the request, in milliseconds.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the request. Valid values:
        # 
        # *       OK: The request was successful.
        # *       FAIL: The request failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFunctionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionResourceRequestDataGeneratorsInputFeatures(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFunctionResourceRequestDataGeneratorsInput(TeaModel):
    def __init__(
        self,
        features: List[UpdateFunctionResourceRequestDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = UpdateFunctionResourceRequestDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class UpdateFunctionResourceRequestDataGenerators(TeaModel):
    def __init__(
        self,
        generator: str = None,
        input: UpdateFunctionResourceRequestDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = UpdateFunctionResourceRequestDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class UpdateFunctionResourceRequestData(TeaModel):
    def __init__(
        self,
        content: str = None,
        generators: List[UpdateFunctionResourceRequestDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = UpdateFunctionResourceRequestDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class UpdateFunctionResourceRequest(TeaModel):
    def __init__(
        self,
        data: UpdateFunctionResourceRequestData = None,
        description: str = None,
    ):
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateFunctionResourceRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateFunctionResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: float = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code
        # The HTTP status code returned.
        self.http_code = http_code
        # The time consumed for the request. Unit: milliseconds.
        self.latency = latency
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFunctionResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSearchStrategyRequest(TeaModel):
    def __init__(
        self,
        body: SearchStrategy = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SearchStrategy()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSearchStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSearchStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSearchStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSortScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSortScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSortScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSummariesRequestBody(TeaModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: int = None,
    ):
        # The HTML tag that is used to highlight terms in red.
        self.element = element
        # The connector that is used to connect segments.
        self.ellipsis = ellipsis
        # The field.
        self.field = field
        # The length of a segment.
        self.len = len
        # The number of segments.
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class UpdateSummariesRequest(TeaModel):
    def __init__(
        self,
        body: List[UpdateSummariesRequestBody] = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether the request is a dry run.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateSummariesRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateSummariesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateSummariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSummariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSummariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateDataSourcesRequest(TeaModel):
    def __init__(
        self,
        body: DataSource = None,
    ):
        # The request parameter. For more information, see [DataSource](https://help.aliyun.com/document_detail/170005.html).
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DataSource()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateDataSourcesResponseBodyResultDataSource(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        table_name: str = None,
        type: str = None,
    ):
        # The parameters of the data source.
        self.parameters = parameters
        # The name of the table.
        self.table_name = table_name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ValidateDataSourcesResponseBodyResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_source: ValidateDataSourcesResponseBodyResultDataSource = None,
        message: str = None,
    ):
        # The code returned for the request.
        self.code = code
        # The data source.
        self.data_source = data_source
        # The status of the execution.
        self.message = message

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataSource') is not None:
            temp_model = ValidateDataSourcesResponseBodyResultDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ValidateDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ValidateDataSourcesResponseBodyResult] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The result returned.
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ValidateDataSourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ValidateDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateDataSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


