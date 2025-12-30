# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryDomainTransferStatusResponseBody(DaraModel):
    def __init__(
        self,
        domain_transfer_status: List[main_models.QueryDomainTransferStatusResponseBodyDomainTransferStatus] = None,
        request_id: str = None,
    ):
        self.domain_transfer_status = domain_transfer_status
        self.request_id = request_id

    def validate(self):
        if self.domain_transfer_status:
            for v1 in self.domain_transfer_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTransferStatus'] = []
        if self.domain_transfer_status is not None:
            for k1 in self.domain_transfer_status:
                result['DomainTransferStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_transfer_status = []
        if m.get('DomainTransferStatus') is not None:
            for k1 in m.get('DomainTransferStatus'):
                temp_model = main_models.QueryDomainTransferStatusResponseBodyDomainTransferStatus()
                self.domain_transfer_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDomainTransferStatusResponseBodyDomainTransferStatus(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_status_description: str = None,
    ):
        self.domain_name = domain_name
        self.domain_status_description = domain_status_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status_description is not None:
            result['DomainStatusDescription'] = self.domain_status_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatusDescription') is not None:
            self.domain_status_description = m.get('DomainStatusDescription')

        return self

