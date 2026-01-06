# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListCertResponseBody(DaraModel):
    def __init__(
        self,
        cert_list: List[main_models.ListCertResponseBodyCertList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # An array that consists of the certificates.
        self.cert_list = cert_list
        # The page number of the returned page. Default value: 1.
        self.current_page = current_page
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned per page. Default value: 50.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k1 in m.get('CertList'):
                temp_model = main_models.ListCertResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCertResponseBodyCertList(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        before_date: int = None,
        cert_type: str = None,
        common_name: str = None,
        exist_private_key: bool = None,
        identifier: str = None,
        issuer: str = None,
        sans: str = None,
        source_type: str = None,
        status: str = None,
        wh_id: int = None,
        wh_instance_id: str = None,
    ):
        # The expiration time of the certificate. The value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The issuance time of the certificate. The value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # 证书的类型 。取值：
        # 
        # - **CA**：表示CA证书。
        # - **CERT**：表示签发的证书。
        self.cert_type = cert_type
        # The domain name.
        self.common_name = common_name
        # Indicates whether the certificate contains a private key. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.exist_private_key = exist_private_key
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The issuer of the certificate.
        self.issuer = issuer
        # The domain names that are bound to the certificate. Multiple domain names are separated by commas.
        self.sans = sans
        # The source of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **aliyun**: Alibaba Cloud certificate
        self.source_type = source_type
        # The status of the certificate. Valid values:
        # 
        # *   **ISSUE**: issued
        # *   **REVOKE**: revoked
        self.status = status
        # The ID of the certificate repository.
        self.wh_id = wh_id
        # The instance ID of the certificate repository.
        self.wh_instance_id = wh_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.exist_private_key is not None:
            result['ExistPrivateKey'] = self.exist_private_key

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.wh_id is not None:
            result['WhId'] = self.wh_id

        if self.wh_instance_id is not None:
            result['WhInstanceId'] = self.wh_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('ExistPrivateKey') is not None:
            self.exist_private_key = m.get('ExistPrivateKey')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')

        if m.get('WhInstanceId') is not None:
            self.wh_instance_id = m.get('WhInstanceId')

        return self

