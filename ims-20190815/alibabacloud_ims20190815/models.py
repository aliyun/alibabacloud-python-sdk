# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddClientIdToOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        oidcprovider_name: str = None,
    ):
        # The client ID that you want to add.
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are periods (.), hyphens (-), underscores (_), colons (:), and forward slashes (/). 
        # 
        # The client ID can be up to 64 characters in length.
        self.client_id = client_id
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class AddClientIdToOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class AddClientIdToOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: AddClientIdToOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = AddClientIdToOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddClientIdToOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddClientIdToOIDCProviderResponseBody = None,
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
            temp_model = AddClientIdToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFingerprintToOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        oidcprovider_name: str = None,
    ):
        # The fingerprint of the HTTPS certificate.
        # 
        # The fingerprint can contain letters and digits.
        # 
        # The fingerprint can be up to 40 characters in length.
        self.fingerprint = fingerprint
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class AddFingerprintToOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class AddFingerprintToOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: AddFingerprintToOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The name of the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = AddFingerprintToOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFingerprintToOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFingerprintToOIDCProviderResponseBody = None,
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
            temp_model = AddFingerprintToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        user_principal_name: str = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class AddUserToGroupResponseBody(TeaModel):
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


class AddUserToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserToGroupResponseBody = None,
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
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        authentication_code_1: str = None,
        authentication_code_2: str = None,
        serial_number: str = None,
        user_principal_name: str = None,
    ):
        # The first verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_1 = authentication_code_1
        # The second verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_2 = authentication_code_2
        # The serial number of the MFA device.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to obtain the serial number of the MFA device.
        self.serial_number = serial_number
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')
        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class BindMFADeviceResponseBody(TeaModel):
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


class BindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindMFADeviceResponseBody = None,
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
            temp_model = BindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(
        self,
        new_password: str = None,
        old_password: str = None,
    ):
        # The new password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements. For more information, see [GetPasswordPolicy](https://help.aliyun.com/document_detail/186691.html).
        # 
        # This parameter is required.
        self.new_password = new_password
        # The old password that is used to log on to the console.
        # 
        # This parameter is required.
        self.old_password = old_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        return self


class ChangePasswordResponseBody(TeaModel):
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


class ChangePasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangePasswordResponseBody = None,
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
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, an AccessKey pair is created for the current user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateAccessKeyResponseBodyAccessKey(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        create_date: str = None,
        status: str = None,
    ):
        # The AccessKey ID provided to you by Alibaba Cloud.
        self.access_key_id = access_key_id
        # The AccessKey secret provided to you by Alibaba Cloud.
        self.access_key_secret = access_key_secret
        # The time when the AccessKey pair was created.
        self.create_date = create_date
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        access_key: CreateAccessKeyResponseBodyAccessKey = None,
        request_id: str = None,
    ):
        # The information of the AccessKey pair.
        self.access_key = access_key
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            temp_model = CreateAccessKeyResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m['AccessKey'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessKeyResponseBody = None,
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
            temp_model = CreateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        app_secret_value: str = None,
        create_date: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the application secret.
        self.app_secret_id = app_secret_id
        # The content of the application secret. This value can be used as the client secret for open authorization.
        self.app_secret_value = app_secret_value
        # The creation time.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        app_secret: CreateAppSecretResponseBodyAppSecret = None,
        request_id: str = None,
    ):
        # The information of the application secret.
        self.app_secret = app_secret
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            temp_model = CreateAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppSecretResponseBody = None,
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
            temp_model = CreateAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        access_token_validity: int = None,
        app_name: str = None,
        app_type: str = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        predefined_scopes: str = None,
        redirect_uris: str = None,
        refresh_token_validity: int = None,
        required_scopes: str = None,
        secret_required: bool = None,
    ):
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        # 
        # Default value: 3600.
        self.access_token_validity = access_token_validity
        # The application name.
        # 
        # The name can be up to 64 characters in length. The name can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.app_name = app_name
        # The type of the application. Valid values:
        # 
        # *   WebApp: a web application that interacts with a browser.
        # *   NativeApp: a native application that runs on an operating system, such as a desktop operating system or a mobile operating system.
        # *   ServerApp: an application that accesses Alibaba Cloud services without the need of manual user logon. User provisioning is automated based on the System for Cross-Domain Identity Management (SCIM) protocol.
        # 
        # This parameter is required.
        self.app_type = app_type
        # The display name of the application.
        # 
        # The name can be up to 24 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts. Valid values:
        # 
        # *   true: If you do not set this parameter for applications of the NativeApp and ServerApp types, true is used.
        # *   false: If you do not set this parameter for applications of the WebApp type, false is used.
        self.is_multi_tenant = is_multi_tenant
        # The scope of application permissions.
        # 
        # For more information about the application permission scope, see [Open authorization scope](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to obtain the permission scopes supported by different types of applications.
        # 
        # If you enter multiple permission scopes, separate them with semicolons (;).
        self.predefined_scopes = predefined_scopes
        # The callback URL.
        # 
        # If you enter multiple callback URLs, separate them with semicolons (;).
        self.redirect_uris = redirect_uris
        # The validity period of the refreshed token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        # 
        # Default value:
        # 
        # *   For applications of the WebApp and ServerApp types, if this parameter is left empty, the value 2592000 is used. The value 2592000 indicates that the validity period of the refreshed token is 30 days.
        # *   For applications of the NativeApp type, if this parameter is left empty, the value 7776000 is used. The value 7776000 indicates that the validity period of the refreshed token is 90 days.
        self.refresh_token_validity = refresh_token_validity
        # The required permission.
        # 
        # You can specify one or more permissions for the `RequiredScopes` parameter. After you specify this parameter, the required permissions are automatically selected and cannot be revoked when a user grants permissions on the application.
        # 
        # If you enter multiple permissions, separate them with semicolons (;).
        # 
        # >  If the permission that you specify for the `RequiredScopes` parameter is not included in value of the `PredefinedScopes` parameter, the permission does not take effect.
        self.required_scopes = required_scopes
        # Indicates whether a secret is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >- For applications of the WebApp and ServerApp types, this parameter is automatically set to true and cannot be changed.
        # >- For applications of the NativeApp type, this parameter can be set to true or false. If you do not set this parameter, false is used. Applications of the NativeApp type run in untrusted environments and the secrets of these applications are not protected. Therefore, we recommend that you do not set this parameter to true unless otherwise specified. For more information, see [Use an application of the NativeApp type to log on to Alibaba Cloud](https://help.aliyun.com/document_detail/93697.html).
        self.secret_required = secret_required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.required_scopes is not None:
            result['RequiredScopes'] = self.required_scopes
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('PredefinedScopes') is not None:
            self.predefined_scopes = m.get('PredefinedScopes')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('RequiredScopes') is not None:
            self.required_scopes = m.get('RequiredScopes')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        return self


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The description of the permission.
        self.description = description
        # The name of the permission.
        self.name = name
        # Indicates whether the permission is automatically selected by default when you install the application. Valid values:
        # 
        # *   true
        # *   false
        # 
        # `openid` is required by default.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        # The information about the permissions that are granted on the application.
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class CreateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        access_token_validity: int = None,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        create_date: str = None,
        delegated_scope: CreateApplicationResponseBodyApplicationDelegatedScope = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        redirect_uris: CreateApplicationResponseBodyApplicationRedirectUris = None,
        refresh_token_validity: int = None,
        secret_required: bool = None,
        update_date: str = None,
    ):
        # The validity period of the access token. Unit: seconds.
        self.access_token_validity = access_token_validity
        # The ID of the Alibaba Cloud account to which the application belongs.
        self.account_id = account_id
        # The ID of the application.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application type.
        self.app_type = app_type
        # The creation time.
        self.create_date = create_date
        # The information about the permissions that are granted on the application.
        self.delegated_scope = delegated_scope
        # The display name of the application.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts.
        self.is_multi_tenant = is_multi_tenant
        # The callback URLs.
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token. Unit: seconds.
        self.refresh_token_validity = refresh_token_validity
        # Indicates whether a secret is required.
        self.secret_required = secret_required
        # The update time.
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = CreateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: CreateApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationResponseBody = None,
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        group_name: str = None,
    ):
        # The description.
        # 
        # The value can be up to 128 characters in length.
        self.comments = comments
        # The display name of the RAM user group.
        # 
        # The name can be up to 24 characters in length.
        self.display_name = display_name
        # The name of the RAM user group. You must specify this parameter.
        # 
        # The name can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        update_date: str = None,
    ):
        # The description.
        self.comments = comments
        # The creation time.
        self.create_date = create_date
        # The display name of the RAM user group.
        self.display_name = display_name
        # The ID of the RAM user group.
        self.group_id = group_id
        # The name of the RAM user group.
        self.group_name = group_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: CreateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information of the RAM user group.
        self.group = group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password: str = None,
        password_reset_required: bool = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # Specifies whether multi-factor authentication (MFA) must be enabled. Valid values:
        # 
        # *   true: MFA must be enabled. The RAM user must bind an MFA device at the next logon.
        # *   false: MFA is not enabled. This is the default value.
        self.mfabind_required = mfabind_required
        # The password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements.
        self.password = password
        # Specifies whether the RAM user must reset the password at the next logon. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.password_reset_required = password_reset_required
        # The status of password-based logon. Valid values:
        # 
        # *   Active: Password-based logon is enabled. This is the default value.
        # *   Inactive: Password-based logon is disabled.
        self.status = status
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password_reset_required: bool = None,
        status: str = None,
        update_date: str = None,
        user_principal_name: str = None,
    ):
        # Indicates whether MFA must be enabled.
        self.mfabind_required = mfabind_required
        # Indicates whether the RAM user must reset the password at the next logon.
        self.password_reset_required = password_reset_required
        # The status of password-based logon.
        self.status = status
        # The update time.
        self.update_date = update_date
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        login_profile: CreateLoginProfileResponseBodyLoginProfile = None,
        request_id: str = None,
    ):
        # The logon information.
        self.login_profile = login_profile
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = CreateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLoginProfileResponseBody = None,
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
            temp_model = CreateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        client_ids: str = None,
        description: str = None,
        fingerprints: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
    ):
        # The ID of the client, which is provided by the external IdP Okta. If you want to specify multiple client IDs, separate the client IDs with commas (,).
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # The client ID can be up to 64 characters in length.
        self.client_ids = client_ids
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.description = description
        # The fingerprint of the HTTPS certificate, which is provided by the external IdP Okta. If you want to specify multiple fingerprints, separate the fingerprints with commas (,).
        # 
        # The fingerprint can contain letters and digits.
        # 
        # The fingerprint can be up to 40 characters in length.
        self.fingerprints = fingerprints
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer, which is provided by the external IdP. The URL of the issuer must be unique within an Alibaba Cloud account.
        # 
        # The URL of the issuer must start with `https` and be in the valid URL format. The URL cannot contain query parameters that follow a question mark (`?`) or logon information that is identified by at signs (`@`). The URL cannot be a fragment URL that contains number signs (`#`).
        # 
        # The URL can be up to 255 characters in length.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        # 
        # The name can contain letters, digits, and special characters and cannot start or end with the special characters. The special characters are `periods, (.), hyphens (-), and underscores (_)`.``
        # 
        # The name can be up to 128 characters in length.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class CreateOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client.
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate.
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: CreateOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = CreateOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOIDCProviderResponseBody = None,
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
            temp_model = CreateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
    ):
        # The description.
        self.description = description
        # The metadata file, which is Base64 encoded.
        # 
        # The file is provided by an IdP that supports SAML 2.0.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        # The name of the IdP.
        # 
        # The value can be up to 128 characters in length. The name can contain letters, digits,`  periods (.), hyphens (-), and underscores (_) `. The name cannot start or end with`  periods (.), hyphens (-), or underscores (_) `.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class CreateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn
        # The creation time.
        self.create_date = create_date
        # The description.
        self.description = description
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: CreateSAMLProviderResponseBodySAMLProvider = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the IdP.
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = CreateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class CreateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSAMLProviderResponseBody = None,
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
            temp_model = CreateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:`.
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


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        email: str = None,
        mobile_phone: str = None,
        tag: List[CreateUserRequestTag] = None,
        user_principal_name: str = None,
    ):
        # The description.
        # 
        # The description must be 1 to 128 characters in length.
        self.comments = comments
        # The display name of the RAM user.
        # 
        # The name must be 1 to 24 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The mobile number of the RAM user.
        # 
        # Format: Country code-Mobile phone number.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The tag value.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:`.
        self.tag = tag
        # The logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name. For more information about how to obtain the default domain name, see [GetDefaultDomain](https://help.aliyun.com/document_detail/186720.html).
        # 
        # The value of `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The value of `<username>` must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateUserRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBodyUserTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateUserResponseBodyUserTags(TeaModel):
    def __init__(
        self,
        tag: List[CreateUserResponseBodyUserTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateUserResponseBodyUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        email: str = None,
        last_login_date: str = None,
        mobile_phone: str = None,
        provision_type: str = None,
        tags: CreateUserResponseBodyUserTags = None,
        update_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The time when the RAM user was created.
        self.create_date = create_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date
        # The mobile phone number of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type
        # The tag value.
        self.tags = tags
        # The time when the information about the RAM user was updated.
        self.update_date = update_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Tags') is not None:
            temp_model = CreateUserResponseBodyUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: CreateUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = CreateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserResponseBody = None,
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        virtual_mfadevice_name: str = None,
    ):
        # The name of the MFA device.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.virtual_mfadevice_name = virtual_mfadevice_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')
        return self


class CreateVirtualMFADeviceResponseBodyVirtualMFADevice(TeaModel):
    def __init__(
        self,
        base_32string_seed: str = None,
        qrcode_png: str = None,
        serial_number: str = None,
    ):
        # The key of the MFA device.
        self.base_32string_seed = base_32string_seed
        # The Base64-encoded QR code of the key.
        self.qrcode_png = qrcode_png
        # The serial number of the MFA device.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed
        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base32StringSeed') is not None:
            self.base_32string_seed = m.get('Base32StringSeed')
        if m.get('QRCodePNG') is not None:
            self.qrcode_png = m.get('QRCodePNG')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class CreateVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_mfadevice: CreateVirtualMFADeviceResponseBodyVirtualMFADevice = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the MFA device.
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseBodyVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m['VirtualMFADevice'])
        return self


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVirtualMFADeviceResponseBody = None,
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
            temp_model = CreateVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        # The ID of the AccessKey pair that you want to delete.
        # 
        # This parameter is required.
        self.user_access_key_id = user_access_key_id
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the AccessKey pair of the current user is deleted.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteAccessKeyResponseBody(TeaModel):
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


class DeleteAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessKeyResponseBody = None,
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
            temp_model = DeleteAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the application secret.
        # 
        # This parameter is required.
        self.app_secret_id = app_secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class DeleteAppSecretResponseBody(TeaModel):
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


class DeleteAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppSecretResponseBody = None,
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
            temp_model = DeleteAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBody(TeaModel):
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


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationResponseBody = None,
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteGroupResponseBody(TeaModel):
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


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGroupResponseBody = None,
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteLoginProfileResponseBody(TeaModel):
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


class DeleteLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLoginProfileResponseBody = None,
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
            temp_model = DeleteLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        oidcprovider_name: str = None,
    ):
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class DeleteOIDCProviderResponseBody(TeaModel):
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


class DeleteOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteOIDCProviderResponseBody = None,
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
            temp_model = DeleteOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
    ):
        # The name of the IdP that you want to delete.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class DeleteSAMLProviderResponseBody(TeaModel):
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


class DeleteSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSAMLProviderResponseBody = None,
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
            temp_model = DeleteSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_id = user_id
        # The logon name of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteUserResponseBody(TeaModel):
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


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        # The serial number of the MFA device.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
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


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVirtualMFADeviceResponseBody = None,
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
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DisableVirtualMFAResponseBody(TeaModel):
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


class DisableVirtualMFAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableVirtualMFAResponseBody = None,
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
            temp_model = DisableVirtualMFAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCredentialReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The generation status of the user credential report. Valid values:
        # 
        # *   STARTED: The user credential report starts to generate.
        # *   INPROGRESS: The user credential report is being generated.
        # *   COMPLETED: The user credential report is generated.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GenerateCredentialReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCredentialReportResponseBody = None,
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
            temp_model = GenerateCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        # The ID of the AccessKey pair that you want to query.
        # 
        # This parameter is required.
        self.user_access_key_id = user_access_key_id
        # The logon name of the RAM user.
        # 
        # If you do not specify this parameter, the AccessKey pair of the current user is queried.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed(TeaModel):
    def __init__(
        self,
        last_used_date: str = None,
        service_name: str = None,
    ):
        # The time when the AccessKey pair was used for the last time.
        self.last_used_date = last_used_date
        # The Alibaba Cloud service that was last accessed by using the AccessKey pair.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAccessKeyLastUsedResponseBody(TeaModel):
    def __init__(
        self,
        access_key_last_used: GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed = None,
        request_id: str = None,
    ):
        # The details of the time when the AccessKey pair was used for the last time.
        self.access_key_last_used = access_key_last_used
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m['AccessKeyLastUsed'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessKeyLastUsedResponseBody = None,
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
            temp_model = GetAccessKeyLastUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountMFAInfoResponseBody(TeaModel):
    def __init__(
        self,
        is_mfaenable: bool = None,
        request_id: str = None,
    ):
        # Indicates whether MFA is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.is_mfaenable = is_mfaenable
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountMFAInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountMFAInfoResponseBody = None,
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
            temp_model = GetAccountMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(
        self,
        bind_mfa: bool = None,
        old_ak_num: int = None,
        root_with_access_key: int = None,
        sub_user: int = None,
        sub_user_bind_mfa: int = None,
        sub_user_pwd_level: str = None,
        sub_user_with_old_access_key: int = None,
        sub_user_with_unused_access_key: int = None,
        unused_ak_num: int = None,
    ):
        # Indicates whether MFA is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.bind_mfa = bind_mfa
        # The number of old AccessKey pairs for the Alibaba Cloud account.
        self.old_ak_num = old_ak_num
        # The number of AccessKey pairs for the Alibaba Cloud account.
        self.root_with_access_key = root_with_access_key
        # The number of RAM users within the Alibaba Cloud account.
        self.sub_user = sub_user
        # The number of RAM users that have MFA devices bound.
        self.sub_user_bind_mfa = sub_user_bind_mfa
        # The complexity level of the password for the RAM user. Valid values:
        # 
        # *   low
        # *   mid
        # *   high
        self.sub_user_pwd_level = sub_user_pwd_level
        # The number of RAM users that use the old AccessKey pairs.
        self.sub_user_with_old_access_key = sub_user_with_old_access_key
        # The number of RAM users that have no AccessKey pairs.
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key
        # The number of AccessKey pairs that are not used for the Alibaba Cloud account.
        self.unused_ak_num = unused_ak_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa
        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num
        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa
        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level
        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key
        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key
        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindMfa') is not None:
            self.bind_mfa = m.get('BindMfa')
        if m.get('OldAkNum') is not None:
            self.old_ak_num = m.get('OldAkNum')
        if m.get('RootWithAccessKey') is not None:
            self.root_with_access_key = m.get('RootWithAccessKey')
        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')
        if m.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = m.get('SubUserBindMfa')
        if m.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = m.get('SubUserPwdLevel')
        if m.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = m.get('SubUserWithOldAccessKey')
        if m.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = m.get('SubUserWithUnusedAccessKey')
        if m.get('UnusedAkNum') is not None:
            self.unused_ak_num = m.get('UnusedAkNum')
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo(TeaModel):
    def __init__(
        self,
        account_security_practice_user_info: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo = None,
        score: int = None,
    ):
        # The information of the security report for the Alibaba Cloud account.
        self.account_security_practice_user_info = account_security_practice_user_info
        # The security score of the Alibaba Cloud account.
        self.score = score

    def validate(self):
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(m['AccountSecurityPracticeUserInfo'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class GetAccountSecurityPracticeReportResponseBody(TeaModel):
    def __init__(
        self,
        account_security_practice_info: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo = None,
        request_id: str = None,
    ):
        # The information of the security report for the Alibaba Cloud account.
        self.account_security_practice_info = account_security_practice_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_security_practice_info is not None:
            result['AccountSecurityPracticeInfo'] = self.account_security_practice_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPracticeInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(m['AccountSecurityPracticeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountSecurityPracticeReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountSecurityPracticeReportResponseBody = None,
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
            temp_model = GetAccountSecurityPracticeReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSummaryResponseBodySummaryMap(TeaModel):
    def __init__(
        self,
        access_keys_per_user_quota: int = None,
        attached_policies_per_group_quota: int = None,
        attached_policies_per_role_quota: int = None,
        attached_policies_per_user_quota: int = None,
        attached_system_policies_per_group_quota: int = None,
        attached_system_policies_per_role_quota: int = None,
        attached_system_policies_per_user_quota: int = None,
        groups: int = None,
        groups_per_user_quota: int = None,
        groups_quota: int = None,
        mfadevices: int = None,
        mfadevices_in_use: int = None,
        policies: int = None,
        policies_quota: int = None,
        policy_size_quota: int = None,
        roles: int = None,
        roles_quota: int = None,
        users: int = None,
        users_quota: int = None,
        versions_per_policy_quota: int = None,
        virtual_mfadevices_quota: int = None,
    ):
        # The maximum number of AccessKey pairs that a RAM user can have.
        self.access_keys_per_user_quota = access_keys_per_user_quota
        # The maximum number of custom policies that can be added to a RAM user group.
        self.attached_policies_per_group_quota = attached_policies_per_group_quota
        # The maximum number of custom policies that can be added to a RAM role.
        self.attached_policies_per_role_quota = attached_policies_per_role_quota
        # The maximum number of custom policies that can be added to a RAM user.
        self.attached_policies_per_user_quota = attached_policies_per_user_quota
        # The maximum number of system policies that can be added to a RAM user group.
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota
        # The maximum number of system policies that can be added to a RAM role.
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota
        # The maximum number of system policies that can be added to a RAM user.
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota
        # The number of RAM user groups.
        self.groups = groups
        # The maximum number of RAM user groups to which a RAM user can be added.
        self.groups_per_user_quota = groups_per_user_quota
        # The maximum number of RAM user groups that can be created.
        self.groups_quota = groups_quota
        # The number of virtual multi-factor authentication (MFA) devices.
        self.mfadevices = mfadevices
        # The number of virtual MFA devices in use.
        self.mfadevices_in_use = mfadevices_in_use
        # The number of custom policies.
        self.policies = policies
        # The maximum number of custom policies that can be created.
        self.policies_quota = policies_quota
        # The maximum length of the policy content.
        self.policy_size_quota = policy_size_quota
        # The number of RAM roles.
        self.roles = roles
        # The maximum number of RAM roles that can be created.
        self.roles_quota = roles_quota
        # The number of RAM users.
        self.users = users
        # The maximum number of RAM users that can be created.
        self.users_quota = users_quota
        # The maximum number of policy versions.
        self.versions_per_policy_quota = versions_per_policy_quota
        # The maximum number of virtual MFA devices that can be created.
        self.virtual_mfadevices_quota = virtual_mfadevices_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota
        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota
        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices
        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.users is not None:
            result['Users'] = self.users
        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = m.get('AccessKeysPerUserQuota')
        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')
        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')
        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')
        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')
        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')
        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = m.get('GroupsPerUserQuota')
        if m.get('GroupsQuota') is not None:
            self.groups_quota = m.get('GroupsQuota')
        if m.get('MFADevices') is not None:
            self.mfadevices = m.get('MFADevices')
        if m.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = m.get('MFADevicesInUse')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')
        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('UsersQuota') is not None:
            self.users_quota = m.get('UsersQuota')
        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')
        if m.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = m.get('VirtualMFADevicesQuota')
        return self


class GetAccountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        summary_map: GetAccountSummaryResponseBodySummaryMap = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The overview information of the Alibaba Cloud account.
        self.summary_map = summary_map

    def validate(self):
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SummaryMap') is not None:
            temp_model = GetAccountSummaryResponseBodySummaryMap()
            self.summary_map = temp_model.from_map(m['SummaryMap'])
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountSummaryResponseBody = None,
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
            temp_model = GetAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the application secret.
        # 
        # This parameter is required.
        self.app_secret_id = app_secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class GetAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        app_secret_value: str = None,
        create_date: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the application secret.
        self.app_secret_id = app_secret_id
        # The content of the application secret.
        self.app_secret_value = app_secret_value
        # The creation time.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        app_secret: GetAppSecretResponseBodyAppSecret = None,
        request_id: str = None,
    ):
        # The details of the application secret.
        self.app_secret = app_secret
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            temp_model = GetAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppSecretResponseBody = None,
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
            temp_model = GetAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The description of the permission.
        self.description = description
        # The name of the permission.
        self.name = name
        # Indicates whether the permission is automatically selected by default when you install the application. Valid values:
        # 
        # *   true
        # *   false
        # 
        # `openid` is required by default.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class GetApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        # The information about the permissions that are granted on the application.
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class GetApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        access_token_validity: int = None,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        create_date: str = None,
        delegated_scope: GetApplicationResponseBodyApplicationDelegatedScope = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        redirect_uris: GetApplicationResponseBodyApplicationRedirectUris = None,
        refresh_token_validity: int = None,
        secret_required: bool = None,
        update_date: str = None,
    ):
        # The validity period of the access token. Unit: seconds.
        self.access_token_validity = access_token_validity
        # The ID of the Alibaba Cloud account to which the application belongs.
        self.account_id = account_id
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The type of the application. Valid values:
        # 
        # *   WebApp: a web application.
        # *   NativeApp: a native application that runs on an operating system, such as a desktop or mobile operating system.
        # *   ServerApp: an application that can access Alibaba Cloud services without the need for user logon. Only applications that synchronize user information based on the System for Cross-domain Identity Management (SCIM) protocol are supported.
        self.app_type = app_type
        # The creation time.
        self.create_date = create_date
        # The information about the permissions that are granted on the application.
        self.delegated_scope = delegated_scope
        # The display name of the application.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts.
        self.is_multi_tenant = is_multi_tenant
        # The callback URL.
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token. Unit: seconds.
        self.refresh_token_validity = refresh_token_validity
        # Indicates whether a secret is required.
        self.secret_required = secret_required
        # The update time.
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = GetApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: GetApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationResponseBody = None,
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialReportRequest(TeaModel):
    def __init__(
        self,
        max_items: str = None,
        next_token: str = None,
    ):
        # The number of entries per page. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be true.
        # 
        # Valid values: 1 to 3501. Default value: 3501.
        self.max_items = max_items
        # The token that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.``
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetCredentialReportResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        generated_time: str = None,
        is_truncated: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The content of the user credential report.
        # 
        # The report is Base64-encoded. After you decode the report, the credential report is in the CSV format.
        self.content = content
        # The time when the user credential report was generated.
        self.generated_time = generated_time
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The parameter that is used to obtain the truncated part. This parameter takes effect only when `IsTruncated` is set to true.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.generated_time is not None:
            result['GeneratedTime'] = self.generated_time
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GeneratedTime') is not None:
            self.generated_time = m.get('GeneratedTime')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCredentialReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCredentialReportResponseBody = None,
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
            temp_model = GetCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDomainResponseBody(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        # The default domain name.
        self.default_domain_name = default_domain_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultDomainResponseBody = None,
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
            temp_model = GetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        update_date: str = None,
    ):
        # The description.
        self.comments = comments
        # The creation time.
        self.create_date = create_date
        # The display name of the RAM user group.
        self.display_name = display_name
        # The ID of the RAM user group.
        self.group_id = group_id
        # The name of the RAM user group.
        self.group_name = group_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information about the RAM user group.
        self.group = group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupResponseBody = None,
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
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        last_login_time: str = None,
        mfabind_required: bool = None,
        password_reset_required: bool = None,
        status: str = None,
        update_date: str = None,
        user_principal_name: str = None,
    ):
        # The time of the most recent logon. The time is displayed in UTC.
        self.last_login_time = last_login_time
        # Indicates whether multi-factor authentication (MFA) must be enabled. Valid values:
        # 
        # *   false
        # *   true
        self.mfabind_required = mfabind_required
        # Indicates whether the RAM user is required to reset the password upon the next logon. Valid values:
        # 
        # *   false
        # *   true
        self.password_reset_required = password_reset_required
        # Indicates whether console logon is enabled. Valid values:
        # 
        # *   Active: enabled.
        # *   Inactive: disabled.
        self.status = status
        # The modification time. The time is displayed in UTC.
        self.update_date = update_date
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        login_profile: GetLoginProfileResponseBodyLoginProfile = None,
        request_id: str = None,
    ):
        # The console logon configurations.
        self.login_profile = login_profile
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = GetLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoginProfileResponseBody = None,
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
            temp_model = GetLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        oidcprovider_name: str = None,
    ):
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class GetOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: GetOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = GetOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOIDCProviderResponseBody = None,
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
            temp_model = GetOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        hard_expire: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        minimum_password_different_character: int = None,
        minimum_password_length: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_uppercase_characters: bool = None,
    ):
        # Indicates whether to disable logon after the password expires.
        self.hard_expire = hard_expire
        # The maximum number of password retries.
        self.max_login_attemps = max_login_attemps
        # The validity period of the password.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in the password.
        self.minimum_password_different_character = minimum_password_different_character
        # The minimum required number of characters in a password.
        self.minimum_password_length = minimum_password_length
        # Indicates whether to exclude the username from the password.
        self.password_not_contain_user_name = password_not_contain_user_name
        # The policy for password history check.
        self.password_reuse_prevention = password_reuse_prevention
        # Indicates whether the password must contain lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters
        # Indicates whether the password must contain digits.
        self.require_numbers = require_numbers
        # Indicates whether the password must contain special characters.
        self.require_symbols = require_symbols
        # Indicates whether the password must contain uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class GetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        password_policy: GetPasswordPolicyResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        # The details of the password policy.
        self.password_policy = password_policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPasswordPolicyResponseBody = None,
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
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        samlprovider_name: str = None,
    ):
        # The name of the IdP.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class GetSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn
        # The creation time.
        self.create_date = create_date
        # The description.
        self.description = description
        # The metadata file, which is Base64 encoded.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: GetSAMLProviderResponseBodySAMLProvider = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the IdP.
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = GetSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class GetSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSAMLProviderResponseBody = None,
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
            temp_model = GetSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        # Indicates whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        operation_for_risk_login: str = None,
    ):
        # Indicates whether RAM users can change their passwords. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Indicates whether RAM users can remember the multi-factor authentication (MFA) devices for seven days. Valid values:
        # 
        # *   true
        # *   false
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users. Unit: hours.
        self.login_session_duration = login_session_duration
        # Indicates whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use EnforceMFAForLogin, set the value to true.
        # *   independent (default): User-specific settings are applied. If you use EnforceMFAForLogin, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # Indicates whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous (default): yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA.
        # *   enforceVerify: MFA is prompted for RAM users who initiated unusual logons and the RAM users cannot skip MFA.
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        # Indicates whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_personal_ding_talk: bool = None,
    ):
        # Indicates whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true
        # *   false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference(TeaModel):
    def __init__(
        self,
        verification_types: List[str] = None,
    ):
        # The MFA methods.
        self.verification_types = verification_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class GetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        login_profile_preference: GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        mfapreference: GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
        personal_info_preference: GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference = None,
        verification_preference: GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference = None,
    ):
        # The AccessKey pair preference.
        self.access_key_preference = access_key_preference
        # The logon preference.
        self.login_profile_preference = login_profile_preference
        # The MFA preference.
        self.mfapreference = mfapreference
        # The personal information preference.
        self.personal_info_preference = personal_info_preference
        # The MFA method preference.
        self.verification_preference = verification_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()
        if self.verification_preference:
            self.verification_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.personal_info_preference is not None:
            result['PersonalInfoPreference'] = self.personal_info_preference.to_map()
        if self.verification_preference is not None:
            result['VerificationPreference'] = self.verification_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('PersonalInfoPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference()
            self.personal_info_preference = temp_model.from_map(m['PersonalInfoPreference'])
        if m.get('VerificationPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference()
            self.verification_preference = temp_model.from_map(m['VerificationPreference'])
        return self


class GetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: GetSecurityPreferenceResponseBodySecurityPreference = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of security preferences.
        self.security_preference = security_preference

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecurityPreferenceResponseBody = None,
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
            temp_model = GetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The AccessKey ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_access_key_id = user_access_key_id
        # The ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_id = user_id
        # The logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name.
        # 
        # The value of `UserPrincipalName` must be `1 to 128` characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The value of `<username>` must be `1 to 64` characters in length.
        # 
        # > You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserResponseBodyUserTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetUserResponseBodyUserTags(TeaModel):
    def __init__(
        self,
        tag: List[GetUserResponseBodyUserTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetUserResponseBodyUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        email: str = None,
        last_login_date: str = None,
        mobile_phone: str = None,
        provision_type: str = None,
        tags: GetUserResponseBodyUserTags = None,
        update_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The time when the RAM user was created.
        self.create_date = create_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date
        # The mobile phone number of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The source of the RAM user. Valid value:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type
        # The tags.
        self.tags = tags
        # The time when the information about the RAM user was updated.
        self.update_date = update_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Tags') is not None:
            temp_model = GetUserResponseBodyUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: GetUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMFAInfoRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user. This parameter is differently set in the following scenarios:
        # 
        # *   If you use a RAM user to call this operation, this parameter can be left empty. If you do not specify this parameter, the information of the MFA device that is bound to the RAM user is queried.
        # *   If you use an Alibaba Cloud account to call this operation, you must set this parameter to the logon name of the RAM user that you want to query.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserMFAInfoResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        type: str = None,
    ):
        # The serial number of the MFA device.
        self.serial_number = serial_number
        # The type of the MFA device. Valid values:
        # 
        # *   VMFA: virtual MFA device
        # *   U2F: Universal 2nd Factor (U2F) security key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserMFAInfoResponseBody(TeaModel):
    def __init__(
        self,
        is_mfaenable: bool = None,
        mfadevice: GetUserMFAInfoResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        # Indicates whether the MFA device is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.is_mfaenable = is_mfaenable
        # The information about the MFA device.
        self.mfadevice = mfadevice
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        if m.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserMFAInfoResponseBody = None,
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
            temp_model = GetUserMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(
        self,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
        sso_login_with_domain: bool = None,
    ):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain
        # The metadata file, which is Base64-encoded.
        self.metadata_document = metadata_document
        # Indicates whether user-based SSO is enabled.
        self.sso_enabled = sso_enabled
        self.sso_login_with_domain = sso_login_with_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.sso_login_with_domain is not None:
            result['SsoLoginWithDomain'] = self.sso_login_with_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('SsoLoginWithDomain') is not None:
            self.sso_login_with_domain = m.get('SsoLoginWithDomain')
        return self


class GetUserSsoSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_sso_settings: GetUserSsoSettingsResponseBodyUserSsoSettings = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The configurations of user-based SSO.
        self.user_sso_settings = user_sso_settings

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = GetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class GetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserSsoSettingsResponseBody = None,
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
            temp_model = GetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVerificationInfoRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetVerificationInfoResponseBodySecurityEmailDevice(TeaModel):
    def __init__(
        self,
        email: str = None,
        status: str = None,
    ):
        self.email = email
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetVerificationInfoResponseBodySecurityPhoneDevice(TeaModel):
    def __init__(
        self,
        area_code: str = None,
        phone_number: str = None,
        status: str = None,
    ):
        self.area_code = area_code
        self.phone_number = phone_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetVerificationInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_email_device: GetVerificationInfoResponseBodySecurityEmailDevice = None,
        security_phone_device: GetVerificationInfoResponseBodySecurityPhoneDevice = None,
    ):
        self.request_id = request_id
        self.security_email_device = security_email_device
        self.security_phone_device = security_phone_device

    def validate(self):
        if self.security_email_device:
            self.security_email_device.validate()
        if self.security_phone_device:
            self.security_phone_device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_email_device is not None:
            result['SecurityEmailDevice'] = self.security_email_device.to_map()
        if self.security_phone_device is not None:
            result['SecurityPhoneDevice'] = self.security_phone_device.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityEmailDevice') is not None:
            temp_model = GetVerificationInfoResponseBodySecurityEmailDevice()
            self.security_email_device = temp_model.from_map(m['SecurityEmailDevice'])
        if m.get('SecurityPhoneDevice') is not None:
            temp_model = GetVerificationInfoResponseBodySecurityPhoneDevice()
            self.security_phone_device = temp_model.from_map(m['SecurityPhoneDevice'])
        return self


class GetVerificationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVerificationInfoResponseBody = None,
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
            temp_model = GetVerificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the AccessKey pairs of the current user are queried.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListAccessKeysResponseBodyAccessKeysAccessKey(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        create_date: str = None,
        status: str = None,
        update_date: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The time when the AccessKey pair was created.
        self.create_date = create_date
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status
        # The time when the AccessKey pair was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListAccessKeysResponseBodyAccessKeys(TeaModel):
    def __init__(
        self,
        access_key: List[ListAccessKeysResponseBodyAccessKeysAccessKey] = None,
    ):
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessKey'] = []
        if self.access_key is not None:
            for k in self.access_key:
                result['AccessKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_key = []
        if m.get('AccessKey') is not None:
            for k in m.get('AccessKey'):
                temp_model = ListAccessKeysResponseBodyAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class ListAccessKeysResponseBody(TeaModel):
    def __init__(
        self,
        access_keys: ListAccessKeysResponseBodyAccessKeys = None,
        request_id: str = None,
    ):
        # The list of AccessKey pairs.
        self.access_keys = access_keys
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseBodyAccessKeys()
            self.access_keys = temp_model.from_map(m['AccessKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessKeysResponseBody = None,
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
            temp_model = ListAccessKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSecretIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppSecretIdsResponseBodyAppSecretsAppSecret(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret_id: str = None,
        create_date: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the application secret.
        self.app_secret_id = app_secret_id
        # The creation time.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListAppSecretIdsResponseBodyAppSecrets(TeaModel):
    def __init__(
        self,
        app_secret: List[ListAppSecretIdsResponseBodyAppSecretsAppSecret] = None,
    ):
        self.app_secret = app_secret

    def validate(self):
        if self.app_secret:
            for k in self.app_secret:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSecret'] = []
        if self.app_secret is not None:
            for k in self.app_secret:
                result['AppSecret'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_secret = []
        if m.get('AppSecret') is not None:
            for k in m.get('AppSecret'):
                temp_model = ListAppSecretIdsResponseBodyAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k))
        return self


class ListAppSecretIdsResponseBody(TeaModel):
    def __init__(
        self,
        app_secrets: ListAppSecretIdsResponseBodyAppSecrets = None,
        request_id: str = None,
    ):
        # The details of the application secret.
        self.app_secrets = app_secrets
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecrets') is not None:
            temp_model = ListAppSecretIdsResponseBodyAppSecrets()
            self.app_secrets = temp_model.from_map(m['AppSecrets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppSecretIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppSecretIdsResponseBody = None,
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
            temp_model = ListAppSecretIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The description of the permission.
        self.description = description
        # The name of the permission.
        self.name = name
        # Indicates whether the permission is automatically selected by default when you install the application. Valid values:
        # 
        # *   true
        # *   false
        # 
        # `openid` is required by default.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes = None,
    ):
        # The information about the permissions that are granted on the application.
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class ListApplicationsResponseBodyApplicationsApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class ListApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(
        self,
        access_token_validity: int = None,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        create_date: str = None,
        delegated_scope: ListApplicationsResponseBodyApplicationsApplicationDelegatedScope = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        redirect_uris: ListApplicationsResponseBodyApplicationsApplicationRedirectUris = None,
        refresh_token_validity: int = None,
        secret_required: bool = None,
        update_date: str = None,
    ):
        # The validity period of the access token. Unit: seconds.
        self.access_token_validity = access_token_validity
        # The ID of the Alibaba Cloud account to which the application belongs.
        self.account_id = account_id
        # The ID of the application.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application type. Valid values:
        # 
        # *   WebApp: a web application.
        # *   NativeApp: a native application that runs on an operating system, such as a desktop or mobile operating system.
        # *   ServerApp: an application that can access Alibaba Cloud services without the need for user logon. Only applications that synchronize user information based on the System for Cross-domain Identity Management (SCIM) protocol are supported.
        self.app_type = app_type
        # The creation time.
        self.create_date = create_date
        # The information about the permissions that are granted on the application.
        self.delegated_scope = delegated_scope
        # The display name of the application.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts.
        self.is_multi_tenant = is_multi_tenant
        # The callback URLs.
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token. Unit: seconds.
        self.refresh_token_validity = refresh_token_validity
        # Indicates whether a secret is required.
        self.secret_required = secret_required
        # The update time.
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application: List[ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: ListApplicationsResponseBodyApplications = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.applications = applications
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applications') is not None:
            temp_model = ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationsResponseBody = None,
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        update_date: str = None,
    ):
        # The description.
        self.comments = comments
        # The creation time.
        self.create_date = create_date
        # The display name of the RAM user group.
        self.display_name = display_name
        # The ID of the RAM user group.
        self.group_id = group_id
        # The name of the RAM user group.
        self.group_name = group_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: ListGroupsResponseBodyGroups = None,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
    ):
        # The information of the RAM user groups.
        self.groups = groups
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # - false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = ListGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupsResponseBody = None,
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListGroupsForUserResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        join_date: str = None,
    ):
        # The description.
        self.comments = comments
        # The display name of the RAM user group.
        self.display_name = display_name
        # The ID of the RAM user group.
        self.group_id = group_id
        # The name of the RAM user group.
        self.group_name = group_name
        # The time when the RAM user was added.
        self.join_date = join_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListGroupsForUserResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsForUserResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsForUserResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsForUserResponseBody(TeaModel):
    def __init__(
        self,
        groups: ListGroupsForUserResponseBodyGroups = None,
        request_id: str = None,
    ):
        # The information of the RAM user groups.
        self.groups = groups
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = ListGroupsForUserResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupsForUserResponseBody = None,
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
            temp_model = ListGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOIDCProvidersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries per page. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client, If you want to specify multiple client IDs, separate the client IDs with commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListOIDCProvidersResponseBodyOIDCProviders(TeaModel):
    def __init__(
        self,
        oidcprovider: List[ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider] = None,
    ):
        self.oidcprovider = oidcprovider

    def validate(self):
        if self.oidcprovider:
            for k in self.oidcprovider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OIDCProvider'] = []
        if self.oidcprovider is not None:
            for k in self.oidcprovider:
                result['OIDCProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.oidcprovider = []
        if m.get('OIDCProvider') is not None:
            for k in m.get('OIDCProvider'):
                temp_model = ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider()
                self.oidcprovider.append(temp_model.from_map(k))
        return self


class ListOIDCProvidersResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        oidcproviders: ListOIDCProvidersResponseBodyOIDCProviders = None,
        request_id: str = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.``
        self.marker = marker
        # The information about the OIDC IdP.
        self.oidcproviders = oidcproviders
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcproviders:
            self.oidcproviders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.oidcproviders is not None:
            result['OIDCProviders'] = self.oidcproviders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('OIDCProviders') is not None:
            temp_model = ListOIDCProvidersResponseBodyOIDCProviders()
            self.oidcproviders = temp_model.from_map(m['OIDCProviders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOIDCProvidersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOIDCProvidersResponseBody = None,
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
            temp_model = ListOIDCProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPredefinedScopesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
    ):
        # The type of the application. Valid values:
        # 
        # *   WebApp
        # *   NativeApp
        # *   ServerApp
        # 
        # If this parameter is empty, the permissions on all types of applications are queried.
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the permission scope.
        self.description = description
        # The name of the scope.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListPredefinedScopesResponseBodyPredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListPredefinedScopesResponseBody(TeaModel):
    def __init__(
        self,
        predefined_scopes: ListPredefinedScopesResponseBodyPredefinedScopes = None,
        request_id: str = None,
    ):
        # The information of application permissions.
        self.predefined_scopes = predefined_scopes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListPredefinedScopesResponseBodyPredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPredefinedScopesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPredefinedScopesResponseBody = None,
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
            temp_model = ListPredefinedScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn
        # The creation time.
        self.create_date = create_date
        # The description.
        self.description = description
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListSAMLProvidersResponseBodySAMLProviders(TeaModel):
    def __init__(
        self,
        samlprovider: List[ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider] = None,
    ):
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            for k in self.samlprovider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SAMLProvider'] = []
        if self.samlprovider is not None:
            for k in self.samlprovider:
                result['SAMLProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.samlprovider = []
        if m.get('SAMLProvider') is not None:
            for k in m.get('SAMLProvider'):
                temp_model = ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k))
        return self


class ListSAMLProvidersResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        samlproviders: ListSAMLProvidersResponseBodySAMLProviders = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker
        # The ID of the request.
        self.request_id = request_id
        # The information of the IdP.
        self.samlproviders = samlproviders

    def validate(self):
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProviders') is not None:
            temp_model = ListSAMLProvidersResponseBodySAMLProviders()
            self.samlproviders = temp_model.from_map(m['SAMLProviders'])
        return self


class ListSAMLProvidersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSAMLProvidersResponseBody = None,
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
            temp_model = ListSAMLProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        page_size: int = None,
        resource_id: List[str] = None,
        resource_principal_name: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The token that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The number of entries per page. If a response is truncated because it reaches the value of PageSize, the value of IsTruncated will be true. Valid values: 1 to 100. Default value: 100.
        self.page_size = page_size
        # The ID of resource N.
        # 
        # Valid values of N: 1 to 50. If ResourceType is set to user, the resource ID is the ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_id = resource_id
        # The name of resource N.
        # 
        # Valid values of N: 1 to 50. If ResourceType is set to user, the resource name is the name of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_principal_name = resource_principal_name
        # The type of the resource. Valid value:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type
        # The tag value.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The marker. This parameter is returned only if the value of IsTruncated is true. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tag key.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserBasicInfosRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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


class ListUserBasicInfosRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        status: str = None,
        tag: List[ListUserBasicInfosRequestTag] = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items
        self.status = status
        # The tag value.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListUserBasicInfosRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        status: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The display name of the RAM user.
        self.display_name = display_name
        self.status = status
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUserBasicInfosResponseBodyUserBasicInfos(TeaModel):
    def __init__(
        self,
        user_basic_info: List[ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo] = None,
    ):
        self.user_basic_info = user_basic_info

    def validate(self):
        if self.user_basic_info:
            for k in self.user_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserBasicInfo'] = []
        if self.user_basic_info is not None:
            for k in self.user_basic_info:
                result['UserBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_basic_info = []
        if m.get('UserBasicInfo') is not None:
            for k in m.get('UserBasicInfo'):
                temp_model = ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        user_basic_infos: ListUserBasicInfosResponseBodyUserBasicInfos = None,
    ):
        # Indicates whether the response is truncated. Valid value:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the information about the RAM user.
        self.user_basic_infos = user_basic_infos

    def validate(self):
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserBasicInfos') is not None:
            temp_model = ListUserBasicInfosResponseBodyUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(m['UserBasicInfos'])
        return self


class ListUserBasicInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserBasicInfosResponseBody = None,
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
            temp_model = ListUserBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        status: str = None,
        tag: List[ListUsersRequestTag] = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries per page. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be true.
        # 
        # Valid values: 1 to 1000. Default value: 1000.
        self.max_items = max_items
        self.status = status
        # The tags. A maximum number of 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListUsersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUsersResponseBodyUsersUserTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListUsersResponseBodyUsersUserTags(TeaModel):
    def __init__(
        self,
        tag: List[ListUsersResponseBodyUsersUserTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListUsersResponseBodyUsersUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUsersResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        email: str = None,
        last_login_date: str = None,
        mobile_phone: str = None,
        provision_type: str = None,
        status: str = None,
        tags: ListUsersResponseBodyUsersUserTags = None,
        update_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The point in time when the RAM user was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # >  This parameter applies only to the Alibaba Cloud China site (aliyun.com).
        self.email = email
        # The timestamp when the RAM user last logged on to the console.
        self.last_login_date = last_login_date
        # The mobile phone number of the RAM user.
        # 
        # >  This parameter applies only to the Alibaba Cloud China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type
        self.status = status
        # The tags.
        self.tags = tags
        # The point in time when the information about the RAM user was last modified. The time is displayed in UTC.
        self.update_date = update_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListUsersResponseBodyUsersUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        users: ListUsersResponseBodyUsers = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The parameter that is used to obtain the truncated part. It takes effect only when `IsTruncated` is set to `true`.
        self.marker = marker
        # The request ID.
        self.request_id = request_id
        # The details of the RAM user.
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersForGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        marker: str = None,
        max_items: int = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.``
        # 
        # When you call the operation for the first time, if the total number of returned entries exceeds the value of `MaxItems`, the entries are truncated. The system returns entries based on the value of `MaxItems` and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and `Marker` is returned. In the next call, you can use the value of `Marker` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.marker = marker
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 100.
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersForGroupResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        join_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The display name of the RAM user.
        self.display_name = display_name
        # The time when the RAM user was added to the RAM user group. The time is displayed in UTC.
        self.join_date = join_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUsersForGroupResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersForGroupResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersForGroupResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersForGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        users: ListUsersForGroupResponseBodyUsers = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when `IsTruncated` is `true`.
        self.marker = marker
        # The request ID.
        self.request_id = request_id
        # The information about the RAM users.
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            temp_model = ListUsersForGroupResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersForGroupResponseBody = None,
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
            temp_model = ListUsersForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.``
        # 
        # When you call the operation for the first time, if the total number of returned entries exceeds the value of `MaxItems`, the entries are truncated. The system returns entries based on the value of `MaxItems` and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and `Marker` is returned. In the next call, you can use the value of `Marker` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of the `IsTruncated` parameter becomes `false`. This way, all entries are returned.
        self.marker = marker
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 100.
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The display name of the RAM user.
        self.display_name = display_name
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(
        self,
        activate_date: str = None,
        serial_number: str = None,
        user: ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser = None,
    ):
        # The time when the MFA device was activated.
        self.activate_date = activate_date
        # The serial number of the MFA device.
        self.serial_number = serial_number
        # The information of the RAM user that has an MFA device bound.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: List[ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice] = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_mfadevice = []
        if m.get('VirtualMFADevice') is not None:
            for k in m.get('VirtualMFADevice'):
                temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListVirtualMFADevicesResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        virtual_mfadevices: ListVirtualMFADevicesResponseBodyVirtualMFADevices = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when `IsTruncated` is `true`.
        self.marker = marker
        # The request ID.
        self.request_id = request_id
        # The information about the MFA device.
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m['VirtualMFADevices'])
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVirtualMFADevicesResponseBody = None,
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
            temp_model = ListVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientIdFromOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        oidcprovider_name: str = None,
    ):
        # The client ID that you want to remove.
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # The client ID can be up to 64 characters in length.
        self.client_id = client_id
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class RemoveClientIdFromOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveClientIdFromOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveClientIdFromOIDCProviderResponseBody = None,
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
            temp_model = RemoveClientIdFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFingerprintFromOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        oidcprovider_name: str = None,
    ):
        # The fingerprint that you want to remove.
        self.fingerprint = fingerprint
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class RemoveFingerprintFromOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveFingerprintFromOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveFingerprintFromOIDCProviderResponseBody = None,
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
            temp_model = RemoveFingerprintFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        user_principal_name: str = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class RemoveUserFromGroupResponseBody(TeaModel):
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


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserFromGroupResponseBody = None,
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
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
    ):
        # The default domain name.
        # 
        # The name is in the format of `<AccountAlias>.onaliyun.com`. `<AccountAlias>` indicates the account alias. By default, the value of AccountAlias is the ID of the Alibaba Cloud account. The default domain name must end with `.onaliyun.com`.
        # 
        # The default domain name can contain up to 64 characters in length. The name can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  The default domain name cannot start or end with a hyphen (-) and cannot have two consecutive hyphens (-).
        # 
        # This parameter is required.
        self.default_domain_name = default_domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        return self


class SetDefaultDomainResponseBody(TeaModel):
    def __init__(
        self,
        default_domain_name: str = None,
        request_id: str = None,
    ):
        # The default domain name.
        self.default_domain_name = default_domain_name
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDefaultDomainResponseBody = None,
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
            temp_model = SetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        hard_expire: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        minimum_password_different_character: int = None,
        minimum_password_length: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_uppercase_characters: bool = None,
    ):
        # Specifies whether to disable logon after the password expires. Valid values:
        # 
        # *   true: After the password expires, you cannot use the password to log on to the console. You can log on to the console only after you reset the password by using your Alibaba Cloud account or as a RAM user that has administrative rights.
        # *   false: After the password expires, you can change the password to log on to the console. This is the default value.
        self.hard_expire = hard_expire
        # The maximum number of password retries. If you enter the wrong passwords for the specified consecutive times, the account is locked for one hour.
        # 
        # Valid values: 0 to 32.
        # 
        # The default value is 0, which indicates that the password retries are not limited.
        self.max_login_attemps = max_login_attemps
        # The validity period of the password.
        # 
        # Valid values: 0 to 1095. Unit: days.
        # 
        # The default value is 0, which indicates that the password never expires.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in the password.
        # 
        # Valid values: 0 to 8.
        # 
        # The default value is 0, which indicates that no limits are imposed on the number of unique characters in a password.
        self.minimum_password_different_character = minimum_password_different_character
        # The minimum number of characters in the password.
        # 
        # Valid values: 8 to 32. Default value: 8.
        self.minimum_password_length = minimum_password_length
        # Specifies whether to exclude the username from the password. Valid values:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username. This is the default value.
        self.password_not_contain_user_name = password_not_contain_user_name
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24.
        # 
        # The default value is 0, which indicates that RAM users can reuse previous passwords.
        self.password_reuse_prevention = password_reuse_prevention
        # Specifies whether the password must contain lowercase letters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_lowercase_characters = require_lowercase_characters
        # Specifies whether the password must contain digits. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_numbers = require_numbers
        # Specifies whether the password must contain special characters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_symbols = require_symbols
        # Specifies whether the password must contain uppercase letters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_uppercase_characters = require_uppercase_characters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class SetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        hard_expire: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        minimum_password_different_character: int = None,
        minimum_password_length: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_uppercase_characters: bool = None,
    ):
        # Indicates whether to disable logon after the password expires.
        self.hard_expire = hard_expire
        # The maximum number of password retries.
        self.max_login_attemps = max_login_attemps
        # The validity period of the password.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in the password.
        self.minimum_password_different_character = minimum_password_different_character
        # The minimum number of characters in the password.
        self.minimum_password_length = minimum_password_length
        # Indicates whether to exclude the username from the password.
        self.password_not_contain_user_name = password_not_contain_user_name
        # The policy for password history check.
        self.password_reuse_prevention = password_reuse_prevention
        # Indicates whether the password must contain lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters
        # Indicates whether the password must contain digits.
        self.require_numbers = require_numbers
        # Indicates whether the password must contain special characters.
        self.require_symbols = require_symbols
        # Indicates whether the password must contain uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class SetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        password_policy: SetPasswordPolicyResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        # The details of the password policy.
        self.password_policy = password_policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = SetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPasswordPolicyResponseBody = None,
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
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        allow_user_to_manage_personal_ding_talk: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        operation_for_risk_login: str = None,
        verification_types: List[str] = None,
    ):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true
        # *   false (default)
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        # Specifies whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk
        # Specifies whether RAM users can remember the MFA devices for seven days. Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). This parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you need to specify multiple subnet masks, separate the subnet masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # You can specify up to 40 subnet masks. The total length of the subnet masks can be a maximum of 512 characters.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace EnforceMFAForLogin. EnforceMFAForLogin is still valid. However, we recommend that you use MFAOperationForLogin. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use EnforceMFAForLogin, set the value to true.
        # *   independent (default): User-specific settings are applied. If you use EnforceMFAForLogin, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous (default): yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA.
        # *   enforceVerify: MFA is prompted for RAM users who initiated unusual logons and the RAM users cannot skip MFA.
        self.operation_for_risk_login = operation_for_risk_login
        # The MFA methods.
        self.verification_types = verification_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceShrinkRequest(TeaModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        allow_user_to_manage_personal_ding_talk: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        operation_for_risk_login: str = None,
        verification_types_shrink: str = None,
    ):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_change_password = allow_user_to_change_password
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true
        # *   false (default)
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        # Specifies whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true (default)
        # *   false
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk
        # Specifies whether RAM users can remember the MFA devices for seven days. Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). This parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you need to specify multiple subnet masks, separate the subnet masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # You can specify up to 40 subnet masks. The total length of the subnet masks can be a maximum of 512 characters.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace EnforceMFAForLogin. EnforceMFAForLogin is still valid. However, we recommend that you use MFAOperationForLogin. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use EnforceMFAForLogin, set the value to true.
        # *   independent (default): User-specific settings are applied. If you use EnforceMFAForLogin, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous (default): yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA.
        # *   enforceVerify: MFA is prompted for RAM users who initiated unusual logons and the RAM users cannot skip MFA.
        self.operation_for_risk_login = operation_for_risk_login
        # The MFA methods.
        self.verification_types_shrink = verification_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        if self.verification_types_shrink is not None:
            result['VerificationTypes'] = self.verification_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        if m.get('VerificationTypes') is not None:
            self.verification_types_shrink = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        # Indicates whether RAM users can manage their AccessKey pairs.
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        allow_user_to_change_password: bool = None,
        enable_save_mfaticket: bool = None,
        login_network_masks: str = None,
        login_session_duration: int = None,
        mfaoperation_for_login: str = None,
        operation_for_risk_login: str = None,
    ):
        # Indicates whether RAM users can change their passwords.
        self.allow_user_to_change_password = allow_user_to_change_password
        # Indicates whether RAM users can remember the MFA devices for seven days.
        self.enable_save_mfaticket = enable_save_mfaticket
        # The subnet mask.
        self.login_network_masks = login_network_masks
        # The validity period of the logon session of RAM users.
        self.login_session_duration = login_session_duration
        # Indicates whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console.
        self.mfaoperation_for_login = mfaoperation_for_login
        # Indicates whether to enable MFA for RAM users who initiated unusual logons.
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        # Indicates whether RAM users can manage their MFA devices.
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_personal_ding_talk: bool = None,
    ):
        # Indicates whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts.
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference(TeaModel):
    def __init__(
        self,
        verification_types: List[str] = None,
    ):
        # The MFA methods.
        self.verification_types = verification_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        login_profile_preference: SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        mfapreference: SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
        personal_info_preference: SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference = None,
        verification_preference: SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference = None,
    ):
        # The AccessKey pair preference.
        self.access_key_preference = access_key_preference
        # The logon preference.
        self.login_profile_preference = login_profile_preference
        # The MFA preference.
        self.mfapreference = mfapreference
        # The personal information preference.
        self.personal_info_preference = personal_info_preference
        # The MFA method preference.
        self.verification_preference = verification_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()
        if self.verification_preference:
            self.verification_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.personal_info_preference is not None:
            result['PersonalInfoPreference'] = self.personal_info_preference.to_map()
        if self.verification_preference is not None:
            result['VerificationPreference'] = self.verification_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('PersonalInfoPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference()
            self.personal_info_preference = temp_model.from_map(m['PersonalInfoPreference'])
        if m.get('VerificationPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference()
            self.verification_preference = temp_model.from_map(m['VerificationPreference'])
        return self


class SetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_preference: SetSecurityPreferenceResponseBodySecurityPreference = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of security preferences.
        self.security_preference = security_preference

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSecurityPreferenceResponseBody = None,
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
            temp_model = SetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(
        self,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
        sso_login_with_domain: bool = None,
    ):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain
        # The metadata file, which is Base64-encoded.
        # 
        # The file is provided by an IdP that supports SAML 2.0.
        self.metadata_document = metadata_document
        # Specifies whether to enable SSO for the RAM user. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.sso_enabled = sso_enabled
        self.sso_login_with_domain = sso_login_with_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.sso_login_with_domain is not None:
            result['SsoLoginWithDomain'] = self.sso_login_with_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('SsoLoginWithDomain') is not None:
            self.sso_login_with_domain = m.get('SsoLoginWithDomain')
        return self


class SetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(
        self,
        auxiliary_domain: str = None,
        metadata_document: str = None,
        sso_enabled: bool = None,
        sso_login_with_domain: bool = None,
    ):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain
        # The metadata file, which is Base64-encoded.
        self.metadata_document = metadata_document
        # Indicates whether user-based SSO is enabled.
        self.sso_enabled = sso_enabled
        self.sso_login_with_domain = sso_login_with_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.sso_login_with_domain is not None:
            result['SsoLoginWithDomain'] = self.sso_login_with_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('SsoLoginWithDomain') is not None:
            self.sso_login_with_domain = m.get('SsoLoginWithDomain')
        return self


class SetUserSsoSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_sso_settings: SetUserSsoSettingsResponseBodyUserSsoSettings = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The configurations of user-based SSO.
        self.user_sso_settings = user_sso_settings

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = SetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class SetUserSsoSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetUserSsoSettingsResponseBody = None,
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
            temp_model = SetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be a up to128 characters in length and cannot contain `http://` or `https://`.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_principal_name: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of resource N.
        # 
        # Valid values of N: 1 to 50. If ResourceType is set to user, the resource ID is the ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_id = resource_id
        # The name of resource N.
        # 
        # Valid values of N: 1 to 50. If ResourceType is set to user, the resource name is the name of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_principal_name = resource_principal_name
        # The type of the resource. Valid value:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type
        # The tag value.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UnbindMFADeviceResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        # The serial number of the MFA device.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnbindMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        mfadevice: UnbindMFADeviceResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        # The information of the MFA device.
        self.mfadevice = mfadevice
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindMFADeviceResponseBody = None,
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
            temp_model = UnbindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_principal_name: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resource. Valid values:
        # 
        # *   true: remove all tags from the resources.
        # *   false (default): does not remove all tags from the resources.
        # 
        # > This parameter takes effect only when TagKey.N is not set in the request.
        self.all = all
        # The IDs of resources.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource ID is the ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_id = resource_id
        # The names of resources.
        # 
        # Valid values of N: 1 to 50. If the ResourceType parameter is set to user, the resource name is the name of the RAM user.
        # 
        # > You must specify only one of the following parameters: ResourceId and ResourcePrincipalName.
        self.resource_principal_name = resource_principal_name
        # The type of the resource. Valid value:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type
        # The tag keys of resources.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        # 
        # This parameter is required.
        self.status = status
        # The AccessKey ID of the AccessKey pair for which you want to modify the status.
        # 
        # This parameter is required.
        self.user_access_key_id = user_access_key_id
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the status of the AccessKey pair for the current user is modified.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateAccessKeyResponseBody(TeaModel):
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


class UpdateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccessKeyResponseBody = None,
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
            temp_model = UpdateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        new_access_token_validity: int = None,
        new_display_name: str = None,
        new_is_multi_tenant: bool = None,
        new_predefined_scopes: str = None,
        new_redirect_uris: str = None,
        new_refresh_token_validity: int = None,
        new_required_scopes: str = None,
        new_secret_required: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The validity period of the access token.
        # 
        # Valid values: 900 to 10800. Unit: seconds.
        self.new_access_token_validity = new_access_token_validity
        # The display name.
        self.new_display_name = new_display_name
        # Specifies whether the application can be installed by using other Alibaba Cloud accounts. Valid values:
        # 
        # *   true
        # *   false
        self.new_is_multi_tenant = new_is_multi_tenant
        # The permission that is granted on the application.
        # 
        # For more information about the application permission scope, see [OAuth scopes](https://help.aliyun.com/document_detail/93693.html). You can also call the [ListPredefinedScopes](https://help.aliyun.com/document_detail/187206.html) operation to query the permissions that are supported by different types of applications.
        # 
        # If you enter multiple permissions, separate them with semicolons (;).
        # 
        # The new value of this parameter overwrites the original value, and the permission specified by the new value takes effect. For example, if the original value is `/acs/ccc`, and the new value is `/acs/alidns`, `/acs/alidns` takes effect. If you want to retain the original permission and the `/acs/alidns` permission, set the value to `/acs/ccc;/acs/alidns`.
        self.new_predefined_scopes = new_predefined_scopes
        # The callback URL.
        # 
        # If you enter multiple callback URLs, separate them with semicolons (;).
        self.new_redirect_uris = new_redirect_uris
        # The validity period of the refresh token.
        # 
        # Valid values: 7200 to 31536000. Unit: seconds.
        self.new_refresh_token_validity = new_refresh_token_validity
        # The required permission.
        # 
        # You can specify one or more permissions for the `RequiredScopes` parameter. After you specify this parameter, the required permissions are automatically selected and cannot be revoked when a user grants permissions on the application.
        # 
        # If you also specify the `NewPredefinedScopes` parameter, the `NewPredefinedScopes` parameter specifies the permissions that can be granted on the application, and this parameter specifies the required permissions.
        # 
        # If you enter multiple permissions, separate them with semicolons (;).
        # 
        # The new value of this parameter overwrites the original value, and the required permission specified by the new value takes effect.
        # 
        # >  If the permission that you specify for the `RequiredScopes` parameter is not included in value of the `PredefinedScopes` parameter, the permission does not take effect.
        self.new_required_scopes = new_required_scopes
        # Specifies whether a secret is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > 
        # 
        # *   For applications of the WebApp and ServerApp types, this parameter is automatically set to true and cannot be changed.
        # *   For applications of the NativeApp type, this parameter can be set to true or false. If you do not set this parameter, false is used. Applications of the NativeApp type run in untrusted environments and the secrets of these applications are not protected. Therefore, we recommend that you do not set this parameter to true unless otherwise specified. For more information, see [Use an application of the NativeApp type to log on to Alibaba Cloud](https://help.aliyun.com/document_detail/93697.html).
        self.new_secret_required = new_secret_required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.new_access_token_validity is not None:
            result['NewAccessTokenValidity'] = self.new_access_token_validity
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_is_multi_tenant is not None:
            result['NewIsMultiTenant'] = self.new_is_multi_tenant
        if self.new_predefined_scopes is not None:
            result['NewPredefinedScopes'] = self.new_predefined_scopes
        if self.new_redirect_uris is not None:
            result['NewRedirectUris'] = self.new_redirect_uris
        if self.new_refresh_token_validity is not None:
            result['NewRefreshTokenValidity'] = self.new_refresh_token_validity
        if self.new_required_scopes is not None:
            result['NewRequiredScopes'] = self.new_required_scopes
        if self.new_secret_required is not None:
            result['NewSecretRequired'] = self.new_secret_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NewAccessTokenValidity') is not None:
            self.new_access_token_validity = m.get('NewAccessTokenValidity')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = m.get('NewIsMultiTenant')
        if m.get('NewPredefinedScopes') is not None:
            self.new_predefined_scopes = m.get('NewPredefinedScopes')
        if m.get('NewRedirectUris') is not None:
            self.new_redirect_uris = m.get('NewRedirectUris')
        if m.get('NewRefreshTokenValidity') is not None:
            self.new_refresh_token_validity = m.get('NewRefreshTokenValidity')
        if m.get('NewRequiredScopes') is not None:
            self.new_required_scopes = m.get('NewRequiredScopes')
        if m.get('NewSecretRequired') is not None:
            self.new_secret_required = m.get('NewSecretRequired')
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        required: bool = None,
    ):
        # The description of the permission.
        self.description = description
        # The name of the permission.
        self.name = name
        # Indicates whether the permission is automatically selected by default when you install the application. Valid values:
        # 
        # *   true
        # *   false
        # 
        # `openid` is required by default.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(
        self,
        predefined_scope: List[UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(
        self,
        predefined_scopes: UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes = None,
    ):
        # The information about the permissions that are granted on the application.
        self.predefined_scopes = predefined_scopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class UpdateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(
        self,
        redirect_uri: List[str] = None,
    ):
        self.redirect_uri = redirect_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        access_token_validity: int = None,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        create_date: str = None,
        delegated_scope: UpdateApplicationResponseBodyApplicationDelegatedScope = None,
        display_name: str = None,
        is_multi_tenant: bool = None,
        redirect_uris: UpdateApplicationResponseBodyApplicationRedirectUris = None,
        refresh_token_validity: int = None,
        secret_required: bool = None,
        update_date: str = None,
    ):
        # The validity period of the access token. Unit: seconds.
        self.access_token_validity = access_token_validity
        # The ID of the Alibaba Cloud account to which the application belongs.
        self.account_id = account_id
        # The ID of the application.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application type.
        self.app_type = app_type
        # The creation time.
        self.create_date = create_date
        # The information about the permissions that are granted on the application.
        self.delegated_scope = delegated_scope
        # The display name of the application.
        self.display_name = display_name
        # Indicates whether the application can be installed by using other Alibaba Cloud accounts.
        self.is_multi_tenant = is_multi_tenant
        # The callback URLs.
        self.redirect_uris = redirect_uris
        # The validity period of the refresh token. Unit: seconds.
        self.refresh_token_validity = refresh_token_validity
        # Indicates whether a secret is required.
        self.secret_required = secret_required
        # The update time.
        self.update_date = update_date

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: UpdateApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationResponseBody = None,
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
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        new_comments: str = None,
        new_display_name: str = None,
        new_group_name: str = None,
    ):
        # The name of the RAM user group.
        self.group_name = group_name
        # The new description.
        # 
        # The value can be up to 128 characters in length.
        self.new_comments = new_comments
        # The new display name of the RAM user group.
        # 
        # The name can be up to 24 characters in length.
        self.new_display_name = new_display_name
        # The new name of the RAM user group.
        # 
        # The name can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.new_group_name = new_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        group_id: str = None,
        group_name: str = None,
        update_date: str = None,
    ):
        # The description.
        self.comments = comments
        # The creation time.
        self.create_date = create_date
        # The display name of the RAM user group.
        self.display_name = display_name
        # The ID of the RAM user group.
        self.group_id = group_id
        # The name of the RAM user group.
        self.group_name = group_name
        # The update time.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: UpdateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The information of the RAM user group.
        self.group = group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = UpdateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupResponseBody = None,
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
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password: str = None,
        password_reset_required: bool = None,
        status: str = None,
        user_principal_name: str = None,
    ):
        # Specifies whether multi-factor authentication (MFA) must be enabled. Valid values:
        # 
        # *   true. The value true indicates that the RAM user must bind an MFA device at the next logon.
        # *   false.
        self.mfabind_required = mfabind_required
        # The new password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements.
        self.password = password
        # Specifies whether the RAM user must reset the password at the next logon. Valid values:
        # 
        # *   true
        # *   false
        self.password_reset_required = password_reset_required
        # The status of password-based logon. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        mfabind_required: bool = None,
        password_reset_required: bool = None,
        status: str = None,
        update_date: str = None,
        user_principal_name: str = None,
    ):
        # Indicates whether MFA must be enabled.
        self.mfabind_required = mfabind_required
        # Indicates whether the RAM user must reset the password at the next logon.
        self.password_reset_required = password_reset_required
        # The status of password-based logon.
        self.status = status
        # The update time.
        self.update_date = update_date
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        login_profile: UpdateLoginProfileResponseBodyLoginProfile = None,
        request_id: str = None,
    ):
        # The logon information.
        self.login_profile = login_profile
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = UpdateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLoginProfileResponseBody = None,
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
            temp_model = UpdateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOIDCProviderRequest(TeaModel):
    def __init__(
        self,
        client_ids: str = None,
        issuance_limit_time: int = None,
        new_description: str = None,
        oidcprovider_name: str = None,
    ):
        # The ID of the client. If you want to specify multiple client IDs, separate the client IDs with commas (,).
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # The client ID can be up to 64 characters in length.
        # 
        # > If you specify this parameter, all the client IDs of the OIDC IdP are replaced. If you need to only add or remove a client ID, call the AddClientIdToOIDCProvider or RemoveClientIdFromOIDCProvider operation. For more information, see [AddClientIdToOIDCProvider](https://help.aliyun.com/document_detail/332057.html) or [RemoveClientIdFromOIDCProvider](https://help.aliyun.com/document_detail/332058.html).
        self.client_ids = client_ids
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.new_description = new_description
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class UpdateOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateOIDCProviderResponseBody(TeaModel):
    def __init__(
        self,
        oidcprovider: UpdateOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = UpdateOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOIDCProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOIDCProviderResponseBody = None,
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
            temp_model = UpdateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(
        self,
        new_description: str = None,
        new_encoded_samlmetadata_document: str = None,
        samlprovider_name: str = None,
    ):
        # The new description.
        # 
        # >  You must specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_description = new_description
        # The new metadata file.
        # 
        # >  You must specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document
        # The name of the IdP whose information you want to modify.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = m.get('NewEncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class UpdateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn
        # The point in time at which the IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the IdP.
        self.description = description
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name
        # The point in time at which the information about the IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateSAMLProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlprovider: UpdateSAMLProviderResponseBodySAMLProvider = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the IdP.
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = UpdateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class UpdateSAMLProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSAMLProviderResponseBody = None,
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
            temp_model = UpdateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        new_comments: str = None,
        new_display_name: str = None,
        new_email: str = None,
        new_mobile_phone: str = None,
        new_user_principal_name: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The new description of the RAM user.
        # 
        # The description must be 1 to 128 characters in length.
        self.new_comments = new_comments
        # The new display name of the RAM user.
        # 
        # The name must be 1 to 24 characters in length.
        self.new_display_name = new_display_name
        # The new email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.new_email = new_email
        # The new mobile phone number of the RAM user.
        # 
        # Format: \\<Country code>-\\<Mobile phone number>.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.new_mobile_phone = new_mobile_phone
        # The new logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name.
        # 
        # The value of `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_). The value of `<username>` must be 1 to 64 characters in length.
        self.new_user_principal_name = new_user_principal_name
        # The ID of the RAM user.
        # 
        # > You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_id = user_id
        # The logon name of the RAM user.
        # 
        # > You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_email is not None:
            result['NewEmail'] = self.new_email
        if self.new_mobile_phone is not None:
            result['NewMobilePhone'] = self.new_mobile_phone
        if self.new_user_principal_name is not None:
            result['NewUserPrincipalName'] = self.new_user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')
        if m.get('NewMobilePhone') is not None:
            self.new_mobile_phone = m.get('NewMobilePhone')
        if m.get('NewUserPrincipalName') is not None:
            self.new_user_principal_name = m.get('NewUserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_date: str = None,
        display_name: str = None,
        email: str = None,
        last_login_date: str = None,
        mobile_phone: str = None,
        provision_type: str = None,
        update_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        # The description.
        self.comments = comments
        # The time when the RAM user was created.
        self.create_date = create_date
        # The display name of the RAM user.
        self.display_name = display_name
        # The email address of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.email = email
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date
        # The mobile phone number of the RAM user.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone
        # The source of the RAM user. Valid values:
        # 
        # - Manual: The RAM user is manually created in the RAM console.
        # - SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # - CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type
        # The time when the information about the RAM user was updated.
        self.update_date = update_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: UpdateUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


