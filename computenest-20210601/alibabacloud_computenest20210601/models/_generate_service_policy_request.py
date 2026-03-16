# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GenerateServicePolicyRequest(DaraModel):
    def __init__(
        self,
        operation_types: List[str] = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The type of operation N for which you want to generate the policy information.
        # 
        # Valid values:
        # 
        # *   CreateServiceInstance: creates a serviceInstance by calling the CreateServiceInstance operation.
        # *   UpdateServiceInstance: updates a serviceInstance by calling the UpdateServiceInstance operation.
        # *   DeleteServiceInstance: deletes a serviceInstance by calling the DeleteServiceInstance operation.
        # 
        # >  The default value is the combination of all valid values.
        self.operation_types = operation_types
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The name of the template.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

