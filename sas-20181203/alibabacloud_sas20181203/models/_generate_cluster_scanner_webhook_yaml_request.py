# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateClusterScannerWebhookYamlRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        webhook_open: int = None,
    ):
        # The ID of the container cluster.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) API to obtain this parameter from the ClusterId field.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Indicates whether the incremental scan switch is enabled. Values:
        # - **0**: Not enabled
        # - **1**: Enabled
        self.webhook_open = webhook_open

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.webhook_open is not None:
            result['WebhookOpen'] = self.webhook_open

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('WebhookOpen') is not None:
            self.webhook_open = m.get('WebhookOpen')

        return self

