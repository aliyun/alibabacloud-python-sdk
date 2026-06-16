# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateCustomCertificateRequest(DaraModel):
    def __init__(
        self,
        api_passthrough: main_models.CreateCustomCertificateRequestApiPassthrough = None,
        csr: str = None,
        enable_crl: int = None,
        immediately: int = None,
        parent_identifier: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateCustomCertificateRequestTags] = None,
        validity: str = None,
        custom_identifier: str = None,
    ):
        # Pass-through parameters.
        self.api_passthrough = api_passthrough
        # The content of the CSR. You can generate a CSR using tools such as OpenSSL or Keytool. For more information, see [Create a CSR file](https://help.aliyun.com/document_detail/42218.html).
        # 
        # This parameter is required.
        self.csr = csr
        # Specifies whether to include a CRL address.
        # 
        # - 0 - No
        # 
        # - 1 - Yes
        self.enable_crl = enable_crl
        # Obtain the certificate immediately.
        # 
        # - 0 - Issue the certificate asynchronously.
        # 
        # - 1 - Issue the certificate immediately.
        # 
        # - 2 - Issue the certificate immediately and return the CA certificate chain.
        self.immediately = immediately
        # The identifier of the CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The ID of the resource group. You can obtain this ID by calling the [ListResources](https://help.aliyun.com/document_detail/2716559.html) operation.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tags = tags
        # The validity period of the certificate. This period cannot exceed the validity period of the instance. You can use relative time or absolute time.
        # 
        # Relative time: Supports years, months, and days.
        # 
        # - Year - y
        # 
        # - Month - m
        # 
        # - Day - d
        # 
        # Absolute time: Uses GMT. Format: `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"`
        # 
        # - Specify the end time - $NotAfter
        # 
        # - Specify the start and end times - $NotBefore/$NotAfter
        # 
        # This parameter is required.
        self.validity = validity
        # A custom identifier.
        self.custom_identifier = custom_identifier

    def validate(self):
        if self.api_passthrough:
            self.api_passthrough.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_passthrough is not None:
            result['ApiPassthrough'] = self.api_passthrough.to_map()

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl

        if self.immediately is not None:
            result['Immediately'] = self.immediately

        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.validity is not None:
            result['Validity'] = self.validity

        if self.custom_identifier is not None:
            result['customIdentifier'] = self.custom_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiPassthrough') is not None:
            temp_model = main_models.CreateCustomCertificateRequestApiPassthrough()
            self.api_passthrough = temp_model.from_map(m.get('ApiPassthrough'))

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')

        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')

        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateCustomCertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Validity') is not None:
            self.validity = m.get('Validity')

        if m.get('customIdentifier') is not None:
            self.custom_identifier = m.get('customIdentifier')

        return self

class CreateCustomCertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class CreateCustomCertificateRequestApiPassthrough(DaraModel):
    def __init__(
        self,
        extensions: main_models.CreateCustomCertificateRequestApiPassthroughExtensions = None,
        serial_number: str = None,
        subject: main_models.CreateCustomCertificateRequestApiPassthroughSubject = None,
    ):
        # The certificate extensions.
        self.extensions = extensions
        # The custom serial number of the certificate. Must be a long integer.
        self.serial_number = serial_number
        # The certificate subject.
        self.subject = subject

    def validate(self):
        if self.extensions:
            self.extensions.validate()
        if self.subject:
            self.subject.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extensions is not None:
            result['Extensions'] = self.extensions.to_map()

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.subject is not None:
            result['Subject'] = self.subject.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extensions') is not None:
            temp_model = main_models.CreateCustomCertificateRequestApiPassthroughExtensions()
            self.extensions = temp_model.from_map(m.get('Extensions'))

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Subject') is not None:
            temp_model = main_models.CreateCustomCertificateRequestApiPassthroughSubject()
            self.subject = temp_model.from_map(m.get('Subject'))

        return self

class CreateCustomCertificateRequestApiPassthroughSubject(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        country: str = None,
        custom_attributes: List[main_models.CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes] = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        state: str = None,
    ):
        # The common name of the certificate user.
        self.common_name = common_name
        # The country code. Use the two-letter country code from ISO 3166-1. For more information, see [ISO](https://www.iso.org/obp/ui/#search/code/).
        self.country = country
        # The custom subject properties of the certificate.
        self.custom_attributes = custom_attributes
        # The name of the city where the organization is located. Chinese characters and letters are supported.
        self.locality = locality
        # The name of the organization.
        self.organization = organization
        # The name of the department or branch within the organization.
        self.organization_unit = organization_unit
        # The province or state where the organization is located.
        self.state = state

    def validate(self):
        if self.custom_attributes:
            for v1 in self.custom_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        result['CustomAttributes'] = []
        if self.custom_attributes is not None:
            for k1 in self.custom_attributes:
                result['CustomAttributes'].append(k1.to_map() if k1 else None)

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        self.custom_attributes = []
        if m.get('CustomAttributes') is not None:
            for k1 in m.get('CustomAttributes'):
                temp_model = main_models.CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes()
                self.custom_attributes.append(temp_model.from_map(k1))

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes(DaraModel):
    def __init__(
        self,
        object_identifier: str = None,
        value: str = None,
    ):
        # The key of the custom property. It must comply with industry standards. Examples:
        # 
        # - 2.5.4.6: Country code
        # 
        # - 2.5.4.10: Organization
        # 
        # - 2.5.4.11: Organizational unit name
        # 
        # - 2.5.4.12: Title
        # 
        # - 2.5.4.3: Common name
        # 
        # - 2.5.4.9: Street
        # 
        # - 2.5.4.5: Serial number
        # 
        # - 2.5.4.7: Locality
        # 
        # - 2.5.4.8: State or province
        # 
        # - 1.3.6.1.4.1.37244.1.1: Matter certificate - Node ID
        # 
        # - 1.3.6.1.4.1.37244.1.5: Matter certificate - Fabric ID
        # 
        # - 1.3.6.1.4.1.37244.2.1: Matter certificate Vendor ID (VID)
        # 
        # - 1.3.6.1.4.1.37244.2.2: Matter certificate Product ID (PID)
        self.object_identifier = object_identifier
        # The value of the custom property.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_identifier is not None:
            result['ObjectIdentifier'] = self.object_identifier

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectIdentifier') is not None:
            self.object_identifier = m.get('ObjectIdentifier')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateCustomCertificateRequestApiPassthroughExtensions(DaraModel):
    def __init__(
        self,
        criticals: List[str] = None,
        extended_key_usages: List[str] = None,
        key_usage: main_models.CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage = None,
        subject_alternative_names: List[main_models.CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames] = None,
    ):
        # If an extension is critical, its name is included in the criticals list.
        self.criticals = criticals
        # The extended key usages.
        self.extended_key_usages = extended_key_usages
        # The key usage.
        self.key_usage = key_usage
        # The subject alternative names (SANs) of the certificate.
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        if self.key_usage:
            self.key_usage.validate()
        if self.subject_alternative_names:
            for v1 in self.subject_alternative_names:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criticals is not None:
            result['Criticals'] = self.criticals

        if self.extended_key_usages is not None:
            result['ExtendedKeyUsages'] = self.extended_key_usages

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage.to_map()

        result['SubjectAlternativeNames'] = []
        if self.subject_alternative_names is not None:
            for k1 in self.subject_alternative_names:
                result['SubjectAlternativeNames'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criticals') is not None:
            self.criticals = m.get('Criticals')

        if m.get('ExtendedKeyUsages') is not None:
            self.extended_key_usages = m.get('ExtendedKeyUsages')

        if m.get('KeyUsage') is not None:
            temp_model = main_models.CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage()
            self.key_usage = temp_model.from_map(m.get('KeyUsage'))

        self.subject_alternative_names = []
        if m.get('SubjectAlternativeNames') is not None:
            for k1 in m.get('SubjectAlternativeNames'):
                temp_model = main_models.CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames()
                self.subject_alternative_names.append(temp_model.from_map(k1))

        return self

class CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The following values are allowed:
        # 
        # - rfc822Name - Email address
        # 
        # - dNSName - Domain name
        # 
        # - uniformResourceIdentifier - Uniform Resource Identifier (URI)
        # 
        # - iPAddress - IP address
        # 
        # This parameter is required.
        self.type = type
        # A value that matches the specified Type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage(DaraModel):
    def __init__(
        self,
        content_commitment: bool = None,
        data_encipherment: bool = None,
        decipher_only: bool = None,
        digital_signature: bool = None,
        encipher_only: bool = None,
        key_agreement: bool = None,
        key_encipherment: bool = None,
        non_repudiation: bool = None,
    ):
        # Content commitment. Formerly known as NonRepudiation. Allows the certificate key to be used for content commitment.
        self.content_commitment = content_commitment
        # Data encipherment.
        self.data_encipherment = data_encipherment
        # When KeyAgreement is true, this marks that the certificate key can only be used for decryption.
        self.decipher_only = decipher_only
        # Digital signature. Allows the private key of the certificate to be used for digital signatures and the public key to be used to verify digital signatures.
        self.digital_signature = digital_signature
        # When KeyAgreement is true, this marks that the certificate key can only be used for encryption.
        self.encipher_only = encipher_only
        # Key agreement.
        self.key_agreement = key_agreement
        # Key encipherment. Allows the certificate key to be used to encrypt other keys.
        self.key_encipherment = key_encipherment
        # Non-repudiation. This has been renamed to ContentCommitment in the X.509 standard.
        self.non_repudiation = non_repudiation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_commitment is not None:
            result['ContentCommitment'] = self.content_commitment

        if self.data_encipherment is not None:
            result['DataEncipherment'] = self.data_encipherment

        if self.decipher_only is not None:
            result['DecipherOnly'] = self.decipher_only

        if self.digital_signature is not None:
            result['DigitalSignature'] = self.digital_signature

        if self.encipher_only is not None:
            result['EncipherOnly'] = self.encipher_only

        if self.key_agreement is not None:
            result['KeyAgreement'] = self.key_agreement

        if self.key_encipherment is not None:
            result['KeyEncipherment'] = self.key_encipherment

        if self.non_repudiation is not None:
            result['NonRepudiation'] = self.non_repudiation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentCommitment') is not None:
            self.content_commitment = m.get('ContentCommitment')

        if m.get('DataEncipherment') is not None:
            self.data_encipherment = m.get('DataEncipherment')

        if m.get('DecipherOnly') is not None:
            self.decipher_only = m.get('DecipherOnly')

        if m.get('DigitalSignature') is not None:
            self.digital_signature = m.get('DigitalSignature')

        if m.get('EncipherOnly') is not None:
            self.encipher_only = m.get('EncipherOnly')

        if m.get('KeyAgreement') is not None:
            self.key_agreement = m.get('KeyAgreement')

        if m.get('KeyEncipherment') is not None:
            self.key_encipherment = m.get('KeyEncipherment')

        if m.get('NonRepudiation') is not None:
            self.non_repudiation = m.get('NonRepudiation')

        return self

