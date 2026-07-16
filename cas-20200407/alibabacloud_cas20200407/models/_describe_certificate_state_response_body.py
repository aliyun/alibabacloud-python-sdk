# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCertificateStateResponseBody(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        certificate: str = None,
        content: str = None,
        domain: str = None,
        private_key: str = None,
        record_domain: str = None,
        record_type: str = None,
        record_value: str = None,
        request_id: str = None,
        type: str = None,
        uri: str = None,
        validate_type: str = None,
    ):
        # The certificate ID.
        # 
        # > This parameter is returned when the certificate is issued.
        self.cert_id = cert_id
        # The certificate content (in PEM format). For more information about the PEM format and how to convert the format of a certificate, see [What are the formats of mainstream digital certificates?](https://help.aliyun.com/document_detail/42214.html).
        # 
        # > This parameter is returned only when **Type** is set to **certificate** (indicating that the certificate has been issued).
        self.certificate = certificate
        # The content that you need to write to the newly created file when you use the file validation method for domain validation.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **FILE** (indicating the file validation method).
        self.content = content
        # The domain name to be validated when you use the file validation method for domain validation. You need to connect to the server corresponding to this domain name and create the specified file (i.e., **Uri**) on the server.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **FILE** (indicating the file validation method).
        self.domain = domain
        # The content of the certificate private key (in PEM format). For more information about the PEM format and how to convert the format of a certificate, see [What are the formats of mainstream digital certificates?](https://help.aliyun.com/document_detail/42214.html).
        # 
        # > This parameter is returned only when **Type** is set to **certificate** (indicating that the certificate has been issued).
        self.private_key = private_key
        # The host record that you need to operate when you use the DNS validation method for domain validation.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **DNS** (indicating the DNS validation method).
        self.record_domain = record_domain
        # The type of DNS record that you need to add when you use the DNS validation method for domain validation. Valid values:
        # 
        # - **TXT**: text record.
        # 
        # - **CNAME**: alias record.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **DNS** (indicating the DNS validation method).
        self.record_type = record_type
        # The record value that you need to add when you use the DNS validation method for domain validation.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **DNS** (indicating the DNS validation method).
        self.record_value = record_value
        # The ID of the request.
        self.request_id = request_id
        # The status of the certificate request order. Valid values:
        # 
        # - **domain_verify**: **Pending validation**, which indicates that you have not completed domain validation after submitting the certificate request.
        # 
        #   > After you submit a certificate request, you must manually complete domain ownership validation before the certificate request can enter the review stage. If you have not completed domain validation, you can refer to the response parameters of this operation to complete domain validation.
        # 
        # - **process**: **Under review**, which indicates that the certificate request is being reviewed by the CA center.
        # 
        # - **verify_fail**: **Review failed**, which indicates that the certificate request failed the review.
        # 
        #   > The review may fail because the certificate request information you submitted is incorrect. We recommend that you call [DeleteCertificateRequest](https://help.aliyun.com/document_detail/455294.html) to delete the order that failed the review (deleted orders do not consume certificate resource plan quota) and submit a new certificate request.
        # 
        # - **certificate**: **Issued**, which indicates that the certificate has been issued.
        # 
        # - **payed**: **Pending request**, which indicates that the certificate is pending request.
        # 
        # - **unknow**: **Unknown status**.
        self.type = type
        # The file that you need to create on the domain server when you use the file validation method for domain validation. **Uri** includes the file path and name.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage) and **ValidateType** is set to **FILE** (indicating the file validation method).
        self.uri = uri
        # The domain validation method selected when submitting the certificate request. Valid values:
        # 
        # - **DNS**: DNS validation. This method validates domain ownership by adding the specified DNS record to the domain on the DNS management platform.
        # 
        # - **FILE**: file validation. This method validates domain ownership by creating the specified file on the domain server.
        # 
        # > This parameter is returned only when **Type** is set to **domain_verify** (indicating the domain validation stage).
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.content is not None:
            result['Content'] = self.content

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.record_domain is not None:
            result['RecordDomain'] = self.record_domain

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.record_value is not None:
            result['RecordValue'] = self.record_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('RecordDomain') is not None:
            self.record_domain = m.get('RecordDomain')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')

        return self

