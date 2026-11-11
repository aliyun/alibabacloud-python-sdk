# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetModuleVersionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        version: main_models.GetModuleVersionResponseBodyVersion = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The version details.
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.version is not None:
            result['version'] = self.version.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('version') is not None:
            temp_model = main_models.GetModuleVersionResponseBodyVersion()
            self.version = temp_model.from_map(m.get('version'))

        return self

class GetModuleVersionResponseBodyVersion(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        terraform_context: Dict[str, Any] = None,
        version_strategy: str = None,
    ):
        # The time when the version was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.create_time = create_time
        # The version description.
        self.description = description
        # The template ID.
        self.module_id = module_id
        # The template version number.
        self.module_version = module_version
        # The version name.
        self.name = name
        # The source of the version. Valid values:
        # 
        # - OSS: imported from OSS
        # - Registry: created by using a template in the template center
        # - ExportTask: referenced from a template exported by a resource export task
        # - Upload: uploaded as a file
        # - Shared: cloned from a shared template
        # - Editor: edited online
        self.source = source
        # The path value of the version source.
        # 
        # - If the source is Registry, the value is in the <Workspace name>/<Module name>:<Module version> format. Example: terraform-alicloud-modules/rds:1.0.0.
        # - If the source is OSS, the value is in the oss::<File URL> format. Example: oss::https://terraform-pipeline.oss-eu-central-1.aliyuncs.com/code.zip.
        # - If the source is ExportTask, the value is in the <Export task ID>:<Exported version> format. Example: ex-3b6cb9fa4751afff298da723c24ac:v1.
        self.source_path = source_path
        # The path value of the state file corresponding to the template. Currently, only OSS paths are supported. The value is in the oss::<OSS path of the file>/terraform.tfstate format.
        self.state_path = state_path
        # The Terraform content.
        self.terraform_context = terraform_context
        # The version generation strategy. Valid values:
        # 
        # - Manual: manually generated version (default)
        # - SourcePathUpdated: a new version is generated when sourcePath is modified
        self.version_strategy = version_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context

        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')

        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')

        return self

