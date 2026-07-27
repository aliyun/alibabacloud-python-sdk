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
        check_after_data_complete: bool = None,
        dimensions: List[Dict[str, str]] = None,
        duration_secs: int = None,
        enable_data_complete_check: bool = None,
        entity_domain: str = None,
        entity_fields: List[main_models.EntityFields] = None,
        entity_filters: List[main_models.EntityFilters] = None,
        entity_type: str = None,
        expr: str = None,
        filter_list: List[main_models.FilterList] = None,
        filter_values: List[main_models.PrometheusMetricFilterValue] = None,
        group_field_list: List[str] = None,
        group_id: str = None,
        group_type: str = None,
        joinings: List[main_models.Joinings] = None,
        label_filters: List[main_models.LabelFilters] = None,
        legacy_raw: str = None,
        legacy_type: str = None,
        log_set: str = None,
        measure_group_key: str = None,
        measure_list: List[main_models.MeasureList] = None,
        metric: str = None,
        metric_group_id: str = None,
        metric_id: str = None,
        metric_ids: List[str] = None,
        metric_set: str = None,
        namespace: str = None,
        offset_secs: int = None,
        param_values: List[main_models.PrometheusMetricParamValue] = None,
        prom_ql: str = None,
        queries: List[main_models.Queries] = None,
        relation_type: str = None,
        service_id_list: List[str] = None,
        type: str = None,
        window_secs: int = None,
    ):
        self.aggregate = aggregate
        self.check_after_data_complete = check_after_data_complete
        self.dimensions = dimensions
        self.duration_secs = duration_secs
        self.enable_data_complete_check = enable_data_complete_check
        self.entity_domain = entity_domain
        self.entity_fields = entity_fields
        self.entity_filters = entity_filters
        self.entity_type = entity_type
        self.expr = expr
        self.filter_list = filter_list
        self.filter_values = filter_values
        self.group_field_list = group_field_list
        self.group_id = group_id
        self.group_type = group_type
        self.joinings = joinings
        self.label_filters = label_filters
        self.legacy_raw = legacy_raw
        self.legacy_type = legacy_type
        self.log_set = log_set
        self.measure_group_key = measure_group_key
        self.measure_list = measure_list
        self.metric = metric
        self.metric_group_id = metric_group_id
        self.metric_id = metric_id
        self.metric_ids = metric_ids
        self.metric_set = metric_set
        self.namespace = namespace
        self.offset_secs = offset_secs
        self.param_values = param_values
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
        if self.filter_values:
            for v1 in self.filter_values:
                 if v1:
                    v1.validate()
        if self.joinings:
            for v1 in self.joinings:
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
        if self.param_values:
            for v1 in self.param_values:
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

        if self.check_after_data_complete is not None:
            result['checkAfterDataComplete'] = self.check_after_data_complete

        if self.dimensions is not None:
            result['dimensions'] = self.dimensions

        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

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

        result['filterValues'] = []
        if self.filter_values is not None:
            for k1 in self.filter_values:
                result['filterValues'].append(k1.to_map() if k1 else None)

        if self.group_field_list is not None:
            result['groupFieldList'] = self.group_field_list

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_type is not None:
            result['groupType'] = self.group_type

        result['joinings'] = []
        if self.joinings is not None:
            for k1 in self.joinings:
                result['joinings'].append(k1.to_map() if k1 else None)

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

        if self.measure_group_key is not None:
            result['measureGroupKey'] = self.measure_group_key

        result['measureList'] = []
        if self.measure_list is not None:
            for k1 in self.measure_list:
                result['measureList'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_group_id is not None:
            result['metricGroupId'] = self.metric_group_id

        if self.metric_id is not None:
            result['metricId'] = self.metric_id

        if self.metric_ids is not None:
            result['metricIds'] = self.metric_ids

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.offset_secs is not None:
            result['offsetSecs'] = self.offset_secs

        result['paramValues'] = []
        if self.param_values is not None:
            for k1 in self.param_values:
                result['paramValues'].append(k1.to_map() if k1 else None)

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

        if m.get('checkAfterDataComplete') is not None:
            self.check_after_data_complete = m.get('checkAfterDataComplete')

        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('enableDataCompleteCheck') is not None:
            self.enable_data_complete_check = m.get('enableDataCompleteCheck')

        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        self.entity_fields = []
        if m.get('entityFields') is not None:
            for k1 in m.get('entityFields'):
                temp_model = main_models.EntityFields()
                self.entity_fields.append(temp_model.from_map(k1))

        self.entity_filters = []
        if m.get('entityFilters') is not None:
            for k1 in m.get('entityFilters'):
                temp_model = main_models.EntityFilters()
                self.entity_filters.append(temp_model.from_map(k1))

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        self.filter_list = []
        if m.get('filterList') is not None:
            for k1 in m.get('filterList'):
                temp_model = main_models.FilterList()
                self.filter_list.append(temp_model.from_map(k1))

        self.filter_values = []
        if m.get('filterValues') is not None:
            for k1 in m.get('filterValues'):
                temp_model = main_models.PrometheusMetricFilterValue()
                self.filter_values.append(temp_model.from_map(k1))

        if m.get('groupFieldList') is not None:
            self.group_field_list = m.get('groupFieldList')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        self.joinings = []
        if m.get('joinings') is not None:
            for k1 in m.get('joinings'):
                temp_model = main_models.Joinings()
                self.joinings.append(temp_model.from_map(k1))

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.LabelFilters()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('legacyRaw') is not None:
            self.legacy_raw = m.get('legacyRaw')

        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')

        if m.get('logSet') is not None:
            self.log_set = m.get('logSet')

        if m.get('measureGroupKey') is not None:
            self.measure_group_key = m.get('measureGroupKey')

        self.measure_list = []
        if m.get('measureList') is not None:
            for k1 in m.get('measureList'):
                temp_model = main_models.MeasureList()
                self.measure_list.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricGroupId') is not None:
            self.metric_group_id = m.get('metricGroupId')

        if m.get('metricId') is not None:
            self.metric_id = m.get('metricId')

        if m.get('metricIds') is not None:
            self.metric_ids = m.get('metricIds')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('offsetSecs') is not None:
            self.offset_secs = m.get('offsetSecs')

        self.param_values = []
        if m.get('paramValues') is not None:
            for k1 in m.get('paramValues'):
                temp_model = main_models.PrometheusMetricParamValue()
                self.param_values.append(temp_model.from_map(k1))

        if m.get('promQl') is not None:
            self.prom_ql = m.get('promQl')

        self.queries = []
        if m.get('queries') is not None:
            for k1 in m.get('queries'):
                temp_model = main_models.Queries()
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

