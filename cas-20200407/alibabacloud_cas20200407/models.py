# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelCertificateForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        # The order ID.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelCertificateForPackageRequestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CancelCertificateForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCertificateForPackageRequestResponseBody = None,
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
            temp_model = CancelCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        # The order ID.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CancelOrderRequestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CancelOrderRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOrderRequestResponseBody = None,
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
            temp_model = CancelOrderRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateForPackageRequestRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCertificateForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        company_name: str = None,
        csr: str = None,
        domain: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        tags: List[CreateCertificateForPackageRequestRequestTags] = None,
        username: str = None,
        validate_type: str = None,
    ):
        # The company name of the certificate application.
        # 
        # >  This parameter is available only when you apply for OV certificates. For more information, see [Manage company profiles](https://help.aliyun.com/document_detail/198289.html). If you want to apply for a DV certificate, you do not need to add a company profile.
        # 
        # If you specify a company name, the information about the company that is configured in the **Information Management** module is used. If you do not specify this parameter, the information about the most recent company that is added to the **Information Management** module is used.
        self.company_name = company_name
        # The content of the certificate signing request (CSR) file that is manually generated by using OpenSSL or Keytool for the domain name. The key algorithm in the CSR file must be Rivest-Shamir-Adleman (RSA) or elliptic-curve cryptography (ECC), and the key length of the RSA algorithm must be greater than or equal to 2,048 characters. For more information about how to create a CSR file, see [Create a CSR file](https://help.aliyun.com/document_detail/313297.html). If you do not specify this parameter, Certificate Management Service automatically creates a CSR file.
        # 
        # A CSR file contains the information about your server and company. When you apply for a certificate, you must submit the CSR file to the CA. The CA signs the CSR file by using the private key of the root certificate and generates a public key file to issue your certificate.
        # 
        # >  The \\*\\*CN\\*\\* field in CSR file specifies the domain name that is bound to the certificate. You must include the field in the parameter value.
        self.csr = csr
        # The domain name that you want to bind to the certificate. The domain name must meet the following requirements:
        # 
        # *   The domain name must be a single domain name or a wildcard domain name. Example: `*.aliyundoc.com`.
        # *   You can specify multiple domain names. Separate multiple domain names with commas (,). You can specify a maximum of five domain names.
        # *   If you specify multiple domain names, the domain names must be only single domain names or only wildcard domain names. You cannot specify both single domain names and wildcard domain names.
        # 
        # >  If you want to bind multiple domain names to the certificate, you must specify this parameter. You must specify at least one of the Domain parameter and the \\*\\*Csr\\*\\* parameter. If you specify both the Domain parameter and the \\*\\*Csr\\*\\* parameter, the value of the \\*\\*CN\\*\\* field in the \\*\\*Csr\\*\\* parameter is used as the domain name that is bound to the certificate.
        self.domain = domain
        # The email address of the applicant. After the CA receives your certificate application, the CA sends a verification email to the email address that you specify. You must log on to the mailbox, open the mail, and complete the verification of the domain name ownership based on the steps that are described in the email.
        # 
        # If you do not specify this parameter, the information about the most recent contact that is added to the **Information Management** module is used. For more information about how to add a contact to the **Information Management** module, see [Manage contacts](https://help.aliyun.com/document_detail/198262.html).
        self.email = email
        # The contact phone number of the applicant. CA staff can call the phone number to confirm the information in your certificate application.
        # 
        # If you do not specify this parameter, the information about the most recent contact that is added to the **Information Management** module is used. For more information about how to add a contact to the **Information Management** module, see [Manage contacts](https://help.aliyun.com/document_detail/198262.html).
        self.phone = phone
        # The specifications of the certificate that you want to apply for. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain domain validated (DV) certificate, which is free and valid for 3 months. This value is available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate, which is free and valid for 1 year. This value is available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **symantec-ov-1-personal**: DigiCert single-domain organization validated (OV) certificate.
        # *   **symantec-ov-w-personal**: DigiCert wildcard OV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **geotrust-ov-1-personal**: GeoTrust single-domain OV certificate.
        # *   **geotrust-ov-w-personal**: GeoTrust wildcard OV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        # *   **globalsign-ov-1-personal**: GlobalSign single-domain OV certificate.
        # *   **globalsign-ov-w-advanced**: GlobalSign wildcard OV certificate.
        # *   **cfca-ov-1-personal**: China Financial Certification Authority (CFCA) single-domain OV certificate, available only on the China site (aliyun.com).
        # *   **cfca-ev-w-advanced**: CFCA wildcard OV certificate, available only on the China site (aliyun.com).
        self.product_code = product_code
        # The list of tags.
        self.tags = tags
        # The name of the applicant.
        # 
        # If you do not specify this parameter, the information about the most recent contact that is added to the **Information Management** module is used. For more information about how to add a contact to the **Information Management** module, see [Manage contacts](https://help.aliyun.com/document_detail/198262.html).
        self.username = username
        # The verification method of the domain name ownership. Valid values:
        # 
        # *   **DNS**: DNS verification. If you use this method, you must add a TXT record to the DNS records of the domain name in the management platform of the domain name. You must have operation permissions on domain name resolution to verify the ownership of the domain name.
        # *   **FILE**: file verification. If you use this method, you must create a specified file on the DNS server. You must have administrative rights on the DNS server to verify the ownership of the domain name.
        # 
        # For more information about the verification methods, see [Verify the ownership of a domain name](https://help.aliyun.com/document_detail/48016.html).
        self.validate_type = validate_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateCertificateForPackageRequestRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateForPackageRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the certificate application order.
        # 
        # >  You can use the ID to query the status of the certificate application order. For more information, see [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html).
        self.order_id = order_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateForPackageRequestResponseBody = None,
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
            temp_model = CreateCertificateForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequestRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. You cannot specify empty strings as tag keys.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCertificateRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        tags: List[CreateCertificateRequestRequestTags] = None,
        username: str = None,
        validate_type: str = None,
    ):
        # The domain name that you want to bind to the certificate. You can specify only one domain name.
        # 
        # >  The domain name must match the certificate specifications that you specify for the **ProductCode** parameter. If you apply for a single-domain certificate, you must specify a single domain name for this parameter. If you apply for a wildcard certificate, you must specify a wildcard domain name such as `*.aliyundoc.com` for this parameter.
        # 
        # This parameter is required.
        self.domain = domain
        # The contact email address of the applicant.
        # 
        # This parameter is required.
        self.email = email
        # The phone number of the applicant.
        # 
        # This parameter is required.
        self.phone = phone
        # The specifications of the certificate. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain DV certificate, which is free and valid for 3 months.
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate, which is free and valid for 1 year. This value is available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        self.product_code = product_code
        # The tags.
        self.tags = tags
        # The name of the applicant.
        # 
        # This parameter is required.
        self.username = username
        # The method to verify the ownership of a domain name. Valid values:
        # 
        # *   **DNS**: DNS verification. If you use this method, you must add a TXT record to the DNS records of the domain name in the management platform of the domain name. You must have operation permissions on domain name resolution to verify the ownership of the domain name.
        # *   **FILE**: file verification. If you use this method, you must create a specified file on the DNS server. You must have administrative rights on the DNS server to verify the ownership of the domain name.
        # 
        # For more information about the verification methods, see [Verify the ownership of a domain name](https://help.aliyun.com/document_detail/48016.html).
        # 
        # This parameter is required.
        self.validate_type = validate_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateCertificateRequestRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the certificate application order.
        # 
        # >  You can use the ID to query the status of the certificate application. For more information, see [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html).
        self.order_id = order_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateRequestResponseBody = None,
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
            temp_model = CreateCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateWithCsrRequestRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCertificateWithCsrRequestRequest(TeaModel):
    def __init__(
        self,
        csr: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        tags: List[CreateCertificateWithCsrRequestRequestTags] = None,
        username: str = None,
        validate_type: str = None,
    ):
        # The content of the CSR file.\\
        # The key algorithm in the CSR file must be Rivest-Shamir-Adleman (RSA) or elliptic-curve cryptography (ECC), and the key length of the RSA algorithm must be greater than or equal to 2,048 characters. For more information about how to create a CSR file, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html)\\
        # A CSR file contains the information about your server and company. When you apply for a certificate, you must submit the CSR file to the CA. The CA signs the CSR file by using the private key of the root certificate and generates a public key file to issue your certificate.
        # 
        # >  The **CN** field in the CSR file specifies the domain name that is bound to the certificate.
        # 
        # This parameter is required.
        self.csr = csr
        # The contact email address of the applicant.
        # 
        # This parameter is required.
        self.email = email
        # The phone number of the applicant.
        # 
        # This parameter is required.
        self.phone = phone
        # The specifications of the certificate that you want to apply for. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain DV certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        self.product_code = product_code
        # The tag list.
        self.tags = tags
        # The name of the applicant.
        # 
        # This parameter is required.
        self.username = username
        # The method to verify the ownership of a domain name. Valid values:
        # 
        # *   **DNS**: DNS verification. If you use this method, you must add a TXT record to the DNS records of the domain name in the management platform of the domain name. You must have operation permissions on domain name resolution to verify the ownership of the domain name.
        # *   **FILE**: file verification. If you use this method, you must create a specified file on the DNS server. You must have administrative rights on the DNS server to verify the ownership of the domain name.
        # 
        # For more information about the verification methods, see [Verify the ownership of a domain name](https://help.aliyun.com/document_detail/48016.html).
        # 
        # This parameter is required.
        self.validate_type = validate_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.username is not None:
            result['Username'] = self.username
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateCertificateWithCsrRequestRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class CreateCertificateWithCsrRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the certificate application order.
        # 
        # >  You can use the ID to query the status of the certificate application. For more information, see [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html).
        self.order_id = order_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCertificateWithCsrRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertificateWithCsrRequestResponseBody = None,
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
            temp_model = CreateCertificateWithCsrRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCsrRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCsrResponseBody(TeaModel):
    def __init__(
        self,
        csr: str = None,
        csr_id: int = None,
        request_id: str = None,
    ):
        # The content of the CSR.
        self.csr = csr
        # The unique identifier of the CSR. You can use this value to obtain the content of the CSR. For more information about the operation that you can call to obtain the content of a CSR, see [GetCsrDetail](https://help.aliyun.com/document_detail/2709720.html).
        self.csr_id = csr_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCsrResponseBody = None,
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
            temp_model = CreateCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentJobRequest(TeaModel):
    def __init__(
        self,
        cert_ids: str = None,
        contact_ids: str = None,
        job_type: str = None,
        name: str = None,
        resource_ids: str = None,
        schedule_time: int = None,
    ):
        # The ID of the certificate. Separate multiple certificate IDs with commas (,). You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the IDs of certificates from the **CertificateId** parameter.
        # 
        # This parameter is required.
        self.cert_ids = cert_ids
        # The ID of the contact. Separate multiple contact IDs with commas (,). You can call the [ListContact](https://help.aliyun.com/document_detail/2712221.html) operation to obtain the IDs of contacts from the **ContactId** parameter.
        # 
        # This parameter is required.
        self.contact_ids = contact_ids
        # The type of the deployment task.
        # 
        # Valid values:
        # 
        # *   cloud: multi-cloud deployment task.
        # *   user: cloud service deployment task. This type of task does not support cloud servers.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The name of the deployment task.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the cloud resource. Separate multiple resource IDs with commas (,). You can call the [ListCloudResources](https://help.aliyun.com/document_detail/2712230.html) operation to obtain the IDs of cloud resources from the **Id** parameter.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The time when the task starts. The value is a UNIX timestamp. If you do not specify this parameter, the system immediately starts the task after the task is in the pending state.
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        return self


class CreateDeploymentJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        request_id: str = None,
    ):
        # The ID of the deployment task.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeploymentJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeploymentJobResponseBody = None,
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
            temp_model = CreateDeploymentJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        ciphertext_blob: str = None,
        message_type: str = None,
    ):
        # The encryption algorithm. Valid values:
        # 
        # *   **RSAES_OAEP_SHA_1**\
        # *   **RSAES_OAEP_SHA_256**\
        # *   **SM2PKE**\
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to query the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        # 
        # This parameter is required.
        self.cert_identifier = cert_identifier
        # The data that you want to decrypt. The value is encoded in Base64.
        # 
        # This parameter is required.
        self.ciphertext_blob = ciphertext_blob
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: The returned result is raw data encoded in UTF-8.
        # *   Base64: The returned result is Base64-encoded data. This is the default value.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class DecryptResponseBody(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The unique identifier of the certificate.
        self.cert_identifier = cert_identifier
        # The data after decryption.
        self.plaintext = plaintext
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DecryptResponseBody = None,
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
            temp_model = DecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequestRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        # The ID of the certificate application order that you want to delete.
        # 
        # >  After you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html), [CreateCertificateRequest](https://help.aliyun.com/document_detail/455292.html), or [CreateCertificateWithCsrRequest](https://help.aliyun.com/document_detail/455801.html) operation to submit a certificate application, you can obtain the ID of the certificate application order from the **OrderId** response parameter. You can also call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the order ID.
        # 
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteCertificateRequestResponseBody(TeaModel):
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


class DeleteCertificateRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCertificateRequestResponseBody = None,
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
            temp_model = DeleteCertificateRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCsrRequest(TeaModel):
    def __init__(
        self,
        csr_id: int = None,
    ):
        # The ID of the CSR.
        # 
        # This parameter is required.
        self.csr_id = csr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')
        return self


class DeleteCsrResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCsrResponseBody = None,
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
            temp_model = DeleteCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeploymentJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteDeploymentJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteDeploymentJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeploymentJobResponseBody = None,
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
            temp_model = DeleteDeploymentJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePCACertRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/452331.html) operation to query the unique identifiers of certificates.
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


class DeletePCACertResponseBody(TeaModel):
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


class DeletePCACertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePCACertResponseBody = None,
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
            temp_model = DeletePCACertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
    ):
        # The ID of the certificate.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class DeleteUserCertificateResponseBody(TeaModel):
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


class DeleteUserCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserCertificateResponseBody = None,
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
            temp_model = DeleteUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkerResourceRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        worker_id: int = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the worker for the deployment task.
        # 
        # This parameter is required.
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class DeleteWorkerResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteWorkerResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkerResourceResponseBody = None,
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
            temp_model = DeleteWorkerResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateStateRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        # The ID of the certificate application order that you want to query.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribeCertificateStateResponseBody(TeaModel):
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
        # *   **TXT**\
        # *   **CNAME**\
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
        # The file that you need to create on the DNS server when you use the file verification method. **The value of this parameter contains the file path and file name.**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeCertificateStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCertificateStateResponseBody = None,
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
            temp_model = DescribeCertificateStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudResourceStatusRequest(TeaModel):
    def __init__(
        self,
        secret_id: str = None,
    ):
        # The AccessKey secret used to access cloud resources.
        # 
        # >  You can call the [ListCloudAccess](https://help.aliyun.com/document_detail/2712219.html) operation to obtain the ID.
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DescribeCloudResourceStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        cloud_name: str = None,
        cloud_product: str = None,
        total_count: int = None,
    ):
        # The cloud service provider.
        self.cloud_name = cloud_name
        # The cloud service.
        self.cloud_product = cloud_product
        # The total number of cloud resources on which certificates are deployed.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudResourceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeCloudResourceStatusResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCloudResourceStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCloudResourceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudResourceStatusResponseBody = None,
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
            temp_model = DescribeCloudResourceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeploymentJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the deployment job. The **ID** of the job is returned after you call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeDeploymentJobResponseBodyCasContacts(TeaModel):
    def __init__(
        self,
        email: str = None,
        id: str = None,
        mobile: str = None,
        name: str = None,
    ):
        # The email address of the contact.
        self.email = email
        # The ID of the contact.
        self.id = id
        # The phone number of the contact.
        self.mobile = mobile
        # The name of the contact.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDeploymentJobResponseBody(TeaModel):
    def __init__(
        self,
        cas_contacts: List[DescribeDeploymentJobResponseBodyCasContacts] = None,
        cert_domain: str = None,
        cert_type: str = None,
        config: str = None,
        del_: int = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_type: str = None,
        name: str = None,
        product_name: str = None,
        request_id: str = None,
        rollback: int = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # The information about the contact.
        self.cas_contacts = cas_contacts
        # The domain names bound to the certificate of the deployment task.
        self.cert_domain = cert_domain
        # The type of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **buy**: purchased certificate
        # *   **free**: free certificate available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # The configurations of the deployment task.
        self.config = config
        # Indicates whether the deployment job was deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.del_ = del_
        # The end time of the deployment job. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The time when the deployment job was created. The value is a UNIX timestamp. Unit: seconds.
        self.gmt_create = gmt_create
        # The time when the deployment job was last modified. The value is a UNIX timestamp. Unit: seconds.
        self.gmt_modified = gmt_modified
        # The ID of the deployment job.
        self.id = id
        # The instance ID of the deployment task.
        self.instance_id = instance_id
        # The type of the deployment job. Valid values:
        # 
        # *   **cloud**: multi-cloud deployment job.
        # *   **trustee**: hosted deployment job available only on the China site (aliyun.com).
        # *   **user**: cloud service deployment job. The cloud server is not included.
        self.job_type = job_type
        # The name of the deployment task.
        self.name = name
        # The cloud services included in the deployment task.
        self.product_name = product_name
        # The request ID.
        self.request_id = request_id
        # Indicates whether the deployment job includes the rollback worker. For example, if a cloud service in a deployment job has been rolled back, **1** is returned. Valid values:
        # 
        # *   **0**: The rollback worker is not included.
        # *   **1**: The rollback worker is included.
        self.rollback = rollback
        # The time when the deployment job was scheduled. The value is a UNIX timestamp. Unit: seconds.
        self.schedule_time = schedule_time
        # The start time of the deployment job. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the deployment job. Valid values:
        # 
        # *   **pending**\
        # *   **editing**\
        # *   **scheduling**\
        # *   **processing**\
        # *   **error**\
        # *   **success**\
        self.status = status
        # The ID of the Alibaba Cloud account in which the deployment job is created.
        self.user_id = user_id

    def validate(self):
        if self.cas_contacts:
            for k in self.cas_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CasContacts'] = []
        if self.cas_contacts is not None:
            for k in self.cas_contacts:
                result['CasContacts'].append(k.to_map() if k else None)
        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.config is not None:
            result['Config'] = self.config
        if self.del_ is not None:
            result['Del'] = self.del_
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cas_contacts = []
        if m.get('CasContacts') is not None:
            for k in m.get('CasContacts'):
                temp_model = DescribeDeploymentJobResponseBodyCasContacts()
                self.cas_contacts.append(temp_model.from_map(k))
        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Del') is not None:
            self.del_ = m.get('Del')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeDeploymentJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeploymentJobResponseBody = None,
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
            temp_model = DescribeDeploymentJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeploymentJobStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **JobId** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeDeploymentJobStatusResponseBodyProductWorkerCount(TeaModel):
    def __init__(
        self,
        count: int = None,
        product_name: str = None,
    ):
        # The total number of resources of a cloud service in the deployment task.
        self.count = count
        # The name of the cloud service. Valid values:
        # 
        # *   **SLB**: Classic Load Balancer (CLB). This value is supported only at the China site (aliyun.com).
        # *   **LIVE**: ApsaraVideo Live. This value is supported only at the China site (aliyun.com).
        # *   **webHosting**: Cloud Web Hosting. This value is supported only at the China site (aliyun.com).
        # *   **VOD**: ApsaraVideo VOD. This value is supported only at the China site (aliyun.com).
        # *   **CR**: Container Registry. This value is supported only at the China site (aliyun.com).
        # *   **DCDN**: Dynamic Content Delivery Network (DCDN).
        # *   **DDOS**: Anti-DDoS.
        # *   **CDN**: Alibaba Cloud CDN (CDN).
        # *   **ALB**: Application Load Balancer (ALB).
        # *   **APIGateway**: API Gateway.
        # *   **FC**: Function Compute.
        # *   **GA**: Global Accelerator (GA).
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NLB**: Network Load Balancer (NLB).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **SAE**: Serverless App Engine (SAE).
        # *   **TencentCDN**: Tencent Cloud Content Delivery Network (CDN).
        # *   **WAF**: Web Application Firewall (WAF).
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class DescribeDeploymentJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        buy_count: int = None,
        cert_count: int = None,
        cost_count: int = None,
        failed_count: int = None,
        match_worker_count: int = None,
        product_worker_count: List[DescribeDeploymentJobStatusResponseBodyProductWorkerCount] = None,
        request_id: str = None,
        resource_count: int = None,
        rollback_count: int = None,
        rollback_failed_count: int = None,
        rollback_success_count: int = None,
        success_count: int = None,
        use_count: int = None,
        worker_count: int = None,
    ):
        # The total number of purchased resources.
        self.buy_count = buy_count
        # The number of certificates involved in the deployment task.
        self.cert_count = cert_count
        # The number of resources consumed by worker tasks.
        self.cost_count = cost_count
        # The number of failed worker tasks, excluding rollback tasks.
        self.failed_count = failed_count
        # The total number of worker tasks that match the certificate.
        self.match_worker_count = match_worker_count
        # The number of cloud resources to which certificates are deployed in the deployment task.
        self.product_worker_count = product_worker_count
        # The request ID.
        self.request_id = request_id
        # The total number of resources.
        self.resource_count = resource_count
        # The number of worker tasks that are rolled backed.
        self.rollback_count = rollback_count
        # The number of worker tasks that failed to be rolled back.
        self.rollback_failed_count = rollback_failed_count
        # The number of worker tasks that are successfully rolled back.
        self.rollback_success_count = rollback_success_count
        # The number of successful worker tasks, excluding rollback tasks.
        self.success_count = success_count
        # The total number of used resources.
        self.use_count = use_count
        # The total number of resources to which certificate are deployed in the current cloud service. The value indicates the total number of worker tasks.
        self.worker_count = worker_count

    def validate(self):
        if self.product_worker_count:
            for k in self.product_worker_count:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count
        if self.cert_count is not None:
            result['CertCount'] = self.cert_count
        if self.cost_count is not None:
            result['CostCount'] = self.cost_count
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.match_worker_count is not None:
            result['MatchWorkerCount'] = self.match_worker_count
        result['ProductWorkerCount'] = []
        if self.product_worker_count is not None:
            for k in self.product_worker_count:
                result['ProductWorkerCount'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.rollback_count is not None:
            result['RollbackCount'] = self.rollback_count
        if self.rollback_failed_count is not None:
            result['RollbackFailedCount'] = self.rollback_failed_count
        if self.rollback_success_count is not None:
            result['RollbackSuccessCount'] = self.rollback_success_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        if self.worker_count is not None:
            result['WorkerCount'] = self.worker_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')
        if m.get('CertCount') is not None:
            self.cert_count = m.get('CertCount')
        if m.get('CostCount') is not None:
            self.cost_count = m.get('CostCount')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('MatchWorkerCount') is not None:
            self.match_worker_count = m.get('MatchWorkerCount')
        self.product_worker_count = []
        if m.get('ProductWorkerCount') is not None:
            for k in m.get('ProductWorkerCount'):
                temp_model = DescribeDeploymentJobStatusResponseBodyProductWorkerCount()
                self.product_worker_count.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('RollbackCount') is not None:
            self.rollback_count = m.get('RollbackCount')
        if m.get('RollbackFailedCount') is not None:
            self.rollback_failed_count = m.get('RollbackFailedCount')
        if m.get('RollbackSuccessCount') is not None:
            self.rollback_success_count = m.get('RollbackSuccessCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        if m.get('WorkerCount') is not None:
            self.worker_count = m.get('WorkerCount')
        return self


class DescribeDeploymentJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeploymentJobStatusResponseBody = None,
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
            temp_model = DescribeDeploymentJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageStateRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
    ):
        # The specifications of the certificate resource plan. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain domain validated (DV) certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **symantec-ov-1-personal**: DigiCert single-domain organization validated (OV) certificate.
        # *   **symantec-ov-w-personal**: DigiCert wildcard OV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **geotrust-ov-1-personal**: GeoTrust single-domain OV certificate.
        # *   **geotrust-ov-w-personal**: GeoTrust wildcard OV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        # *   **globalsign-ov-1-personal**: GlobalSign single-domain OV certificate.
        # *   **globalsign-ov-w-advanced**: GlobalSign wildcard OV certificate.
        # *   **cfca-ov-1-personal**: China Financial Certification Authority (CFCA) single-domain OV certificate, available only on the China site (aliyun.com).
        # *   **cfca-ev-w-advanced**: CFCA wildcard OV certificate, available only on the China site (aliyun.com).
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribePackageStateResponseBody(TeaModel):
    def __init__(
        self,
        issued_count: int = None,
        product_code: str = None,
        request_id: str = None,
        total_count: int = None,
        used_count: int = None,
    ):
        # The number of issued certificates of the specified specifications.
        self.issued_count = issued_count
        # The specifications of the certificate resource plan. Valid values:
        # 
        # *   **digicert-free-1-free**: DigiCert single-domain DV certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **symantec-ov-1-personal**: DigiCert single-domain OV certificate.
        # *   **symantec-ov-w-personal**: DigiCert wildcard OV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **geotrust-ov-1-personal**: GeoTrust single-domain OV certificate.
        # *   **geotrust-ov-w-personal**: GeoTrust wildcard OV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        # *   **globalsign-ov-1-personal**: GlobalSign single-domain OV certificate.
        # *   **globalsign-ov-w-advanced**: GlobalSign wildcard OV certificate.
        # *   **cfca-ov-1-personal**: CFCA single-domain OV certificate, available only on the China site (aliyun.com).
        # *   **cfca-ev-w-advanced**: CFCA wildcard OV certificate, available only on the China site (aliyun.com).
        self.product_code = product_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of purchased certificate resource plans of the specified specifications.
        self.total_count = total_count
        # The number of certificate applications that you submitted for certificates of the specified specifications.
        # 
        # > : A successful call of the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/204087.html), [CreateCertificateRequest](https://help.aliyun.com/document_detail/164105.html), or [CreateCertificateWithCsrRequest](https://help.aliyun.com/document_detail/178732.html) operation is counted as one a certificate application, regardless of whether the certificate is issued.
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issued_count is not None:
            result['IssuedCount'] = self.issued_count
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssuedCount') is not None:
            self.issued_count = m.get('IssuedCount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribePackageStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageStateResponseBody = None,
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
            temp_model = DescribePackageStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        message_type: str = None,
        plaintext: str = None,
    ):
        # The encryption algorithm. Valid values:
        # 
        # *   **RSAES_OAEP_SHA_1**\
        # *   **RSAES_OAEP_SHA_256**\
        # *   **SM2PKE**\
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to obtain the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        # 
        # This parameter is required.
        self.cert_identifier = cert_identifier
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: The value of the Plaintext parameter is directly encrypted. This is the default value.
        # *   Base64: The value of the Plaintext parameter is Base64-encoded data. The data is decoded and then encrypted.
        self.message_type = message_type
        # The data that you want to encrypt. The value of this parameter can be raw data or Base64-encoded data. For more information, see the description of the MessageType parameter. For example, if the hexadecimal data that you want to encrypt is `[0x31, 0x32, 0x33, 0x34]`, the Base64-encoded data is MTIzNA==. The size of data that can be encrypted varies based on the encryption algorithm that you use. The following list describes the relationship between the encryption algorithms and data sizes:
        # 
        # *   **RSAES_OAEP_SHA_1**: 214 bytes
        # *   **RSAES_OAEP_SHA_256**: 190 bytes
        # *   **SM2PKE**: 6,047 bytes
        # 
        # This parameter is required.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class EncryptResponseBody(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        ciphertext_blob: str = None,
        request_id: str = None,
    ):
        # The unique identifier of the certificate.
        self.cert_identifier = cert_identifier
        # The data after encryption. The value is encoded in Base64.
        self.ciphertext_blob = ciphertext_blob
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EncryptResponseBody = None,
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
            temp_model = EncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertWarehouseQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_quota: int = None,
        use_count: int = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total quota for certificate repositories, including the free quota and purchased quota.
        self.total_quota = total_quota
        # The used quota.
        self.use_count = use_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class GetCertWarehouseQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCertWarehouseQuotaResponseBody = None,
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
            temp_model = GetCertWarehouseQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCsrDetailRequest(TeaModel):
    def __init__(
        self,
        csr_id: int = None,
    ):
        # The ID of the CSR.
        # 
        # This parameter is required.
        self.csr_id = csr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')
        return self


class GetCsrDetailResponseBody(TeaModel):
    def __init__(
        self,
        csr: str = None,
        private_key: str = None,
        request_id: str = None,
    ):
        # The content of the CSR.
        self.csr = csr
        # The private key. Specify a Base64-encoded string.
        self.private_key = private_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCsrDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCsrDetailResponseBody = None,
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
            temp_model = GetCsrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        cert_filter: bool = None,
        cert_id: int = None,
    ):
        # Specifies whether to filter return results. Valid values: true and false. Default value: false. **true** specifies that the Cert, Key, EncryptCert, EncryptPrivateKey, SignCert, and SignPrivateKey parameters are not returned. **false** specifies that the parameters are returned.
        self.cert_filter = cert_filter
        # The ID of the certificate.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to query the ID.
        # 
        # This parameter is required.
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_filter is not None:
            result['CertFilter'] = self.cert_filter
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFilter') is not None:
            self.cert_filter = m.get('CertFilter')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        return self


class GetUserCertificateDetailResponseBodyCertChain(TeaModel):
    def __init__(
        self,
        common_name: str = None,
        issuer_common_name: str = None,
        not_after: int = None,
        not_before: int = None,
        remain_day: int = None,
    ):
        # The common name of the certificate.
        self.common_name = common_name
        # The common name of the issuer.
        self.issuer_common_name = issuer_common_name
        # The end of the validity period of the certificate.
        self.not_after = not_after
        # The beginning of the validity period of the certificate.
        self.not_before = not_before
        # The remaining days of the certificate validity period.
        self.remain_day = remain_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.issuer_common_name is not None:
            result['IssuerCommonName'] = self.issuer_common_name
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('IssuerCommonName') is not None:
            self.issuer_common_name = m.get('IssuerCommonName')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')
        return self


class GetUserCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        buy_in_aliyun: bool = None,
        cert: str = None,
        cert_chain: List[GetUserCertificateDetailResponseBodyCertChain] = None,
        cert_identifier: str = None,
        city: str = None,
        common: str = None,
        country: str = None,
        encrypt_cert: str = None,
        encrypt_private_key: str = None,
        end_date: str = None,
        expired: bool = None,
        fingerprint: str = None,
        id: int = None,
        instance_id: str = None,
        issuer: str = None,
        key: str = None,
        name: str = None,
        not_after: int = None,
        not_before: int = None,
        order_id: int = None,
        org_name: str = None,
        province: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_cert: str = None,
        sign_private_key: str = None,
        start_date: str = None,
    ):
        # The algorithm.
        self.algorithm = algorithm
        # Indicates whether the certificate was purchased from Alibaba Cloud. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.buy_in_aliyun = buy_in_aliyun
        # The content of the certificate if the certificate does not use an SM algorithm. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.cert = cert
        # The certificate chain.
        self.cert_chain = cert_chain
        # The certificate identifier. The value is in the "Certificate ID-cn-hangzhou" format. For example, if the ID of the certificate is 123, the value of CertIdentifier is 123-cn-hangzhou.
        self.cert_identifier = cert_identifier
        # The city of the company or organization to which the certificate purchaser belongs.
        self.city = city
        # The primary domain name that is bound to the certificate.
        self.common = common
        # The country or region of the company or organization to which the certificate purchaser belongs.
        self.country = country
        # The content of the encryption certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.encrypt_cert = encrypt_cert
        # The private key of the encryption certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.encrypt_private_key = encrypt_private_key
        # The expiration date of the certificate.
        self.end_date = end_date
        # Indicates whether the certificate has expired. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.expired = expired
        # The fingerprint of the certificate.
        self.fingerprint = fingerprint
        # The ID of the certificate.
        self.id = id
        # The instance ID of the resource.
        self.instance_id = instance_id
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The private key of the certificate if the certificate does not use an SM algorithm. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.key = key
        # The name of the certificate.
        self.name = name
        # The end of the validity period of the certificate.
        self.not_after = not_after
        # The beginning of the validity period of the certificate.
        self.not_before = not_before
        # The order ID.
        self.order_id = order_id
        # The name of the company or organization to which the certificate purchaser belongs.
        self.org_name = org_name
        # The province of the company or organization to which the certificate purchaser belongs.
        self.province = province
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # All domain names that are bound to the certificate.
        self.sans = sans
        # The serial number of the certificate.
        self.serial_no = serial_no
        # The SHA-2 value of the certificate.
        self.sha_2 = sha_2
        # The content of the signing certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.sign_cert = sign_cert
        # The private key of the signing certificate if the certificate uses an SM algorithm and is encoded in the PEM format. If certFilter is set to false, this parameter is returned. Otherwise, this parameter is not returned.
        self.sign_private_key = sign_private_key
        # The issuance date of the certificate.
        self.start_date = start_date

    def validate(self):
        if self.cert_chain:
            for k in self.cert_chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.buy_in_aliyun is not None:
            result['BuyInAliyun'] = self.buy_in_aliyun
        if self.cert is not None:
            result['Cert'] = self.cert
        result['CertChain'] = []
        if self.cert_chain is not None:
            for k in self.cert_chain:
                result['CertChain'].append(k.to_map() if k else None)
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.city is not None:
            result['City'] = self.city
        if self.common is not None:
            result['Common'] = self.common
        if self.country is not None:
            result['Country'] = self.country
        if self.encrypt_cert is not None:
            result['EncryptCert'] = self.encrypt_cert
        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.province is not None:
            result['Province'] = self.province
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert
        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BuyInAliyun') is not None:
            self.buy_in_aliyun = m.get('BuyInAliyun')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        self.cert_chain = []
        if m.get('CertChain') is not None:
            for k in m.get('CertChain'):
                temp_model = GetUserCertificateDetailResponseBodyCertChain()
                self.cert_chain.append(temp_model.from_map(k))
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EncryptCert') is not None:
            self.encrypt_cert = m.get('EncryptCert')
        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')
        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetUserCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserCertificateDetailResponseBody = None,
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
            temp_model = GetUserCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertRequest(TeaModel):
    def __init__(
        self,
        cert_type: str = None,
        current_page: int = None,
        key_word: str = None,
        show_size: int = None,
        source_type: str = None,
        status: str = None,
        warehouse_id: int = None,
    ):
        # 证书的类型 。取值：
        # 
        # - **CA**：表示CA证书。
        # - **CERT**：表示签发的证书。
        self.cert_type = cert_type
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The keyword for the query. You can enter a name, domain name, or Subject Alternative Name (SAN) extension. Fuzzy match is supported.
        self.key_word = key_word
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
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
        # The ID of the certificate repository. You can call the ListCertWarehouse API operation to query the IDs of certificate repositories.
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')
        return self


class ListCertResponseBodyCertList(TeaModel):
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
        # *   **true**\
        # *   **false**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCertResponseBody(TeaModel):
    def __init__(
        self,
        cert_list: List[ListCertResponseBodyCertList] = None,
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
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
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
            for k in m.get('CertList'):
                temp_model = ListCertResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
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


class ListCertWarehouseRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        name: str = None,
        show_size: int = None,
        type: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The instance ID of the certificate application repository.
        self.instance_id = instance_id
        # The name of the certificate application repository. Fuzzy match is supported.
        self.name = name
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The type of the certificate application repository. Valid values:
        # 
        # *   **ssl**: certificate application repository of SSL certificates
        # *   **uploadPCA**: certificate application repository of uploaded private certificates
        # *   **free**: certificate application repository of free certificates, available only on the China site (aliyun.com)
        # *   **aliyunPCA**: certificate application repository of private certificates purchased from Alibaba Cloud Private Certificate Authority (PCA), available only on the China site (aliyun.com)
        # *   **disable**: disabled certificate application repository
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCertWarehouseResponseBodyCertWarehouseList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        is_expired: bool = None,
        name: str = None,
        pca_instance_id: str = None,
        qps: int = None,
        type: str = None,
        wh_id: int = None,
    ):
        # The timestamp when the certificate application repository expires. Unit: milliseconds.
        self.end_time = end_time
        # The instance ID of the certificate application repository.
        self.instance_id = instance_id
        # Indicates whether the certificate application repository has expired. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_expired = is_expired
        # The name of the certificate application repository.
        self.name = name
        # The instance ID of the private CA.
        self.pca_instance_id = pca_instance_id
        # The queries per second (QPS).
        self.qps = qps
        # The type of the certificate application repository. Valid values:
        # 
        # *   **ssl**: certificate application repository of SSL certificates
        # *   **uploadPCA**: certificate application repository of uploaded private certificates
        # *   **free**: certificate application repository of free certificates, available only on the China site (aliyun.com)
        # *   **aliyunPCA**: certificate application repository of private certificates purchased from Alibaba Cloud Private Certificate Authority (PCA), available only on the China site (aliyun.com)
        # *   **disable**: disabled certificate application repository
        self.type = type
        # The ID of the certificate application repository.
        self.wh_id = wh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.name is not None:
            result['Name'] = self.name
        if self.pca_instance_id is not None:
            result['PcaInstanceId'] = self.pca_instance_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.type is not None:
            result['Type'] = self.type
        if self.wh_id is not None:
            result['WhId'] = self.wh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PcaInstanceId') is not None:
            self.pca_instance_id = m.get('PcaInstanceId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhId') is not None:
            self.wh_id = m.get('WhId')
        return self


class ListCertWarehouseResponseBody(TeaModel):
    def __init__(
        self,
        cert_warehouse_list: List[ListCertWarehouseResponseBodyCertWarehouseList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The certificate application repositories.
        self.cert_warehouse_list = cert_warehouse_list
        # The page number of the returned page. Default value: 1.
        self.current_page = current_page
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned per page. Default value: 50.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cert_warehouse_list:
            for k in self.cert_warehouse_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertWarehouseList'] = []
        if self.cert_warehouse_list is not None:
            for k in self.cert_warehouse_list:
                result['CertWarehouseList'].append(k.to_map() if k else None)
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
        self.cert_warehouse_list = []
        if m.get('CertWarehouseList') is not None:
            for k in m.get('CertWarehouseList'):
                temp_model = ListCertWarehouseResponseBodyCertWarehouseList()
                self.cert_warehouse_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCertWarehouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCertWarehouseResponseBody = None,
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
            temp_model = ListCertWarehouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudAccessRequest(TeaModel):
    def __init__(
        self,
        cloud_name: str = None,
        current_page: int = None,
        secret_id: str = None,
        show_size: int = None,
    ):
        # The cloud service provider. Set the value to **Tencent**, which indicates Tencent Cloud.
        self.cloud_name = cloud_name
        # The page number. Default value: 1.
        self.current_page = current_page
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The number of entries per page. Valid values: **10**, **20**, and **50**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListCloudAccessResponseBodyCloudAccessList(TeaModel):
    def __init__(
        self,
        access_id: int = None,
        cloud_name: str = None,
        secret_id: str = None,
        service_status: str = None,
    ):
        # The ID of the primary key.
        self.access_id = access_id
        # The cloud service provider.
        self.cloud_name = cloud_name
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The service status. The value normal indicates that the service runs as expected.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ListCloudAccessResponseBody(TeaModel):
    def __init__(
        self,
        cloud_access_list: List[ListCloudAccessResponseBodyCloudAccessList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The query results.
        self.cloud_access_list = cloud_access_list
        # The default value is the current page. If CurrentPage is not specified, this parameter is not returned.
        self.current_page = current_page
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. If ShowSize is not specified, this parameter is not returned.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cloud_access_list:
            for k in self.cloud_access_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudAccessList'] = []
        if self.cloud_access_list is not None:
            for k in self.cloud_access_list:
                result['CloudAccessList'].append(k.to_map() if k else None)
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
        self.cloud_access_list = []
        if m.get('CloudAccessList') is not None:
            for k in m.get('CloudAccessList'):
                temp_model = ListCloudAccessResponseBodyCloudAccessList()
                self.cloud_access_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCloudAccessResponseBody = None,
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
            temp_model = ListCloudAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudResourcesRequest(TeaModel):
    def __init__(
        self,
        cert_ids: List[int] = None,
        cloud_name: str = None,
        cloud_product: str = None,
        current_page: int = None,
        keyword: str = None,
        secret_id: str = None,
        show_size: int = None,
    ):
        # The certificate IDs.
        self.cert_ids = cert_ids
        # The cloud service provider.
        # 
        # Valid values:
        # 
        # *   Tencent
        # *   Huawei
        # *   Aws
        # *   aliyun
        self.cloud_name = cloud_name
        # The cloud service.
        # 
        # Valid values when CloudName is set to aliyun:
        # 
        # *   SLB: Classic Load Balancer (CLB). This value is available only on the China site (aliyun.com).
        # *   LIVE: ApsaraVideo Live. This value is available only on the China site (aliyun.com).
        # *   webHosting: Cloud Web Hosting. This value is available only on the China site (aliyun.com).
        # *   VOD: ApsaraVideo VOD. This value is available only on the China site (aliyun.com).
        # *   CR: Container Registry. This value is available only on the China site (aliyun.com).
        # *   DCDN: Dynamic Content Delivery Network (DCDN).
        # *   DDOS: Anti-DDoS.
        # *   CDN: Alibaba Cloud CDN (CDN).
        # *   ALB: Application Load Balancer (ALB).
        # *   APIGateway: API Gateway.
        # *   FC: Function Compute.
        # *   GA: Global Accelerator (GA).
        # *   MSE: Microservices Engine (MSE).
        # *   NLB: Network Load Balancer (NLB).
        # *   OSS: Object Storage Service (OSS).
        # *   SAE: Serverless App Engine (SAE).
        # *   WAF: Web Application Firewall (WAF).
        # 
        # Valid values when CloudName is set to Tencent:
        # 
        # *   TencentCDN: Content Delivery Network (CDN).
        # *   TencentCLB: CLB.
        # *   TencentWAF: WAF.
        # 
        # Valid value when CloudName is set to Huawei:
        # 
        # *   HuaweiCDN: CDN.
        # 
        # Valid values when CloudName is set to Aws:
        # 
        # *   AwsCloudFront: Amazon CloudFront.
        # *   AwsCLB: CLB.
        # *   AwsALB: ALB.
        # *   AwsNLB: NLB.
        self.cloud_product = cloud_product
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The keyword of the domain name or instance ID bound to the cloud resource.
        self.keyword = keyword
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The number of entries per page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListCloudResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        cert_ids_shrink: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        current_page: int = None,
        keyword: str = None,
        secret_id: str = None,
        show_size: int = None,
    ):
        # The certificate IDs.
        self.cert_ids_shrink = cert_ids_shrink
        # The cloud service provider.
        # 
        # Valid values:
        # 
        # *   Tencent
        # *   Huawei
        # *   Aws
        # *   aliyun
        self.cloud_name = cloud_name
        # The cloud service.
        # 
        # Valid values when CloudName is set to aliyun:
        # 
        # *   SLB: Classic Load Balancer (CLB). This value is available only on the China site (aliyun.com).
        # *   LIVE: ApsaraVideo Live. This value is available only on the China site (aliyun.com).
        # *   webHosting: Cloud Web Hosting. This value is available only on the China site (aliyun.com).
        # *   VOD: ApsaraVideo VOD. This value is available only on the China site (aliyun.com).
        # *   CR: Container Registry. This value is available only on the China site (aliyun.com).
        # *   DCDN: Dynamic Content Delivery Network (DCDN).
        # *   DDOS: Anti-DDoS.
        # *   CDN: Alibaba Cloud CDN (CDN).
        # *   ALB: Application Load Balancer (ALB).
        # *   APIGateway: API Gateway.
        # *   FC: Function Compute.
        # *   GA: Global Accelerator (GA).
        # *   MSE: Microservices Engine (MSE).
        # *   NLB: Network Load Balancer (NLB).
        # *   OSS: Object Storage Service (OSS).
        # *   SAE: Serverless App Engine (SAE).
        # *   WAF: Web Application Firewall (WAF).
        # 
        # Valid values when CloudName is set to Tencent:
        # 
        # *   TencentCDN: Content Delivery Network (CDN).
        # *   TencentCLB: CLB.
        # *   TencentWAF: WAF.
        # 
        # Valid value when CloudName is set to Huawei:
        # 
        # *   HuaweiCDN: CDN.
        # 
        # Valid values when CloudName is set to Aws:
        # 
        # *   AwsCloudFront: Amazon CloudFront.
        # *   AwsCLB: CLB.
        # *   AwsALB: ALB.
        # *   AwsNLB: NLB.
        self.cloud_product = cloud_product
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The keyword of the domain name or instance ID bound to the cloud resource.
        self.keyword = keyword
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The number of entries per page. Default value: **20**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ids_shrink is not None:
            result['CertIds'] = self.cert_ids_shrink
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids_shrink = m.get('CertIds')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListCloudResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_end_time: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert_start_time: str = None,
        cloud_access_id: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        cloud_region: str = None,
        default_resource: int = None,
        domain: str = None,
        enable_https: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        listener_id: str = None,
        listener_port: str = None,
        region_id: str = None,
        status: str = None,
        use_ssl: int = None,
        user_id: int = None,
    ):
        # The end date of the certificate bound to the cloud resource. The value is a timestamp in seconds.
        self.cert_end_time = cert_end_time
        # The ID of the certificate bound to the cloud resource.
        self.cert_id = cert_id
        # The name of the certificate bound to the cloud resource.
        self.cert_name = cert_name
        # The start date of the certificate bound to the cloud resource. The value is a timestamp in seconds.
        self.cert_start_time = cert_start_time
        # The AccessKey ID that is used to access cloud resources.
        # 
        # >  This parameter is returned only when you deploy certificates to cloud services of third-party clouds.
        self.cloud_access_id = cloud_access_id
        # The cloud service provider.
        # 
        # Valid values:
        # 
        # *   Tencent
        # *   Huawei
        # *   Aws
        # *   aliyun
        self.cloud_name = cloud_name
        # The cloud service.
        self.cloud_product = cloud_product
        # The region ID of the cloud service provider to which the cloud resource belongs.
        self.cloud_region = cloud_region
        # Indicates whether the cloud resource is the default resource. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.default_resource = default_resource
        # The domain name bound to the cloud resource.
        self.domain = domain
        # Indicates whether HTTPS is enabled for the cloud resource. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        self.enable_https = enable_https
        # The time when the cloud resource was created. The time is a timestamp in seconds.
        self.gmt_create = gmt_create
        # The time when the cloud resource was last modified. The time is a timestamp in seconds.
        self.gmt_modified = gmt_modified
        # The ID of the cloud resource.
        self.id = id
        # The instance ID of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.instance_id = instance_id
        # The listener ID of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_id = listener_id
        # The listening port of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_port = listener_port
        # The region ID of the cloud resource.
        self.region_id = region_id
        # The status of the cloud resource.
        self.status = status
        # Indicates whether an Alibaba Cloud SSL certificate is used. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # >  This parameter is required only when you deploy certificates to services of multiple clouds.
        self.use_ssl = use_ssl
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cloud_access_id is not None:
            result['CloudAccessId'] = self.cloud_access_id
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region
        if self.default_resource is not None:
            result['DefaultResource'] = self.default_resource
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_https is not None:
            result['EnableHttps'] = self.enable_https
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CloudAccessId') is not None:
            self.cloud_access_id = m.get('CloudAccessId')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')
        if m.get('DefaultResource') is not None:
            self.default_resource = m.get('DefaultResource')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableHttps') is not None:
            self.enable_https = m.get('EnableHttps')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListCloudResourcesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListCloudResourcesResponseBodyData] = None,
        request_id: str = None,
        show_size: int = None,
        total: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The data returned for the request.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. Default value: **20**.
        self.show_size = show_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCloudResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCloudResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCloudResourcesResponseBody = None,
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
            temp_model = ListCloudResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContactRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        show_size: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The keyword used in the query. For example, you can specify a keyword in names, email addresses, and mobile phone numbers.
        self.keyword = keyword
        # The number of contacts per page.
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
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListContactResponseBodyContactList(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        email: str = None,
        email_status: int = None,
        mobile: str = None,
        mobile_status: int = None,
        name: str = None,
        webhooks: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        self.email = email
        # Indicates whether the email address passed the verification.
        self.email_status = email_status
        # The phone number.
        self.mobile = mobile
        # Indicates whether the phone number was verified.
        self.mobile_status = mobile_status
        # The name of the contact.
        self.name = name
        # The webhook URL of the chatbot.
        self.webhooks = webhooks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email is not None:
            result['Email'] = self.email
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_status is not None:
            result['MobileStatus'] = self.mobile_status
        if self.name is not None:
            result['Name'] = self.name
        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileStatus') is not None:
            self.mobile_status = m.get('MobileStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')
        return self


class ListContactResponseBody(TeaModel):
    def __init__(
        self,
        contact_list: List[ListContactResponseBodyContactList] = None,
        current_page: int = None,
        keyword: str = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The contacts.
        self.contact_list = contact_list
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The keyword used in the fuzzy search.
        self.keyword = keyword
        # The request ID.
        self.request_id = request_id
        # The number of certificates per page. Default value: **20**.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.contact_list:
            for k in self.contact_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactList'] = []
        if self.contact_list is not None:
            for k in self.contact_list:
                result['ContactList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_list = []
        if m.get('ContactList') is not None:
            for k in m.get('ContactList'):
                temp_model = ListContactResponseBodyContactList()
                self.contact_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListContactResponseBody = None,
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
            temp_model = ListContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCsrRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        current_page: int = None,
        key_word: str = None,
        show_size: int = None,
    ):
        # The algorithm. Valid values: RSA, ECC, and SM2.
        self.algorithm = algorithm
        # The page number.
        self.current_page = current_page
        # The keyword.
        self.key_word = key_word
        # The number of entries per page. Default value: 50.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        return self


class ListCsrResponseBodyCsrList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCsrResponseBody(TeaModel):
    def __init__(
        self,
        csr_list: List[ListCsrResponseBodyCsrList] = None,
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
            for k in self.csr_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CsrList'] = []
        if self.csr_list is not None:
            for k in self.csr_list:
                result['CsrList'].append(k.to_map() if k else None)
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
            for k in m.get('CsrList'):
                temp_model = ListCsrResponseBodyCsrList()
                self.csr_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCsrResponseBody = None,
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
            temp_model = ListCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentJobRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        job_type: str = None,
        show_size: int = None,
        status: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The type of the deployment task.
        # 
        # Valid values:
        # 
        # *   cloud: multi-cloud deployment task.
        # *   user: cloud service deployment task. This type of task does not support Elastic Compute Service (ECS) instances.
        self.job_type = job_type
        # The number of certificates per page. Default value: **50**.
        self.show_size = show_size
        # The status of the deployment task.
        # 
        # Valid values:
        # 
        # *   success
        # *   pending
        # *   scheduling
        # *   processing
        # *   error
        # *   editing
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeploymentJobResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_domain: str = None,
        cert_type: str = None,
        del_: int = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_type: str = None,
        name: str = None,
        product_name: str = None,
        rollback: int = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        user_id: int = None,
    ):
        # The domain names bound to the certificate of the deployment task.
        self.cert_domain = cert_domain
        # The type of the certificate. Valid values:
        # 
        # *   **upload**: uploaded certificate
        # *   **buy**: purchased certificate
        # *   **free**: free certificate, available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # Indicates whether the deployment task is deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.del_ = del_
        # The end time of the deployment task.
        self.end_time = end_time
        # The time when the deployment task was created.
        self.gmt_create = gmt_create
        # The time when the deployment task was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the deployment task. You can use the ID to query the details and status of the deployment task.
        self.id = id
        # The instance ID of the deployment task.
        self.instance_id = instance_id
        # The type of the deployment task.
        # 
        # *   **cloud**: multi-cloud deployment task.
        # *   **user**: cloud service deployment task. This type of task does not support ECS instances.
        self.job_type = job_type
        # The name of the deployment task.
        self.name = name
        # The cloud service included in the resources of the deployment task.
        self.product_name = product_name
        # Indicates whether the rollback worker is included. For example, if a cloud service involved in a deployment task has been rolled back, **1** is returned. Valid values:
        # 
        # *   **0**: The rollback worker is not included.
        # *   **1**: The rollback worker is included.
        self.rollback = rollback
        # The time when the deployment task was scheduled.
        self.schedule_time = schedule_time
        # The start time of the deployment task.
        self.start_time = start_time
        # The status of the deployment task. Valid values:
        # 
        # *   **pending**\
        # *   **editing**\
        # *   **scheduling**\
        # *   **processing**\
        # *   **error**\
        # *   **success**\
        self.status = status
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.del_ is not None:
            result['Del'] = self.del_
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.rollback is not None:
            result['Rollback'] = self.rollback
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Del') is not None:
            self.del_ = m.get('Del')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListDeploymentJobResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListDeploymentJobResponseBodyData] = None,
        request_id: str = None,
        show_size: int = None,
        total: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The data returned for the request.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of deployment tasks per page. Default value: **50**.
        self.show_size = show_size
        # The total number of deployment tasks returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeploymentJobResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeploymentJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentJobResponseBody = None,
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
            temp_model = ListDeploymentJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentJobCertRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **JobId** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListDeploymentJobCertResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_instance_id: str = None,
        cert_name: str = None,
        cert_order_type: str = None,
        cert_type: str = None,
        common_name: str = None,
        is_trustee: bool = None,
        month: int = None,
        not_after_time: int = None,
        not_before_time: int = None,
        order_id: int = None,
        sans: List[str] = None,
        status_code: str = None,
    ):
        # The algorithm of the certificate public key.
        self.algorithm = algorithm
        # The ID of the certificate.
        self.cert_id = cert_id
        # The instance ID of the certificate.
        self.cert_instance_id = cert_instance_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The type of the certificate order. Valid values:
        # 
        # *   **upload**: uploaded certificate.
        # *   **buy**: purchased certificate.
        # *   **free**: free certificate. This value is available only on the China site (aliyun.com).
        self.cert_order_type = cert_order_type
        # The type of the certificate.
        self.cert_type = cert_type
        # The common name of the certificate.
        self.common_name = common_name
        # Indicates whether the certificate is hosted. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_trustee = is_trustee
        # The month in which the certificate is applied for.
        self.month = month
        # The end time of the validity period of the certificate. The value is a timestamp in seconds.
        self.not_after_time = not_after_time
        # The start time of the validity period of the certificate. The value is a timestamp in seconds.
        self.not_before_time = not_before_time
        # The ID of the certificate order.
        # 
        # >  If CertId is returned, this parameter is not returned.
        self.order_id = order_id
        # The subject alternative name (SAN) extensions of the certificate.
        self.sans = sans
        # The status code of the certificate. Valid values:
        # 
        # *   **payed**: paid and pending application
        # *   **checking**: being validated
        # *   **checkedFail**: validation failed
        # *   **revoked**: revoked
        # *   **revokeChecking**: revocation request being validated
        # *   **issued**: issued (excluding hosted certificates that are issued, certificates that are about to expire, expired certificates, and uploaded certificates)
        # *   **trustee**: hosted and issued
        # *   **upload**: uploaded (excluding certificates that are about to expire and expired certificates)
        # *   **willExpired**: about to expire (including certificates issued by using the Certificate Management Service console and uploaded certificates)
        # *   **expired**: expired (including certificates issued by using the Certificate Management Service console and uploaded certificates)
        # *   **validity**: valid (including certificates that are not expired or revoked)
        # *   **refund**: refunded
        # *   **closed**: closed
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_instance_id is not None:
            result['CertInstanceId'] = self.cert_instance_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_order_type is not None:
            result['CertOrderType'] = self.cert_order_type
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.is_trustee is not None:
            result['IsTrustee'] = self.is_trustee
        if self.month is not None:
            result['Month'] = self.month
        if self.not_after_time is not None:
            result['NotAfterTime'] = self.not_after_time
        if self.not_before_time is not None:
            result['NotBeforeTime'] = self.not_before_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertInstanceId') is not None:
            self.cert_instance_id = m.get('CertInstanceId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrderType') is not None:
            self.cert_order_type = m.get('CertOrderType')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('IsTrustee') is not None:
            self.is_trustee = m.get('IsTrustee')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NotAfterTime') is not None:
            self.not_after_time = m.get('NotAfterTime')
        if m.get('NotBeforeTime') is not None:
            self.not_before_time = m.get('NotBeforeTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListDeploymentJobCertResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListDeploymentJobCertResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeploymentJobCertResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeploymentJobCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentJobCertResponseBody = None,
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
            temp_model = ListDeploymentJobCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentJobResourceRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListDeploymentJobResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_end_time: str = None,
        cert_id: int = None,
        cert_name: str = None,
        cert_start_time: str = None,
        cloud_access_id: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        cloud_region: str = None,
        default_resource: int = None,
        domain: str = None,
        enable_https: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        listener_id: str = None,
        listener_port: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        use_ssl: int = None,
        user_id: int = None,
    ):
        # The end date of the certificate bound to the cloud resource. The value is a timestamp in seconds.
        self.cert_end_time = cert_end_time
        # The ID of the certificate bound to the cloud resource.
        self.cert_id = cert_id
        # The name of the certificate bound to the cloud resource.
        self.cert_name = cert_name
        # The start date of the certificate bound to the cloud resource. The value is a timestamp in seconds.
        self.cert_start_time = cert_start_time
        # The AccessKey ID used to access cloud resources.
        # 
        # >  This parameter is required only when you deploy certificates to services of multiple clouds.
        self.cloud_access_id = cloud_access_id
        # The cloud service provider of the cloud resource. Valid values:
        # 
        # *   **aliyun**: Alibaba Cloud
        # *   **Tencent**: Tencent Cloud
        self.cloud_name = cloud_name
        # The cloud service. Valid values:
        # 
        # *   **CDN**: Alibaba Cloud CDN (CDN). This value is supported only at the China site (aliyun.com).
        # *   **SLB**: Classic Load Balancer (CLB). This value is supported only at the China site (aliyun.com).
        # *   **DCDN**: Dynamic Content Delivery Network (DCDN). This value is supported only at the China site (aliyun.com).
        # *   **DDOS**: Anti-DDoS. This value is supported only at the China site (aliyun.com).
        # *   **LIVE**: ApsaraVideo Live. This value is supported only at the China site (aliyun.com).
        # *   **webHosting**: Cloud Web Hosting. This value is supported only at the China site (aliyun.com).
        # *   **VOD**: ApsaraVideo VOD. This value is supported only at the China site (aliyun.com).
        # *   **CR**: Container Registry. This value is supported only at the China site (aliyun.com).
        # *   **ALB**: Application Load Balancer (ALB).
        # *   **APIGateway**: API Gateway.
        # *   **FC**: Function Compute.
        # *   **GA**: Global Accelerator (GA).
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NLB**: Network Load Balancer (NLB).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **SAE**: Serverless App Engine (SAE).
        # *   **TencentCDN**: Tencent Cloud Content Delivery Network (CDN).
        # *   **WAF**: Web Application Firewall (WAF).
        self.cloud_product = cloud_product
        # The region ID of the cloud service provider to which the cloud resource belongs.
        self.cloud_region = cloud_region
        # Indicates whether the cloud resource is the default resource. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.default_resource = default_resource
        # The domain name bound to the cloud resource.
        self.domain = domain
        # Indicates whether HTTPS is enabled for the cloud resource. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_https = enable_https
        # The time when the cloud resource was created. The time is a timestamp in seconds.
        self.gmt_create = gmt_create
        # The time when the cloud resource was last modified. The time is in the timestamp format.
        self.gmt_modified = gmt_modified
        # The ID of the cloud resource.
        self.id = id
        # The instance ID of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.instance_id = instance_id
        # The listener ID of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_id = listener_id
        # The listening port of the cloud resource.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_port = listener_port
        # The region ID of the cloud resource.
        self.region_id = region_id
        # The other metadata related to the cloud resource.
        self.remark = remark
        # The status of the cloud resource.
        self.status = status
        # Indicates whether an Alibaba Cloud SSL certificate is used. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # >  This parameter is required only when you deploy certificates to services of multiple clouds.
        self.use_ssl = use_ssl
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cloud_access_id is not None:
            result['CloudAccessId'] = self.cloud_access_id
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region
        if self.default_resource is not None:
            result['DefaultResource'] = self.default_resource
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_https is not None:
            result['EnableHttps'] = self.enable_https
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CloudAccessId') is not None:
            self.cloud_access_id = m.get('CloudAccessId')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')
        if m.get('DefaultResource') is not None:
            self.default_resource = m.get('DefaultResource')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableHttps') is not None:
            self.enable_https = m.get('EnableHttps')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListDeploymentJobResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListDeploymentJobResourceResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeploymentJobResourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeploymentJobResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentJobResourceResponseBody = None,
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
            temp_model = ListDeploymentJobResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCertificateOrderRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        order_type: str = None,
        resource_group_id: str = None,
        show_size: int = None,
        status: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The domain name that is bound or the ID of the resource. Fuzzy match is supported.
        self.keyword = keyword
        # The type of the order. Default value: **CPACK**. Valid values:
        # 
        # *   **CPACK**: virtual resource order. If you set OrderType to CPACK, only the information about orders that are generated to consume the certificate quota is returned.
        # *   **BUY**: purchase order. If you set OrderType to BUY, only the information about purchase orders is returned. In most cases, this type of order can be ignored.
        # *   **UPLOAD**: uploaded certificate. If you set OrderType to UPLOAD, only uploaded certificates are returned.
        # *   **CERT**: certificate. If you set OrderType to CERT, both issued certificates and uploaded certificates are returned.
        self.order_type = order_type
        # The ID of the resource group. You can call the [ListResources](https://help.aliyun.com/document_detail/2716559.html) operation to obtain the ID.
        self.resource_group_id = resource_group_id
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The certificate status of the order. Valid values:
        # 
        # *   **PAYED**: pending application. You can set Status to PAYED only if you set OrderType to CPACK or BUY.
        # *   **CHECKING**: validating. You can set Status to CHECKING only if you set OrderType to CPACK or BUY.
        # *   **CHECKED_FAIL**: validation failed. You can set Status to CHECKED_FAIL only if you set OrderType to CPACK or BUY.
        # *   **ISSUED**: issued.
        # *   **WILLEXPIRED**: about to expire.
        # *   **EXPIRED**: expired.
        # *   **NOTACTIVATED**: not activated. You can set Status to NOTACTIVATED only if you set OrderType to CPACK or BUY.
        # *   **REVOKED**: revoked. You can set Status to REVOKED only if you set OrderType to CPACK or BUY.
        # 
        # If you set OrderType to CERT or UPLOAD and Status is left empty, valid certificates are returned by default, including issued certificates and certificates that are about to expire. If you set OrderType to CPACK or BUY and Status is left empty, all orders are returned by default.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUserCertificateOrderResponseBodyCertificateOrderList(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        aliyun_order_id: int = None,
        buy_date: int = None,
        cert_end_time: int = None,
        cert_start_time: int = None,
        cert_type: str = None,
        certificate_id: int = None,
        city: str = None,
        common_name: str = None,
        country: str = None,
        domain: str = None,
        domain_count: int = None,
        domain_type: str = None,
        end_date: str = None,
        expired: bool = None,
        fingerprint: str = None,
        instance_id: str = None,
        issuer: str = None,
        name: str = None,
        order_id: int = None,
        org_name: str = None,
        partner_order_id: str = None,
        product_code: str = None,
        product_name: str = None,
        province: str = None,
        resource_group_id: str = None,
        root_brand: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        source_type: str = None,
        start_date: str = None,
        status: str = None,
        trustee_status: str = None,
        upload: bool = None,
        wild_domain_count: int = None,
    ):
        # The algorithm. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.algorithm = algorithm
        # The ID of the Alibaba Cloud order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.aliyun_order_id = aliyun_order_id
        # The time at which the order was placed. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.buy_date = buy_date
        # The time at which the certificate expires. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.cert_end_time = cert_end_time
        # The time at which the certificate starts to take effect. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.cert_start_time = cert_start_time
        # The type of the certificate. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **DV**: domain validated (DV) certificate
        # *   **EV**: extended validation (EV) certificate
        # *   **OV**: organization validated (OV) certificate **FREE**: free certificate, available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # The ID of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.certificate_id = certificate_id
        # The city in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.city = city
        # The parent domain name of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.common_name = common_name
        # The code of the country in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.country = country
        # The domain name. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.domain = domain
        # The total number of domain names that can be bound to the certificate. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.domain_count = domain_count
        # The type of the domain name. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **ONE**: single domain name
        # *   **MULTIPLE**: multiple domain names
        # *   **WILDCARD**: single wildcard domain name
        # *   **M_WILDCARD**: multiple wildcard domain names
        # *   **MIX**: hybrid domain name
        self.domain_type = domain_type
        # The time at which the certificate expires. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.end_date = end_date
        # Indicates whether the certificate expires. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.expired = expired
        # The fingerprint of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.fingerprint = fingerprint
        # The ID of the resource.
        self.instance_id = instance_id
        # The issuer of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.issuer = issuer
        # The name of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.name = name
        # The order ID. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.order_id = order_id
        # The name of the organization that is associated with the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.org_name = org_name
        # The ID of the third-party certificate authority (CA) order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.partner_order_id = partner_order_id
        # The specification ID of the order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.product_code = product_code
        # The specification name of the order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.product_name = product_name
        # The province or autonomous region in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.province = province
        # The ID of the resource group. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.resource_group_id = resource_group_id
        # The brand of the certificate. Valid values: WoSign, CFCA, DigiCert, and vTrus. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.root_brand = root_brand
        # All domain names that are bound to the certificate. Multiple domain names are separated by commas (,). This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.sans = sans
        # The serial number of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.serial_no = serial_no
        # The SHA-2 value of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.sha_2 = sha_2
        # The type of the order. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **cpack**: virtual resource order
        # *   **buy**: purchase order
        self.source_type = source_type
        # The time at which the certificate starts to take effect. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.start_date = start_date
        # The certificate status of the order. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **PAYED**: pending application
        # *   **CHECKING**: reviewing
        # *   **CHECKED_FAIL**: review failed
        # *   **ISSUED**: issued
        # *   **WILLEXPIRED**: about to expire
        # *   **EXPIRED**: expired
        # *   **NOTACTIVATED**: not activated
        # *   **REVOKED**: revoked
        self.status = status
        # The hosting status of the certificate. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **unTrustee**: not hosted
        # *   **trustee**: hosted
        self.trustee_status = trustee_status
        # Indicates whether the certificate is an uploaded certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.upload = upload
        # The number of wildcard domain names that can be bound to the certificate. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.wild_domain_count = wild_domain_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.buy_date is not None:
            result['BuyDate'] = self.buy_date
        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.city is not None:
            result['City'] = self.city
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.country is not None:
            result['Country'] = self.country
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.partner_order_id is not None:
            result['PartnerOrderId'] = self.partner_order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.province is not None:
            result['Province'] = self.province
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.root_brand is not None:
            result['RootBrand'] = self.root_brand
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.trustee_status is not None:
            result['TrusteeStatus'] = self.trustee_status
        if self.upload is not None:
            result['Upload'] = self.upload
        if self.wild_domain_count is not None:
            result['WildDomainCount'] = self.wild_domain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('BuyDate') is not None:
            self.buy_date = m.get('BuyDate')
        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('PartnerOrderId') is not None:
            self.partner_order_id = m.get('PartnerOrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RootBrand') is not None:
            self.root_brand = m.get('RootBrand')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrusteeStatus') is not None:
            self.trustee_status = m.get('TrusteeStatus')
        if m.get('Upload') is not None:
            self.upload = m.get('Upload')
        if m.get('WildDomainCount') is not None:
            self.wild_domain_count = m.get('WildDomainCount')
        return self


class ListUserCertificateOrderResponseBody(TeaModel):
    def __init__(
        self,
        certificate_order_list: List[ListUserCertificateOrderResponseBodyCertificateOrderList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The certificates and orders.
        self.certificate_order_list = certificate_order_list
        # The page number of the returned page.
        self.current_page = current_page
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of entries returned per page.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_order_list:
            for k in self.certificate_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateOrderList'] = []
        if self.certificate_order_list is not None:
            for k in self.certificate_order_list:
                result['CertificateOrderList'].append(k.to_map() if k else None)
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
        self.certificate_order_list = []
        if m.get('CertificateOrderList') is not None:
            for k in m.get('CertificateOrderList'):
                temp_model = ListUserCertificateOrderResponseBodyCertificateOrderList()
                self.certificate_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserCertificateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserCertificateOrderResponseBody = None,
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
            temp_model = ListUserCertificateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkerResourceRequest(TeaModel):
    def __init__(
        self,
        cloud_product: str = None,
        current_page: int = None,
        job_id: int = None,
        show_size: int = None,
        status: str = None,
    ):
        # The cloud service in the deployment task.
        self.cloud_product = cloud_product
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **ID** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The number of entries per page. Default value: 50.
        self.show_size = show_size
        # The status of the worker task.
        # 
        # Valid values:
        # 
        # *   rollback
        # *   rollback_error
        # *   success
        # *   rollback_success
        # *   pending
        # *   scheduling
        # *   processing
        # *   error
        # *   editing
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListWorkerResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_domain: str = None,
        cert_id: int = None,
        cert_instance_id: str = None,
        cert_name: str = None,
        cloud_name: str = None,
        cloud_product: str = None,
        cloud_region: str = None,
        default_resource: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        job_id: int = None,
        listener_id: str = None,
        namespace_id: str = None,
        order_id: int = None,
        port: int = None,
        region_id: str = None,
        resource_cert_id: int = None,
        resource_domain: str = None,
        resource_id: int = None,
        status: str = None,
        user_id: int = None,
    ):
        # The domain name bound to the certificate in the worker task.
        self.cert_domain = cert_domain
        # The ID of the certificate in the worker task.
        self.cert_id = cert_id
        # The instance ID of the certificate in the worker task.
        self.cert_instance_id = cert_instance_id
        # The name of the certificate in the worker task.
        self.cert_name = cert_name
        # The cloud service provider to which the cloud resource in the worker task belongs.
        # 
        # >  This parameter is not returned if you deploy certificates to Alibaba Cloud services.
        self.cloud_name = cloud_name
        # The cloud service to which the cloud resource in the worker task belongs. Valid values:
        # 
        # *   **CDN**: Alibaba Cloud CDN (CDN). This value is supported only at the China site (aliyun.com).
        # *   **SLB**: Classic Load Balancer (CLB). This value is supported only at the China site (aliyun.com).
        # *   **DCDN**: Dynamic Content Delivery Network (DCDN). This value is supported only at the China site (aliyun.com).
        # *   **DDOS**: Anti-DDoS. This value is supported only at the China site (aliyun.com).
        # *   **LIVE**: ApsaraVideo Live. This value is supported only at the China site (aliyun.com).
        # *   **webHosting**: Cloud Web Hosting. This value is supported only at the China site (aliyun.com).
        # *   **VOD**: ApsaraVideo VOD. This value is supported only at the China site (aliyun.com).
        # *   **CR**: Container Registry. This value is supported only at the China site (aliyun.com).
        # *   **ALB**: Application Load Balancer (ALB).
        # *   **APIGateway**: API Gateway.
        # *   **FC**: Function Compute.
        # *   **GA**: Global Accelerator (GA).
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NLB**: Network Load Balancer (NLB).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **SAE**: Serverless App Engine (SAE).
        # *   **TencentCDN**: Tencent Cloud Content Delivery Network (CDN).
        # *   **WAF**: Web Application Firewall (WAF).
        self.cloud_product = cloud_product
        # The original region ID of the cloud resource in the worker task. The value is the region ID defined by the cloud service provider. This parameter is required only when you deploy certificates to services of multiple clouds.
        self.cloud_region = cloud_region
        # Indicates whether the cloud resource in the worker task is the default resource. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.default_resource = default_resource
        # The time when the worker task was created. The time is a timestamp in seconds.
        self.gmt_create = gmt_create
        # The time when the worker task was last modified. The time is a timestamp in seconds.
        self.gmt_modified = gmt_modified
        # The ID of the worker task.
        self.id = id
        # The ID of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.instance_id = instance_id
        # The ID of the deployment task to which the worker task belongs.
        self.job_id = job_id
        # The listener ID of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.listener_id = listener_id
        # The ID of the namespace in SAE. This parameter is returned only if you deploy certificates to SAE.
        self.namespace_id = namespace_id
        # The order ID of the worker task, which is the same as the order ID of the certificate.
        # 
        # >  If the CertId parameter is returned, this parameter is not returned.
        self.order_id = order_id
        # The listening port of the cloud resource in the worker task.
        # 
        # >  This parameter is returned only when the value of CloudProduct is SLB, NLB, ALB, or GA.
        self.port = port
        # The region ID of the cloud resource in the worker task.
        self.region_id = region_id
        # The ID of the certificate that was originally bound to the cloud resource in the worker task.
        self.resource_cert_id = resource_cert_id
        # The domain name that was originally bound to the cloud resource in the worker task.
        self.resource_domain = resource_domain
        # The ID of the cloud resource in the worker task.
        self.resource_id = resource_id
        # The status of the worker task. Valid values:
        # 
        # *   **editing**\
        # *   **pending**\
        # *   **scheduling**\
        # *   **processing**\
        # *   **error**\
        # *   **success**\
        # *   **rollback**\
        # *   **rollback_success**\
        # *   **rollback_error**\
        self.status = status
        # The ID of the Alibaba Cloud account to which the worker task belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain is not None:
            result['CertDomain'] = self.cert_domain
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_instance_id is not None:
            result['CertInstanceId'] = self.cert_instance_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region
        if self.default_resource is not None:
            result['DefaultResource'] = self.default_resource
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_cert_id is not None:
            result['ResourceCertId'] = self.resource_cert_id
        if self.resource_domain is not None:
            result['ResourceDomain'] = self.resource_domain
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomain') is not None:
            self.cert_domain = m.get('CertDomain')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertInstanceId') is not None:
            self.cert_instance_id = m.get('CertInstanceId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')
        if m.get('DefaultResource') is not None:
            self.default_resource = m.get('DefaultResource')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceCertId') is not None:
            self.resource_cert_id = m.get('ResourceCertId')
        if m.get('ResourceDomain') is not None:
            self.resource_domain = m.get('ResourceDomain')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListWorkerResourceResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListWorkerResourceResponseBodyData] = None,
        request_id: str = None,
        show_size: int = None,
        total: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The number of entries per page. Default value: **50**.
        self.show_size = show_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWorkerResourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListWorkerResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkerResourceResponseBody = None,
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
            temp_model = ListWorkerResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The region of the organization to which the owner of the certificate belongs. Valid values: ap-southeast-1 and cn-hangzhou.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.\\
        # Default value: **instance**\
        # 
        # Valid values:
        # 
        # *   instance: certificate order
        # *   Certificate: certificate
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewCertificateOrderForPackageRequestRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The value of the resource tag. A maximum of 20 tag values can be entered. If this value needs to be passed in, an empty string can be entered.
        # 
        # A maximum of 128 characters are supported, it cannot start with \\"aliyun\\" or \\"acs:\\", and it cannot contain \\"http://\\" or \\"https://\\".
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RenewCertificateOrderForPackageRequestRequest(TeaModel):
    def __init__(
        self,
        csr: str = None,
        order_id: int = None,
        tags: List[RenewCertificateOrderForPackageRequestRequestTags] = None,
    ):
        # The content of the certificate signing request (CSR) file that is manually generated for the domain name by using OpenSSL or Keytool. The key algorithm in the CSR file must be Rivest-Shamir-Adleman (RSA) or elliptic-curve cryptography (ECC), and the key length of the RSA algorithm must be greater than or equal to 2,048 characters. For more information about how to create a CSR file, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html)
        # 
        # If you do not specify this parameter, Certificate Management Service automatically generates a CSR file for the domain name in the certificate application order that you want to renew.
        # 
        # A CSR file contains the information about your server and company. When you apply for a certificate, you must submit the CSR file to the CA. The CA signs the CSR file by using the private key of the root certificate and generates a public key file to issue your certificate.
        # 
        # >  The **CN** field in the CSR file specifies the domain name that is bound to the certificate.
        self.csr = csr
        # The ID of the certificate application order that you want to renew.
        # 
        # >  After you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html), [CreateCertificateRequest](https://help.aliyun.com/document_detail/455292.html), or [CreateCertificateWithCsrRequest](https://help.aliyun.com/document_detail/455801.html) operation to submit a certificate application, you can obtain the ID of the certificate application order from the **OrderId** response parameter. You can also call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the order ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RenewCertificateOrderForPackageRequestRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class RenewCertificateOrderForPackageRequestResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the certificate application order that is renewed.
        # 
        # >  You can use the ID to query the status of the certificate application order. For more information, see [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html).
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewCertificateOrderForPackageRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewCertificateOrderForPackageRequestResponseBody = None,
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
            temp_model = RenewCertificateOrderForPackageRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signing_algorithm: str = None,
    ):
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to obtain the identifier.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        # 
        # This parameter is required.
        self.cert_identifier = cert_identifier
        # The data to sign. The value must be encoded in Base64.\\
        # For example, if the hexadecimal data that you want to sign is [0x31, 0x32, 0x33, 0x34], set the parameter to the Base64-encoded value MTIzNA==. If you set MessageType to RAW, the size of the data must be less than 4 KB. If the size of the data is greater than 4 KB, you can set MessageType to DIGEST and set Message to the digest of the data. The digest is a hash value. You can compute the digest of the data on an on-premises machine. The certificate application repository uses the digest that you compute in your own certificate application system. The message digest algorithm that you use must match the specified signature algorithm. The following items describe the details:
        # 
        # *   If the signature algorithm is SHA256withRSA, SHA256withRSA/PSS, or SHA256withECDSA, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM3withSM2, the message digest algorithm must be SM3.
        # 
        # This parameter is required.
        self.message = message
        # The value type of the Message parameter. Valid values:
        # 
        # *   RAW: the raw data. This is the default value.
        # *   DIGEST: the message digest (hash value) of the raw data.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The signature algorithm. Valid values:
        # 
        # *   SHA256withRSA
        # *   SHA256withRSA/PSS
        # *   SHA256withECDSA
        # *   SM3withSM2
        # 
        # This parameter is required.
        self.signing_algorithm = signing_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class SignResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The signature.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class SignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SignResponseBody = None,
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
            temp_model = SignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCsrRequest(TeaModel):
    def __init__(
        self,
        csr_id: int = None,
        key: str = None,
    ):
        # The ID of the CSR.
        # 
        # This parameter is required.
        self.csr_id = csr_id
        # The private key content of the certificate in the PEM format.
        # 
        # This parameter is required.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class UpdateCsrResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCsrResponseBody = None,
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
            temp_model = UpdateCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentJobRequest(TeaModel):
    def __init__(
        self,
        cert_ids: str = None,
        contact_ids: str = None,
        job_id: int = None,
        name: str = None,
        resource_ids: str = None,
        schedule_time: int = None,
    ):
        # The ID of the certificate. Separate multiple certificate IDs with commas (,). You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID of a certificate from the **CertificateId** parameter.
        self.cert_ids = cert_ids
        # The ID of the contact. Separate multiple contact IDs with commas (,). You can call the [ListContact](https://help.aliyun.com/document_detail/2712221.html) operation to obtain the ID of a contact from the **ContactId** parameter.
        self.contact_ids = contact_ids
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the JobId parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The name of the deployment task.
        self.name = name
        # The ID of the cloud resource. Separate multiple resource IDs with commas (,). You can call the [ListCloudResources](https://help.aliyun.com/document_detail/2712230.html) operation to obtain the ID of a cloud resource from the **Id** parameter.
        self.resource_ids = resource_ids
        # The time when the task starts. The value is a UNIX timestamp. If you do not specify this parameter, the system immediately starts the task after it is created.
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        return self


class UpdateDeploymentJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateDeploymentJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentJobResponseBody = None,
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
            temp_model = UpdateDeploymentJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentJobStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        status: str = None,
    ):
        # The ID of the deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The desired status.
        # 
        # Valid values:
        # 
        # *   pending
        # *   scheduling
        # *   editing
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDeploymentJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeploymentJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentJobStatusResponseBody = None,
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
            temp_model = UpdateDeploymentJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkerResourceStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        status: str = None,
        worker_id: int = None,
    ):
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **JobId** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The desired status.
        # 
        # Valid values:
        # 
        # *   rollback
        # 
        # This parameter is required.
        self.status = status
        # The ID of the worker task. You can call the [ListWorkerResource](https://help.aliyun.com/document_detail/2712224.html) operation to obtain the ID of a worker task.
        # 
        # This parameter is required.
        self.worker_id = worker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        if self.worker_id is not None:
            result['WorkerId'] = self.worker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkerId') is not None:
            self.worker_id = m.get('WorkerId')
        return self


class UpdateWorkerResourceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWorkerResourceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkerResourceStatusResponseBody = None,
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
            temp_model = UpdateWorkerResourceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCsrRequest(TeaModel):
    def __init__(
        self,
        csr: str = None,
        key: str = None,
        name: str = None,
    ):
        # The content of the CSR.
        # 
        # This parameter is required.
        self.csr = csr
        # The private key content of the certificate in the PEM format.
        self.key = key
        # The name of the CSR.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UploadCsrResponseBody(TeaModel):
    def __init__(
        self,
        csr_id: int = None,
        request_id: str = None,
    ):
        # The ID of the CSR.
        self.csr_id = csr_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadCsrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadCsrResponseBody = None,
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
            temp_model = UploadCsrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadUserCertificateRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UploadUserCertificateRequest(TeaModel):
    def __init__(
        self,
        cert: str = None,
        encrypt_cert: str = None,
        encrypt_private_key: str = None,
        key: str = None,
        name: str = None,
        resource_group_id: str = None,
        sign_cert: str = None,
        sign_private_key: str = None,
        tags: List[UploadUserCertificateRequestTags] = None,
    ):
        # The content of the certificate in the PEM format.
        self.cert = cert
        # The content of the encryption certificate in PEM format.
        self.encrypt_cert = encrypt_cert
        # The private key of the encryption certificate in the PEM format.
        self.encrypt_private_key = encrypt_private_key
        # The private key of the certificate in the PEM format.
        self.key = key
        # The name of the certificate. The name can be up to 64 characters in length, and can contain all types of characters, such as letters, digits, and underscores (_).
        # 
        # >  The name must be unique within an Alibaba Cloud account.
        self.name = name
        # the resource group id.
        self.resource_group_id = resource_group_id
        # The content of the signing certificate in the PEM format.
        self.sign_cert = sign_cert
        # The private key of the signing certificate in the PEM format.
        self.sign_private_key = sign_private_key
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.encrypt_cert is not None:
            result['EncryptCert'] = self.encrypt_cert
        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert
        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('EncryptCert') is not None:
            self.encrypt_cert = m.get('EncryptCert')
        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')
        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UploadUserCertificateRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UploadUserCertificateResponseBody(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        request_id: str = None,
        resource_id: str = None,
    ):
        # The ID of the certificate.
        self.cert_id = cert_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UploadUserCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadUserCertificateResponseBody = None,
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
            temp_model = UploadUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRequest(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        message: str = None,
        message_type: str = None,
        signature_value: str = None,
        signing_algorithm: str = None,
    ):
        # The unique identifier of the certificate. You can call the [ListCert](https://help.aliyun.com/document_detail/455806.html) operation to obtain the unique identifier of a certificate.
        # 
        # *   If the certificate is an SSL certificate, the value of this parameter must be in the {Certificate ID}-cn-hangzhou format.
        # *   If the certificate is a private certificate, the value of this parameter must be the value of the Identifier field for the private certificate.
        # 
        # This parameter is required.
        self.cert_identifier = cert_identifier
        # The data for which you want to verify the signature. The value must be encoded in Base64.\\
        # For example, if the hexadecimal data that you want to verify is [0x31, 0x32, 0x33, 0x34], set the parameter to the Base64-encoded value MTIzNA==. If you set MessageType to RAW, the size of the data must be less than 4 KB. If the size of the data is greater than 4 KB, you can set MessageType to DIGEST and set Message to the digest of the data. The digest is also called hash value. You can compute the digest of the data on an on-premises machine. The certificate repository uses your certificate application system to compute the message digest. The message digest algorithm that is used must meet the requirements of the specified signature algorithm. The following signature algorithms require different message digest algorithms:
        # 
        # *   If the signature algorithm is SHA256withRSA, SHA256withRSA/PSS, or SHA256withECDSA, the message digest algorithm must be SHA-256.
        # *   If the signature algorithm is SM3withSM2, the message digest algorithm must be SM3.
        # 
        # This parameter is required.
        self.message = message
        # The value type of the Message parameter. Valid values:
        # 
        # *   **RAW**: the raw data. This is the default value.
        # *   **DIGEST**: the message digest of the raw data.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The signature value. The value must be encoded in Base64.
        # 
        # This parameter is required.
        self.signature_value = signature_value
        # The signature algorithm. Valid values:
        # 
        # *   **SHA256withRSA**\
        # *   **SHA256withRSA/PSS**\
        # *   **SHA256withECDSA**\
        # *   **SM3withSM2**\
        # 
        # This parameter is required.
        self.signing_algorithm = signing_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.signing_algorithm is not None:
            result['SigningAlgorithm'] = self.signing_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('SigningAlgorithm') is not None:
            self.signing_algorithm = m.get('SigningAlgorithm')
        return self


class VerifyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature_valid: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the signature is valid. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.signature_valid = signature_valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class VerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyResponseBody = None,
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
            temp_model = VerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


