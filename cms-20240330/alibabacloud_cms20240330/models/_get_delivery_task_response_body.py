# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetDeliveryTaskResponseBody(DaraModel):
    def __init__(
        self,
        delivery_task: main_models.GetDeliveryTaskResponseBodyDeliveryTask = None,
        request_id: str = None,
    ):
        self.delivery_task = delivery_task
        self.request_id = request_id

    def validate(self):
        if self.delivery_task:
            self.delivery_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_task is not None:
            result['deliveryTask'] = self.delivery_task.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryTask') is not None:
            temp_model = main_models.GetDeliveryTaskResponseBodyDeliveryTask()
            self.delivery_task = temp_model.from_map(m.get('deliveryTask'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDeliveryTaskResponseBodyDeliveryTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_id: str = None,
        external_labels: Dict[str, str] = None,
        extra_info: main_models.GetDeliveryTaskResponseBodyDeliveryTaskExtraInfo = None,
        label_filters: Dict[str, str] = None,
        label_filters_type: str = None,
        region_id: str = None,
        sink_list: List[main_models.GetDeliveryTaskResponseBodyDeliveryTaskSinkList] = None,
        status: str = None,
        tags: List[main_models.GetDeliveryTaskResponseBodyDeliveryTaskTags] = None,
        task_description: str = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.data_source_id = data_source_id
        self.external_labels = external_labels
        self.extra_info = extra_info
        self.label_filters = label_filters
        self.label_filters_type = label_filters_type
        self.region_id = region_id
        self.sink_list = sink_list
        self.status = status
        self.tags = tags
        self.task_description = task_description
        self.task_id = task_id
        self.task_name = task_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.sink_list:
            for v1 in self.sink_list:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.external_labels is not None:
            result['externalLabels'] = self.external_labels

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info.to_map()

        if self.label_filters is not None:
            result['labelFilters'] = self.label_filters

        if self.label_filters_type is not None:
            result['labelFiltersType'] = self.label_filters_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        result['sinkList'] = []
        if self.sink_list is not None:
            for k1 in self.sink_list:
                result['sinkList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('externalLabels') is not None:
            self.external_labels = m.get('externalLabels')

        if m.get('extraInfo') is not None:
            temp_model = main_models.GetDeliveryTaskResponseBodyDeliveryTaskExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        if m.get('labelFilters') is not None:
            self.label_filters = m.get('labelFilters')

        if m.get('labelFiltersType') is not None:
            self.label_filters_type = m.get('labelFiltersType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        self.sink_list = []
        if m.get('sinkList') is not None:
            for k1 in m.get('sinkList'):
                temp_model = main_models.GetDeliveryTaskResponseBodyDeliveryTaskSinkList()
                self.sink_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetDeliveryTaskResponseBodyDeliveryTaskTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDeliveryTaskResponseBodyDeliveryTaskTags(DaraModel):
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

class GetDeliveryTaskResponseBodyDeliveryTaskSinkList(DaraModel):
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

class GetDeliveryTaskResponseBodyDeliveryTaskExtraInfo(DaraModel):
    def __init__(
        self,
        task_name_list: List[str] = None,
    ):
        self.task_name_list = task_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_name_list is not None:
            result['taskNameList'] = self.task_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskNameList') is not None:
            self.task_name_list = m.get('taskNameList')

        return self

