# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ApplyCertificateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ApplyCertificateResponseBodyResult] = None,
        site_name: str = None,
        total_count: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of free certificate application details.
        self.result = result
        # Site name.
        self.site_name = site_name
        # Number of certificates applied for, which is the same as the number of input domains.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ApplyCertificateResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ApplyCertificateResponseBodyResult(DaraModel):
    def __init__(
        self,
        domain: str = None,
        id: str = None,
        status: str = None,
    ):
        # Certificate domain.
        self.domain = domain
        # Certificate ID.
        self.id = id
        # Status of the certificate application.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

