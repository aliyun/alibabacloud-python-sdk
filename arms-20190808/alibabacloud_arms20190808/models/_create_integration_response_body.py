# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateIntegrationResponseBody(DaraModel):
    def __init__(
        self,
        integration: main_models.CreateIntegrationResponseBodyIntegration = None,
        request_id: str = None,
    ):
        # The returned information about the alert integration.
        self.integration = integration
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.integration:
            self.integration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integration is not None:
            result['Integration'] = self.integration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Integration') is not None:
            temp_model = main_models.CreateIntegrationResponseBodyIntegration()
            self.integration = temp_model.from_map(m.get('Integration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateIntegrationResponseBodyIntegration(DaraModel):
    def __init__(
        self,
        auto_recover: bool = None,
        description: str = None,
        integration_id: int = None,
        integration_name: str = None,
        integration_product_type: str = None,
        recover_time: int = None,
    ):
        # Indicates whether alert events are automatically cleared. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.auto_recover = auto_recover
        # The description of the alert integration.
        self.description = description
        # The ID of the alert integration.
        self.integration_id = integration_id
        # The name of the alert integration.
        self.integration_name = integration_name
        # The service of the alert integration. Valid values:
        # 
        # *   CLOUD_MONITOR: CloudMonitor
        # *   LOG_SERVICE: Log Service
        self.integration_product_type = integration_product_type
        # The period of time within which alert events are automatically cleared. Unit: seconds. Default value: 300.
        self.recover_time = recover_time

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

        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type

        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')

        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')

        return self

