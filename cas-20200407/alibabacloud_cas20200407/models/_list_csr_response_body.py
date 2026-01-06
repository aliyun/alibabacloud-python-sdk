# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListCsrResponseBody(DaraModel):
    def __init__(
        self,
        csr_list: List[main_models.ListCsrResponseBodyCsrList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The CSRs.
        self.csr_list = csr_list
        # The page number.
        self.current_page = current_page
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. Default value: 50.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.csr_list:
            for v1 in self.csr_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CsrList'] = []
        if self.csr_list is not None:
            for k1 in self.csr_list:
                result['CsrList'].append(k1.to_map() if k1 else None)

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
        self.csr_list = []
        if m.get('CsrList') is not None:
            for k1 in m.get('CsrList'):
                temp_model = main_models.ListCsrResponseBodyCsrList()
                self.csr_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCsrResponseBodyCsrList(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        common_name: str = None,
        corp_name: str = None,
        country_code: str = None,
        csr_id: int = None,
        department: str = None,
        has_private_key: bool = None,
        key_sha_2: str = None,
        key_size: int = None,
        locality: str = None,
        name: str = None,
        province: str = None,
        sans: str = None,
    ):
        # The algorithm. Valid values: RSA, SM2, and ECC.
        self.algorithm = algorithm
        # The primary domain name, which is a common name.
        self.common_name = common_name
        # The name of the company.
        self.corp_name = corp_name
        # The code of the country or region in which the organization is located. For example, you can use CN to indicate China and use US to indicate the United States. The default value is the code of the country or region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued. For more information about country codes, see the "Country codes" section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # The ID of the CSR.
        self.csr_id = csr_id
        # The department that uses the certificate.
        self.department = department
        # Indicates whether the certificate contains a private key.
        self.has_private_key = has_private_key
        # The public key that is calculated by using the SHA256 algorithm.
        self.key_sha_2 = key_sha_2
        # The key length that is used by the algorithm. The key length for RSA algorithms can be 2,048, 3,072, and 4,096 bits. The key length for ECC and SM2 algorithms can be 256 bits.
        self.key_size = key_size
        # The city where the company is located.
        self.locality = locality
        # The name of the CSR.
        self.name = name
        # The province or location.
        self.province = province
        # The secondary domain names. Separate multiple domain names with commas (,).
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.csr_id is not None:
            result['CsrId'] = self.csr_id

        if self.department is not None:
            result['Department'] = self.department

        if self.has_private_key is not None:
            result['HasPrivateKey'] = self.has_private_key

        if self.key_sha_2 is not None:
            result['KeySha2'] = self.key_sha_2

        if self.key_size is not None:
            result['KeySize'] = self.key_size

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.name is not None:
            result['Name'] = self.name

        if self.province is not None:
            result['Province'] = self.province

        if self.sans is not None:
            result['Sans'] = self.sans

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('HasPrivateKey') is not None:
            self.has_private_key = m.get('HasPrivateKey')

        if m.get('KeySha2') is not None:
            self.key_sha_2 = m.get('KeySha2')

        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        return self

