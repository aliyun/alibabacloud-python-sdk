# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOpsNoticeShrinkRequest(DaraModel):
    def __init__(
        self,
        attributes_shrink: str = None,
        category: str = None,
        client_token: str = None,
        content: str = None,
        region_id: str = None,
        service_id: str = None,
        service_version: List[str] = None,
        severity: str = None,
        solutions: str = None,
        type: str = None,
    ):
        # The properties of the O\\&M item.
        self.attributes_shrink = attributes_shrink
        # The category of the notice. Valid values:
        # 
        # - Availability
        # 
        # - Cost
        # 
        # - Performance
        # 
        # - Recovery
        # 
        # - Security
        # 
        # This parameter is required.
        self.category = category
        # A client token to ensure that the request is idempotent. Generate a unique token for each request. The token can contain only ASCII characters. Note: If you do not set this parameter, the system uses the RequestId as the ClientToken. The RequestId may be different for each request.
        self.client_token = client_token
        # The content of the notice.
        # 
        # This parameter is required.
        self.content = content
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        self.service_id = service_id
        # The service versions to which the notice applies.
        self.service_version = service_version
        # The severity level of the notice. Valid values:
        # 
        # - Critical
        # 
        # - High
        # 
        # - Medium
        # 
        # - Low
        # 
        # This parameter is required.
        self.severity = severity
        # The solution.
        self.solutions = solutions
        # The type of the notice. Valid values:
        # 
        # - ServiceInstanceUpgrade: Upgrade
        # 
        # - VulnerabilityFix: Vulnerability
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink

        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.solutions is not None:
            result['Solutions'] = self.solutions

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

