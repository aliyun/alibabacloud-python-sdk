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
        # The basic analyzer.
        self.business = business
        # The application ID of the custom analyzer.
        self.business_app_group_id = business_app_group_id
        # The basic analyzer type. Valid values: AUTO, MODEL, SYSTEM, and USER.
        self.business_type = business_type
        # The analyzer name.
        self.name = name
        # The engine type. Valid values: HA3 and ES.
        self.type = type
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # Valid values:
        # *   **true**
        # *   **false**
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

