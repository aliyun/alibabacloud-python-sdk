# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserAnalyzerRequest(DaraModel):
    def __init__(
        self,
        business: str = None,
        business_app_group_id: str = None,
        business_type: str = None,
        name: str = None,
        type: str = None,
        dry_run: bool = None,
    ):
        # The name of the basic analyzer.
        self.business = business
        # The application ID for the custom model-based analyzer.
        self.business_app_group_id = business_app_group_id
        # The type of the basic analyzer. Valid values: AUTO, MODEL, SYSTEM, and USER.
        self.business_type = business_type
        # The name of the analyzer.
        self.name = name
        # The engine type. Valid values: HA3 and ES.
        self.type = type
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - true: sends a check request without creating the analyzer. The system checks the AccessKey, RAM user authorization, and required parameters.
        # 
        # - false (default): sends a regular request to create the analyzer.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business is not None:
            result['business'] = self.business

        if self.business_app_group_id is not None:
            result['businessAppGroupId'] = self.business_app_group_id

        if self.business_type is not None:
            result['businessType'] = self.business_type

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business') is not None:
            self.business = m.get('business')

        if m.get('businessAppGroupId') is not None:
            self.business_app_group_id = m.get('businessAppGroupId')

        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

