# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCmsServiceResponseBody(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        error_code: str = None,
        request_id: str = None,
    ):
        # Indicates whether the service or product is activated.
        self.enabled = enabled
        # PROM_NOT_OPEN: Prometheus is not activated.SLS_NOT_OPEN: Simple Log Service (SLS), a dependency of Prometheus, is not activated.CMS_SLR_NOT_EXIST: The service-linked role (SLR) for CloudMonitor does not exist.SLS_SLR_NOT_EXIST: The SLR for SLS does not exist.
        self.error_code = error_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

