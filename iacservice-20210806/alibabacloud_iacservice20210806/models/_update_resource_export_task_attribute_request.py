# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceExportTaskAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        export_to_module: main_models.UpdateResourceExportTaskAttributeRequestExportToModule = None,
        include_rules: List[main_models.UpdateResourceExportTaskAttributeRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[main_models.UpdateResourceExportTaskAttributeRequestVariables] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.export_to_module = export_to_module
        self.include_rules = include_rules
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
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
            temp_model = main_models.UpdateResourceExportTaskAttributeRequestExportToModule()
            self.export_to_module = temp_model.from_map(m.get('exportToModule'))

        self.include_rules = []
        if m.get('includeRules') is not None:
            for k1 in m.get('includeRules'):
                temp_model = main_models.UpdateResourceExportTaskAttributeRequestIncludeRules()
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
                temp_model = main_models.UpdateResourceExportTaskAttributeRequestVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateResourceExportTaskAttributeRequestVariables(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
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

class UpdateResourceExportTaskAttributeRequestIncludeRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
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

class UpdateResourceExportTaskAttributeRequestExportToModule(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
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

