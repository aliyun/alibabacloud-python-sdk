# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateClientCertificateRequest(TeaModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        days: int = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        san_type: int = None,
        san_value: str = None,
        state: str = None,
        years: int = None,
    ):
        # The expiration time of the client certificate. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.after_time = after_time
        # The key algorithm of the client certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the client certificate must be the same with the encryption algorithm of the intermediate certificate authority (CA) certificate. The key length can be different. For example, if the key algorithm of the intermediate CA certificate is RSA_2048, the key algorithm of the client certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # > You can call the [DescribeCACertificate] operation to query the key algorithm of an intermediate CA certificate.
        self.algorithm = algorithm
        # The issuance time of the client certificate. This value is a UNIX timestamp. The default value is the time when you call this operation. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.before_time = before_time
        # The name of the client certificate user. In most cases, the user of a client certificate is an individual, a company, an organization, or an application. We recommend that you enter the common name of a user. Examples: Bob, Alibaba, Alibaba Cloud password platform, and Tmall Genie.
        self.common_name = common_name
        # The country in which the organization is located. Default value: CN.
        self.country = country
        # The validity period of the client certificate. Unit: day. You must specify at least one of the **Days**, **BeforeTime**, and **AfterTime** parameters. The **BeforeTime** and **AfterTime** parameters must be both empty or both specified. The following list describes how to specify these parameters:
        # 
        # *   If you specify the **Days** parameter, you can specify both the **BeforeTime** and **AfterTime** parameters or leave them both empty.
        # *   If you do not specify the **Days** parameter, you must specify both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > 
        # 
        # *   If you specify the **Days**, **BeforeTime**, and **AfterTime** parameters at the same time, the validity period of the client certificate is determined by the value of the **Days** parameter.
        # 
        # *   The validity period of the client certificate cannot exceed the validity period of the intermediate CA certificate. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) operation to query the validity period of an intermediate CA certificate.
        self.days = days
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the certificate. Valid values:
        # 
        # *   **0**: does not return the certificate. This is the default value.
        # *   **1**: returns the certificate.
        # *   **2**: returns the certificate and the certificate chain of the certificate.
        self.immediately = immediately
        # The name of the city in which the organization is located. The value can contain letters. The default value is the name of the city in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.locality = locality
        # The validity period of the client certificate. Unit: months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate CA certificate from which the server certificate is issued.
        # 
        # > You can call the [DescribeCACertificateList] operation to query the unique identifier of an intermediate CA certificate.
        self.parent_identifier = parent_identifier
        # The type of the Subject Alternative Name (SAN) extension that is supported by the client certificate. Valid values:
        # 
        # *   **1**: an email address
        # *   **6**: a Uniform Resource Identifier (URI)
        self.san_type = san_type
        # The content of the extension. You can specify multiple SAN extensions. If you want to specify multiple SAN extensions, separate them with commas (,).
        self.san_value = san_value
        # The province, municipality, or autonomous region in which the organization is located. The value can contain letters. The default value is the name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.state = state
        # The validity period of the client certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.days is not None:
            result['Days'] = self.days
        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.san_type is not None:
            result['SanType'] = self.san_type
        if self.san_value is not None:
            result['SanValue'] = self.san_value
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')
        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
        x_509certificate: str = None,
    ):
        # The certificate chain of the client certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the client certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The content of the client certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClientCertificateWithCsrRequest(TeaModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
        days: int = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        san_type: int = None,
        san_value: str = None,
        state: str = None,
        years: int = None,
    ):
        # The expiration time of the client certificate. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.after_time = after_time
        # The key algorithm of the client certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the client certificate must be the same with the encryption algorithm of the intermediate CA certificate. The key length can be different. For example, if the key algorithm of the intermediate CA certificate is RSA_2048, the key algorithm of the client certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # >  You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the key algorithm of an intermediate CA certificate.
        self.algorithm = algorithm
        # The issuance time of the client certificate. This value is a UNIX timestamp. The default value is the time when you call this operation. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.before_time = before_time
        # The common name of the certificate. The value can contain letters.
        # 
        # >  If you specify the **CsrPemString** parameter, the value of the **CommonName** parameter is determined by the **CsrPemString** parameter.
        self.common_name = common_name
        # The code of the country in which the organization is located, such as **CN** and **US**.
        self.country = country
        # The content of the CSR file. You can generate a CSR file by using the OpenSSL tool or Keytool. For more information, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html) You can also create a CSR file in the Certificate Management Service console. For more information, see [Create a CSR](https://help.aliyun.com/document_detail/313297.html).
        self.csr = csr
        # The validity period of the client certificate. Unit: days. You must specify at least one of the **Days**, **BeforeTime**, and **AfterTime** parameters. The **BeforeTime** and **AfterTime** parameters must be both empty or both specified. The following list describes how to specify these parameters:
        # 
        # *   If you specify the **Days** parameter, you can specify both the **BeforeTime** and **AfterTime** parameters or leave them both empty.********\
        # *   If you do not specify the **Days** parameter, you must specify both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > 
        # 
        # *   If you specify the **Days**, **BeforeTime**, and **AfterTime** parameters together, the validity period of the client certificate is determined by the value of the **Days** parameter.
        # 
        # *   The validity period of the client certificate cannot exceed the validity period of the intermediate CA certificate. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the validity period of an intermediate CA certificate.
        self.days = days
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the certificate. Valid values:
        # 
        # *   **0**: does not return the certificate. This is the default value.
        # *   **1**: returns the certificate.
        # *   **2**: returns the certificate and the certificate chain of the certificate.
        self.immediately = immediately
        # The name of the city in which the organization is located. The value can contain letters. The default value is the name of the city in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.locality = locality
        # The validity period of the client certificate. Unit: months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate CA certificate from which the client certificate is issued.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifier of an intermediate CA certificate.
        self.parent_identifier = parent_identifier
        # The type of the Subject Alternative Name (SAN) extension that is supported by the client certificate. Valid values:
        # 
        # *   **1**: an email address
        # *   **6**: a Uniform Resource Identifier (URI)
        self.san_type = san_type
        # The content of the extension. You can specify multiple SAN extensions. If you want to specify multiple SAN extensions, separate them with commas (,).
        self.san_value = san_value
        # The province, municipality, or autonomous region in which the organization is located. The value can contain letters. The default value is the name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.state = state
        # The validity period of the client certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.days is not None:
            result['Days'] = self.days
        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.san_type is not None:
            result['SanType'] = self.san_type
        if self.san_value is not None:
            result['SanValue'] = self.san_value
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')
        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateClientCertificateWithCsrResponseBody(TeaModel):
    def __init__(
        self,
        cert_kmc_rep_1: str = None,
        cert_sign_buf_kmc: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
        x_509certificate: str = None,
    ):
        # CertKmcRep1.
        self.cert_kmc_rep_1 = cert_kmc_rep_1
        # Cert Sign Buf Kmc.
        self.cert_sign_buf_kmc = cert_sign_buf_kmc
        # The certificate chain of the client certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the client certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The serial number of the server certificate.
        self.serial_number = serial_number
        # The content of the client certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_kmc_rep_1 is not None:
            result['CertKmcRep1'] = self.cert_kmc_rep_1
        if self.cert_sign_buf_kmc is not None:
            result['CertSignBufKmc'] = self.cert_sign_buf_kmc
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertKmcRep1') is not None:
            self.cert_kmc_rep_1 = m.get('CertKmcRep1')
        if m.get('CertSignBufKmc') is not None:
            self.cert_sign_buf_kmc = m.get('CertSignBufKmc')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateClientCertificateWithCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClientCertificateWithCsrResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClientCertificateWithCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage(TeaModel):
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
        # The original name of the parameter is NonRepudiation.
        self.content_commitment = content_commitment
        # Specifies whether the key can be used for data encryption.
        self.data_encipherment = data_encipherment
        # Specifies whether the key can be used only for data decryption.
        self.decipher_only = decipher_only
        # Specifies whether the key can be used for digital signing. If you set this parameter to true, the private key of the certificate can be used to generate digital signatures, and the public key of the certificate can be used to verify digital signatures.
        self.digital_signature = digital_signature
        # Specifies whether the key can be used only for data encryption.
        self.encipher_only = encipher_only
        # Specifies whether the key can be used for key agreement.
        self.key_agreement = key_agreement
        # Specifies whether the key can be used for data encipherment.
        self.key_encipherment = key_encipherment
        # Specifies whether the key can be used for non-repudiation. This parameter is renamed ContentCommitment in the X.509 standard.
        self.non_repudiation = non_repudiation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the alias. Valid values:
        # 
        # *   rfc822Name: email address
        # *   dNSName: domain name
        # *   uniformResourceIdentifier: URI
        # *   iPAddress: IP address
        # 
        # This parameter is required.
        self.type = type
        # The alias that meets the requirement of a specified type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCustomCertificateRequestApiPassthroughExtensions(TeaModel):
    def __init__(
        self,
        criticals: List[str] = None,
        extended_key_usages: List[str] = None,
        key_usage: CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage = None,
        subject_alternative_names: List[CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames] = None,
    ):
        # If it is a necessary parameter, the critical list contains the parameter name.
        self.criticals = criticals
        # The extended key usage.
        self.extended_key_usages = extended_key_usages
        # The key usage.
        self.key_usage = key_usage
        # The aliases of the entities.
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        if self.key_usage:
            self.key_usage.validate()
        if self.subject_alternative_names:
            for k in self.subject_alternative_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.criticals is not None:
            result['Criticals'] = self.criticals
        if self.extended_key_usages is not None:
            result['ExtendedKeyUsages'] = self.extended_key_usages
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage.to_map()
        result['SubjectAlternativeNames'] = []
        if self.subject_alternative_names is not None:
            for k in self.subject_alternative_names:
                result['SubjectAlternativeNames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criticals') is not None:
            self.criticals = m.get('Criticals')
        if m.get('ExtendedKeyUsages') is not None:
            self.extended_key_usages = m.get('ExtendedKeyUsages')
        if m.get('KeyUsage') is not None:
            temp_model = CreateCustomCertificateRequestApiPassthroughExtensionsKeyUsage()
            self.key_usage = temp_model.from_map(m['KeyUsage'])
        self.subject_alternative_names = []
        if m.get('SubjectAlternativeNames') is not None:
            for k in m.get('SubjectAlternativeNames'):
                temp_model = CreateCustomCertificateRequestApiPassthroughExtensionsSubjectAlternativeNames()
                self.subject_alternative_names.append(temp_model.from_map(k))
        return self


class CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes(TeaModel):
    def __init__(
        self,
        object_identifier: str = None,
        value: str = None,
    ):
        # Custom attribute type as:
        # 
        # - 2.5.4.6 : country
        # - 2.5.4.10 : organization
        # - 2.5.4.11 : organizational unit
        # - 2.5.4.12 : title
        # - 2.5.4.3 : common name
        # - 2.5.4.9 : street
        # - 2.5.4.5 : serial number
        # - 2.5.4.7 : locality
        # - 2.5.4.8 : state
        # - 1.3.6.1.4.1.37244.1.1 : Matter Operational Certificate - Node ID
        # - 1.3.6.1.4.1.37244.1.5 : Matter Operational Certificate - Fabric ID
        # - 1.3.6.1.4.1.37244.2.1 : Matter Device Attestation Certificate Vender ID (VID)
        # - 1.3.6.1.4.1.37244.2.2 : Matter Device Attestation Certificate Product ID (PID).
        self.object_identifier = object_identifier
        # Custom attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCustomCertificateRequestApiPassthroughSubject(TeaModel):
    def __init__(
        self,
        common_name: str = None,
        country: str = None,
        custom_attributes: List[CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes] = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        state: str = None,
    ):
        # The common name of the certificate user.
        self.common_name = common_name
        # The code of the country. The value is an alpha-2 country code that complies with the ISO 3166-1 standard. For more information about country codes, visit <https://www.iso.org/obp/ui/#search/code/>.
        self.country = country
        # Customize the Subject attributes of the certificate.
        self.custom_attributes = custom_attributes
        # The name of the city in which the organization is located. The value can contain letters.
        self.locality = locality
        # The name of the organization.
        self.organization = organization
        # The name of the department or branch in the organization.
        self.organization_unit = organization_unit
        # The name of the province or state in which the organization associated with the certificate is located.
        self.state = state

    def validate(self):
        if self.custom_attributes:
            for k in self.custom_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        result['CustomAttributes'] = []
        if self.custom_attributes is not None:
            for k in self.custom_attributes:
                result['CustomAttributes'].append(k.to_map() if k else None)
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
            for k in m.get('CustomAttributes'):
                temp_model = CreateCustomCertificateRequestApiPassthroughSubjectCustomAttributes()
                self.custom_attributes.append(temp_model.from_map(k))
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class CreateCustomCertificateRequestApiPassthrough(TeaModel):
    def __init__(
        self,
        extensions: CreateCustomCertificateRequestApiPassthroughExtensions = None,
        serial_number: str = None,
        subject: CreateCustomCertificateRequestApiPassthroughSubject = None,
    ):
        # The extensions of the certificate.
        self.extensions = extensions
        # The serial number MUST be a positive integer assigned by the CA to each certificate.
        self.serial_number = serial_number
        # The name of the entity that uses the certificate.
        self.subject = subject

    def validate(self):
        if self.extensions:
            self.extensions.validate()
        if self.subject:
            self.subject.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateCustomCertificateRequestApiPassthroughExtensions()
            self.extensions = temp_model.from_map(m['Extensions'])
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Subject') is not None:
            temp_model = CreateCustomCertificateRequestApiPassthroughSubject()
            self.subject = temp_model.from_map(m['Subject'])
        return self


class CreateCustomCertificateRequest(TeaModel):
    def __init__(
        self,
        api_passthrough: CreateCustomCertificateRequestApiPassthrough = None,
        csr: str = None,
        enable_crl: int = None,
        immediately: int = None,
        parent_identifier: str = None,
        validity: str = None,
    ):
        # The passthrough parameters.
        self.api_passthrough = api_passthrough
        # The content of the CSR. You can generate a CSR by using the OpenSSL tool or the Keytool tool. For more information, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html)
        # 
        # This parameter is required.
        self.csr = csr
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to immediately issue the certificate. Valid values:
        # 
        # *   0: asynchronously issues the certificate.
        # *   1: immediately issues the certificate.
        # *   2: immediately issues the certificate and returns the certificate chain.
        self.immediately = immediately
        # The identifier of the certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The validity period of the certificate. The value cannot exceed the validity period of the certificate instance. Relative time and absolute time are supported.
        # 
        # Units of relative time: year, month, and day.
        # 
        # *   Use y to specify years.
        # *   Use m to specify months.
        # *   Use d to specify days.
        # 
        # Absolute time: Use Greenwich Mean Time (GMT). Format: `yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\"`
        # 
        # *   Format of the end time: $NotAfter
        # *   Format of the start time and end time: $NotBefore/$NotAfter
        # 
        # This parameter is required.
        self.validity = validity

    def validate(self):
        if self.api_passthrough:
            self.api_passthrough.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.validity is not None:
            result['Validity'] = self.validity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiPassthrough') is not None:
            temp_model = CreateCustomCertificateRequestApiPassthrough()
            self.api_passthrough = temp_model.from_map(m['ApiPassthrough'])
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Validity') is not None:
            self.validity = m.get('Validity')
        return self


class CreateCustomCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
    ):
        # The content of the certificate. This parameter is returned only if Immediately is set to 1 or 2.
        self.certificate = certificate
        # The certificate chain of the certificate. This parameter is returned only if Immediately is set to 2.
        self.certificate_chain = certificate_chain
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The request ID.
        self.request_id = request_id
        # The serial number of the certificate. This parameter is returned only if Immediately is set to 1 or 2.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class CreateCustomCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRevokeClientCertificateRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the client certificate or server certificate that you want to revoke.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class CreateRevokeClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRevokeClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRevokeClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRevokeClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRootCACertificateRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        common_name: str = None,
        country_code: str = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        state: str = None,
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
        # 
        # This parameter is required.
        self.algorithm = algorithm
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
        # The name of the province, municipality, or autonomous region in which the organization is located. The value can contain letters.
        # 
        # This parameter is required.
        self.state = state
        # The validity period of the root CA certificate. Unit: years.
        # 
        # >  We recommend that you set this parameter to a value from 5 to 10.
        # 
        # This parameter is required.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
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
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
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
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateRootCACertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
    ):
        # The root CA certificate in the PEM format.
        self.certificate = certificate
        # The certificate chain of the root CA certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the root CA certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRootCACertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRootCACertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRootCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerCertificateRequest(TeaModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        days: int = None,
        domain: str = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        state: str = None,
        years: int = None,
    ):
        # The expiration time of the server certificate. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.after_time = after_time
        # The key algorithm of the server certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the server certificate must be the same as the encryption algorithm of the intermediate CA certificate. The key length can be different. For example, if the key algorithm of the intermediate CA certificate is RSA_2048, the key algorithm of the server certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # >  You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the key algorithm of an intermediate CA certificate.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The issuance time of the server certificate. This value is a UNIX timestamp. The default value is the time when you call this operation. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.before_time = before_time
        # The name of the certificate user. The user of a server certificate is a server. We recommend that you enter the domain name or IP address of the server.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The code of the country in which the organization is located, such as CN or US.
        self.country = country
        # The validity period of the server certificate. Unit: days. You must specify at least one of the **Days**, **BeforeTime**, and **AfterTime** parameters. The **BeforeTime** and **AfterTime** parameters must be both empty or both specified. The following list describes how to specify these parameters:
        # 
        # *   If you specify the **Days** parameter, you can specify both the **BeforeTime** and **AfterTime** parameters or leave them both empty.
        # *   If you do not specify the **Days** parameter, you must specify both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > 
        # 
        # *   If you specify the **Days**, **BeforeTime**, and **AfterTime** parameters together, the validity period of the server certificate is determined by the value of the **Days** parameter.
        # 
        # *   The validity period of the server certificate cannot exceed the validity period of the intermediate CA certificate. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the validity period of an intermediate CA certificate.
        self.days = days
        # The additional domain names and additional IP addresses of the server certificate. After you add additional domain names and additional IP addresses to a certificate, you can apply the certificate to the domain names and IP addresses.
        # 
        # Separate multiple domain names and multiple IP addresses with commas (,).
        self.domain = domain
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the certificate. Valid values:
        # 
        # *   **0**: does not return the certificate. This is the default value.
        # *   **1**: returns the certificate.
        # *   **2**: returns the certificate and the certificate chain of the certificate.
        self.immediately = immediately
        # The name of the city in which the organization is located. The value can contain letters. The default value is the name of the city in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.locality = locality
        # The validity period of the server certificate. Unit: months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate CA certificate from which the server certificate is issued.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifier of an intermediate CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The province, municipality, or autonomous region in which the organization is located. The value can contain letters. The default value is the name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.state = state
        # The validity period of the server certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.days is not None:
            result['Days'] = self.days
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateServerCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
        x_509certificate: str = None,
    ):
        # The certificate chain of the server certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the server certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The serial number of the server certificate.
        self.serial_number = serial_number
        # The content of the server certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServerCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerCertificateWithCsrRequest(TeaModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
        days: int = None,
        domain: str = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        state: str = None,
        years: int = None,
    ):
        # The expiration time of the server certificate. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.after_time = after_time
        # The key algorithm of the server certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the server certificate must be the same as the encryption algorithm of the intermediate CA certificate. The key length can be different. For example, if the key algorithm of the intermediate CA certificate is RSA_2048, the key algorithm of the server certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # >  You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the key algorithm of an intermediate CA certificate.
        self.algorithm = algorithm
        # The issuance time of the server certificate. This value is a UNIX timestamp. The default value is the time when you call this operation. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.before_time = before_time
        # The name of the certificate user. The user of a server certificate is a server. We recommend that you enter the domain name or IP address of the server.
        self.common_name = common_name
        # The code of the country in which the organization is located, such as CN or US.
        self.country = country
        # The content of the CSR.
        # 
        # You can generate a CSR by using the OpenSSL tool or the Keytool tool. For more information, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html)
        # 
        # This parameter is required.
        self.csr = csr
        # The validity period of the server certificate. Unit: days.
        # 
        # You must specify at least one of the **Days**, **BeforeTime**, and **AfterTime** parameters. The **BeforeTime** and **AfterTime** parameters must be both empty or both specified. The following list describes how to specify these parameters:
        # 
        # *   If you specify the **Days** parameter, you can specify both the **BeforeTime** and **AfterTime** parameters or leave them both empty.********\
        # *   If you do not specify the **Days** parameter, you must specify both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > 
        # 
        # *   If you specify the **Days**, **BeforeTime**, and **AfterTime** parameters at the same time, the validity period of the server certificate is determined by the value of the **Days** parameter.
        # *   The validity period of the server certificate cannot exceed the validity period of the intermediate CA certificate. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the validity period of an intermediate CA certificate.
        self.days = days
        # The additional domain names or additional IP addresses of the server certificate. After you add additional domain names and additional IP addresses to a certificate, you can apply the certificate to the domain names and IP addresses.
        # 
        # You can specify multiple domain names and IP addresses. If you specify multiple domain names and IP addresses, separate them with commas (,).
        self.domain = domain
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the certificate. Valid values:
        # 
        # *   **0**: does not return the certificate. This is the default value.
        # *   **1**: returns the certificate.
        # *   **2**: returns the certificate and the certificate chain of the certificate.
        self.immediately = immediately
        # The name of the city in which the organization is located. The value can contain letters. The default value is the name of the city in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.locality = locality
        # The validity period of the server certificate. Unit: months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate CA certificate from which the server certificate is issued.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifier of an intermediate CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The province, municipality, or autonomous region in which the organization is located. The value can contain letters. The default value is the name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.state = state
        # The validity period of the server certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.days is not None:
            result['Days'] = self.days
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl
        if self.immediately is not None:
            result['Immediately'] = self.immediately
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.months is not None:
            result['Months'] = self.months
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateServerCertificateWithCsrResponseBody(TeaModel):
    def __init__(
        self,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
        x_509certificate: str = None,
    ):
        # The certificate chain of the server certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the server certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The serial number of the server certificate.
        self.serial_number = serial_number
        # The content of the server certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class CreateServerCertificateWithCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServerCertificateWithCsrResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServerCertificateWithCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubCACertificateRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        common_name: str = None,
        country_code: str = None,
        crl_day: int = None,
        enable_crl: bool = None,
        extended_key_usages: List[str] = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        path_len_constraint: int = None,
        state: str = None,
        years: int = None,
    ):
        # The type of the key algorithm of the intermediate CA. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of an intermediate CA certificate must be consistent with the encryption algorithm of a root CA certificate. The length of the keys can be different. For example, if the key algorithm of the root CA certificate is **RSA_2048**, the key algorithm of the intermediate CA certificate must be **RSA_1024**, **RSA_2048**, or **RSA_4096**.
        # 
        # > You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) operation to query the key algorithm of a root CA certificate.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The common name or abbreviation of the organization. The value can contain letters.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The code of the country or region in which the organization is located. You can enter an alpha-2 or alpha-3 code. For example, you can use **CN** to indicate China and use **US** to indicate the United States.
        # 
        # For more information about country codes, see the **"Country codes"** section in [Manage company profiles](https://help.aliyun.com/document_detail/198289.html).
        self.country_code = country_code
        # CRL validity period: 1-365 days
        self.crl_day = crl_day
        # Enable Crl Service.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # The extended key usages of the certificate.
        self.extended_key_usages = extended_key_usages
        # The name of the city in which the organization is located. The value can contain letters.
        # 
        # This parameter is required.
        self.locality = locality
        # The name of the organization that is associated with the intermediate CA certificate. You can enter the name of your enterprise or company. The value can contain letters.
        # 
        # This parameter is required.
        self.organization = organization
        # The name of the department or branch in the organization. The value can contain letters.
        # 
        # This parameter is required.
        self.organization_unit = organization_unit
        # The unique identifier of the root CA certificate.
        # 
        # > You can call the [DescribeCACertificateList] operation to query the unique identifiers of all CA certificates.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The path length constraint of the certificate. Default value: 0.
        self.path_len_constraint = path_len_constraint
        # The name of the province or state in which the organization is located. The value can contain letters.
        # 
        # This parameter is required.
        self.state = state
        # The validity period of the intermediate CA certificate. Unit: years.
        # 
        # We recommend that you set this parameter to 5 to 10.
        # 
        # > The validity period of the intermediate CA certificate cannot exceed the validity period of the root CA certificate. You can call the [DescribeCACertificate]operation to query the validity period of a root CA certificate.
        # 
        # This parameter is required.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.crl_day is not None:
            result['CrlDay'] = self.crl_day
        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl
        if self.extended_key_usages is not None:
            result['ExtendedKeyUsages'] = self.extended_key_usages
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.path_len_constraint is not None:
            result['PathLenConstraint'] = self.path_len_constraint
        if self.state is not None:
            result['State'] = self.state
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CrlDay') is not None:
            self.crl_day = m.get('CrlDay')
        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')
        if m.get('ExtendedKeyUsages') is not None:
            self.extended_key_usages = m.get('ExtendedKeyUsages')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('PathLenConstraint') is not None:
            self.path_len_constraint = m.get('PathLenConstraint')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class CreateSubCACertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
    ):
        # The CA certificate in the PEM format.
        self.certificate = certificate
        # The certificate chain of the CA certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the sub CA certificate created in this request.
        self.identifier = identifier
        # The ID of this call request is a unique identifier generated by Alibaba Cloud for the request, which can be used for troubleshooting and locating issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSubCACertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubCACertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClientCertificateRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the client certificate or server certificate that you want to delete. The status of the certificate must be **REVOKE**.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers and status of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DeleteClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the CA certificate that you want to query.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifiers of all CA certificates.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeCACertificateResponseBodyCertificate(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        ca_cert_chain: str = None,
        cert_issued_count: int = None,
        cert_remaining_count: int = None,
        cert_total_count: int = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        crl_day: int = None,
        crl_status: str = None,
        crl_url: str = None,
        identifier: str = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
        x_509certificate: str = None,
    ):
        # The expiration date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The encryption algorithm of the CA certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The issuance date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # CA certificate chain.
        self.ca_cert_chain = ca_cert_chain
        # The number of certificates issued by private CA instances.
        self.cert_issued_count = cert_issued_count
        # The remaining number of assignable certificate quotas.
        self.cert_remaining_count = cert_remaining_count
        # The total number of purchased certificate quotas.
        self.cert_total_count = cert_total_count
        # The type of the CA certificate. Valid values:
        # 
        # *   **ROOT**: root CA certificate
        # *   **SUB_ROOT**: intermediate CA certificate
        self.certificate_type = certificate_type
        # The common name or abbreviation of the organization that is associated with the CA certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # CRL validity period: 1-365 days.
        self.crl_day = crl_day
        # The status of the certificate revocation list (CRL) feature.
        self.crl_status = crl_status
        # The address of the CRL.
        self.crl_url = crl_url
        # The unique identifier of the CA certificate.
        self.identifier = identifier
        # The key length of the CA certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located.
        self.locality = locality
        # The MD5 fingerprint of the CA certificate.
        self.md_5 = md_5
        # The name of the organization that is associated with the CA certificate.
        self.organization = organization
        # The name of the department or branch in the organization that is associated with the CA certificate.
        self.organization_unit = organization_unit
        # The unique identifier of the root CA certificate from which the CA certificate is issued.
        # 
        # >  This parameter is returned only if the value of the **CertificateType** parameter is **SUB_ROOT**. The value SUB_ROOT indicates an intermediate CA certificate.
        self.parent_identifier = parent_identifier
        # This parameter is deprecated.
        self.sans = sans
        # The serial number of the CA certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the CA certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the CA certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located.
        self.state = state
        # The status of the CA certificate. Valid values:
        # 
        # *   **ISSUE**: The CA certificate is issued.
        # *   **REVOKE**: The CA certificate is revoked.
        self.status = status
        # The user attribute of the CA certificate, which contains the following information:
        # 
        # *   **C**: the country code in which the organization is located
        # *   **O**: the name of the organization
        # *   **OU**: the name of the department or branch in the organization
        # *   **L**: the name of the city in which the organization is located
        # *   **ST**: the name of the province, municipality, or autonomous region in which the organization is located
        # *   **CN**: the common name or abbreviation of the organization
        self.subject_dn = subject_dn
        # The content of the CA certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.ca_cert_chain is not None:
            result['CaCertChain'] = self.ca_cert_chain
        if self.cert_issued_count is not None:
            result['CertIssuedCount'] = self.cert_issued_count
        if self.cert_remaining_count is not None:
            result['CertRemainingCount'] = self.cert_remaining_count
        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.crl_day is not None:
            result['CrlDay'] = self.crl_day
        if self.crl_status is not None:
            result['CrlStatus'] = self.crl_status
        if self.crl_url is not None:
            result['CrlUrl'] = self.crl_url
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CaCertChain') is not None:
            self.ca_cert_chain = m.get('CaCertChain')
        if m.get('CertIssuedCount') is not None:
            self.cert_issued_count = m.get('CertIssuedCount')
        if m.get('CertRemainingCount') is not None:
            self.cert_remaining_count = m.get('CertRemainingCount')
        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CrlDay') is not None:
            self.crl_day = m.get('CrlDay')
        if m.get('CrlStatus') is not None:
            self.crl_status = m.get('CrlStatus')
        if m.get('CrlUrl') is not None:
            self.crl_url = m.get('CrlUrl')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class DescribeCACertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: DescribeCACertificateResponseBodyCertificate = None,
        request_id: str = None,
        years: int = None,
    ):
        # The details about the CA certificate.
        self.certificate = certificate
        # The ID of the request.
        self.request_id = request_id
        # The validity period of the CA certificate. Unit: years.
        self.years = years

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = DescribeCACertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class DescribeCACertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCACertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of created CA certificates, which includes root CA certificates and intermediate CA certificates.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCACertificateCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCACertificateCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCACertificateCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificateListRequest(TeaModel):
    def __init__(
        self,
        ca_status: str = None,
        cert_type: str = None,
        current_page: int = None,
        identifier: str = None,
        issuer_type: str = None,
        show_size: int = None,
        valid_status: str = None,
    ):
        # Ca status.
        # 
        # - issue: inUse.
        # - forbidden: forbidden.
        # - revoke: revoked.
        self.ca_status = ca_status
        # The type of the certificate. Valid values:
        # 
        # - root: rootCA.
        # - subRoot: subCA.
        # - externalCa: import.
        self.cert_type = cert_type
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The unique identifier of the CA certificate.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifiers of all CA certificates.
        self.identifier = identifier
        # The CA Issuer Type.
        # 
        # - local: Private certificate.
        # - iTrusChina: Compliance CA.
        # - external: External Import.
        self.issuer_type = issuer_type
        # The number of CA certificates per page. Default value: **20**.
        self.show_size = show_size
        # valid time.
        # 
        # - valid: means in the valid period.
        # - notValid: means expired.
        self.valid_status = valid_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_status is not None:
            result['CaStatus'] = self.ca_status
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.issuer_type is not None:
            result['IssuerType'] = self.issuer_type
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.valid_status is not None:
            result['ValidStatus'] = self.valid_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaStatus') is not None:
            self.ca_status = m.get('CaStatus')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('IssuerType') is not None:
            self.issuer_type = m.get('IssuerType')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('ValidStatus') is not None:
            self.valid_status = m.get('ValidStatus')
        return self


class DescribeCACertificateListResponseBodyCertificateList(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        alias: str = None,
        before_date: int = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        gift: int = None,
        identifier: str = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
        trial: int = None,
        x_509certificate: str = None,
        years: int = None,
    ):
        # The expiration date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The encryption algorithm of the CA certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The alias of the CA.
        self.alias = alias
        # The issuance date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # The type of the CA certificate. Valid values:
        # 
        # *   **ROOT**: a root CA certificate.
        # *   **SUB_ROOT**: an intermediate CA certificate.
        self.certificate_type = certificate_type
        # The common name or abbreviation of the organization that is associated with the CA certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        self.gift = gift
        # The unique identifier of the CA certificate.
        self.identifier = identifier
        # The key length of the CA certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located.
        self.locality = locality
        # The MD5 fingerprint of the CA certificate.
        self.md_5 = md_5
        # The name of the organization that is associated with the CA certificate.
        self.organization = organization
        # The name of the department or branch in the organization that is associated with the CA certificate.
        self.organization_unit = organization_unit
        # The unique identifier of the root CA certificate from which the CA certificate is issued.
        # 
        # >  This parameter is returned only if the value of the **CertificateType** parameter is **SUB_ROOT**. The value SUB_ROOT indicates an intermediate CA certificate.
        self.parent_identifier = parent_identifier
        # This parameter is deprecated.
        self.sans = sans
        # The serial number of the CA certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the CA certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the CA certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located.
        self.state = state
        # The status of the CA certificate. Valid values:
        # 
        # *   **ISSUE**: The CA certificate is issued.
        # *   **REVOKE**: The CA certificate is revoked.
        self.status = status
        # The Distinguished Name (DN) attribute of the CA certificate, which indicates the user information of the certificate. The DN attribute contains the following information:
        # 
        # *   **C**: the code of the country in which the organization is located.
        # *   **O**: the name of the organization.
        # *   **OU**: the name of the department or branch in the organization.
        # *   **L**: the name of the city in which the organization is located.
        # *   **CN**: the common name or abbreviation of the organization.
        self.subject_dn = subject_dn
        self.trial = trial
        # The content of the CA certificate.
        self.x_509certificate = x_509certificate
        # The validity period of the CA certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.gift is not None:
            result['Gift'] = self.gift
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.trial is not None:
            result['Trial'] = self.trial
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        if self.years is not None:
            result['Years'] = self.years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Gift') is not None:
            self.gift = m.get('Gift')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        if m.get('Years') is not None:
            self.years = m.get('Years')
        return self


class DescribeCACertificateListResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list: List[DescribeCACertificateListResponseBodyCertificateList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The details about the CA certificates.
        self.certificate_list = certificate_list
        # The page number of the returned page.
        self.current_page = current_page
        # The number of returned pages.
        self.page_count = page_count
        # The ID of the request.
        self.request_id = request_id
        # The number of CA certificates returned per page.
        self.show_size = show_size
        # The total number of root CA certificates and intermediate CA certificates that are returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = DescribeCACertificateListResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCACertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCACertificateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCACertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificatePrivateKeyRequest(TeaModel):
    def __init__(
        self,
        encrypted_code: str = None,
        identifier: str = None,
    ):
        # The password that is used to encrypt the private key. The password can contain letters, digits, and special characters, such as `, + - _ #`. The password can be up to 32 bytes in length.
        # 
        # **Warning** You must remember the password that you specify. The password is required to decrypt the encrypted private key. If you forget the password, the encrypted private key that is returned cannot be decrypted. You must call this operation again.
        # 
        # This parameter is required.
        self.encrypted_code = encrypted_code
        # The unique identifier of the client certificate or server certificate that you want to query.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_code is not None:
            result['EncryptedCode'] = self.encrypted_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedCode') is not None:
            self.encrypted_code = m.get('EncryptedCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeCertificatePrivateKeyResponseBody(TeaModel):
    def __init__(
        self,
        encrypted_data: str = None,
        request_id: str = None,
    ):
        # The content of the encrypted private key.
        self.encrypted_data = encrypted_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_data is not None:
            result['EncryptedData'] = self.encrypted_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedData') is not None:
            self.encrypted_data = m.get('EncryptedData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificatePrivateKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificatePrivateKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCertificatePrivateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientCertificateRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the client certificate or the server certificate that you want to query.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeClientCertificateResponseBodyCertificate(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        days: int = None,
        identifier: str = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
        x_509certificate: str = None,
    ):
        # The expiration date of the certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The type of the encryption algorithm of the certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The issuance date of the certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # The type of the certificate. Valid values:
        # 
        # *   **CLIENT**: client certificate
        # *   **SERVER**: server certificate
        self.certificate_type = certificate_type
        # The common name of the certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # The validity period of the certificate. Unit: days.
        self.days = days
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The key length of the certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.locality = locality
        # The MD5 fingerprint of the certificate.
        self.md_5 = md_5
        # The name of the organization. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.organization = organization
        # The name of the department in the organization. The organization is associated with the intermediate certificate authority (CA) certificate from which the certificate is issued.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate certificate from which the client certificate is issued.
        self.parent_identifier = parent_identifier
        # The subject alternative name (SAN) extension of the certificate. The value indicates additional information, including the additional domain names or IP addresses that are associated with the certificate.
        # 
        # The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that corresponds to a SAN extension. A SAN extension struct contains the following parameters:
        # 
        # *   **Type**: the type of the extension. Data type: integer. Valid values:
        # 
        #     *   **1**: an email address
        #     *   **2**: a domain name
        #     *   **6**: a Uniform Resource Identifier (URI)
        #     *   **7**: an IP address
        # 
        # *   **Value**: the value of the extension. Data type: string.
        self.sans = sans
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.state = state
        # The status of the certificate. Valid values:
        # 
        # *   **ISSUE**: issued
        # *   **REVOKE**: revoked
        self.status = status
        # The distinguished name (DN) extension of the certificate, which indicates the user of the certificate. The DN extension includes the following information:
        # 
        # *   **C**: the country
        # *   **O**: the organization
        # *   **OU**: the department
        # *   **L**: the city
        # *   **ST**: the province, municipality, or autonomous region
        # *   **CN**: the common name
        self.subject_dn = subject_dn
        # The content of the certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.days is not None:
            result['Days'] = self.days
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class DescribeClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate: DescribeClientCertificateResponseBodyCertificate = None,
        request_id: str = None,
    ):
        # The details about the client certificate or the server certificate.
        self.certificate = certificate
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = DescribeClientCertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientCertificateStatusRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifiers of the client certificates or server certificates that you want to query. Separate multiple unique identifiers with commas (,).
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class DescribeClientCertificateStatusResponseBodyCertificateStatus(TeaModel):
    def __init__(
        self,
        revoke_time: int = None,
        serial_number: str = None,
        status: str = None,
    ):
        # The date on which the certificate was revoked.
        # 
        # >  This parameter is returned only when the value of the **Status** parameter is **revoked**. The value revoked indicates that the certificate is revoked.
        self.revoke_time = revoke_time
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The status of the certificate. Valid values:
        # 
        # *   **good**: The certificate is not revoked.
        # *   **revoked**: The certificate is revoked.
        # *   **unknown**: The server cannot determine the status of the certificate.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.revoke_time is not None:
            result['RevokeTime'] = self.revoke_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RevokeTime') is not None:
            self.revoke_time = m.get('RevokeTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClientCertificateStatusResponseBody(TeaModel):
    def __init__(
        self,
        certificate_status: List[DescribeClientCertificateStatusResponseBodyCertificateStatus] = None,
        request_id: str = None,
    ):
        # An array that consists of the status information about the certificates.
        self.certificate_status = certificate_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate_status:
            for k in self.certificate_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateStatus'] = []
        if self.certificate_status is not None:
            for k in self.certificate_status:
                result['CertificateStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_status = []
        if m.get('CertificateStatus') is not None:
            for k in m.get('CertificateStatus'):
                temp_model = DescribeClientCertificateStatusResponseBodyCertificateStatus()
                self.certificate_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClientCertificateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClientCertificateStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClientCertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCAInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        instance_id: str = None,
    ):
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The ID of the private CA instance.
        # 
        # >  After you purchase a private CA instance by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist), you can click **Details** for the private CA instance on the **Private Certificates** page to query the ID of the private CA instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCAInstanceStatusResponseBodyInstanceStatusList(TeaModel):
    def __init__(
        self,
        after_time: int = None,
        before_time: int = None,
        cert_issued_count: int = None,
        cert_total_count: int = None,
        identifier: str = None,
        instance_id: str = None,
        status: str = None,
        type: str = None,
        use_expire_time: int = None,
    ):
        # The expiration date of the private CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >  This parameter is returned only when the value of the **Status** parameter is **USED** or **REVOKE**. The value USED indicates that the private CA instance is enabled, and the value REVOKE indicates that the instance is revoked.
        self.after_time = after_time
        # The issuance date of the private CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >  This parameter is returned only when the value of the **Status** parameter is **USED** or **REVOKE**. The value USED indicates that the private CA instance is enabled, and the value REVOKE indicates that the instance is revoked.
        self.before_time = before_time
        # The number of certificates that are issued by using the private CA instance.
        self.cert_issued_count = cert_issued_count
        # The number of certificates that can be issued by using the private CA instance.
        # 
        # For a private root CA instance whose **Type** is **ROOT**, this parameter indicates the number of intermediate CA certificates that can be issued.
        # 
        # For a private intermediate CA instance whose **Type** is **SUB_ROOT**, this parameter indicates the total number of client certificates and server certificates that can be issued
        self.cert_total_count = cert_total_count
        # The unique identifier of the private CA certificate.
        # 
        # >  This parameter is returned only when the value of the **Status** parameter is **USED** or **REVOKE**. The value USED indicates that the private CA instance is enabled, and the value REVOKE indicates that the instance is revoked.
        self.identifier = identifier
        # The ID of the private CA instance.
        self.instance_id = instance_id
        # The status of the private CA instance. Valid values:
        # 
        # *   **BUY**: The private CA instance is purchased but is not enabled.
        # *   **USED**: The private CA instance is enabled.
        # *   **REFUND**: The private CA instance is refunded.
        # *   **REVOKE**: The private CA instance is revoked.
        self.status = status
        # The type of the private CA instance. Valid values:
        # 
        # *   **ROOT**: root CA instance
        # *   **SUB_ROOT**: intermediate CA instance
        self.type = type
        # The expiration date of the private CA instance. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >  This parameter corresponds to the duration that you select when you purchase the private CA instance. The duration indicates the subscription period of the Private Certificate Authority (PCA) service.
        self.use_expire_time = use_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_time is not None:
            result['AfterTime'] = self.after_time
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.cert_issued_count is not None:
            result['CertIssuedCount'] = self.cert_issued_count
        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.use_expire_time is not None:
            result['UseExpireTime'] = self.use_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('CertIssuedCount') is not None:
            self.cert_issued_count = m.get('CertIssuedCount')
        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseExpireTime') is not None:
            self.use_expire_time = m.get('UseExpireTime')
        return self


class GetCAInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        instance_status_list: List[GetCAInstanceStatusResponseBodyInstanceStatusList] = None,
        request_id: str = None,
    ):
        # The status information of the private CA instance.
        self.instance_status_list = instance_status_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_status_list:
            for k in self.instance_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k in self.instance_status_list:
                result['InstanceStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k in m.get('InstanceStatusList'):
                temp_model = GetCAInstanceStatusResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCAInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCAInstanceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCAInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertRequest(TeaModel):
    def __init__(
        self,
        after_date: str = None,
        before_date: str = None,
        current_page: int = None,
        instance_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        show_size: int = None,
        status: str = None,
        type: str = None,
    ):
        self.after_date = after_date
        self.before_date = before_date
        self.current_page = current_page
        self.instance_uuid = instance_uuid
        self.max_results = max_results
        self.next_token = next_token
        self.show_size = show_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCertResponseBodyList(TeaModel):
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
        extra: str = None,
        id: str = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCertResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[ListCertResponseBodyList] = None,
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
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
            for k in m.get('List'):
                temp_model = ListCertResponseBodyList()
                self.list.append(temp_model.from_map(k))
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


class ListCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCertResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClientCertificateRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        identifier: str = None,
        show_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The unique identifier of the client certificate or the server certificate that you want to query.
        # 
        # >  You can call the [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) operation to query the unique identifiers of all client certificates and server certificates.
        self.identifier = identifier
        # The number of certificates to return on each page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListClientCertificateResponseBodyCertificateList(TeaModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        days: int = None,
        identifier: str = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
        x_509certificate: str = None,
    ):
        # The expiration date of the certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The type of the encryption algorithm of the certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The issuance date of the certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # The type of the certificate. Valid values:
        # 
        # *   **CLIENT**: client certificate
        # *   **SERVER**: server certificate
        self.certificate_type = certificate_type
        # The common name of the certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # The validity period of the certificate. Unit: days.
        self.days = days
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The key length of the certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.locality = locality
        # The MD5 fingerprint of the certificate.
        self.md_5 = md_5
        # The name of the organization. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.organization = organization
        # The name of the department in the organization. The organization is associated with the intermediate certificate authority (CA) certificate from which the certificate is issued.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate certificate from which the client certificate is issued.
        self.parent_identifier = parent_identifier
        # The subject alternative name (SAN) extension of the certificate. The value indicates additional information, including the additional domain names or IP addresses that are associated with the certificate.
        # 
        # The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that corresponds to a SAN extension. A SAN extension struct contains the following parameters:
        # 
        # *   **Type**: the type of the extension. Data type: integer. Valid values:
        # 
        #     *   **1**: an email address
        #     *   **2**: a domain name
        #     *   **6**: a Uniform Resource Identifier (URI)
        #     *   **7**: an IP address
        # 
        # *   **Value**: the value of the extension. Data type: string.
        self.sans = sans
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.state = state
        # The status of the certificate. Valid values:
        # 
        # *   **ISSUE**: issued
        # *   **REVOKE**: revoked
        self.status = status
        # The distinguished name (DN) extension of the certificate, which indicates the user of the certificate. The DN extension includes the following information:
        # 
        # *   **C**: the country
        # *   **O**: the organization
        # *   **OU**: the department
        # *   **L**: the city
        # *   **ST**: the province, municipality, or autonomous region
        # *   **CN**: the common name
        self.subject_dn = subject_dn
        # The content of the certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.days is not None:
            result['Days'] = self.days
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class ListClientCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list: List[ListClientCertificateResponseBodyCertificateList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # An array that consists of the details about all client certificates and server certificates.
        self.certificate_list = certificate_list
        # The page number of the current page.
        self.current_page = current_page
        # The total number of pages returned.
        self.page_count = page_count
        # The ID of the request.
        self.request_id = request_id
        # The number of certificates that are returned per page.
        self.show_size = show_size
        # The number of client certificates and server certificates that are returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = ListClientCertificateResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClientCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClientCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClientCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRevokeCertificateRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        show_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The number of revoked certificates to return on each page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListRevokeCertificateResponseBodyCertificateList(TeaModel):
    def __init__(
        self,
        after_date: str = None,
        algorithm: str = None,
        before_date: str = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        identifier: str = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        revoke_date: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
    ):
        # The expiration date of the certificate. The date is in the `yyyy-MM-ddT00:00Z` format. For example, the value `2021-12-31T00:00Z` indicates December 31, 2021.
        self.after_date = after_date
        # The type of the encryption algorithm of the certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The issuance date of the certificate. The date is in the `yyyy-MM-ddT00:00Z` format. For example, the value `2021-01-01T00:00Z` indicates January 1, 2021.
        self.before_date = before_date
        # The type of the certificate.
        self.certificate_type = certificate_type
        # The common name of the certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The key length of the certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.locality = locality
        # The MD5 fingerprint of the certificate.
        self.md_5 = md_5
        # The name of the organization. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.organization = organization
        # The name of the department in the organization. The organization is associated with the intermediate certificate authority (CA) certificate from which the certificate is issued.
        self.organization_unit = organization_unit
        # The identifier of the root certificate.
        self.parent_identifier = parent_identifier
        # The date on which the certificate was revoked. The value is in the `yyyy-MM-ddT00:00Z` format. For example, the value `2021-09-01T00:00Z` indicates September 1, 2021.
        self.revoke_date = revoke_date
        # The subject alternative name (SAN) extension of the certificate.
        # 
        # The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that corresponds to a SAN extension. A SAN extension struct contains the following parameters:
        # 
        # *   **Type**: the type of the extension. Data type: integer. Valid values:
        # 
        #     *   **1**: an email address
        #     *   **2**: a domain name
        #     *   **6**: a Uniform Resource Identifier (URI)
        #     *   **7**: an IP address
        # 
        # *   **Value**: the value of the extension. Data type: string.
        self.sans = sans
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate certificate from which the certificate is issued.
        self.state = state
        # The status.
        self.status = status
        # The distinguished name (DN) extension of the certificate, which indicates the user of the certificate. The DN extension includes the following information:
        # 
        # *   **C**: the country
        # *   **O**: the organization
        # *   **OU**: the department
        # *   **L**: the city
        # *   **ST**: the province, municipality, or autonomous region
        # *   **CN**: the common name
        self.subject_dn = subject_dn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.key_size is not None:
            result['KeySize'] = self.key_size
        if self.locality is not None:
            result['Locality'] = self.locality
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit
        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier
        if self.revoke_date is not None:
            result['RevokeDate'] = self.revoke_date
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')
        if m.get('Locality') is not None:
            self.locality = m.get('Locality')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')
        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')
        if m.get('RevokeDate') is not None:
            self.revoke_date = m.get('RevokeDate')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')
        return self


class ListRevokeCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list: List[ListRevokeCertificateResponseBodyCertificateList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # An array that consists of the details about the revoked client certificates or server certificates.
        self.certificate_list = certificate_list
        # The page number of the current page.
        self.current_page = current_page
        # The total number of pages returned.
        self.page_count = page_count
        # The ID of the request.
        self.request_id = request_id
        # The number of revoked certificates that are returned per page.
        self.show_size = show_size
        # The total number of revoked client certificates and server certificates that are returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_list:
            for k in self.certificate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k in self.certificate_list:
                result['CertificateList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k in m.get('CertificateList'):
                temp_model = ListRevokeCertificateResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRevokeCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRevokeCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRevokeCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCACertificateStatusRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        status: str = None,
    ):
        # The unique identifier of the CA certificate whose status you want to change.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifiers of all CA certificates.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The state to which you want to change the CA certificate. Set to the value to **REVOKE**. After this operation is called, the status of the CA certificate is changed to **REVOKE**.
        # 
        # >  You can call this operation only if the status of a CA certificate is **ISSUE**. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the status of a CA certificate.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateCACertificateStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCACertificateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCACertificateStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCACertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadPcaCertToCasRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # This parameter is required.
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class UploadPcaCertToCasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadPcaCertToCasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadPcaCertToCasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadPcaCertToCasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


