# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackDeploymentsRequest(DaraModel):
    def __init__(
        self,
        config_version: str = None,
        deployment_name: str = None,
        deployment_no: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.config_version = config_version
        self.deployment_name = deployment_name
        self.deployment_no = deployment_no
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_version is not None:
            result['configVersion'] = self.config_version

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.deployment_no is not None:
            result['deploymentNo'] = self.deployment_no

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configVersion') is not None:
            self.config_version = m.get('configVersion')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('deploymentNo') is not None:
            self.deployment_no = m.get('deploymentNo')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

