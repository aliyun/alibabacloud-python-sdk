# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Dataset(DaraModel):
    def __init__(
        self,
        bind_count: int = None,
        create_time: str = None,
        dataset_config: main_models.DatasetConfig = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        file_count: int = None,
        project_name: str = None,
        template_id: str = None,
        total_file_size: int = None,
        update_time: str = None,
        workflow_parameters: List[main_models.WorkflowParameter] = None,
    ):
        # The current number of OSS buckets that are bound to the dataset.
        self.bind_count = bind_count
        # The timestamp when the dataset was created. The timestamp must be in the RFC3339Nano format.
        self.create_time = create_time
        self.dataset_config = dataset_config
        # The maximum number of bindings for the dataset.
        self.dataset_max_bind_count = dataset_max_bind_count
        # The maximum number of metadata entities for the dataset.
        self.dataset_max_entity_count = dataset_max_entity_count
        # The maximum number of files for the dataset.
        self.dataset_max_file_count = dataset_max_file_count
        # The maximum number of metadata relationships for the dataset.
        self.dataset_max_relation_count = dataset_max_relation_count
        # The maximum total size of files in the dataset. Unit: bytes.
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The dataset description.
        self.description = description
        # The current number of files in the dataset.
        self.file_count = file_count
        # The name of the project.
        self.project_name = project_name
        # The ID of the workflow template.
        self.template_id = template_id
        # The total size of files in the dataset. Unit: bytes.
        self.total_file_size = total_file_size
        # The timestamp when the dataset was last modified. The timestamp must be in the RFC3339Nano format.
        # 
        # >  If a dataset has never been modified after it was created, the timestamp when the dataset was last modified is the same as the timestamp when the dataset was created.
        self.update_time = update_time
        # 自定义参数
        self.workflow_parameters = workflow_parameters

    def validate(self):
        if self.dataset_config:
            self.dataset_config.validate()
        if self.workflow_parameters:
            for v1 in self.workflow_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_config is not None:
            result['DatasetConfig'] = self.dataset_config.to_map()

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

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.description is not None:
            result['Description'] = self.description

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        result['WorkflowParameters'] = []
        if self.workflow_parameters is not None:
            for k1 in self.workflow_parameters:
                result['WorkflowParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetConfig') is not None:
            temp_model = main_models.DatasetConfig()
            self.dataset_config = temp_model.from_map(m.get('DatasetConfig'))

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

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        self.workflow_parameters = []
        if m.get('WorkflowParameters') is not None:
            for k1 in m.get('WorkflowParameters'):
                temp_model = main_models.WorkflowParameter()
                self.workflow_parameters.append(temp_model.from_map(k1))

        return self

