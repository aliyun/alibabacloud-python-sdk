# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateDeliveryTaskRequest(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        external_labels: Dict[str, str] = None,
        label_filters: Dict[str, str] = None,
        label_filters_type: str = None,
        resource_group_id: str = None,
        sink_list: List[main_models.UpdateDeliveryTaskRequestSinkList] = None,
        status: str = None,
        task_description: str = None,
        task_name: str = None,
    ):
        self.data_source_id = data_source_id
        self.external_labels = external_labels
        self.label_filters = label_filters
        self.label_filters_type = label_filters_type
        self.resource_group_id = resource_group_id
        self.sink_list = sink_list
        self.status = status
        self.task_description = task_description
        self.task_name = task_name

    def validate(self):
        if self.sink_list:
            for v1 in self.sink_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.external_labels is not None:
            result['externalLabels'] = self.external_labels

        if self.label_filters is not None:
            result['labelFilters'] = self.label_filters

        if self.label_filters_type is not None:
            result['labelFiltersType'] = self.label_filters_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['sinkList'] = []
        if self.sink_list is not None:
            for k1 in self.sink_list:
                result['sinkList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('externalLabels') is not None:
            self.external_labels = m.get('externalLabels')

        if m.get('labelFilters') is not None:
            self.label_filters = m.get('labelFilters')

        if m.get('labelFiltersType') is not None:
            self.label_filters_type = m.get('labelFiltersType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.sink_list = []
        if m.get('sinkList') is not None:
            for k1 in m.get('sinkList'):
                temp_model = main_models.UpdateDeliveryTaskRequestSinkList()
                self.sink_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

class UpdateDeliveryTaskRequestSinkList(DaraModel):
    def __init__(
        self,
        sink_configs: Dict[str, str] = None,
        sink_type: str = None,
    ):
        self.sink_configs = sink_configs
        self.sink_type = sink_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sink_configs is not None:
            result['sinkConfigs'] = self.sink_configs

        if self.sink_type is not None:
            result['sinkType'] = self.sink_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sinkConfigs') is not None:
            self.sink_configs = m.get('sinkConfigs')

        if m.get('sinkType') is not None:
            self.sink_type = m.get('sinkType')

        return self

