# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCaInstanceCrlAddressResponseBody(DaraModel):
    def __init__(
        self,
        ca_instance_status: str = None,
        crl_url: str = None,
        hash_code: str = None,
        next_update_time: str = None,
        request_id: str = None,
    ):
        # The status of the CA instance.
        self.ca_instance_status = ca_instance_status
        # The cron expression.
        self.crl_url = crl_url
        # Used to identify whether there are new revoked certificates in the revocation list.
        self.hash_code = hash_code
        # The next update time of the revocation list.
        self.next_update_time = next_update_time
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_instance_status is not None:
            result['CaInstanceStatus'] = self.ca_instance_status

        if self.crl_url is not None:
            result['CrlUrl'] = self.crl_url

        if self.hash_code is not None:
            result['HashCode'] = self.hash_code

        if self.next_update_time is not None:
            result['NextUpdateTime'] = self.next_update_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaInstanceStatus') is not None:
            self.ca_instance_status = m.get('CaInstanceStatus')

        if m.get('CrlUrl') is not None:
            self.crl_url = m.get('CrlUrl')

        if m.get('HashCode') is not None:
            self.hash_code = m.get('HashCode')

        if m.get('NextUpdateTime') is not None:
            self.next_update_time = m.get('NextUpdateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

