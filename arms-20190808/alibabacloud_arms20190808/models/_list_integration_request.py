# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntegrationRequest(DaraModel):
    def __init__(
        self,
        integration_name: str = None,
        integration_product_type: str = None,
        is_detail: bool = None,
        page: int = None,
        size: int = None,
    ):
        # The name of the alert integration.
        self.integration_name = integration_name
        # The type of the alert integration. Valid values:
        # 
        # *   CLOUD_MONITOR: CloudMonitor
        # *   LOG_SERVICE: Log Service
        # 
        # This parameter is required.
        self.integration_product_type = integration_product_type
        # Specifies whether to display the details of each alert integration:
        # 
        # *   true
        # *   false
        self.is_detail = is_detail
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The number of alert integrations to return on each page.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type

        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')

        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

