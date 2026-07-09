# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleQuery(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        check_after_data_complete: bool = None,
        dimensions: List[Dict[str, str]] = None,
        domain: str = None,
        duration: int = None,
        entity_fields: List[main_models.AlertRuleQueryEntityFields] = None,
        entity_filter: main_models.AlertRuleQueryEntityFilter = None,
        expr: str = None,
        first_join: main_models.AlertRuleSlsQueryJoin = None,
        group_field_list: List[str] = None,
        group_id: str = None,
        group_type: str = None,
        label_filters: List[main_models.AlertRuleQueryLabelFilters] = None,
        log_set: str = None,
        mark_tags: List[main_models.AlertRuleQueryMarkTags] = None,
        metric: str = None,
        metric_set: str = None,
        namespace: str = None,
        offset_secs: int = None,
        queries: List[main_models.AlertRuleQueryQueries] = None,
        relation_type: str = None,
        second_join: main_models.AlertRuleSlsQueryJoin = None,
        service_ids: List[str] = None,
        type: str = None,
        window_secs: int = None,
    ):
        self.aggregate = aggregate
        # Applicable query type: PROMQL_QUERY.
        # 
        # Specifies whether to perform alert detection only after data is complete.
        self.check_after_data_complete = check_after_data_complete
        # Applicable query type: CMS_BASIC_QUERY.  
        # 
        # The list of filter dimensions for the resource.
        self.dimensions = dimensions
        # The domain to which the resource belongs.
        self.domain = domain
        # Applicable query type: PROMQL_QUERY.
        # 
        # The duration for which alert data persists. Unit: seconds.
        self.duration = duration
        # The array of entity field filters.
        self.entity_fields = entity_fields
        # The resource filter used to filter target resources.
        self.entity_filter = entity_filter
        # Applicable query type: PROMQL_QUERY.
        # 
        # The query expression (PromQL).
        self.expr = expr
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The set join operation configuration for the results of subquery 1 (queries[0]) and subquery 2 (queries[1]).
        self.first_join = first_join
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The list of group field names.
        self.group_field_list = group_field_list
        # Applicable query type: CMS_BASIC_QUERY.
        # 
        # The ID of the associated application group. This parameter takes effect only when relationType is set to GROUP.
        self.group_id = group_id
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The group type. Valid values:
        # - none: no grouping.
        # - label: automatic label-based grouping.
        # - custom: custom label-based grouping.
        self.group_type = group_type
        # The array of label filters.
        self.label_filters = label_filters
        self.log_set = log_set
        self.mark_tags = mark_tags
        # The metric name.
        self.metric = metric
        # The collection of monitoring metrics.
        self.metric_set = metric_set
        # Applicable query type: CMS_BASIC_QUERY.
        # 
        # The namespace of the metric.
        self.namespace = namespace
        self.offset_secs = offset_secs
        # Applicable query types: SLS_MULTI_QUERY and APM_MULTI_QUERY.
        # 
        # The list of subqueries.
        # 
        # For the SLS_MULTI_QUERY query type, a maximum of three subqueries are supported. The number and order of subqueries must match the sub-datasource config in datasource.dsList.
        self.queries = queries
        # Applicable query type: CMS_BASIC_QUERY.
        # 
        # The resource scope of the rule query. Valid values:
        # - USER: all resources under the user UID.
        # - GROUP: application group.
        # - INSTANCE: specified instance list.
        self.relation_type = relation_type
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The set join operation configuration for the results of subquery 2 (queries[2]) and subquery 3 (queries[3]).
        self.second_join = second_join
        # The list of service IDs.
        self.service_ids = service_ids
        # The query type. 
        # 
        # Valid values:
        # - PROMQL_QUERY: PromQL query.
        # - SLS_MULTI_QUERY: SLS query.
        # - APM_MULTI_QUERY: APM query.
        # - CMS_BASIC_QUERY: basic cloud service monitoring query.
        # 
        # Different query types use different valid fields in the query object. For more information, see the "Applicable query type" description of each field.
        # 
        # The query type must match the data source type. The mappings are as follows:
        # - Prometheus data source (PROMETHEUS_DS): PROMQL_QUERY
        # - APM data source (APM_DS): APM_MULTI_QUERY
        # - SLS data source (SLS_MULTI_DS): SLS_MULTI_QUERY
        # - Basic cloud service monitoring data source (CMS_BASIC_DS): CMS_BASIC_QUERY
        # 
        # This parameter is required.
        self.type = type
        self.window_secs = window_secs

    def validate(self):
        if self.entity_fields:
            for v1 in self.entity_fields:
                 if v1:
                    v1.validate()
        if self.entity_filter:
            self.entity_filter.validate()
        if self.first_join:
            self.first_join.validate()
        if self.label_filters:
            for v1 in self.label_filters:
                 if v1:
                    v1.validate()
        if self.mark_tags:
            for v1 in self.mark_tags:
                 if v1:
                    v1.validate()
        if self.queries:
            for v1 in self.queries:
                 if v1:
                    v1.validate()
        if self.second_join:
            self.second_join.validate()

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

        if self.domain is not None:
            result['domain'] = self.domain

        if self.duration is not None:
            result['duration'] = self.duration

        result['entityFields'] = []
        if self.entity_fields is not None:
            for k1 in self.entity_fields:
                result['entityFields'].append(k1.to_map() if k1 else None)

        if self.entity_filter is not None:
            result['entityFilter'] = self.entity_filter.to_map()

        if self.expr is not None:
            result['expr'] = self.expr

        if self.first_join is not None:
            result['firstJoin'] = self.first_join.to_map()

        if self.group_field_list is not None:
            result['groupFieldList'] = self.group_field_list

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_type is not None:
            result['groupType'] = self.group_type

        result['labelFilters'] = []
        if self.label_filters is not None:
            for k1 in self.label_filters:
                result['labelFilters'].append(k1.to_map() if k1 else None)

        if self.log_set is not None:
            result['logSet'] = self.log_set

        result['markTags'] = []
        if self.mark_tags is not None:
            for k1 in self.mark_tags:
                result['markTags'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.offset_secs is not None:
            result['offsetSecs'] = self.offset_secs

        result['queries'] = []
        if self.queries is not None:
            for k1 in self.queries:
                result['queries'].append(k1.to_map() if k1 else None)

        if self.relation_type is not None:
            result['relationType'] = self.relation_type

        if self.second_join is not None:
            result['secondJoin'] = self.second_join.to_map()

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

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

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        self.entity_fields = []
        if m.get('entityFields') is not None:
            for k1 in m.get('entityFields'):
                temp_model = main_models.AlertRuleQueryEntityFields()
                self.entity_fields.append(temp_model.from_map(k1))

        if m.get('entityFilter') is not None:
            temp_model = main_models.AlertRuleQueryEntityFilter()
            self.entity_filter = temp_model.from_map(m.get('entityFilter'))

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('firstJoin') is not None:
            temp_model = main_models.AlertRuleSlsQueryJoin()
            self.first_join = temp_model.from_map(m.get('firstJoin'))

        if m.get('groupFieldList') is not None:
            self.group_field_list = m.get('groupFieldList')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.AlertRuleQueryLabelFilters()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('logSet') is not None:
            self.log_set = m.get('logSet')

        self.mark_tags = []
        if m.get('markTags') is not None:
            for k1 in m.get('markTags'):
                temp_model = main_models.AlertRuleQueryMarkTags()
                self.mark_tags.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('offsetSecs') is not None:
            self.offset_secs = m.get('offsetSecs')

        self.queries = []
        if m.get('queries') is not None:
            for k1 in m.get('queries'):
                temp_model = main_models.AlertRuleQueryQueries()
                self.queries.append(temp_model.from_map(k1))

        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')

        if m.get('secondJoin') is not None:
            temp_model = main_models.AlertRuleSlsQueryJoin()
            self.second_join = temp_model.from_map(m.get('secondJoin'))

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('windowSecs') is not None:
            self.window_secs = m.get('windowSecs')

        return self

class AlertRuleQueryQueries(DaraModel):
    def __init__(
        self,
        apm_alert_metric_id: str = None,
        apm_filters: List[main_models.AlertRuleQueryQueriesApmFilters] = None,
        apm_group_by: List[str] = None,
        duration: int = None,
        end: int = None,
        expr: str = None,
        label_filters: List[main_models.AlertRuleQueryQueriesLabelFilters] = None,
        metric: str = None,
        metric_set: str = None,
        name: str = None,
        prom_ql: str = None,
        start: int = None,
        time_unit: str = None,
        window: int = None,
    ):
        # Applicable query type: APM_MULTI_QUERY.
        # 
        # The ID of the APM predefined metric.
        self.apm_alert_metric_id = apm_alert_metric_id
        # Applicable query type: ARMS_MULTI_QUERY.
        # 
        # The dimension filter configuration for the APM metric. Must be used together with apmAlertMetricId.
        self.apm_filters = apm_filters
        # Applicable query type: ARMS_MULTI_QUERY.
        # 
        # The list of aggregation dimensions for the query, specifying which metric dimensions to aggregate by.
        self.apm_group_by = apm_group_by
        # Applicable query type: ARMS_MULTI_QUERY.
        # 
        # The alert data duration.
        self.duration = duration
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The relative time offset end time.
        # 
        # If start and end are specified, do not specify window.
        self.end = end
        # Applicable query types: APM_MULTI_QUERY, SLS_MULTI_QUERY.
        # 
        # The query expression.
        # 
        # - For APM_MULTI_QUERY, this field is optional and contains the PromQL generated for predefined metrics (used for data preview).
        # - For SLS_MULTI_QUERY, this field contains the SQL query statement.
        self.expr = expr
        self.label_filters = label_filters
        self.metric = metric
        self.metric_set = metric_set
        self.name = name
        self.prom_ql = prom_ql
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The relative time offset start time for the SLS query.
        # 
        # If start and end are specified, do not specify window. Example: start=15, timeUnit=minute indicates 15 minutes ago.
        self.start = start
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The time unit for the start, end, and window parameters: day/hour/minute/second.
        self.time_unit = time_unit
        # Applicable query type: SLS_MULTI_QUERY.
        # 
        # The time frame query interval. If window is specified, do not specify start or end.
        self.window = window

    def validate(self):
        if self.apm_filters:
            for v1 in self.apm_filters:
                 if v1:
                    v1.validate()
        if self.label_filters:
            for v1 in self.label_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apm_alert_metric_id is not None:
            result['apmAlertMetricId'] = self.apm_alert_metric_id

        result['apmFilters'] = []
        if self.apm_filters is not None:
            for k1 in self.apm_filters:
                result['apmFilters'].append(k1.to_map() if k1 else None)

        if self.apm_group_by is not None:
            result['apmGroupBy'] = self.apm_group_by

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end is not None:
            result['end'] = self.end

        if self.expr is not None:
            result['expr'] = self.expr

        result['labelFilters'] = []
        if self.label_filters is not None:
            for k1 in self.label_filters:
                result['labelFilters'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.name is not None:
            result['name'] = self.name

        if self.prom_ql is not None:
            result['promQl'] = self.prom_ql

        if self.start is not None:
            result['start'] = self.start

        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit

        if self.window is not None:
            result['window'] = self.window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apmAlertMetricId') is not None:
            self.apm_alert_metric_id = m.get('apmAlertMetricId')

        self.apm_filters = []
        if m.get('apmFilters') is not None:
            for k1 in m.get('apmFilters'):
                temp_model = main_models.AlertRuleQueryQueriesApmFilters()
                self.apm_filters.append(temp_model.from_map(k1))

        if m.get('apmGroupBy') is not None:
            self.apm_group_by = m.get('apmGroupBy')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.AlertRuleQueryQueriesLabelFilters()
                self.label_filters.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('promQl') is not None:
            self.prom_ql = m.get('promQl')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')

        if m.get('window') is not None:
            self.window = m.get('window')

        return self

class AlertRuleQueryQueriesLabelFilters(DaraModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.name = name
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleQueryQueriesApmFilters(DaraModel):
    def __init__(
        self,
        dim: str = None,
        type: str = None,
        value: str = None,
    ):
        # The dimension in the APM metric.
        self.dim = dim
        # The filter operation type. Valid values:
        # - eq: equal to
        # - neq: not equal to
        # - match: regex match
        # - nmatch: regex not match
        self.type = type
        # The value corresponding to the filter operation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dim is not None:
            result['dim'] = self.dim

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleQueryMarkTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class AlertRuleQueryLabelFilters(DaraModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The label name.
        self.name = name
        # The comparison operator that determines how to match the label value.
        self.operator = operator
        # The label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleQueryEntityFilter(DaraModel):
    def __init__(
        self,
        domain: str = None,
        filters: List[main_models.AlertRuleQueryEntityFilterFilters] = None,
        type: str = None,
    ):
        # The resource type domain.
        self.domain = domain
        # The list of filter conditions used to further filter resources.
        self.filters = filters
        # The resource type.
        self.type = type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        result['filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['filters'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        self.filters = []
        if m.get('filters') is not None:
            for k1 in m.get('filters'):
                temp_model = main_models.AlertRuleQueryEntityFilterFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AlertRuleQueryEntityFilterFilters(DaraModel):
    def __init__(
        self,
        field: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The field.
        self.field = field
        # The comparison operator.
        self.operator = operator
        # The matched value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleQueryEntityFields(DaraModel):
    def __init__(
        self,
        field: str = None,
        value: str = None,
    ):
        # The entity field name.
        self.field = field
        # The field value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

