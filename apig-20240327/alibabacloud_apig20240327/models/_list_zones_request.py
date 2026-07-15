# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListZonesRequest(DaraModel):
    def __init__(
        self,
        gateway_edition: str = None,
    ):
        # The target gateway edition for querying zones. Valid values:
        # - Professional: standard gateway. This is the default value.
        # - ServerlessV2: API multi-tenant Serverless V2.
        # 
        # If this parameter is not specified, Professional is used.
        self.gateway_edition = gateway_edition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_edition is not None:
            result['gatewayEdition'] = self.gateway_edition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayEdition') is not None:
            self.gateway_edition = m.get('gatewayEdition')

        return self

