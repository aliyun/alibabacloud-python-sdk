# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateAppRequest(DaraModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: main_models.CreateAppRequestCluster = None,
        config_items: List[Dict[str, Any]] = None,
        data_sources: List[main_models.CreateAppRequestDataSources] = None,
        description: str = None,
        domain: main_models.CreateAppRequestDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[main_models.CreateAppRequestFirstRanks] = None,
        interpretations: List[Dict[str, Any]] = None,
        network_type: str = None,
        prompts: List[Dict[str, Any]] = None,
        query_processors: List[main_models.CreateAppRequestQueryProcessors] = None,
        realtime_shared: bool = None,
        schema: main_models.CreateAppRequestSchema = None,
        schemas: List[main_models.CreateAppRequestSchemas] = None,
        second_ranks: List[main_models.CreateAppRequestSecondRanks] = None,
        summaries: List[main_models.CreateAppRequestSummaries] = None,
        dry_run: bool = None,
    ):
        # Specifies whether to automatically switch the created version to an online version. Valid values:
        # 
        # *   true
        # *   false
        self.auto_switch = auto_switch
        # The capability opening configurations.
        self.cluster = cluster
        self.config_items = config_items
        # The configurations of data sources.
        self.data_sources = data_sources
        # The version description.
        self.description = description
        # The industry model module.
        self.domain = domain
        # The default display fields.
        self.fetch_fields = fetch_fields
        # The configurations of rough sort.
        self.first_ranks = first_ranks
        self.interpretations = interpretations
        # The zone identifier. Valid values:
        # 
        # *   vpc
        # *   oxs
        self.network_type = network_type
        self.prompts = prompts
        # The query intent understanding configurations.
        self.query_processors = query_processors
        self.realtime_shared = realtime_shared
        # The single-table schema.
        self.schema = schema
        # The multi-table schema.
        self.schemas = schemas
        # The configurations of fine sort.
        self.second_ranks = second_ranks
        # The summary configurations of search results.
        self.summaries = summaries
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for v1 in self.first_ranks:
                 if v1:
                    v1.validate()
        if self.query_processors:
            for v1 in self.query_processors:
                 if v1:
                    v1.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for v1 in self.schemas:
                 if v1:
                    v1.validate()
        if self.second_ranks:
            for v1 in self.second_ranks:
                 if v1:
                    v1.validate()
        if self.summaries:
            for v1 in self.summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch

        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()

        if self.config_items is not None:
            result['configItems'] = self.config_items

        result['dataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['dataSources'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain.to_map()

        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields

        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k1 in self.first_ranks:
                result['firstRanks'].append(k1.to_map() if k1 else None)

        if self.interpretations is not None:
            result['interpretations'] = self.interpretations

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.prompts is not None:
            result['prompts'] = self.prompts

        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k1 in self.query_processors:
                result['queryProcessors'].append(k1.to_map() if k1 else None)

        if self.realtime_shared is not None:
            result['realtimeShared'] = self.realtime_shared

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        result['schemas'] = []
        if self.schemas is not None:
            for k1 in self.schemas:
                result['schemas'].append(k1.to_map() if k1 else None)

        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k1 in self.second_ranks:
                result['secondRanks'].append(k1.to_map() if k1 else None)

        result['summaries'] = []
        if self.summaries is not None:
            for k1 in self.summaries:
                result['summaries'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')

        if m.get('cluster') is not None:
            temp_model = main_models.CreateAppRequestCluster()
            self.cluster = temp_model.from_map(m.get('cluster'))

        if m.get('configItems') is not None:
            self.config_items = m.get('configItems')

        self.data_sources = []
        if m.get('dataSources') is not None:
            for k1 in m.get('dataSources'):
                temp_model = main_models.CreateAppRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            temp_model = main_models.CreateAppRequestDomain()
            self.domain = temp_model.from_map(m.get('domain'))

        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')

        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k1 in m.get('firstRanks'):
                temp_model = main_models.CreateAppRequestFirstRanks()
                self.first_ranks.append(temp_model.from_map(k1))

        if m.get('interpretations') is not None:
            self.interpretations = m.get('interpretations')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('prompts') is not None:
            self.prompts = m.get('prompts')

        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k1 in m.get('queryProcessors'):
                temp_model = main_models.CreateAppRequestQueryProcessors()
                self.query_processors.append(temp_model.from_map(k1))

        if m.get('realtimeShared') is not None:
            self.realtime_shared = m.get('realtimeShared')

        if m.get('schema') is not None:
            temp_model = main_models.CreateAppRequestSchema()
            self.schema = temp_model.from_map(m.get('schema'))

        self.schemas = []
        if m.get('schemas') is not None:
            for k1 in m.get('schemas'):
                temp_model = main_models.CreateAppRequestSchemas()
                self.schemas.append(temp_model.from_map(k1))

        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k1 in m.get('secondRanks'):
                temp_model = main_models.CreateAppRequestSecondRanks()
                self.second_ranks.append(temp_model.from_map(k1))

        self.summaries = []
        if m.get('summaries') is not None:
            for k1 in m.get('summaries'):
                temp_model = main_models.CreateAppRequestSummaries()
                self.summaries.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

class CreateAppRequestSummaries(DaraModel):
    def __init__(
        self,
        meta: List[main_models.CreateAppRequestSummariesMeta] = None,
        name: str = None,
    ):
        # The collection of summary configurations.
        self.meta = meta
        # The group name.
        self.name = name

    def validate(self):
        if self.meta:
            for v1 in self.meta:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['meta'] = []
        if self.meta is not None:
            for k1 in self.meta:
                result['meta'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('meta') is not None:
            for k1 in m.get('meta'):
                temp_model = main_models.CreateAppRequestSummariesMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateAppRequestSummariesMeta(DaraModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        # The element that is used for highlighting.
        self.element = element
        # The connector that is used to connect segments.
        self.ellipsis = ellipsis
        # The field.
        self.field = field
        # The length of the segment. Valid values: 1 to 300.
        self.len = len
        # The number of segments. Valid values: 1 to 5.
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestSecondRanks(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        # Specifies whether the expression is the default one.
        self.active = active
        # The description.
        self.description = description
        # The fine sort expression. You can define an expression that contains fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta
        # The name of the fine sort expression.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestSchemas(DaraModel):
    def __init__(
        self,
        index_sort_config: List[main_models.CreateAppRequestSchemasIndexSortConfig] = None,
        indexes: main_models.CreateAppRequestSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: main_models.CreateAppRequestSchemasTtlField = None,
    ):
        # The sort configurations.
        self.index_sort_config = index_sort_config
        # The index schema.
        self.indexes = indexes
        # The name of the wide table.
        self.name = name
        # The name of the level-1 routing field.
        self.route_field = route_field
        # The hot values of the level-1 routing field. After you configure this parameter, level-2 routing is enabled.
        self.route_field_values = route_field_values
        # The name of the level-2 routing field. This parameter takes effect only when the routeFieldValues parameter is configured. By default, the wide-table primary key field is used as the level-2 routing field.
        self.second_route_field = second_route_field
        # The table schema.
        self.tables = tables
        # The document clearing configurations.
        self.ttl_field = ttl_field

    def validate(self):
        if self.index_sort_config:
            for v1 in self.index_sort_config:
                 if v1:
                    v1.validate()
        if self.indexes:
            self.indexes.validate()
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

        if self.tables is not None:
            result['tables'] = self.tables

        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k1 in m.get('indexSortConfig'):
                temp_model = main_models.CreateAppRequestSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k1))

        if m.get('indexes') is not None:
            temp_model = main_models.CreateAppRequestSchemasIndexes()
            self.indexes = temp_model.from_map(m.get('indexes'))

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
            temp_model = main_models.CreateAppRequestSchemasTtlField()
            self.ttl_field = temp_model.from_map(m.get('ttlField'))

        return self

class CreateAppRequestSchemasTtlField(DaraModel):
    def __init__(
        self,
        name: str = None,
        ttl: int = None,
    ):
        # The name of the document time field.
        self.name = name
        # The TTL. Unit: milliseconds.
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

class CreateAppRequestSchemasIndexes(DaraModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        # The attribute fields.
        self.filter_fields = filter_fields
        # The index fields.
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestSchemasIndexSortConfig(DaraModel):
    def __init__(
        self,
        direction: str = None,
        field: str = None,
    ):
        # The sort method.
        # 
        # *   ASC
        # *   DESC
        self.direction = direction
        # The sort field.
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

class CreateAppRequestSchema(DaraModel):
    def __init__(
        self,
        index_sort_config: List[main_models.CreateAppRequestSchemaIndexSortConfig] = None,
        indexes: main_models.CreateAppRequestSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: main_models.CreateAppRequestSchemaTtlField = None,
    ):
        # The sort configurations.
        self.index_sort_config = index_sort_config
        # The index schema.
        self.indexes = indexes
        # The name of the wide table.
        self.name = name
        # The name of the level-1 routing field.
        self.route_field = route_field
        # The hot values of the level-1 routing field. After you configure this parameter, level-2 routing is enabled.
        self.route_field_values = route_field_values
        # The name of the level-2 routing field. This parameter takes effect only when the `routeFieldValues` parameter is configured. By default, the wide-table primary key field is used as the level-2 routing field.
        self.second_route_field = second_route_field
        # The table schema.
        self.tables = tables
        # The document clearing configurations.
        self.ttl_field = ttl_field

    def validate(self):
        if self.index_sort_config:
            for v1 in self.index_sort_config:
                 if v1:
                    v1.validate()
        if self.indexes:
            self.indexes.validate()
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

        if self.tables is not None:
            result['tables'] = self.tables

        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k1 in m.get('indexSortConfig'):
                temp_model = main_models.CreateAppRequestSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k1))

        if m.get('indexes') is not None:
            temp_model = main_models.CreateAppRequestSchemaIndexes()
            self.indexes = temp_model.from_map(m.get('indexes'))

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
            temp_model = main_models.CreateAppRequestSchemaTtlField()
            self.ttl_field = temp_model.from_map(m.get('ttlField'))

        return self

class CreateAppRequestSchemaTtlField(DaraModel):
    def __init__(
        self,
        name: str = None,
        ttl: int = None,
    ):
        # The name of the document time field.
        self.name = name
        # The TTL. Unit: milliseconds.
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

class CreateAppRequestSchemaIndexes(DaraModel):
    def __init__(
        self,
        filter_fields: List[str] = None,
        search_fields: Dict[str, Any] = None,
    ):
        # The attribute fields.
        self.filter_fields = filter_fields
        # The index fields.
        self.search_fields = search_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestSchemaIndexSortConfig(DaraModel):
    def __init__(
        self,
        direction: str = None,
        field: str = None,
    ):
        # The sort method.
        self.direction = direction
        # The sort field.
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

class CreateAppRequestQueryProcessors(DaraModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        # Specifies whether the rule is the default one.
        self.active = active
        # The industry category.
        self.category = category
        # The industry type. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The index range.
        self.indexes = indexes
        # The rule name.
        self.name = name
        # The features.
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestFirstRanks(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        # Specifies whether the expression is the default one.
        self.active = active
        # The description.
        self.description = description
        # The information about the expression. The information can be of the array or string type.
        self.meta = meta
        # The name of the rough sort expression.
        self.name = name
        # The expression type. Valid values:
        # 
        # *   STRUCT: The content of the expression is a structure.
        # *   STRING (default): You can configure a custom formula.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestDomain(DaraModel):
    def __init__(
        self,
        category: str = None,
        functions: Dict[str, Any] = None,
        name: str = None,
    ):
        # The industry category.
        self.category = category
        # The selected feature category. Valid values:
        # 
        # *   qp: query analysis
        # *   algo: sort policy
        # *   service: service
        self.functions = functions
        # The industry type.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestDataSources(DaraModel):
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
        # The information about field mappings.
        self.fields = fields
        # The primary key.
        self.key_field = key_field
        # The information about the data source.
        self.parameters = parameters
        # The plug-ins that are used for data processing.
        # 
        # name:
        # 
        # *   JsonKeyValueExtractor
        # *   MultiValueSpliter
        # *   KeyValueExtractor
        # *   StringCatenateExtractor
        # *   HTMLTagRemover
        # 
        # parameters:
        # 
        # *   JsonKeyValueExtractor
        # *   MultiValueSpliter
        # *   KeyValueExtractor
        # *   StringCatenateExtractor
        # *   HTMLTagRemover
        self.plugins = plugins
        # The name of the wide table.
        self.schema_name = schema_name
        # The name of the table in the application.
        self.table_name = table_name
        # The type of the data source. Valid values:
        # 
        # *   rds
        # *   odps
        # *   opensearch
        # *   polardb
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppRequestCluster(DaraModel):
    def __init__(
        self,
        chunk_models: List[Dict[str, Any]] = None,
        graph_rag: Dict[str, Any] = None,
        image_content_recognizer_models: List[Dict[str, Any]] = None,
        max_query_clause_length: int = None,
        max_timeout_ms: int = None,
        text_embedding_model: str = None,
        text_sparse_embedding_model: str = None,
        vector_index_configs: List[Dict[str, Any]] = None,
    ):
        self.chunk_models = chunk_models
        self.graph_rag = graph_rag
        self.image_content_recognizer_models = image_content_recognizer_models
        # The maximum length of the query clause.
        self.max_query_clause_length = max_query_clause_length
        # The timeout period. Unit: milliseconds.
        self.max_timeout_ms = max_timeout_ms
        self.text_embedding_model = text_embedding_model
        self.text_sparse_embedding_model = text_sparse_embedding_model
        self.vector_index_configs = vector_index_configs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_models is not None:
            result['chunkModels'] = self.chunk_models

        if self.graph_rag is not None:
            result['graphRag'] = self.graph_rag

        if self.image_content_recognizer_models is not None:
            result['imageContentRecognizerModels'] = self.image_content_recognizer_models

        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length

        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms

        if self.text_embedding_model is not None:
            result['textEmbeddingModel'] = self.text_embedding_model

        if self.text_sparse_embedding_model is not None:
            result['textSparseEmbeddingModel'] = self.text_sparse_embedding_model

        if self.vector_index_configs is not None:
            result['vectorIndexConfigs'] = self.vector_index_configs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkModels') is not None:
            self.chunk_models = m.get('chunkModels')

        if m.get('graphRag') is not None:
            self.graph_rag = m.get('graphRag')

        if m.get('imageContentRecognizerModels') is not None:
            self.image_content_recognizer_models = m.get('imageContentRecognizerModels')

        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')

        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')

        if m.get('textEmbeddingModel') is not None:
            self.text_embedding_model = m.get('textEmbeddingModel')

        if m.get('textSparseEmbeddingModel') is not None:
            self.text_sparse_embedding_model = m.get('textSparseEmbeddingModel')

        if m.get('vectorIndexConfigs') is not None:
            self.vector_index_configs = m.get('vectorIndexConfigs')

        return self

