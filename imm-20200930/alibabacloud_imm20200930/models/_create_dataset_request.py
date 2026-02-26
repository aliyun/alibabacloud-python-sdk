# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        dataset_config: main_models.DatasetConfig = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        project_name: str = None,
        template_id: str = None,
        workflow_parameters: List[main_models.WorkflowParameter] = None,
    ):
        self.dataset_config = dataset_config
        # The maximum number of bindings per dataset. The range is 1~10, with a default value of 10.
        self.dataset_max_bind_count = dataset_max_bind_count
        # The maximum number of metadata entities in each dataset. The default value is 10000000000.
        self.dataset_max_entity_count = dataset_max_entity_count
        # The maximum number of files in each dataset. The range is 1~100000000, with a default value of 100000000.
        self.dataset_max_file_count = dataset_max_file_count
        # The maximum number of metadata relationships in each dataset. The default value is 100000000000.
        self.dataset_max_relation_count = dataset_max_relation_count
        # The maximum total size of files in each dataset. Once the limit is exceeded, no more indexes can be added. The default value is 90000000000000000, in bytes.
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # The name of the dataset, which must be unique under the same Project. Naming rules are as follows:
        # - Length should be 1~128 characters.
        # - Can only contain English letters, numbers, hyphens (-), and underscores (_).
        # - Must start with an English letter or underscore (_).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # Description of the dataset. The length should be 1~256 English or Chinese characters, with a default value of empty.
        self.description = description
        # The name of the project. For more information on how to obtain it, see [Create Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Workflow template ID. For more information, see [Workflow Templates and Operators](https://help.aliyun.com/document_detail/466304.html). The default value is empty.
        self.template_id = template_id
        # Invalid parameter.
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

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        result['WorkflowParameters'] = []
        if self.workflow_parameters is not None:
            for k1 in self.workflow_parameters:
                result['WorkflowParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.workflow_parameters = []
        if m.get('WorkflowParameters') is not None:
            for k1 in m.get('WorkflowParameters'):
                temp_model = main_models.WorkflowParameter()
                self.workflow_parameters.append(temp_model.from_map(k1))

        return self

