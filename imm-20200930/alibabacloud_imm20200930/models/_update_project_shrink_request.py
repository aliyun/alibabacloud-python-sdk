# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProjectShrinkRequest(DaraModel):
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
        tag_shrink: str = None,
        template_id: str = None,
    ):
        # The maximum number of bindings for each dataset. Valid values: 1 to 10.
        self.dataset_max_bind_count = dataset_max_bind_count
        # The maximum number of metadata entities in each dataset.
        # >This is a reserved parameter and is not enforced during use.
        self.dataset_max_entity_count = dataset_max_entity_count
        # The maximum number of files in each dataset. Valid values: 1 to 100000000.
        self.dataset_max_file_count = dataset_max_file_count
        # The maximum number of metadata relationships in each dataset.
        # >This is a reserved parameter and is not enforced during use.
        self.dataset_max_relation_count = dataset_max_relation_count
        # The maximum total file size in each dataset. After the limit is exceeded, no more indexes can be added. Unit: bytes.
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # The project description. The description must be 1 to 256 characters in length.
        self.description = description
        # The maximum number of datasets in the project. Valid values: 1 to 1000000000.
        self.project_max_dataset_count = project_max_dataset_count
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The service role that grants Intelligent Media Management (IMM) permissions to access other cloud resources such as Object Storage Service (OSS).
        # 
        # To customize a service role, create a regular service role in the Resource Access Management (RAM) console and grant permissions to the role. For more information, see [Create a regular service role](https://help.aliyun.com/document_detail/116800.html) and [Grant permissions to a role](https://help.aliyun.com/document_detail/116147.html).
        self.service_role = service_role
        # The list of tags.
        self.tag_shrink = tag_shrink
        # The workflow template ID. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        self.template_id = template_id

    def validate(self):
        pass

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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

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

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

