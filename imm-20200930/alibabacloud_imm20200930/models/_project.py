# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Project(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_count: int = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        engine_concurrency: int = None,
        file_count: int = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        project_queries_per_second: int = None,
        service_role: str = None,
        tags: List[main_models.ProjectTags] = None,
        template_id: str = None,
        total_file_size: int = None,
        update_time: str = None,
    ):
        # The timestamp when the project was created. The timestamp is in the RFC3339Nano format.
        self.create_time = create_time
        # The current number of datasets in the project.
        self.dataset_count = dataset_count
        # The maximum number of bindings that a dataset can have. Valid values: 1 to 10. Default value: 10.
        self.dataset_max_bind_count = dataset_max_bind_count
        # The maximum number of metadata entities in a dataset. Default value: 10000000000.
        # 
        # >  This parameter is reserved and does not actually apply a limit.
        self.dataset_max_entity_count = dataset_max_entity_count
        # The maximum number of files in a dataset. Valid values: 1 to 100000000. Default value: 100000000.
        self.dataset_max_file_count = dataset_max_file_count
        # The maximum number of metadata relationships in a dataset. Default value: 100000000000.
        # 
        # >  This parameter is reserved and does not actually apply a limit.
        self.dataset_max_relation_count = dataset_max_relation_count
        # The maximum total file size for a dataset. If the total file size exceeds this limit, indexes can no longer be added. Default value: 90000000000000000. Unit: bytes.
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # The project description.
        self.description = description
        # The maximum number of tasks that the project can process per second. This corresponds to the maximum number of operators that can run in parallel in the project. Default value: 100.
        # 
        # *   If the number of synchronous tasks that run in parallel exceeds this limit, the task execution time will be extended until a timeout occurs.
        # *   If the number of asynchronous tasks that run in parallel exceeds this limit, the tasks will be queued. This causes delayed task completion. If a task remains in the queue for longer than the specified time limit (usually dozens of seconds), the task will fail.
        self.engine_concurrency = engine_concurrency
        # The current number of files in the project.
        self.file_count = file_count
        # The maximum number of datasets that a project can contain. Valid values: 1 to 1000000000. Default value: 1000000000.
        self.project_max_dataset_count = project_max_dataset_count
        # The name of the project.
        self.project_name = project_name
        # The maximum number of requests that can be processed by the project per second. This corresponds to the maximum number of API operations that can be called in the project per second. Default value: 100.
        self.project_queries_per_second = project_queries_per_second
        # The service role.
        self.service_role = service_role
        # The tag list.
        self.tags = tags
        # The ID of the workflow template.
        self.template_id = template_id
        # The current total size of files in the project. Unit: bytes.
        self.total_file_size = total_file_size
        # The timestamp when the project was last modified. The timestamp is in the RFC3339Nano format.
        # 
        # >  If a project is not modified after it is created, the timestamp when the project was created is the same as the timestamp when the project was last modified.
        self.update_time = update_time

    def validate(self):
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
            result['CreateTime'] = self.create_time

        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count

        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count

        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count

        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count

        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count

        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')

        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')

        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')

        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')

        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')

        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ProjectTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ProjectTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

