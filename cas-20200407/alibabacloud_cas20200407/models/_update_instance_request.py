# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_reissue: str = None,
        certificate_name: str = None,
        city: str = None,
        company_id: int = None,
        contact_id_list: List[int] = None,
        country_code: str = None,
        csr: str = None,
        domain: str = None,
        generate_csr_method: str = None,
        instance_id: str = None,
        key_algorithm: str = None,
        province: str = None,
        resource_group_id: str = None,
        tags: List[main_models.UpdateInstanceRequestTags] = None,
        validation_method: str = None,
    ):
        # Whether to enable automatic management.
        # 
        # - enable: enabled
        # 
        # - disable: disabled
        self.auto_reissue = auto_reissue
        # The name of the instance. When issuing a certificate, this value serves as the default certificate name.
        self.certificate_name = certificate_name
        # The city where the company or organization of the certificate requester is located. Required when generating a CSR for a DV certificate. Default value: Beijing.
        self.city = city
        # The company information ID. Required for OV and EV certificates. Otherwise, you cannot call ApplyCertificate to request a certificate.
        self.company_id = company_id
        # The list of contact IDs. You must specify at least one contact. Otherwise, you cannot call ApplyCertificate to request a certificate.
        self.contact_id_list = contact_id_list
        # The country or region code of the certificate organization. For example, CN represents China, and US represents the United States. Required when generating a CSR for a DV certificate. Default value: CN.
        self.country_code = country_code
        # The CSR content. You can generate a CSR using OpenSSL or Keytool. For more information, see [How to create a CSR file](https://help.aliyun.com/document_detail/42218.html).
        self.csr = csr
        # The domain name to bind to the certificate. Requirements are as follows:
        # 
        # - Supports single domain names or wildcard domain names (for example, `*.aliyundoc.com`).
        # 
        # - Supports multiple domain names. Separate multiple domain names with commas (,). The first domain determines whether a free domain is included.
        # 
        # >Notice: 
        # 
        # If you bind multiple domain names to the certificate, this parameter is required. This parameter and the **Csr** parameter cannot both be empty. If you set both parameters, the system uses the **CN** field value from the **Csr** as the domain name for the certificate.
        self.domain = domain
        # The CSR generation method. Default value: online.
        # 
        # - online: The system generates the CSR. The Csr field is ignored.
        # 
        # - upload: You upload the CSR. The Csr field is required.
        self.generate_csr_method = generate_csr_method
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The certificate algorithm. Default value: RSA_2048.
        # 
        # - **RSA_2048**
        # 
        # - **RSA_3072**
        # 
        # - **RSA_4096**
        # 
        # - **ECC_256**
        # 
        # - **SM2**
        self.key_algorithm = key_algorithm
        # The province or region where the company is located. Required when generating a CSR for a DV certificate. Default value: Beijing.
        self.province = province
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # A list of tags.
        self.tags = tags
        # The certificate validation method.
        # 
        # - DNS: DNS validation using TXT or CNAME records.
        # 
        # - HTTP: File-based validation.
        self.validation_method = validation_method

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
        if self.auto_reissue is not None:
            result['AutoReissue'] = self.auto_reissue

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.city is not None:
            result['City'] = self.city

        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        if self.contact_id_list is not None:
            result['ContactIdList'] = self.contact_id_list

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.generate_csr_method is not None:
            result['GenerateCsrMethod'] = self.generate_csr_method

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm

        if self.province is not None:
            result['Province'] = self.province

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.validation_method is not None:
            result['ValidationMethod'] = self.validation_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReissue') is not None:
            self.auto_reissue = m.get('AutoReissue')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        if m.get('ContactIdList') is not None:
            self.contact_id_list = m.get('ContactIdList')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('GenerateCsrMethod') is not None:
            self.generate_csr_method = m.get('GenerateCsrMethod')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ValidationMethod') is not None:
            self.validation_method = m.get('ValidationMethod')

        return self

class UpdateInstanceRequestTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the instance. Valid values for N: **1** to **20**. If you specify this value, it cannot be an empty string.
        # 
        # It can contain up to 64 characters. It cannot start with `aliyun` or `acs:`, and it cannot contain `http://` or `https://`.
        self.tag_key = tag_key
        # The tag value of the instance. Valid values for N: **1** to **20**. If you specify this value, it can be an empty string.
        # 
        # It can contain up to 128 characters. It cannot start with `aliyun` or `acs:`, and it cannot contain `http://` or `https://`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

