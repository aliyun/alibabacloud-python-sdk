# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryConfigUnified(DaraModel):
    def __init__(
        self,
        enable_data_complete_check: bool = None,
        entity_domain: str = None,
        entity_fields: List[main_models.UmodelEntityField] = None,
        entity_filters: List[main_models.UmodelEntityFilter] = None,
        entity_type: str = None,
        filter_list: List[main_models.ApmFilterConfig] = None,
        label_filters: List[main_models.UmodelLabelFilter] = None,
        measure_list: List[main_models.ApmMeasureConfig] = None,
        metric: str = None,
        metric_set: str = None,
        prom_ql: str = None,
        service_id_list: List[str] = None,
        type: str = None,
    ):
        # 是否启用数据完整性检查
        self.enable_data_complete_check = enable_data_complete_check
        # 实体所属域
        self.entity_domain = entity_domain
        # 需要附带返回的实体字段
        self.entity_fields = entity_fields
        # 实体过滤列表
        self.entity_filters = entity_filters
        # 实体类型
        self.entity_type = entity_type
        # APM 过滤条件列表
        self.filter_list = filter_list
        # 标签过滤条件
        self.label_filters = label_filters
        # APM 度量配置列表
        self.measure_list = measure_list
        # 指标名称（type=UMODEL_METRICSET_QUERY）
        self.metric = metric
        # 指标集名称（type=UMODEL_METRICSET_QUERY）
        self.metric_set = metric_set
        # Prometheus 查询语句（type=PROMETHEUS_SINGLE_QUERY）
        self.prom_ql = prom_ql
        # 服务 ID 列表（type=APM_MULTI_QUERY）
        self.service_id_list = service_id_list
        # 查询类型
        # 
        # This parameter is required.
        self.type = type

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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        result['filterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['filterList'].append(k1.to_map() if k1 else None)

        result['labelFilters'] = []
        if self.label_filters is not None:
            for k1 in self.label_filters:
                result['labelFilters'].append(k1.to_map() if k1 else None)

        result['measureList'] = []
        if self.measure_list is not None:
            for k1 in self.measure_list:
                result['measureList'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['metric'] = self.metric

        if self.metric_set is not None:
            result['metricSet'] = self.metric_set

        if self.prom_ql is not None:
            result['promQl'] = self.prom_ql

        if self.service_id_list is not None:
            result['serviceIdList'] = self.service_id_list

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        self.filter_list = []
        if m.get('filterList') is not None:
            for k1 in m.get('filterList'):
                temp_model = main_models.ApmFilterConfig()
                self.filter_list.append(temp_model.from_map(k1))

        self.label_filters = []
        if m.get('labelFilters') is not None:
            for k1 in m.get('labelFilters'):
                temp_model = main_models.UmodelLabelFilter()
                self.label_filters.append(temp_model.from_map(k1))

        self.measure_list = []
        if m.get('measureList') is not None:
            for k1 in m.get('measureList'):
                temp_model = main_models.ApmMeasureConfig()
                self.measure_list.append(temp_model.from_map(k1))

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('metricSet') is not None:
            self.metric_set = m.get('metricSet')

        if m.get('promQl') is not None:
            self.prom_ql = m.get('promQl')

        if m.get('serviceIdList') is not None:
            self.service_id_list = m.get('serviceIdList')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

