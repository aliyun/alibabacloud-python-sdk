# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class CreateProjectRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disable_development: bool = None,
        is_allow_download: int = None,
        project_description: str = None,
        project_identifier: str = None,
        project_mode: int = None,
        project_name: str = None,
        resource_manager_resource_group_id: str = None,
        tags: List[main_models.CreateProjectRequestTags] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. This parameter can be left empty.
        self.client_token = client_token
        # Specifies whether to disable the Develop role. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.disable_development = disable_development
        # Specifies whether to allow you to download the query result from DataStudio. Valid values:
        # 
        # *   **1** (default): allows you to download the query result from DataStudio.
        # *   **0**: does not allow you to download the query result from DataStudio.
        self.is_allow_download = is_allow_download
        # The description of the workspace.
        self.project_description = project_description
        # The name of the workspace. The name can contain only letters, digits, and underscores (_) and must start with a letter or digit.
        # 
        # This parameter is required.
        self.project_identifier = project_identifier
        # The mode of the workspace. For more information about the differences between the modes of workspaces, see [Differences between workspaces in basic mode and workspaces in standard mode](https://help.aliyun.com/document_detail/85772.html).
        # 
        # Valid values:
        # 
        # *   **2** (default): basic mode
        # *   **3**: standard mode
        self.project_mode = project_mode
        # The display name of the workspace.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The tags added to the workspace.
        self.tags = tags

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disable_development is not None:
            result['DisableDevelopment'] = self.disable_development

        if self.is_allow_download is not None:
            result['IsAllowDownload'] = self.is_allow_download

        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.project_mode is not None:
            result['ProjectMode'] = self.project_mode

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisableDevelopment') is not None:
            self.disable_development = m.get('DisableDevelopment')

        if m.get('IsAllowDownload') is not None:
            self.is_allow_download = m.get('IsAllowDownload')

        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('ProjectMode') is not None:
            self.project_mode = m.get('ProjectMode')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateProjectRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateProjectRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # This parameter is required.
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

