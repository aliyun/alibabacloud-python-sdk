# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppServiceResponseBody(DaraModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        region: str = None,
        request_id: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
    ):
        # The public endpoint of the service.
        self.internet_endpoint = internet_endpoint
        # The internal endpoint of the service.
        self.intranet_endpoint = intranet_endpoint
        # The region ID of the service.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The service state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

