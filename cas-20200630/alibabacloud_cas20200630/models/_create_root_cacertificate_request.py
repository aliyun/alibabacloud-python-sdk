# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateRootCACertificateRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        client_token: str = None,
        common_name: str = None,
        country_code: str = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[main_models.CreateRootCACertificateRequestTags] = None,
        years: int = None,
    ):
        # The key algorithm of the root CA certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the root CA certificate must be consistent with the **encryption algorithm** of the private root CA instance that you purchase. For example, if the **encryption algorithm** of the private root CA instance that you purchase is **RSA**, the key algorithm of the root CA certificate must be **RSA_1024**, **RSA_2048**, or **RSA_4096**.
        self.algorithm = algorithm
        self.client_token = client_token
        # The common name or abbreviation of the organization. The value can contain letters.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The code of the country or region in which the organization is located. You can enter an alpha-2 code. For example, you can use **CN** to indicate China and use **US** to indicate the United States.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # The name of the city in which the organization is located. The value can contain letters.
        # 
        # This parameter is required.
        self.locality = locality
        # The name of the organization that is associated with the root CA certificate. You can enter the name of your enterprise or company. The value can contain letters.
        # 
        # This parameter is required.
        self.organization = organization
        # The name of the department or branch in the organization. The value can contain letters.
        # 
        # This parameter is required.
        self.organization_unit = organization_unit
        self.resource_group_id = resource_group_id
        # The name of the province, municipality, or autonomous region in which the organization is located. The value can contain letters.
        # 
        # This parameter is required.
        self.state = state
        self.tags = tags
        # The validity period of the root CA certificate. Unit: years.
        # 
        # >  We recommend that you set this parameter to a value from 5 to 10.
        # 
        # This parameter is required.
        self.years = years

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateRootCACertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class CreateRootCACertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

