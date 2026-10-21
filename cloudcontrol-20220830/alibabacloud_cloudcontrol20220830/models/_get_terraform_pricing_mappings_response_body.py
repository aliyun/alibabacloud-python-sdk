# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class GetTerraformPricingMappingsResponseBody(DaraModel):
    def __init__(
        self,
        mapping_version: str = None,
        mappings: List[main_models.GetTerraformPricingMappingsResponseBodyMappings] = None,
        missing_resource_types: List[str] = None,
        request_id: str = None,
        schema_version: str = None,
        unsupported_resource_types: List[str] = None,
    ):
        # The mapping content version, which is the timestamp of the most recent data change. Consumers can use this value for caching and auditing.
        self.mapping_version = mapping_version
        # The list of matched mappings. Each item contains a resourceType and pricingTargets, which include pricing targets and parameter extraction rules. The rules reference Terraform plan resource properties by using $after/$before.
        self.mappings = mappings
        # The resource types in the request that do not have registered mappings. Consumers must treat these as unknown cost. Do not assume they are free.
        self.missing_resource_types = missing_resource_types
        # Id of the request
        self.request_id = request_id
        # The schema version of the mapping catalog. The current version is 1.0. Consumers use this value to determine compatibility.
        self.schema_version = schema_version
        # The resource types that are confirmed to not support pricing, such as free resources or resources without a pricing interface. These are different from missing resource types.
        self.unsupported_resource_types = unsupported_resource_types

    def validate(self):
        if self.mappings:
            for v1 in self.mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mapping_version is not None:
            result['mappingVersion'] = self.mapping_version

        result['mappings'] = []
        if self.mappings is not None:
            for k1 in self.mappings:
                result['mappings'].append(k1.to_map() if k1 else None)

        if self.missing_resource_types is not None:
            result['missingResourceTypes'] = self.missing_resource_types

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.unsupported_resource_types is not None:
            result['unsupportedResourceTypes'] = self.unsupported_resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mappingVersion') is not None:
            self.mapping_version = m.get('mappingVersion')

        self.mappings = []
        if m.get('mappings') is not None:
            for k1 in m.get('mappings'):
                temp_model = main_models.GetTerraformPricingMappingsResponseBodyMappings()
                self.mappings.append(temp_model.from_map(k1))

        if m.get('missingResourceTypes') is not None:
            self.missing_resource_types = m.get('missingResourceTypes')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('unsupportedResourceTypes') is not None:
            self.unsupported_resource_types = m.get('unsupportedResourceTypes')

        return self

class GetTerraformPricingMappingsResponseBodyMappings(DaraModel):
    def __init__(
        self,
        pricing_targets: List[Dict[str, Any]] = None,
        resource_type: str = None,
    ):
        # The list of pricing targets. Each item contains actions (create/update), popCode/popVersion/apiName, pricingUnit, params (parameter extraction rules: from=$after.xxx / const / default / expand), and when/whenChanged conditions.
        self.pricing_targets = pricing_targets
        # The Terraform resource type, such as alicloud_instance.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pricing_targets is not None:
            result['pricingTargets'] = self.pricing_targets

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pricingTargets') is not None:
            self.pricing_targets = m.get('pricingTargets')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

