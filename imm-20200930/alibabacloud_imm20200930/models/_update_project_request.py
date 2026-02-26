# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class UpdateProjectRequest(DaraModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        service_role: str = None,
        tag: List[main_models.UpdateProjectRequestTag] = None,
        template_id: str = None,
    ):
        # The maximum number of bindings for each dataset. Valid values: 1 to 10.
        self.dataset_max_bind_count = dataset_max_bind_count
        # The maximum number of metadata entities in each dataset.
        # 
        # >  This is a precautionary setting that does not impose practical limitations.
        self.dataset_max_entity_count = dataset_max_entity_count
        # The maximum number of files in each dataset. Valid values: 1 to 100000000.
        self.dataset_max_file_count = dataset_max_file_count
        # The maximum number of metadata relationships in a dataset.
        # 
        # >  This is a precautionary setting that does not impose practical limitations.
        self.dataset_max_relation_count = dataset_max_relation_count
        # The maximum size of files in each dataset. If the maximum size is exceeded, indexes can no longer be added. Unit: bytes.
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # The description of the project. The description must be 1 to 256 characters in length.
        self.description = description
        # The maximum number of datasets in the project. Valid values: 1 to 1000000000.
        self.project_max_dataset_count = project_max_dataset_count
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the Resource Access Management (RAM) role. You must grant the RAM role to Intelligent Media Management (IMM) before IMM can access other cloud resources such as Object Storage Service (OSS).
        # 
        # You can also create a custom service role in the RAM console and grant the required permissions to the role based on your business requirements. For more information, see [Create a regular service role](https://help.aliyun.com/document_detail/116800.html) and [Grant permissions to a role](https://help.aliyun.com/document_detail/116147.html).
        self.service_role = service_role
        # The tags.
        self.tag = tag
        # The ID of the workflow template. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateProjectRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class UpdateProjectRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

