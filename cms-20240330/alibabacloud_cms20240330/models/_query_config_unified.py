# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryConfigUnified(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        dimensions: List[Dict[str, str]] = None,
        enable_data_complete_check: bool = None,
        entity_domain: str = None,
        entity_fields: List[main_models.UmodelEntityField] = None,
        entity_filters: List[main_models.UmodelEntityFilter] = None,
        entity_type: str = None,
        expr: str = None,
        filter_list: List[main_models.ApmFilterConfig] = None,
        group_id: str = None,
        label_filters: List[main_models.UmodelLabelFilter] = None,
        legacy_raw: str = None,
        legacy_type: str = None,
        log_set: str = None,
        measure_list: List[main_models.ApmMeasureConfig] = None,
        metric: str = None,
        metric_set: str = None,
        namespace: str = None,
        offset_secs: int = None,
        prom_ql: str = None,
        queries: List[main_models.MetricSetNamedQueryEntry] = None,
        relation_type: str = None,
        service_id_list: List[str] = None,
        type: str = None,
        window_secs: int = None,
    ):
        self.aggregate = aggregate
        self.dimensions = dimensions
        self.enable_data_complete_check = enable_data_complete_check
        self.entity_domain = entity_domain
        self.entity_fields = entity_fields
        self.entity_filters = entity_filters
        self.entity_type = entity_type
        self.expr = expr
        self.filter_list = filter_list
        self.group_id = group_id
        self.label_filters = label_filters
        self.legacy_raw = legacy_raw
        self.legacy_type = legacy_type
        self.log_set = log_set
        self.measure_list = measure_list
        self.metric = metric
        self.metric_set = metric_set
        self.namespace = namespace
        self.offset_secs = offset_secs
        self.prom_ql = prom_ql
        self.queries = queries
        self.relation_type = relation_type
        self.service_id_list = service_id_list
        # This parameter is required.
        self.type = type
        self.window_secs = window_secs

    def validate(self):
        if self.entity_fields:
            for v1 in self.entity_fields:
                 if v1:
                    v1.validate()
        if self.entity_filters:
            for v1 in self.entity_filters:
                 if v1:
                    v1.validate()
        if self.filter_list:
            for v1 in self.filter_list:
                 if v1:
                    v1.validate()
        if self.label_filters:
            for v1 in self.label_filters:
                 if v1:
                    v1.validate()
        if self.measure_list:
            for v1 in self.measure_list:
                 if v1:
                    v1.validate()
        if self.queries:
            for v1 in self.queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.dimensions is not None:
            result['dimensions'] = self.dimensions

        if self.enable_data_complete_check is not None:
            result['enableDataCompleteCheck'] = self.enable_data_complete_check

        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain

        result['entityFields'] = []
        if self.entity_fields is not None:
            for k1 in self.entity_fields:
                result['entityFields'].append(k1.to_map() if k1 else None)

        result['entityFilters'] = []
        if self.entity_filters is not None:
            for k1 in self.entity_filters:
                result['entityFilters'].append(k1.to_map() if k1 else None)

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.expr is not None:
            result['expr'] = self.expr

        result['filterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['filterList'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['groupId'] = self.group_id

        result['labelFilters'] = []
        if self.label_filters is not None:
            for k1 in self.label_filters:
                result['labelFilters'].append(k1.to_map() if k1 else None)

        if self.legacy_raw is not None:
            result['legacyRaw'] = self.legacy_raw

        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type

        if self.log_set is not None:
            result['logSet'] = self.log_set

        result['measureList'] = []
        if self.measure_list is not None:
            for k1 in self.measure_list:
                result['measureList'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.offset_secs is not None:
            result['offsetSecs'] = self.offset_secs

        if self.prom_ql is not None:
            result['promQl'] = self.prom_ql

        result['queries'] = []
        if self.queries is not None:
            for k1 in self.queries:
                result['queries'].append(k1.to_map() if k1 else None)

        if self.relation_type is not None:
            result['relationType'] = self.relation_type

        if self.service_id_list is not None:
            result['serviceIdList'] = self.service_id_list

        if self.type is not None:
            result['type'] = self.type

        if self.window_secs is not None:
            result['windowSecs'] = self.window_secs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')

        if m.get('enableDataCompleteCheck') is not None:
            self.enable_data_complete_check = m.get('enableDataCompleteCheck')

        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        self.entity_fields = []
        if m.get('entityFields') is not None:
            for k1 in m.get('entityFields'):
                temp_model = main_models.UmodelEntityField()
                self.entity_fields.append(temp_model.from_map(k1))

        self.entity_filters = []
        if m.get('entityFilters') is not None:
            for k1 in m.get('entityFilters'):
                temp_model = main_models.UmodelEntityFilter()
                self.entity_filters.append(temp_model.from_map(k1))

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        self.filter_list = []
        if m.get('filterList') is not None:
            for k1 in m.get('filterList'):
                temp_model = main_models.ApmFilterConfig()
                self.filter_list.append(temp_model.from_map(k1))

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.UmodelLabelFilter()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('legacyRaw') is not None:
            self.legacy_raw = m.get('legacyRaw')

        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')

        if m.get('logSet') is not None:
            self.log_set = m.get('logSet')

        self.measure_list = []
        if m.get('measureList') is not None:
            for k1 in m.get('measureList'):
                temp_model = main_models.ApmMeasureConfig()
                self.measure_list.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('offsetSecs') is not None:
            self.offset_secs = m.get('offsetSecs')

        if m.get('promQl') is not None:
            self.prom_ql = m.get('promQl')

        self.queries = []
        if m.get('queries') is not None:
            for k1 in m.get('queries'):
                temp_model = main_models.MetricSetNamedQueryEntry()
                self.queries.append(temp_model.from_map(k1))

        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')

        if m.get('serviceIdList') is not None:
            self.service_id_list = m.get('serviceIdList')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('windowSecs') is not None:
            self.window_secs = m.get('windowSecs')

        return self

