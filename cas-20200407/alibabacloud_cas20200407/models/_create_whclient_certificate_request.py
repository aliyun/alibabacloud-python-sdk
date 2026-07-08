# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWHClientCertificateRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
        days: int = None,
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
        # The expiration time of the client certificate, specified as a Unix timestamp in seconds.
        # 
        # > The `BeforeTime` and `AfterTime` parameters must be specified together or not at all.
        self.after_time = after_time
        # The key algorithm for the client certificate. The format is `<encryption_algorithm>_<key_length>`. Valid values:
        # 
        # - **RSA_1024**: The corresponding signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_2048**: The corresponding signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_4096**: The corresponding signature algorithm is Sha256WithRSA.
        # 
        # - **ECC_256**: The corresponding signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_384**: The corresponding signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_512**: The corresponding signature algorithm is Sha256WithECDSA.
        # 
        # - **SM2_256**: The corresponding signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the client certificate must match that of the issuing subordinate CA certificate, but the key lengths can differ. For example, if the key algorithm of the subordinate CA certificate is RSA_2048, the key algorithm for the client certificate must be one of RSA_1024, RSA_2048, or RSA_4096.
        self.algorithm = algorithm
        # The issuance time of the client certificate, as a Unix timestamp in seconds. If omitted, this defaults to the time of the API call.
        # 
        # > The `BeforeTime` and `AfterTime` parameters must be specified together or not at all.
        self.before_time = before_time
        # The common name of the client certificate. Supports Chinese, English, and other characters.
        self.common_name = common_name
        # The country where the organization is located.
        self.country = country
        # The content of the certificate signing request (CSR). You can generate a CSR with tools like OpenSSL or Keytool.
        self.csr = csr
        # The validity period of the client certificate, in days.
        # 
        # You cannot leave the `Days`, `BeforeTime`, and `AfterTime` parameters all empty. The `BeforeTime` and `AfterTime` parameters must be specified together or not at all.
        # 
        # - If you specify the `Days` parameter, specifying `BeforeTime` and `AfterTime` is optional.
        # 
        # - If you do not specify the `Days` parameter, you must specify both `BeforeTime` and `AfterTime`.
        # 
        # > If you specify `Days`, `BeforeTime`, and `AfterTime` simultaneously, the `Days` parameter takes precedence in determining the validity period.
        self.days = days
        # Specifies which certificate content to return in the response.
        # 
        # - **0**: Does not return the certificate (default).
        # 
        # - **1**: Returns the certificate.
        # 
        # - **2**: Returns the certificate and its certificate chain.
        self.immediately = immediately
        # The city where the organization is located. Chinese, English, and other characters are supported.
        self.locality = locality
        # The validity period of the certificate, in months.
        self.months = months
        # The organization name associated with the root CA certificate, typically your company or enterprise name. Supports Chinese, English, and other characters.
        self.organization = organization
        # The name of the department or business unit within the organization.
        self.organization_unit = organization_unit
        # The unique identifier of the issuing subordinate CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The type of the subject alternative name (SAN) for the client certificate. Valid values:
        # 
        # - **1**: email address.
        # 
        # - **2**: domain name.
        # 
        # - **6**: Uniform Resource Identifier (URI).
        # 
        # - **7**: IP address.
        self.san_type = san_type
        # The value of the SAN extension. To specify multiple values, separate them with commas (,).
        self.san_value = san_value
        # The province, municipality, or autonomous region where the organization is located. Chinese, English, and other characters are supported.
        self.state = state
        # The validity period of the certificate, in years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

