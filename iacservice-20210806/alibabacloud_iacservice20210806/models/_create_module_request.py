# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class CreateModuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_info: main_models.CreateModuleRequestGroupInfo = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        tags: List[main_models.CreateModuleRequestTags] = None,
        version_strategy: str = None,
    ):
        # The idempotency parameter. We recommend that you use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the template. The description can be up to 256 characters in length.
        self.description = description
        # The project group information to which the template belongs.
        self.group_info = group_info
        # The name of the template. The name must meet the following requirements:
        # - The name must be 2 to 128 characters in length.
        # - The name can contain letters, digits, Chinese characters, hyphens (-), underscores (_), and periods (.). The name cannot start or end with a hyphen, underscore, or period.
        # - The name must be unique among all templates under the current account.
        # 
        # This parameter is required.
        self.name = name
        # The source from which the template is created. Valid values:
        # - OSS: imports from a ZIP file stored in OSS.
        # - Registry: creates from a module in the template registry.
        # - ExportTask: references a template exported by a resource export task.
        # - Editor: creates a blank template that supports online editing.
        # - Upload: uploads a local template file to generate the template.
        # 
        # This parameter is required.
        self.source = source
        # The path of the template source. This parameter takes effect when source is set to Registry, OSS, or ExportTask.
        # - If source is set to Registry, the value is in the format of \\<workspace name>/\\<module name>:\\<module version>. Example: terraform-alicloud-modules/rds:1.0.0.
        # - If source is set to OSS, the value is in the format of oss::<file URL>. The file must be a ZIP file. Example: oss::https://terraform-pipeline.oss-eu-central-1.aliyuncs.com/code.zip.
        # - If source is set to ExportTask, the value is in the format of \\<export task ID>:\\<exported version>. Example: ex-3b6cb9fa4751afff298da723c24ac:v1.
        # - If source is set to Editor or Upload, leave this parameter empty.
        self.source_path = source_path
        # The path of the State file that corresponds to the template. This parameter is valid only when source is set to OSS.
        # The value is in the format of oss::\\<OSS file path>/terraform.tfstate.
        self.state_path = state_path
        # The list of tags for the template.
        self.tags = tags
        # The version generation strategy. Valid values:
        # 
        # - Manual: manually generates a version. This is the default value.
        # - SourcePathUpdated: generates a new version when sourcePath is modified.
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
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
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.CreateModuleRequestGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateModuleRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')

        return self

class CreateModuleRequestTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the template.
        self.tag_key = tag_key
        # The tag value of the template.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class CreateModuleRequestGroupInfo(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # The project ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.project_id is not None:
            result['projectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        return self

