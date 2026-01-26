# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIntegrationRequest(DaraModel):
    def __init__(
        self,
        auto_recover: bool = None,
        description: str = None,
        integration_name: str = None,
        integration_product_type: str = None,
        recover_time: int = None,
        region_id: str = None,
    ):
        # Specifies whether to automatically clear alert events. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.auto_recover = auto_recover
        # The description of the alert integration.
        self.description = description
        # The name of the alert integration.
        # 
        # This parameter is required.
        self.integration_name = integration_name
        # The service of the alert integration. Valid values:
        # 
        # *   CLOUD_MONITOR: CloudMonitor
        # *   LOG_SERVICE: Log Service
        # 
        # This parameter is required.
        self.integration_product_type = integration_product_type
        # The period of time within which alert events are automatically cleared. Unit: seconds. Default value: 300.
        self.recover_time = recover_time
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover

        if self.description is not None:
            result['Description'] = self.description

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type

        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')

        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

