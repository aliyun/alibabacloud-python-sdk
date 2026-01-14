# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateModuleRequest(DaraModel):
    def __init__(
        self,
        generate_source: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        syntax: str = None,
        template: str = None,
        terraform_provider_version: str = None,
        terraform_resource_type: str = None,
    ):
        self.generate_source = generate_source
        self.parameters = parameters
        self.region_id = region_id
        self.syntax = syntax
        self.template = template
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_type = terraform_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_source is not None:
            result['generateSource'] = self.generate_source

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.syntax is not None:
            result['syntax'] = self.syntax

        if self.template is not None:
            result['template'] = self.template

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateSource') is not None:
            self.generate_source = m.get('generateSource')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('syntax') is not None:
            self.syntax = m.get('syntax')

        if m.get('template') is not None:
            self.template = m.get('template')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')

        return self

