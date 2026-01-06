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
        self.cert_id = cert_id
        # The content of the certificate in the PEM format. For more information about the PEM format and how to convert certificate formats, see [What formats are used for mainstream digital certificates?](https://help.aliyun.com/document_detail/42214.html)
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **certificate**. The value certificate indicates that the certificate is issued.
        self.certificate = certificate
        # The content that you need to write to the newly created file when you use the file verification method.
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **FILE**. The value domain_verify indicates that the verification of the domain name ownership is not complete, and the value FILE indicates that the file verification method is used.
        self.content = content
        # The domain name to be verified when you use the file verification method. You must connect to the DNS server of the domain name and create a file on the server. The file is specified by the **Uri** parameter.
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **FILE**. The value domain_verify indicates that the verification of the domain name ownership is not complete, and the value FILE indicates that the file verification method is used.
        self.domain = domain
        # The private key of the certificate in the PEM format. For more information about the PEM format and how to convert certificate formats, see [What formats are used for mainstream digital certificates?](https://help.aliyun.com/document_detail/42214.html)
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **certificate**. The value certificate indicates that the certificate is issued.
        self.private_key = private_key
        # The DNS record that you need to manage when you use the DNS verification method.
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **DNS**. The value domain_verify indicates that the verification of the domain name ownership is not complete, and the value DNS indicates that the DNS verification method is used.
        self.record_domain = record_domain
        # The type of the DNS record that you need to add when you use the DNS verification method. Valid values:
        # 
        # *   **TXT**
        # *   **CNAME**
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **DNS**. The value domain_verify indicates that the verification of the domain name ownership is not complete.
        self.record_type = record_type
        # You need to add a TXT record to the DNS records only when you use the DNS verification method.
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **DNS**. The value domain_verify indicates that the verification of the domain name ownership is not complete, and the value DNS indicates that the DNS verification method is used.
        self.record_value = record_value
        # The ID of the request.
        self.request_id = request_id
        # The status of the certificate application order. Valid values:
        # 
        # *   **domain_verify**: **pending review**, which indicates that you have not completed the verification of the domain name ownership after you submit the certificate application.
        #      >After you submit a certificate application, you must manually complete the verification of the domain name ownership. The CA reviews the certificate application only after the verification is complete. If you have not completed the verification of the domain name ownership, you can complete the verification based on the data returned by this operation.
        # 
        # *   **process**: **being reviewed**, which indicates that the certificate application is being reviewed by the CA.
        # 
        # *   **verify_fail**: **review failed**, which indicates that the certificate application failed to be reviewed.
        #     >  If a certificate application fails to be reviewed, the information that you specified in the certificate application may be incorrect. We recommend that you call the [DeleteCertificateRequest](https://help.aliyun.com/document_detail/164109.html) operation to delete the certificate application order and resubmit a certificate application. After the order is deleted, the quota that is consumed for the order is released.
        # 
        # *   **certificate**: **issued**, which indicates that the certificate is issued.
        # 
        # *   **payed**: **pending application**, which indicates that you have not submitted a certificate application.
        # 
        # *   **unknow**: The status is **unknown**.
        self.type = type
        # The file that you need to create on the DNS server when you use the file verification method. **The value of this parameter contains the file path and file name.**
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify** and the value of the **ValidateType** parameter is **FILE**. The value domain_verify indicates that the verification of the domain name ownership is not complete, and the value FILE indicates that the file verification method is used.
        self.uri = uri
        # The verification method of the domain name ownership. Valid values:
        # 
        # *   **DNS**: DNS verification. If you use this method, you must add a TXT record to the DNS records of the domain name in the management platform of the domain name.
        # *   **FILE**: file verification. If you use this method, you must create a specified file on the DNS server.
        # 
        # >  This parameter is returned only when the value of the **Type** parameter is **domain_verify**. The value domain_verify indicates that the verification of the domain name ownership is not complete.
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

