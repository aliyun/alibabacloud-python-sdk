# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeStsGrantStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sts_grant: main_models.DescribeStsGrantStatusResponseBodyStsGrant = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The authorization status of Anti-DDoS Pro or Anti-DDoS Premium.
        self.sts_grant = sts_grant

    def validate(self):
        if self.sts_grant:
            self.sts_grant.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sts_grant is not None:
            result['StsGrant'] = self.sts_grant.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StsGrant') is not None:
            temp_model = main_models.DescribeStsGrantStatusResponseBodyStsGrant()
            self.sts_grant = temp_model.from_map(m.get('StsGrant'))

        return self

class DescribeStsGrantStatusResponseBodyStsGrant(DaraModel):
    def __init__(
        self,
        status: int = None,
    ):
        # The authorization status. Valid values:
        # 
        # *   **0**: Anti-DDoS Pro or Anti-DDoS Premium is not authorized to access other cloud services.
        # *   **1**: Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

