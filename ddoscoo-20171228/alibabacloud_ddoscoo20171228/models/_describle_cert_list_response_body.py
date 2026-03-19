# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribleCertListResponseBody(DaraModel):
    def __init__(
        self,
        cert_list: List[main_models.DescribleCertListResponseBodyCertList] = None,
        request_id: str = None,
    ):
        self.cert_list = cert_list
        self.request_id = request_id

    def validate(self):
        if self.cert_list:
            for v1 in self.cert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertList'] = []
        if self.cert_list is not None:
            for k1 in self.cert_list:
                result['CertList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k1 in m.get('CertList'):
                temp_model = main_models.DescribleCertListResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribleCertListResponseBodyCertList(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        common: str = None,
        domain_related: bool = None,
        end_date: str = None,
        id: int = None,
        issuer: str = None,
        name: str = None,
        start_date: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.common = common
        self.domain_related = domain_related
        self.end_date = end_date
        self.id = id
        self.issuer = issuer
        self.name = name
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.common is not None:
            result['Common'] = self.common

        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.name is not None:
            result['Name'] = self.name

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

