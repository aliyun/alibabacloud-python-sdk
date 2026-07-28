# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class CreateResourceExportTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        export_to_module: main_models.CreateResourceExportTaskRequestExportToModule = None,
        include_rules: List[main_models.CreateResourceExportTaskRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[main_models.CreateResourceExportTaskRequestVariables] = None,
    ):
        # The idempotency token. Format: [0-9a-zA-Z-]{1,64}. We recommend that you use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the resource export task.
        self.description = description
        # Saves the exported template as a module. If this parameter is not specified, the template is automatically saved in the Registry.
        self.export_to_module = export_to_module
        # The list of inclusion rules used when exporting resources.
        self.include_rules = include_rules
        # The name of the resource export task. The name must meet the following requirements:
        # 
        # - The name must be 3 to 63 characters in length.
        # - The name can contain letters, digits, Chinese characters, hyphens (-), underscores (_), and periods (.). The name cannot start or end with a hyphen, underscore, or period.
        # - The name must be unique among resource export tasks within the current account.
        # 
        # This parameter is required.
        self.name = name
        # The RAM role (1 to 128 characters). The system assumes this role to execute the template when a new job is triggered. This parameter is required when the job trigger method is not manual.
        self.ram_role = ram_role
        # The Terraform provider version. Call **ListTerraformProviderVersions** to view the list of supported versions. Default value: the latest version.
        self.terraform_provider_version = terraform_provider_version
        # The Terraform version. Call **ListAvailableTerraformVersions** to view the list of supported versions. Default value: 1.5.7.
        self.terraform_version = terraform_version
        # The trigger strategy. Valid values:
        # - Auto: triggered when rules are modified or the trigger strategy is changed to Auto.
        # - Manual: manually triggered.
        # 
        # Default value: Manual.
        self.trigger_strategy = trigger_strategy
        # The list of variables. Exported resource parameters are set as variables.
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for v1 in self.include_rules:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
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

        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()

        result['includeRules'] = []
        if self.include_rules is not None:
            for k1 in self.include_rules:
                result['includeRules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version

        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exportToModule') is not None:
            temp_model = main_models.CreateResourceExportTaskRequestExportToModule()
            self.export_to_module = temp_model.from_map(m.get('exportToModule'))

        self.include_rules = []
        if m.get('includeRules') is not None:
            for k1 in m.get('includeRules'):
                temp_model = main_models.CreateResourceExportTaskRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')

        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.CreateResourceExportTaskRequestVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class CreateResourceExportTaskRequestVariables(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        # The list of properties of the Terraform resource that corresponds to the resource type.
        self.properties = properties
        # The resource type. Call **ListResourceTypes** to view the list of supported resources.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties is not None:
            result['properties'] = self.properties

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class CreateResourceExportTaskRequestIncludeRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The name of the inclusion rule used when exporting resources. Valid values:
        # 
        # - ResourceType: required. The resource type. Call **ListResourceTypes** to view the list of supported resources. Example: ALIYUN::VPC::VPC.
        # - RegionId: required. The region to which the resource belongs. Only one region is supported. Example: cn-chengdu.
        # - \\<ResourceType>:Id: the resource ID. Example: ALIYUN::VPC::VPC:Id.
        # - ResourceGroupId: the resource group ID. Example: rg-1234.
        # - ZoneId: the zone to which the resource belongs. Only one zone is supported. Example: cn-hangzhou-h.
        # 
        # By default, multiple filter conditions are evaluated using the AND operator. A resource is considered a match only when all filter conditions are met.
        self.key = key
        # The list of values for the inclusion rule used when exporting resources.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateResourceExportTaskRequestExportToModule(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        # The module type in which the exported template is saved. Valid values:
        # 
        # - OSS: OSS.
        # - Registry: Terraform Registry.
        self.source = source
        # The path for saving the template content. Set this parameter when source is set to OSS.
        self.source_path = source_path
        # The path for saving the template state file. Set this parameter when source is set to OSS.
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        return self

