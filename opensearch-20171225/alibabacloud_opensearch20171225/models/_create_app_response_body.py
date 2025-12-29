# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateAppResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateAppResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateAppResponseBodyResult(DaraModel):
    def __init__(
        self,
        cluster: main_models.CreateAppResponseBodyResultCluster = None,
        cluster_name: str = None,
        config_items: List[Dict[str, Any]] = None,
        created: int = None,
        data_sources: List[main_models.CreateAppResponseBodyResultDataSources] = None,
        description: str = None,
        domain: main_models.CreateAppResponseBodyResultDomain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[main_models.CreateAppResponseBodyResultFirstRanks] = None,
        id: str = None,
        interpretations: List[Dict[str, Any]] = None,
        is_current: bool = None,
        progress_percent: int = None,
        prompts: List[Dict[str, Any]] = None,
        query_processors: List[main_models.CreateAppResponseBodyResultQueryProcessors] = None,
        quota: main_models.CreateAppResponseBodyResultQuota = None,
        schema: main_models.CreateAppResponseBodyResultSchema = None,
        schemas: List[main_models.CreateAppResponseBodyResultSchemas] = None,
        second_ranks: List[main_models.CreateAppResponseBodyResultSecondRanks] = None,
        status: str = None,
        summaries: List[main_models.CreateAppResponseBodyResultSummaries] = None,
        switch_time: int = None,
        type: str = None,
        updated: int = None,
    ):
        # The capability opening configurations.
        self.cluster = cluster
        # The name of the cluster.
        self.cluster_name = cluster_name
        self.config_items = config_items
        self.created = created
        # The configurations of the data sources.
        self.data_sources = data_sources
        # The description of the application.
        self.description = description
        # The industry model module.
        self.domain = domain
        # The default display fields.
        self.fetch_fields = fetch_fields
        # The configurations of rough sort.
        self.first_ranks = first_ranks
        # The application ID.
        self.id = id
        # The descriptions of the LLM table fields.
        self.interpretations = interpretations
        # Indicates whether the version is an online version.
        self.is_current = is_current
        # The percentage for the data import progress.
        self.progress_percent = progress_percent
        # The prompt configurations
        self.prompts = prompts
        # The query intent understanding configurations.
        self.query_processors = query_processors
        # The quota.
        self.quota = quota
        # The single-table schema.
        self.schema = schema
        # The multi-table schema.
        self.schemas = schemas
        # The configurations of fine sort.
        self.second_ranks = second_ranks
        # The status of the application. Valid values:
        # 
        # *   OK
        # *   STOPPED
        # *   FROZEN
        # *   INITIALIZING
        # *   UNAVAILABLE
        # *   DATA_WAITING
        # *   DATA_PREPARING
        self.status = status
        # The summary configurations of search results.
        self.summaries = summaries
        self.switch_time = switch_time
        # The type of the application. Valid values:
        # 
        # *   standard
        # *   enhanced
        self.type = type
        self.updated = updated

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
        if self.quota:
            self.quota.validate()
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
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()

        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.config_items is not None:
            result['configItems'] = self.config_items

        if self.created is not None:
            result['created'] = self.created

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
            for k1 in self.query_processors:
                result['queryProcessors'].append(k1.to_map() if k1 else None)

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

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

        if self.status is not None:
            result['status'] = self.status

        result['summaries'] = []
        if self.summaries is not None:
            for k1 in self.summaries:
                result['summaries'].append(k1.to_map() if k1 else None)

        if self.switch_time is not None:
            result['switchTime'] = self.switch_time

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            temp_model = main_models.CreateAppResponseBodyResultCluster()
            self.cluster = temp_model.from_map(m.get('cluster'))

        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('configItems') is not None:
            self.config_items = m.get('configItems')

        if m.get('created') is not None:
            self.created = m.get('created')

        self.data_sources = []
        if m.get('dataSources') is not None:
            for k1 in m.get('dataSources'):
                temp_model = main_models.CreateAppResponseBodyResultDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            temp_model = main_models.CreateAppResponseBodyResultDomain()
            self.domain = temp_model.from_map(m.get('domain'))

        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')

        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k1 in m.get('firstRanks'):
                temp_model = main_models.CreateAppResponseBodyResultFirstRanks()
                self.first_ranks.append(temp_model.from_map(k1))

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
            for k1 in m.get('queryProcessors'):
                temp_model = main_models.CreateAppResponseBodyResultQueryProcessors()
                self.query_processors.append(temp_model.from_map(k1))

        if m.get('quota') is not None:
            temp_model = main_models.CreateAppResponseBodyResultQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('schema') is not None:
            temp_model = main_models.CreateAppResponseBodyResultSchema()
            self.schema = temp_model.from_map(m.get('schema'))

        self.schemas = []
        if m.get('schemas') is not None:
            for k1 in m.get('schemas'):
                temp_model = main_models.CreateAppResponseBodyResultSchemas()
                self.schemas.append(temp_model.from_map(k1))

        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k1 in m.get('secondRanks'):
                temp_model = main_models.CreateAppResponseBodyResultSecondRanks()
                self.second_ranks.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.summaries = []
        if m.get('summaries') is not None:
            for k1 in m.get('summaries'):
                temp_model = main_models.CreateAppResponseBodyResultSummaries()
                self.summaries.append(temp_model.from_map(k1))

        if m.get('switchTime') is not None:
            self.switch_time = m.get('switchTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class CreateAppResponseBodyResultSummaries(DaraModel):
    def __init__(
        self,
        meta: List[main_models.CreateAppResponseBodyResultSummariesMeta] = None,
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
                temp_model = main_models.CreateAppResponseBodyResultSummariesMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateAppResponseBodyResultSummariesMeta(DaraModel):
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

class CreateAppResponseBodyResultSecondRanks(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
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

class CreateAppResponseBodyResultSchemas(DaraModel):
    def __init__(
        self,
        index_sort_config: List[main_models.CreateAppResponseBodyResultSchemasIndexSortConfig] = None,
        indexes: main_models.CreateAppResponseBodyResultSchemasIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: main_models.CreateAppResponseBodyResultSchemasTtlField = None,
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
                temp_model = main_models.CreateAppResponseBodyResultSchemasIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k1))

        if m.get('indexes') is not None:
            temp_model = main_models.CreateAppResponseBodyResultSchemasIndexes()
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
            temp_model = main_models.CreateAppResponseBodyResultSchemasTtlField()
            self.ttl_field = temp_model.from_map(m.get('ttlField'))

        return self

class CreateAppResponseBodyResultSchemasTtlField(DaraModel):
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

class CreateAppResponseBodyResultSchemasIndexes(DaraModel):
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

class CreateAppResponseBodyResultSchemasIndexSortConfig(DaraModel):
    def __init__(
        self,
        direction: str = None,
        field: str = None,
    ):
        # The sort method. Valid values:
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

class CreateAppResponseBodyResultSchema(DaraModel):
    def __init__(
        self,
        index_sort_config: List[main_models.CreateAppResponseBodyResultSchemaIndexSortConfig] = None,
        indexes: main_models.CreateAppResponseBodyResultSchemaIndexes = None,
        name: str = None,
        route_field: str = None,
        route_field_values: List[str] = None,
        second_route_field: str = None,
        tables: Dict[str, Any] = None,
        ttl_field: main_models.CreateAppResponseBodyResultSchemaTtlField = None,
    ):
        # The sort configurations.
        self.index_sort_config = index_sort_config
        # The index schema.
        self.indexes = indexes
        # The name of the wide table.
        self.name = name
        # The name of the level-1 routing field.
        self.route_field = route_field
        # The name of the level-2 routing field. This parameter takes effect only when the routeFieldValues parameter is configured. By default, the wide-table primary key field is used as the level-2 routing field.
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
                temp_model = main_models.CreateAppResponseBodyResultSchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k1))

        if m.get('indexes') is not None:
            temp_model = main_models.CreateAppResponseBodyResultSchemaIndexes()
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
            temp_model = main_models.CreateAppResponseBodyResultSchemaTtlField()
            self.ttl_field = temp_model.from_map(m.get('ttlField'))

        return self

class CreateAppResponseBodyResultSchemaTtlField(DaraModel):
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

class CreateAppResponseBodyResultSchemaIndexes(DaraModel):
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

class CreateAppResponseBodyResultSchemaIndexSortConfig(DaraModel):
    def __init__(
        self,
        direction: str = None,
        field: str = None,
    ):
        # The sort method. Valid values:
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

class CreateAppResponseBodyResultQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        qps: int = None,
        spec: str = None,
        used_compute_resource: int = None,
        used_doc_size: float = None,
        used_qps: int = None,
    ):
        # The computing resources.
        self.compute_resource = compute_resource
        # The storage capacity.
        self.doc_size = doc_size
        # The search request.
        self.qps = qps
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
        self.spec = spec
        self.used_compute_resource = used_compute_resource
        self.used_doc_size = used_doc_size
        self.used_qps = used_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.qps is not None:
            result['qps'] = self.qps

        if self.spec is not None:
            result['spec'] = self.spec

        if self.used_compute_resource is not None:
            result['usedComputeResource'] = self.used_compute_resource

        if self.used_doc_size is not None:
            result['usedDocSize'] = self.used_doc_size

        if self.used_qps is not None:
            result['usedQps'] = self.used_qps

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

        if m.get('usedComputeResource') is not None:
            self.used_compute_resource = m.get('usedComputeResource')

        if m.get('usedDocSize') is not None:
            self.used_doc_size = m.get('usedDocSize')

        if m.get('usedQps') is not None:
            self.used_qps = m.get('usedQps')

        return self

class CreateAppResponseBodyResultQueryProcessors(DaraModel):
    def __init__(
        self,
        active: bool = None,
        category: str = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        # Indicates whether the rule is the default one.
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

class CreateAppResponseBodyResultFirstRanks(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The description.
        self.description = description
        # The information about the expression. The information can be of the array or string type.
        self.meta = meta
        # The name of the rough sort expression.
        self.name = name
        # The expression type. Valid values:
        # 
        # STRUCT: The content of the expression is a structure. STRING (default): You can configure a custom formula.
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

class CreateAppResponseBodyResultDomain(DaraModel):
    def __init__(
        self,
        category: str = None,
        functions: main_models.CreateAppResponseBodyResultDomainFunctions = None,
        name: str = None,
    ):
        # The industry category.
        self.category = category
        # The selected features.
        self.functions = functions
        # The industry type. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.name = name

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CreateAppResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m.get('functions'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateAppResponseBodyResultDomainFunctions(DaraModel):
    def __init__(
        self,
        algo: List[str] = None,
        qp: List[str] = None,
        service: List[str] = None,
    ):
        # The features of the sort policy category.
        self.algo = algo
        # The features of the query analysis category.
        self.qp = qp
        # The features of the service category.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateAppResponseBodyResultDataSources(DaraModel):
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

class CreateAppResponseBodyResultCluster(DaraModel):
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

