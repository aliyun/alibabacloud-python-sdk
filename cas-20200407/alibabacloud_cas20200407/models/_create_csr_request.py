# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCsrRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        common_name: str = None,
        corp_name: str = None,
        country_code: str = None,
        department: str = None,
        key_size: int = None,
        locality: str = None,
        name: str = None,
        province: str = None,
        sans: str = None,
    ):
        # The algorithm. Valid values: RSA, SM2, and ECC. For more information about algorithms, see [Select an SSL certificate](https://help.aliyun.com/document_detail/197871.html).
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The primary domain name, which is a common name.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The name of the company.
        self.corp_name = corp_name
        # The code of the country or region in which the organization is located. For example, you can use CN to indicate China and use US to indicate the United States.
        # 
        # This parameter is required.
        self.country_code = country_code
        # The department that uses the certificate.
        self.department = department
        # The key length that is used by the algorithm.
        # 
        # *   The key length for RSA algorithms can be 2,048, 3,072, and 4,096 bits.
        # *   The key length for ECC and SM2 algorithms can be 256 bits.
        # 
        # This parameter is required.
        self.key_size = key_size
        # The city where the company is located.
        # 
        # This parameter is required.
        self.locality = locality
        # The name of the CSR. The name can be up to 50 characters in length and can contain letters, digits, underscores (_), hyphens (-), and periods (.).
        self.name = name
        # The province or location where the company is located.
        # 
        # This parameter is required.
        self.province = province
        # The secondary domain names. Separate multiple domain names with commas (,). You can use the CSR to apply for a certificate for both the primary and secondary domain names.
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

        if self.department is not None:
            result['Department'] = self.department

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

        if m.get('Department') is not None:
            self.department = m.get('Department')

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

