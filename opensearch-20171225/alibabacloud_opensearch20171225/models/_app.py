# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class App(DaraModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cluster: main_models.AppCluster = None,
        data_sources: List[main_models.DataSource] = None,
        description: str = None,
        domain: main_models.Domain = None,
        fetch_fields: List[str] = None,
        first_ranks: List[main_models.FirstRank] = None,
        network_type: str = None,
        query_processors: List[main_models.QueryProcessor] = None,
        quota: main_models.Quota = None,
        realtime_shared: bool = None,
        schema: main_models.Schema = None,
        schemas: List[main_models.Schema] = None,
        second_ranks: List[main_models.SecondRank] = None,
        summaries: List[main_models.Summary] = None,
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
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch

        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()

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

        if self.network_type is not None:
            result['networkType'] = self.network_type

        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k1 in self.query_processors:
                result['queryProcessors'].append(k1.to_map() if k1 else None)

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

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

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')

        if m.get('cluster') is not None:
            temp_model = main_models.AppCluster()
            self.cluster = temp_model.from_map(m.get('cluster'))

        self.data_sources = []
        if m.get('dataSources') is not None:
            for k1 in m.get('dataSources'):
                temp_model = main_models.DataSource()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            temp_model = main_models.Domain()
            self.domain = temp_model.from_map(m.get('domain'))

        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')

        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k1 in m.get('firstRanks'):
                temp_model = main_models.FirstRank()
                self.first_ranks.append(temp_model.from_map(k1))

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k1 in m.get('queryProcessors'):
                temp_model = main_models.QueryProcessor()
                self.query_processors.append(temp_model.from_map(k1))

        if m.get('quota') is not None:
            temp_model = main_models.Quota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('realtimeShared') is not None:
            self.realtime_shared = m.get('realtimeShared')

        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        self.schemas = []
        if m.get('schemas') is not None:
            for k1 in m.get('schemas'):
                temp_model = main_models.Schema()
                self.schemas.append(temp_model.from_map(k1))

        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k1 in m.get('secondRanks'):
                temp_model = main_models.SecondRank()
                self.second_ranks.append(temp_model.from_map(k1))

        self.summaries = []
        if m.get('summaries') is not None:
            for k1 in m.get('summaries'):
                temp_model = main_models.Summary()
                self.summaries.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self



class AppCluster(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

