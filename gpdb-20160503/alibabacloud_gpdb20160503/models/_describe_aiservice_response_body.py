# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAIServiceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        private_api_dev_url: str = None,
        private_workbench_url: str = None,
        public_api_dev_url: str = None,
        public_workbench_url: str = None,
        request_id: str = None,
        security_ip_list: str = None,
        service_account: str = None,
        service_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.private_api_dev_url = private_api_dev_url
        self.private_workbench_url = private_workbench_url
        self.public_api_dev_url = public_api_dev_url
        self.public_workbench_url = public_workbench_url
        self.request_id = request_id
        self.security_ip_list = security_ip_list
        self.service_account = service_account
        self.service_id = service_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.private_api_dev_url is not None:
            result['PrivateApiDevUrl'] = self.private_api_dev_url

        if self.private_workbench_url is not None:
            result['PrivateWorkbenchUrl'] = self.private_workbench_url

        if self.public_api_dev_url is not None:
            result['PublicApiDevUrl'] = self.public_api_dev_url

        if self.public_workbench_url is not None:
            result['PublicWorkbenchUrl'] = self.public_workbench_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list

        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PrivateApiDevUrl') is not None:
            self.private_api_dev_url = m.get('PrivateApiDevUrl')

        if m.get('PrivateWorkbenchUrl') is not None:
            self.private_workbench_url = m.get('PrivateWorkbenchUrl')

        if m.get('PublicApiDevUrl') is not None:
            self.public_api_dev_url = m.get('PublicApiDevUrl')

        if m.get('PublicWorkbenchUrl') is not None:
            self.public_workbench_url = m.get('PublicWorkbenchUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')

        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

