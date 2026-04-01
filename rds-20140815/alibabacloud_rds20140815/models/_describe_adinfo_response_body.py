# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeADInfoResponseBody(DaraModel):
    def __init__(
        self,
        addns: str = None,
        adserver_ip_address: str = None,
        adstatus: str = None,
        abnormal_reason: str = None,
        request_id: str = None,
        user_name: str = None,
    ):
        # The DNS information about the AD domain.
        self.addns = addns
        # The service IP address of the AD domain.
        self.adserver_ip_address = adserver_ip_address
        # The status of the AD domain. Valid values:
        # 
        # *   **-1**: The instance is being added to the AD domain.
        # *   **0**: The instance fails to be added to the AD domain.
        # *   **1**: The instance is added to the AD domain.
        self.adstatus = adstatus
        # The cause of the error.
        self.abnormal_reason = abnormal_reason
        # The request ID.
        self.request_id = request_id
        # The username of the AD domain.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addns is not None:
            result['ADDNS'] = self.addns

        if self.adserver_ip_address is not None:
            result['ADServerIpAddress'] = self.adserver_ip_address

        if self.adstatus is not None:
            result['ADStatus'] = self.adstatus

        if self.abnormal_reason is not None:
            result['AbnormalReason'] = self.abnormal_reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADDNS') is not None:
            self.addns = m.get('ADDNS')

        if m.get('ADServerIpAddress') is not None:
            self.adserver_ip_address = m.get('ADServerIpAddress')

        if m.get('ADStatus') is not None:
            self.adstatus = m.get('ADStatus')

        if m.get('AbnormalReason') is not None:
            self.abnormal_reason = m.get('AbnormalReason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

