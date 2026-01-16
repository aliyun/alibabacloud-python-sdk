# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class ListCertResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[main_models.ListCertResponseBodyList] = None,
        max_results: int = None,
        next_token: str = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.max_results = max_results
        self.next_token = next_token
        self.page_count = page_count
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListCertResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertResponseBodyList(DaraModel):
    def __init__(
        self,
        after_date: str = None,
        after_time: int = None,
        algorithm: str = None,
        alias_name: str = None,
        before_date: str = None,
        before_time: int = None,
        certificate_type: str = None,
        common_name: str = None,
        custom_identifier: str = None,
        extra: str = None,
        id: int = None,
        identifier: str = None,
        key_exportable: bool = None,
        organization: str = None,
        organization_unit: str = None,
        serial_number: str = None,
        status: str = None,
        subject_dn: str = None,
        tags: List[str] = None,
    ):
        self.after_date = after_date
        self.after_time = after_time
        self.algorithm = algorithm
        self.alias_name = alias_name
        self.before_date = before_date
        self.before_time = before_time
        self.certificate_type = certificate_type
        self.common_name = common_name
        self.custom_identifier = custom_identifier
        self.extra = extra
        self.id = id
        self.identifier = identifier
        self.key_exportable = key_exportable
        self.organization = organization
        self.organization_unit = organization_unit
        self.serial_number = serial_number
        self.status = status
        self.subject_dn = subject_dn
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.after_time is not None:
            result['AfterTime'] = self.after_time

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.id is not None:
            result['Id'] = self.id

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.key_exportable is not None:
            result['KeyExportable'] = self.key_exportable

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.status is not None:
            result['Status'] = self.status

        if self.subject_dn is not None:
            result['SubjectDn'] = self.subject_dn

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('KeyExportable') is not None:
            self.key_exportable = m.get('KeyExportable')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubjectDn') is not None:
            self.subject_dn = m.get('SubjectDn')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

