# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckImportDataAddressRequest(TeaModel):
    def __init__(
        self,
        mgw_region_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        address_type: str = None,
        direction: str = None,
        domain: str = None,
        address: str = None,
        sub_address: str = None,
        appid: str = None,
        list_file_path: str = None,
        access_method: str = None,
        access_proxy: str = None,
        access_key_secret: str = None,
        access_key: str = None,
        inv_domain: str = None,
        inv_access_key_id: str = None,
        inv_secret_key: str = None,
        inv_path: str = None,
        alias_name: str = None,
    ):
        self.mgw_region_id = mgw_region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.address_type = address_type
        self.direction = direction
        self.domain = domain
        self.address = address
        self.sub_address = sub_address
        self.appid = appid
        self.list_file_path = list_file_path
        self.access_method = access_method
        self.access_proxy = access_proxy
        self.access_key_secret = access_key_secret
        self.access_key = access_key
        self.inv_domain = inv_domain
        self.inv_access_key_id = inv_access_key_id
        self.inv_secret_key = inv_secret_key
        self.inv_path = inv_path
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        if self.access_method is not None:
            result['AccessMethod'] = self.access_method
        if self.access_proxy is not None:
            result['AccessProxy'] = self.access_proxy
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain
        if self.inv_access_key_id is not None:
            result['InvAccessKeyId'] = self.inv_access_key_id
        if self.inv_secret_key is not None:
            result['InvSecretKey'] = self.inv_secret_key
        if self.inv_path is not None:
            result['InvPath'] = self.inv_path
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        if m.get('AccessMethod') is not None:
            self.access_method = m.get('AccessMethod')
        if m.get('AccessProxy') is not None:
            self.access_proxy = m.get('AccessProxy')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')
        if m.get('InvAccessKeyId') is not None:
            self.inv_access_key_id = m.get('InvAccessKeyId')
        if m.get('InvSecretKey') is not None:
            self.inv_secret_key = m.get('InvSecretKey')
        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class CheckImportDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckImportDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckImportDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckImportDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckImportDataAddressExRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        direction: str = None,
    ):
        self.name = name
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.direction is not None:
            result['Direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        return self


class CheckImportDataAddressExResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckImportDataAddressExResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckImportDataAddressExResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckImportDataAddressExResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMigrationLicenseRequest(TeaModel):
    def __init__(
        self,
        license: str = None,
    ):
        self.license = license

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            self.license = m.get('License')
        return self


class CheckMigrationLicenseResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        telephone: str = None,
        message: str = None,
        local_address: str = None,
        expiration_date: int = None,
        order_create_date: int = None,
        request_id: str = None,
        contact: str = None,
        size: int = None,
        code: str = None,
        license_create_date: int = None,
        order_id: int = None,
        uid: int = None,
    ):
        self.success = success
        self.telephone = telephone
        self.message = message
        self.local_address = local_address
        self.expiration_date = expiration_date
        self.order_create_date = order_create_date
        self.request_id = request_id
        self.contact = contact
        self.size = size
        self.code = code
        self.license_create_date = license_create_date
        self.order_id = order_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.message is not None:
            result['Message'] = self.message
        if self.local_address is not None:
            result['LocalAddress'] = self.local_address
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.order_create_date is not None:
            result['OrderCreateDate'] = self.order_create_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.size is not None:
            result['Size'] = self.size
        if self.code is not None:
            result['Code'] = self.code
        if self.license_create_date is not None:
            result['LicenseCreateDate'] = self.license_create_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LocalAddress') is not None:
            self.local_address = m.get('LocalAddress')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('OrderCreateDate') is not None:
            self.order_create_date = m.get('OrderCreateDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LicenseCreateDate') is not None:
            self.license_create_date = m.get('LicenseCreateDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CheckMigrationLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckMigrationLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckMigrationLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataAddressRequest(TeaModel):
    def __init__(
        self,
        mgw_region_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        name: str = None,
        address_type: str = None,
        enable_acceleration: bool = None,
        domain: str = None,
        address: str = None,
        sub_address: str = None,
        appid: str = None,
        list_file_path: str = None,
        access_method: str = None,
        access_proxy: str = None,
        access_version: str = None,
        access_key_secret: str = None,
        access_key: str = None,
        server_encryption: str = None,
        alias_name: str = None,
        inv_domain: str = None,
        inv_access_key_id: str = None,
        inv_secret_key: str = None,
        inv_path: str = None,
    ):
        self.mgw_region_id = mgw_region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.name = name
        self.address_type = address_type
        self.enable_acceleration = enable_acceleration
        self.domain = domain
        self.address = address
        self.sub_address = sub_address
        self.appid = appid
        self.list_file_path = list_file_path
        self.access_method = access_method
        self.access_proxy = access_proxy
        self.access_version = access_version
        self.access_key_secret = access_key_secret
        self.access_key = access_key
        self.server_encryption = server_encryption
        self.alias_name = alias_name
        self.inv_domain = inv_domain
        self.inv_access_key_id = inv_access_key_id
        self.inv_secret_key = inv_secret_key
        self.inv_path = inv_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.name is not None:
            result['Name'] = self.name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.enable_acceleration is not None:
            result['EnableAcceleration'] = self.enable_acceleration
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        if self.access_method is not None:
            result['AccessMethod'] = self.access_method
        if self.access_proxy is not None:
            result['AccessProxy'] = self.access_proxy
        if self.access_version is not None:
            result['AccessVersion'] = self.access_version
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.server_encryption is not None:
            result['ServerEncryption'] = self.server_encryption
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain
        if self.inv_access_key_id is not None:
            result['InvAccessKeyId'] = self.inv_access_key_id
        if self.inv_secret_key is not None:
            result['InvSecretKey'] = self.inv_secret_key
        if self.inv_path is not None:
            result['InvPath'] = self.inv_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('EnableAcceleration') is not None:
            self.enable_acceleration = m.get('EnableAcceleration')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        if m.get('AccessMethod') is not None:
            self.access_method = m.get('AccessMethod')
        if m.get('AccessProxy') is not None:
            self.access_proxy = m.get('AccessProxy')
        if m.get('AccessVersion') is not None:
            self.access_version = m.get('AccessVersion')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('ServerEncryption') is not None:
            self.server_encryption = m.get('ServerEncryption')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')
        if m.get('InvAccessKeyId') is not None:
            self.inv_access_key_id = m.get('InvAccessKeyId')
        if m.get('InvSecretKey') is not None:
            self.inv_secret_key = m.get('InvSecretKey')
        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')
        return self


class CreateDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        total_object_num: int = None,
        total_object_size: str = None,
        expected_import_time: str = None,
        incremental_mode: bool = None,
        incremental_interval: int = None,
        incremental_repeat_count: int = None,
        net_flow_limiter: str = None,
        is_customized_instance: bool = None,
        customized_instances: str = None,
        src_address_region_id: str = None,
        src_address_type: str = None,
        src_domain: str = None,
        src_address: str = None,
        src_sub_address: str = None,
        src_access_key_id: str = None,
        src_access_key_secret: str = None,
        src_appid: str = None,
        src_list_file_path: str = None,
        dest_address_region_id: str = None,
        dest_access_key_id: str = None,
        dest_access_key_secret: str = None,
        dest_bucket: str = None,
        dest_prefix: str = None,
    ):
        self.name = name
        self.total_object_num = total_object_num
        self.total_object_size = total_object_size
        self.expected_import_time = expected_import_time
        self.incremental_mode = incremental_mode
        self.incremental_interval = incremental_interval
        self.incremental_repeat_count = incremental_repeat_count
        self.net_flow_limiter = net_flow_limiter
        self.is_customized_instance = is_customized_instance
        self.customized_instances = customized_instances
        self.src_address_region_id = src_address_region_id
        self.src_address_type = src_address_type
        self.src_domain = src_domain
        self.src_address = src_address
        self.src_sub_address = src_sub_address
        self.src_access_key_id = src_access_key_id
        self.src_access_key_secret = src_access_key_secret
        self.src_appid = src_appid
        self.src_list_file_path = src_list_file_path
        self.dest_address_region_id = dest_address_region_id
        self.dest_access_key_id = dest_access_key_id
        self.dest_access_key_secret = dest_access_key_secret
        self.dest_bucket = dest_bucket
        self.dest_prefix = dest_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.total_object_num is not None:
            result['TotalObjectNum'] = self.total_object_num
        if self.total_object_size is not None:
            result['TotalObjectSize'] = self.total_object_size
        if self.expected_import_time is not None:
            result['ExpectedImportTime'] = self.expected_import_time
        if self.incremental_mode is not None:
            result['IncrementalMode'] = self.incremental_mode
        if self.incremental_interval is not None:
            result['IncrementalInterval'] = self.incremental_interval
        if self.incremental_repeat_count is not None:
            result['IncrementalRepeatCount'] = self.incremental_repeat_count
        if self.net_flow_limiter is not None:
            result['NetFlowLimiter'] = self.net_flow_limiter
        if self.is_customized_instance is not None:
            result['IsCustomizedInstance'] = self.is_customized_instance
        if self.customized_instances is not None:
            result['CustomizedInstances'] = self.customized_instances
        if self.src_address_region_id is not None:
            result['SrcAddressRegionId'] = self.src_address_region_id
        if self.src_address_type is not None:
            result['SrcAddressType'] = self.src_address_type
        if self.src_domain is not None:
            result['SrcDomain'] = self.src_domain
        if self.src_address is not None:
            result['SrcAddress'] = self.src_address
        if self.src_sub_address is not None:
            result['SrcSubAddress'] = self.src_sub_address
        if self.src_access_key_id is not None:
            result['SrcAccessKeyId'] = self.src_access_key_id
        if self.src_access_key_secret is not None:
            result['SrcAccessKeySecret'] = self.src_access_key_secret
        if self.src_appid is not None:
            result['SrcAppid'] = self.src_appid
        if self.src_list_file_path is not None:
            result['SrcListFilePath'] = self.src_list_file_path
        if self.dest_address_region_id is not None:
            result['DestAddressRegionId'] = self.dest_address_region_id
        if self.dest_access_key_id is not None:
            result['DestAccessKeyId'] = self.dest_access_key_id
        if self.dest_access_key_secret is not None:
            result['DestAccessKeySecret'] = self.dest_access_key_secret
        if self.dest_bucket is not None:
            result['DestBucket'] = self.dest_bucket
        if self.dest_prefix is not None:
            result['DestPrefix'] = self.dest_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalObjectNum') is not None:
            self.total_object_num = m.get('TotalObjectNum')
        if m.get('TotalObjectSize') is not None:
            self.total_object_size = m.get('TotalObjectSize')
        if m.get('ExpectedImportTime') is not None:
            self.expected_import_time = m.get('ExpectedImportTime')
        if m.get('IncrementalMode') is not None:
            self.incremental_mode = m.get('IncrementalMode')
        if m.get('IncrementalInterval') is not None:
            self.incremental_interval = m.get('IncrementalInterval')
        if m.get('IncrementalRepeatCount') is not None:
            self.incremental_repeat_count = m.get('IncrementalRepeatCount')
        if m.get('NetFlowLimiter') is not None:
            self.net_flow_limiter = m.get('NetFlowLimiter')
        if m.get('IsCustomizedInstance') is not None:
            self.is_customized_instance = m.get('IsCustomizedInstance')
        if m.get('CustomizedInstances') is not None:
            self.customized_instances = m.get('CustomizedInstances')
        if m.get('SrcAddressRegionId') is not None:
            self.src_address_region_id = m.get('SrcAddressRegionId')
        if m.get('SrcAddressType') is not None:
            self.src_address_type = m.get('SrcAddressType')
        if m.get('SrcDomain') is not None:
            self.src_domain = m.get('SrcDomain')
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('SrcSubAddress') is not None:
            self.src_sub_address = m.get('SrcSubAddress')
        if m.get('SrcAccessKeyId') is not None:
            self.src_access_key_id = m.get('SrcAccessKeyId')
        if m.get('SrcAccessKeySecret') is not None:
            self.src_access_key_secret = m.get('SrcAccessKeySecret')
        if m.get('SrcAppid') is not None:
            self.src_appid = m.get('SrcAppid')
        if m.get('SrcListFilePath') is not None:
            self.src_list_file_path = m.get('SrcListFilePath')
        if m.get('DestAddressRegionId') is not None:
            self.dest_address_region_id = m.get('DestAddressRegionId')
        if m.get('DestAccessKeyId') is not None:
            self.dest_access_key_id = m.get('DestAccessKeyId')
        if m.get('DestAccessKeySecret') is not None:
            self.dest_access_key_secret = m.get('DestAccessKeySecret')
        if m.get('DestBucket') is not None:
            self.dest_bucket = m.get('DestBucket')
        if m.get('DestPrefix') is not None:
            self.dest_prefix = m.get('DestPrefix')
        return self


class CreateImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImportJobExRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        total_object_num: int = None,
        total_object_size: str = None,
        expected_import_time: str = None,
        incremental_mode: bool = None,
        incremental_interval: int = None,
        incremental_repeat_count: int = None,
        net_flow_limiter: str = None,
        is_customized_instance: bool = None,
        customized_instances: str = None,
        last_modified_time: int = None,
        alias_name: str = None,
        include_dir_or_files: str = None,
        exclude_dir_or_files: str = None,
        filter_mode: str = None,
        enable_multi_versioning: bool = None,
        coverage_rule: str = None,
        src_address: str = None,
        dest_address: str = None,
    ):
        self.name = name
        self.total_object_num = total_object_num
        self.total_object_size = total_object_size
        self.expected_import_time = expected_import_time
        self.incremental_mode = incremental_mode
        self.incremental_interval = incremental_interval
        self.incremental_repeat_count = incremental_repeat_count
        self.net_flow_limiter = net_flow_limiter
        self.is_customized_instance = is_customized_instance
        self.customized_instances = customized_instances
        self.last_modified_time = last_modified_time
        self.alias_name = alias_name
        self.include_dir_or_files = include_dir_or_files
        self.exclude_dir_or_files = exclude_dir_or_files
        self.filter_mode = filter_mode
        self.enable_multi_versioning = enable_multi_versioning
        self.coverage_rule = coverage_rule
        self.src_address = src_address
        self.dest_address = dest_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.total_object_num is not None:
            result['TotalObjectNum'] = self.total_object_num
        if self.total_object_size is not None:
            result['TotalObjectSize'] = self.total_object_size
        if self.expected_import_time is not None:
            result['ExpectedImportTime'] = self.expected_import_time
        if self.incremental_mode is not None:
            result['IncrementalMode'] = self.incremental_mode
        if self.incremental_interval is not None:
            result['IncrementalInterval'] = self.incremental_interval
        if self.incremental_repeat_count is not None:
            result['IncrementalRepeatCount'] = self.incremental_repeat_count
        if self.net_flow_limiter is not None:
            result['NetFlowLimiter'] = self.net_flow_limiter
        if self.is_customized_instance is not None:
            result['IsCustomizedInstance'] = self.is_customized_instance
        if self.customized_instances is not None:
            result['CustomizedInstances'] = self.customized_instances
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.include_dir_or_files is not None:
            result['IncludeDirOrFiles'] = self.include_dir_or_files
        if self.exclude_dir_or_files is not None:
            result['ExcludeDirOrFiles'] = self.exclude_dir_or_files
        if self.filter_mode is not None:
            result['FilterMode'] = self.filter_mode
        if self.enable_multi_versioning is not None:
            result['EnableMultiVersioning'] = self.enable_multi_versioning
        if self.coverage_rule is not None:
            result['CoverageRule'] = self.coverage_rule
        if self.src_address is not None:
            result['SrcAddress'] = self.src_address
        if self.dest_address is not None:
            result['DestAddress'] = self.dest_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalObjectNum') is not None:
            self.total_object_num = m.get('TotalObjectNum')
        if m.get('TotalObjectSize') is not None:
            self.total_object_size = m.get('TotalObjectSize')
        if m.get('ExpectedImportTime') is not None:
            self.expected_import_time = m.get('ExpectedImportTime')
        if m.get('IncrementalMode') is not None:
            self.incremental_mode = m.get('IncrementalMode')
        if m.get('IncrementalInterval') is not None:
            self.incremental_interval = m.get('IncrementalInterval')
        if m.get('IncrementalRepeatCount') is not None:
            self.incremental_repeat_count = m.get('IncrementalRepeatCount')
        if m.get('NetFlowLimiter') is not None:
            self.net_flow_limiter = m.get('NetFlowLimiter')
        if m.get('IsCustomizedInstance') is not None:
            self.is_customized_instance = m.get('IsCustomizedInstance')
        if m.get('CustomizedInstances') is not None:
            self.customized_instances = m.get('CustomizedInstances')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('IncludeDirOrFiles') is not None:
            self.include_dir_or_files = m.get('IncludeDirOrFiles')
        if m.get('ExcludeDirOrFiles') is not None:
            self.exclude_dir_or_files = m.get('ExcludeDirOrFiles')
        if m.get('FilterMode') is not None:
            self.filter_mode = m.get('FilterMode')
        if m.get('EnableMultiVersioning') is not None:
            self.enable_multi_versioning = m.get('EnableMultiVersioning')
        if m.get('CoverageRule') is not None:
            self.coverage_rule = m.get('CoverageRule')
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('DestAddress') is not None:
            self.dest_address = m.get('DestAddress')
        return self


class CreateImportJobExResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateImportJobExResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImportJobExResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImportJobExResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImportReportRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        lang: str = None,
    ):
        self.name = name
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class CreateImportReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        report_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.report_id = report_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateImportReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImportReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImportReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        src_address: str = None,
        dest_address: str = None,
        last_scan_time: int = None,
        start_date: int = None,
        interval_in_second: int = None,
        repeat_count: int = None,
        group_file_size_limiter: int = None,
        group_file_count_limiter: int = None,
        speed_time_table_limiter: str = None,
        no_new_run_if_any_running: bool = None,
        run_immediate: bool = None,
    ):
        self.name = name
        self.src_address = src_address
        self.dest_address = dest_address
        self.last_scan_time = last_scan_time
        self.start_date = start_date
        self.interval_in_second = interval_in_second
        self.repeat_count = repeat_count
        self.group_file_size_limiter = group_file_size_limiter
        self.group_file_count_limiter = group_file_count_limiter
        self.speed_time_table_limiter = speed_time_table_limiter
        self.no_new_run_if_any_running = no_new_run_if_any_running
        self.run_immediate = run_immediate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.src_address is not None:
            result['SrcAddress'] = self.src_address
        if self.dest_address is not None:
            result['DestAddress'] = self.dest_address
        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.interval_in_second is not None:
            result['IntervalInSecond'] = self.interval_in_second
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.group_file_size_limiter is not None:
            result['GroupFileSizeLimiter'] = self.group_file_size_limiter
        if self.group_file_count_limiter is not None:
            result['GroupFileCountLimiter'] = self.group_file_count_limiter
        if self.speed_time_table_limiter is not None:
            result['SpeedTimeTableLimiter'] = self.speed_time_table_limiter
        if self.no_new_run_if_any_running is not None:
            result['NoNewRunIfAnyRunning'] = self.no_new_run_if_any_running
        if self.run_immediate is not None:
            result['RunImmediate'] = self.run_immediate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('DestAddress') is not None:
            self.dest_address = m.get('DestAddress')
        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('IntervalInSecond') is not None:
            self.interval_in_second = m.get('IntervalInSecond')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('GroupFileSizeLimiter') is not None:
            self.group_file_size_limiter = m.get('GroupFileSizeLimiter')
        if m.get('GroupFileCountLimiter') is not None:
            self.group_file_count_limiter = m.get('GroupFileCountLimiter')
        if m.get('SpeedTimeTableLimiter') is not None:
            self.speed_time_table_limiter = m.get('SpeedTimeTableLimiter')
        if m.get('NoNewRunIfAnyRunning') is not None:
            self.no_new_run_if_any_running = m.get('NoNewRunIfAnyRunning')
        if m.get('RunImmediate') is not None:
            self.run_immediate = m.get('RunImmediate')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        job_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationLicenseRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
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


class CreateMigrationLicenseResponseBody(TeaModel):
    def __init__(
        self,
        license: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.license = license
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMigrationLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMigrationLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMigrationLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMoverRequest(TeaModel):
    def __init__(
        self,
        mover_region_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        scale: str = None,
    ):
        self.mover_region_id = mover_region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.scale = scale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mover_region_id is not None:
            result['MoverRegionId'] = self.mover_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.scale is not None:
            result['Scale'] = self.scale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoverRegionId') is not None:
            self.mover_region_id = m.get('MoverRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        return self


class CreateMoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        mover_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.mover_id = mover_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMoverResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        mig_size: int = None,
        src_type: str = None,
        dest_type: str = None,
        to_region: str = None,
        contact_name: str = None,
        phone_number: str = None,
        has_gigabit_switch: bool = None,
        has_ten_gigabit_switch: bool = None,
        available_switch_port_num: int = None,
        has_electrical_port: bool = None,
        has_fibre_optical_port: bool = None,
        has_3u: bool = None,
        has_computing_node: bool = None,
        has_browser: bool = None,
        total_file_count: str = None,
        average_file_size: str = None,
    ):
        self.mig_size = mig_size
        self.src_type = src_type
        self.dest_type = dest_type
        self.to_region = to_region
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.has_gigabit_switch = has_gigabit_switch
        self.has_ten_gigabit_switch = has_ten_gigabit_switch
        self.available_switch_port_num = available_switch_port_num
        self.has_electrical_port = has_electrical_port
        self.has_fibre_optical_port = has_fibre_optical_port
        self.has_3u = has_3u
        self.has_computing_node = has_computing_node
        self.has_browser = has_browser
        self.total_file_count = total_file_count
        self.average_file_size = average_file_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mig_size is not None:
            result['MigSize'] = self.mig_size
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.dest_type is not None:
            result['destType'] = self.dest_type
        if self.to_region is not None:
            result['ToRegion'] = self.to_region
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.has_gigabit_switch is not None:
            result['HasGigabitSwitch'] = self.has_gigabit_switch
        if self.has_ten_gigabit_switch is not None:
            result['HasTenGigabitSwitch'] = self.has_ten_gigabit_switch
        if self.available_switch_port_num is not None:
            result['AvailableSwitchPortNum'] = self.available_switch_port_num
        if self.has_electrical_port is not None:
            result['HasElectricalPort'] = self.has_electrical_port
        if self.has_fibre_optical_port is not None:
            result['HasFibreOpticalPort'] = self.has_fibre_optical_port
        if self.has_3u is not None:
            result['Has3U'] = self.has_3u
        if self.has_computing_node is not None:
            result['HasComputingNode'] = self.has_computing_node
        if self.has_browser is not None:
            result['HasBrowser'] = self.has_browser
        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count
        if self.average_file_size is not None:
            result['AverageFileSize'] = self.average_file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigSize') is not None:
            self.mig_size = m.get('MigSize')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('ToRegion') is not None:
            self.to_region = m.get('ToRegion')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('HasGigabitSwitch') is not None:
            self.has_gigabit_switch = m.get('HasGigabitSwitch')
        if m.get('HasTenGigabitSwitch') is not None:
            self.has_ten_gigabit_switch = m.get('HasTenGigabitSwitch')
        if m.get('AvailableSwitchPortNum') is not None:
            self.available_switch_port_num = m.get('AvailableSwitchPortNum')
        if m.get('HasElectricalPort') is not None:
            self.has_electrical_port = m.get('HasElectricalPort')
        if m.get('HasFibreOpticalPort') is not None:
            self.has_fibre_optical_port = m.get('HasFibreOpticalPort')
        if m.get('Has3U') is not None:
            self.has_3u = m.get('Has3U')
        if m.get('HasComputingNode') is not None:
            self.has_computing_node = m.get('HasComputingNode')
        if m.get('HasBrowser') is not None:
            self.has_browser = m.get('HasBrowser')
        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')
        if m.get('AverageFileSize') is not None:
            self.average_file_size = m.get('AverageFileSize')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.serial_number = serial_number
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRemoteRequest(TeaModel):
    def __init__(
        self,
        remote_name: str = None,
        region_id: str = None,
        vpc_id: str = None,
        remote_type: str = None,
        remote_host: str = None,
        path: str = None,
        mount_type: str = None,
        user_name: str = None,
        password: str = None,
        mount_point: str = None,
    ):
        self.remote_name = remote_name
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.remote_type = remote_type
        self.remote_host = remote_host
        self.path = path
        self.mount_type = mount_type
        self.user_name = user_name
        self.password = password
        self.mount_point = mount_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remote_name is not None:
            result['RemoteName'] = self.remote_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.remote_type is not None:
            result['RemoteType'] = self.remote_type
        if self.remote_host is not None:
            result['RemoteHost'] = self.remote_host
        if self.path is not None:
            result['Path'] = self.path
        if self.mount_type is not None:
            result['MountType'] = self.mount_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoteName') is not None:
            self.remote_name = m.get('RemoteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RemoteType') is not None:
            self.remote_type = m.get('RemoteType')
        if m.get('RemoteHost') is not None:
            self.remote_host = m.get('RemoteHost')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('MountType') is not None:
            self.mount_type = m.get('MountType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')
        return self


class CreateRemoteResponseBody(TeaModel):
    def __init__(
        self,
        remote_id: str = None,
        request_id: str = None,
    ):
        self.remote_id = remote_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remote_id is not None:
            result['RemoteId'] = self.remote_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRemoteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRemoteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRemoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualClusterRequest(TeaModel):
    def __init__(
        self,
        machine_id: str = None,
        master_public_ip: str = None,
        master_private_ip: str = None,
        port: str = None,
        workers_private_ip: str = None,
        alias_name: str = None,
        user_nmae: str = None,
        password: str = None,
    ):
        self.machine_id = machine_id
        self.master_public_ip = master_public_ip
        self.master_private_ip = master_private_ip
        self.port = port
        self.workers_private_ip = workers_private_ip
        self.alias_name = alias_name
        self.user_nmae = user_nmae
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.machine_id is not None:
            result['MachineId'] = self.machine_id
        if self.master_public_ip is not None:
            result['MasterPublicIp'] = self.master_public_ip
        if self.master_private_ip is not None:
            result['MasterPrivateIp'] = self.master_private_ip
        if self.port is not None:
            result['Port'] = self.port
        if self.workers_private_ip is not None:
            result['WorkersPrivateIp'] = self.workers_private_ip
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.user_nmae is not None:
            result['UserNmae'] = self.user_nmae
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineId') is not None:
            self.machine_id = m.get('MachineId')
        if m.get('MasterPublicIp') is not None:
            self.master_public_ip = m.get('MasterPublicIp')
        if m.get('MasterPrivateIp') is not None:
            self.master_private_ip = m.get('MasterPrivateIp')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('WorkersPrivateIp') is not None:
            self.workers_private_ip = m.get('WorkersPrivateIp')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('UserNmae') is not None:
            self.user_nmae = m.get('UserNmae')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class CreateVirtualClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        public_key: str = None,
        code: str = None,
        message: str = None,
        cluster_id: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.public_key = public_key
        self.code = code
        self.message = message
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateVirtualClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVirtualClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVirtualClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataAddressRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobRequest(TeaModel):
    def __init__(
        self,
        job_name: str = None,
    ):
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMoverRequest(TeaModel):
    def __init__(
        self,
        mover_id: str = None,
    ):
        self.mover_id = mover_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        return self


class DeleteMoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMoverResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBucketFoldersRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_key_secret: str = None,
        domain: str = None,
        bucket: str = None,
        prefix: str = None,
    ):
        self.access_key = access_key
        self.access_key_secret = access_key_secret
        self.domain = domain
        self.bucket = bucket
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class DescribeBucketFoldersResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[str] = None,
    ):
        self.folder = folder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['folder'] = self.folder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folder') is not None:
            self.folder = m.get('folder')
        return self


class DescribeBucketFoldersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        folders: DescribeBucketFoldersResponseBodyFolders = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.folders = folders

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Folders') is not None:
            temp_model = DescribeBucketFoldersResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        return self


class DescribeBucketFoldersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBucketFoldersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBucketFoldersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBucketsRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_key_secret: str = None,
        domain: str = None,
    ):
        self.access_key = access_key
        self.access_key_secret = access_key_secret
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeBucketsResponseBodyBuckets(TeaModel):
    def __init__(
        self,
        bucket: List[str] = None,
    ):
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        return self


class DescribeBucketsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        buckets: DescribeBucketsResponseBodyBuckets = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.buckets = buckets

    def validate(self):
        if self.buckets:
            self.buckets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.buckets is not None:
            result['Buckets'] = self.buckets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Buckets') is not None:
            temp_model = DescribeBucketsResponseBodyBuckets()
            self.buckets = temp_model.from_map(m['Buckets'])
        return self


class DescribeBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBucketsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataAddressesRequest(TeaModel):
    def __init__(
        self,
        mgw_region_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        address_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.mgw_region_id = mgw_region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.address_type = address_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDataAddressesResponseBodyAddressesAddress(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        private_ip: str = None,
        address_type: str = None,
        ali_address: bool = None,
        access_method: str = None,
        mgw_region_id: str = None,
        address: str = None,
        sub_address: str = None,
        access_key_secret: str = None,
        access_proxy: str = None,
        server_encryption: str = None,
        name: str = None,
        created_time: int = None,
        list_file_path: str = None,
        domain: str = None,
        notes: str = None,
        ali_uid: int = None,
        enable_acceleration: bool = None,
        appid: str = None,
        access_version: str = None,
        access_key_id: str = None,
        v_switch_id: str = None,
        elastic_ip: str = None,
        updated_time: int = None,
        country: str = None,
        alias_name: str = None,
        detailed_status: str = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.private_ip = private_ip
        self.address_type = address_type
        self.ali_address = ali_address
        self.access_method = access_method
        self.mgw_region_id = mgw_region_id
        self.address = address
        self.sub_address = sub_address
        self.access_key_secret = access_key_secret
        self.access_proxy = access_proxy
        self.server_encryption = server_encryption
        self.name = name
        self.created_time = created_time
        self.list_file_path = list_file_path
        self.domain = domain
        self.notes = notes
        self.ali_uid = ali_uid
        self.enable_acceleration = enable_acceleration
        self.appid = appid
        self.access_version = access_version
        self.access_key_id = access_key_id
        self.v_switch_id = v_switch_id
        self.elastic_ip = elastic_ip
        self.updated_time = updated_time
        self.country = country
        self.alias_name = alias_name
        self.detailed_status = detailed_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.ali_address is not None:
            result['AliAddress'] = self.ali_address
        if self.access_method is not None:
            result['AccessMethod'] = self.access_method
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_proxy is not None:
            result['AccessProxy'] = self.access_proxy
        if self.server_encryption is not None:
            result['ServerEncryption'] = self.server_encryption
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.enable_acceleration is not None:
            result['EnableAcceleration'] = self.enable_acceleration
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.access_version is not None:
            result['AccessVersion'] = self.access_version
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.elastic_ip is not None:
            result['ElasticIp'] = self.elastic_ip
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.country is not None:
            result['Country'] = self.country
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('AliAddress') is not None:
            self.ali_address = m.get('AliAddress')
        if m.get('AccessMethod') is not None:
            self.access_method = m.get('AccessMethod')
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessProxy') is not None:
            self.access_proxy = m.get('AccessProxy')
        if m.get('ServerEncryption') is not None:
            self.server_encryption = m.get('ServerEncryption')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EnableAcceleration') is not None:
            self.enable_acceleration = m.get('EnableAcceleration')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('AccessVersion') is not None:
            self.access_version = m.get('AccessVersion')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ElasticIp') is not None:
            self.elastic_ip = m.get('ElasticIp')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('DetailedStatus') is not None:
            self.detailed_status = m.get('DetailedStatus')
        return self


class DescribeDataAddressesResponseBodyAddresses(TeaModel):
    def __init__(
        self,
        address: List[DescribeDataAddressesResponseBodyAddressesAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Address'] = []
        if self.address is not None:
            for k in self.address:
                result['Address'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k in m.get('Address'):
                temp_model = DescribeDataAddressesResponseBodyAddressesAddress()
                self.address.append(temp_model.from_map(k))
        return self


class DescribeDataAddressesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        addresses: DescribeDataAddressesResponseBodyAddresses = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.addresses = addresses

    def validate(self):
        if self.addresses:
            self.addresses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.addresses is not None:
            result['Addresses'] = self.addresses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Addresses') is not None:
            temp_model = DescribeDataAddressesResponseBodyAddresses()
            self.addresses = temp_model.from_map(m['Addresses'])
        return self


class DescribeDataAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataAddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportJobsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeImportJobsResponseBodyJobsJob(TeaModel):
    def __init__(
        self,
        status: str = None,
        finish_time: int = None,
        progress: float = None,
        cid: str = None,
        src_type: str = None,
        ali_uid: int = None,
        src_address: str = None,
        src_sub_address: str = None,
        job_id: str = None,
        job_region_id: str = None,
        name: str = None,
        dest_bucket: str = None,
        created_time: int = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.progress = progress
        self.cid = cid
        self.src_type = src_type
        self.ali_uid = ali_uid
        self.src_address = src_address
        self.src_sub_address = src_sub_address
        self.job_id = job_id
        self.job_region_id = job_region_id
        self.name = name
        self.dest_bucket = dest_bucket
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.src_address is not None:
            result['SrcAddress'] = self.src_address
        if self.src_sub_address is not None:
            result['SrcSubAddress'] = self.src_sub_address
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_region_id is not None:
            result['JobRegionId'] = self.job_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.dest_bucket is not None:
            result['DestBucket'] = self.dest_bucket
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('SrcSubAddress') is not None:
            self.src_sub_address = m.get('SrcSubAddress')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobRegionId') is not None:
            self.job_region_id = m.get('JobRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DestBucket') is not None:
            self.dest_bucket = m.get('DestBucket')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeImportJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        job: List[DescribeImportJobsResponseBodyJobsJob] = None,
    ):
        self.job = job

    def validate(self):
        if self.job:
            for k in self.job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Job'] = []
        if self.job is not None:
            for k in self.job:
                result['Job'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job = []
        if m.get('Job') is not None:
            for k in m.get('Job'):
                temp_model = DescribeImportJobsResponseBodyJobsJob()
                self.job.append(temp_model.from_map(k))
        return self


class DescribeImportJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        jobs: DescribeImportJobsResponseBodyJobs = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Jobs') is not None:
            temp_model = DescribeImportJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        return self


class DescribeImportJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImportJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImportJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportReportRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeImportReportResponseBodyReportsReport(TeaModel):
    def __init__(
        self,
        status: str = None,
        failed_file_list_path: str = None,
        import_file_list_path: str = None,
        description: str = None,
        completed_file_list_path: str = None,
        report_id: str = None,
        created_time: int = None,
    ):
        self.status = status
        self.failed_file_list_path = failed_file_list_path
        self.import_file_list_path = import_file_list_path
        self.description = description
        self.completed_file_list_path = completed_file_list_path
        self.report_id = report_id
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.failed_file_list_path is not None:
            result['FailedFileListPath'] = self.failed_file_list_path
        if self.import_file_list_path is not None:
            result['ImportFileListPath'] = self.import_file_list_path
        if self.description is not None:
            result['Description'] = self.description
        if self.completed_file_list_path is not None:
            result['CompletedFileListPath'] = self.completed_file_list_path
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FailedFileListPath') is not None:
            self.failed_file_list_path = m.get('FailedFileListPath')
        if m.get('ImportFileListPath') is not None:
            self.import_file_list_path = m.get('ImportFileListPath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CompletedFileListPath') is not None:
            self.completed_file_list_path = m.get('CompletedFileListPath')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeImportReportResponseBodyReports(TeaModel):
    def __init__(
        self,
        report: List[DescribeImportReportResponseBodyReportsReport] = None,
    ):
        self.report = report

    def validate(self):
        if self.report:
            for k in self.report:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Report'] = []
        if self.report is not None:
            for k in self.report:
                result['Report'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report = []
        if m.get('Report') is not None:
            for k in m.get('Report'):
                temp_model = DescribeImportReportResponseBodyReportsReport()
                self.report.append(temp_model.from_map(k))
        return self


class DescribeImportReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        reports: DescribeImportReportResponseBodyReports = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.reports = reports

    def validate(self):
        if self.reports:
            self.reports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.reports is not None:
            result['Reports'] = self.reports.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Reports') is not None:
            temp_model = DescribeImportReportResponseBodyReports()
            self.reports = temp_model.from_map(m['Reports'])
        return self


class DescribeImportReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImportReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImportReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobsRequest(TeaModel):
    def __init__(
        self,
        mgw_region_id: str = None,
        job_name: str = None,
        job_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.mgw_region_id = mgw_region_id
        self.job_name = job_name
        self.job_type = job_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeJobsResponseBodyJobsJob(TeaModel):
    def __init__(
        self,
        status: str = None,
        dest_address_name: str = None,
        mover_id: str = None,
        group_file_count_limiter: int = None,
        cid: str = None,
        job_type: str = None,
        src_address_name: str = None,
        last_modified_time: int = None,
        interval_in_second: int = None,
        group_file_size_limiter: int = None,
        speed_time_table_limiter: str = None,
        incremental_mode: bool = None,
        job_name: str = None,
        repeat_count: int = None,
        created_time: int = None,
        progress: float = None,
        archive: bool = None,
        ali_uid: int = None,
        start_date: int = None,
        region_id: str = None,
        last_scan_time: int = None,
        updated_time: int = None,
        job_id: str = None,
        no_new_run_if_any_running: bool = None,
        detailed_status: str = None,
        run_immediate: bool = None,
    ):
        self.status = status
        self.dest_address_name = dest_address_name
        self.mover_id = mover_id
        self.group_file_count_limiter = group_file_count_limiter
        self.cid = cid
        self.job_type = job_type
        self.src_address_name = src_address_name
        self.last_modified_time = last_modified_time
        self.interval_in_second = interval_in_second
        self.group_file_size_limiter = group_file_size_limiter
        self.speed_time_table_limiter = speed_time_table_limiter
        self.incremental_mode = incremental_mode
        self.job_name = job_name
        self.repeat_count = repeat_count
        self.created_time = created_time
        self.progress = progress
        self.archive = archive
        self.ali_uid = ali_uid
        self.start_date = start_date
        self.region_id = region_id
        self.last_scan_time = last_scan_time
        self.updated_time = updated_time
        self.job_id = job_id
        self.no_new_run_if_any_running = no_new_run_if_any_running
        self.detailed_status = detailed_status
        self.run_immediate = run_immediate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dest_address_name is not None:
            result['DestAddressName'] = self.dest_address_name
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        if self.group_file_count_limiter is not None:
            result['GroupFileCountLimiter'] = self.group_file_count_limiter
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.src_address_name is not None:
            result['SrcAddressName'] = self.src_address_name
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.interval_in_second is not None:
            result['IntervalInSecond'] = self.interval_in_second
        if self.group_file_size_limiter is not None:
            result['GroupFileSizeLimiter'] = self.group_file_size_limiter
        if self.speed_time_table_limiter is not None:
            result['SpeedTimeTableLimiter'] = self.speed_time_table_limiter
        if self.incremental_mode is not None:
            result['IncrementalMode'] = self.incremental_mode
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.no_new_run_if_any_running is not None:
            result['NoNewRunIfAnyRunning'] = self.no_new_run_if_any_running
        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status
        if self.run_immediate is not None:
            result['RunImmediate'] = self.run_immediate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DestAddressName') is not None:
            self.dest_address_name = m.get('DestAddressName')
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        if m.get('GroupFileCountLimiter') is not None:
            self.group_file_count_limiter = m.get('GroupFileCountLimiter')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('SrcAddressName') is not None:
            self.src_address_name = m.get('SrcAddressName')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('IntervalInSecond') is not None:
            self.interval_in_second = m.get('IntervalInSecond')
        if m.get('GroupFileSizeLimiter') is not None:
            self.group_file_size_limiter = m.get('GroupFileSizeLimiter')
        if m.get('SpeedTimeTableLimiter') is not None:
            self.speed_time_table_limiter = m.get('SpeedTimeTableLimiter')
        if m.get('IncrementalMode') is not None:
            self.incremental_mode = m.get('IncrementalMode')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NoNewRunIfAnyRunning') is not None:
            self.no_new_run_if_any_running = m.get('NoNewRunIfAnyRunning')
        if m.get('DetailedStatus') is not None:
            self.detailed_status = m.get('DetailedStatus')
        if m.get('RunImmediate') is not None:
            self.run_immediate = m.get('RunImmediate')
        return self


class DescribeJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        job: List[DescribeJobsResponseBodyJobsJob] = None,
    ):
        self.job = job

    def validate(self):
        if self.job:
            for k in self.job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Job'] = []
        if self.job is not None:
            for k in self.job:
                result['Job'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job = []
        if m.get('Job') is not None:
            for k in m.get('Job'):
                temp_model = DescribeJobsResponseBodyJobsJob()
                self.job.append(temp_model.from_map(k))
        return self


class DescribeJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        jobs: DescribeJobsResponseBodyJobs = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Jobs') is not None:
            temp_model = DescribeJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        return self


class DescribeJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationOrdersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMigrationOrdersResponseBodyOrdersOrder(TeaModel):
    def __init__(
        self,
        status: str = None,
        has_host: bool = None,
        telephone: str = None,
        cloud_storage_region: str = None,
        source_type: str = None,
        rent_order_id: str = None,
        switch_port_type: str = None,
        switch_capacity: str = None,
        aliyun_order_id: str = None,
        switch_port: int = None,
        created_time: int = None,
        rent_day: int = None,
        start_date: str = None,
        aliyun_instance_id: str = None,
        local_address: str = None,
        cloud_storage_type: str = None,
        p_2p_size: int = None,
        updated_time: int = None,
        contact: str = None,
        size: int = None,
        device_spec: str = None,
        dest_type: str = None,
        sale_mode: str = None,
        bracket: str = None,
        aliyun_uid: int = None,
    ):
        self.status = status
        self.has_host = has_host
        self.telephone = telephone
        self.cloud_storage_region = cloud_storage_region
        self.source_type = source_type
        self.rent_order_id = rent_order_id
        self.switch_port_type = switch_port_type
        self.switch_capacity = switch_capacity
        self.aliyun_order_id = aliyun_order_id
        self.switch_port = switch_port
        self.created_time = created_time
        self.rent_day = rent_day
        self.start_date = start_date
        self.aliyun_instance_id = aliyun_instance_id
        self.local_address = local_address
        self.cloud_storage_type = cloud_storage_type
        self.p_2p_size = p_2p_size
        self.updated_time = updated_time
        self.contact = contact
        self.size = size
        self.device_spec = device_spec
        self.dest_type = dest_type
        self.sale_mode = sale_mode
        self.bracket = bracket
        self.aliyun_uid = aliyun_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.has_host is not None:
            result['HasHost'] = self.has_host
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.cloud_storage_region is not None:
            result['CloudStorageRegion'] = self.cloud_storage_region
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.rent_order_id is not None:
            result['RentOrderId'] = self.rent_order_id
        if self.switch_port_type is not None:
            result['SwitchPortType'] = self.switch_port_type
        if self.switch_capacity is not None:
            result['SwitchCapacity'] = self.switch_capacity
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.switch_port is not None:
            result['SwitchPort'] = self.switch_port
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.rent_day is not None:
            result['RentDay'] = self.rent_day
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.aliyun_instance_id is not None:
            result['AliyunInstanceId'] = self.aliyun_instance_id
        if self.local_address is not None:
            result['LocalAddress'] = self.local_address
        if self.cloud_storage_type is not None:
            result['CloudStorageType'] = self.cloud_storage_type
        if self.p_2p_size is not None:
            result['P2pSize'] = self.p_2p_size
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.size is not None:
            result['Size'] = self.size
        if self.device_spec is not None:
            result['DeviceSpec'] = self.device_spec
        if self.dest_type is not None:
            result['DestType'] = self.dest_type
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.bracket is not None:
            result['Bracket'] = self.bracket
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HasHost') is not None:
            self.has_host = m.get('HasHost')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('CloudStorageRegion') is not None:
            self.cloud_storage_region = m.get('CloudStorageRegion')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('RentOrderId') is not None:
            self.rent_order_id = m.get('RentOrderId')
        if m.get('SwitchPortType') is not None:
            self.switch_port_type = m.get('SwitchPortType')
        if m.get('SwitchCapacity') is not None:
            self.switch_capacity = m.get('SwitchCapacity')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('SwitchPort') is not None:
            self.switch_port = m.get('SwitchPort')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RentDay') is not None:
            self.rent_day = m.get('RentDay')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('AliyunInstanceId') is not None:
            self.aliyun_instance_id = m.get('AliyunInstanceId')
        if m.get('LocalAddress') is not None:
            self.local_address = m.get('LocalAddress')
        if m.get('CloudStorageType') is not None:
            self.cloud_storage_type = m.get('CloudStorageType')
        if m.get('P2pSize') is not None:
            self.p_2p_size = m.get('P2pSize')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DeviceSpec') is not None:
            self.device_spec = m.get('DeviceSpec')
        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('Bracket') is not None:
            self.bracket = m.get('Bracket')
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        return self


class DescribeMigrationOrdersResponseBodyOrders(TeaModel):
    def __init__(
        self,
        order: List[DescribeMigrationOrdersResponseBodyOrdersOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = DescribeMigrationOrdersResponseBodyOrdersOrder()
                self.order.append(temp_model.from_map(k))
        return self


class DescribeMigrationOrdersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        orders: DescribeMigrationOrdersResponseBodyOrders = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.orders = orders

    def validate(self):
        if self.orders:
            self.orders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.orders is not None:
            result['Orders'] = self.orders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Orders') is not None:
            temp_model = DescribeMigrationOrdersResponseBodyOrders()
            self.orders = temp_model.from_map(m['Orders'])
        return self


class DescribeMigrationOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMigrationOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMoverAttributeRequest(TeaModel):
    def __init__(
        self,
        mover_id: str = None,
    ):
        self.mover_id = mover_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        return self


class DescribeMoverAttributeResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        vpc_id: str = None,
        private_ip: str = None,
        mover_id: str = None,
        success: bool = None,
        ali_uid: int = None,
        message: str = None,
        service_status: str = None,
        ecs_instance_id: str = None,
        region_id: str = None,
        password: str = None,
        v_switch_id: str = None,
        scale: str = None,
        request_id: str = None,
        elastic_ip: str = None,
        updated_time: int = None,
        public_ip: str = None,
        code: str = None,
        note: str = None,
        created_time: int = None,
    ):
        self.status = status
        self.vpc_id = vpc_id
        self.private_ip = private_ip
        self.mover_id = mover_id
        self.success = success
        self.ali_uid = ali_uid
        self.message = message
        self.service_status = service_status
        self.ecs_instance_id = ecs_instance_id
        self.region_id = region_id
        self.password = password
        self.v_switch_id = v_switch_id
        self.scale = scale
        self.request_id = request_id
        self.elastic_ip = elastic_ip
        self.updated_time = updated_time
        self.public_ip = public_ip
        self.code = code
        self.note = note
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        if self.success is not None:
            result['Success'] = self.success
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.message is not None:
            result['Message'] = self.message
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.password is not None:
            result['Password'] = self.password
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_ip is not None:
            result['ElasticIp'] = self.elastic_ip
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.code is not None:
            result['Code'] = self.code
        if self.note is not None:
            result['Note'] = self.note
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticIp') is not None:
            self.elastic_ip = m.get('ElasticIp')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeMoverAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMoverAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMoverAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMoversRequest(TeaModel):
    def __init__(
        self,
        mover_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.mover_region_id = mover_region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mover_region_id is not None:
            result['MoverRegionId'] = self.mover_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoverRegionId') is not None:
            self.mover_region_id = m.get('MoverRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMoversResponseBodyMoversGateway(TeaModel):
    def __init__(
        self,
        mover_region_id: str = None,
        vpc_id: str = None,
        status: str = None,
        private_ip: str = None,
        mover_id: str = None,
        ali_uid: int = None,
        ecs_instance_id: str = None,
        service_status: str = None,
        v_switch_id: str = None,
        scale: str = None,
        elastic_ip: str = None,
        updated_time: int = None,
        public_ip: str = None,
        note: str = None,
        created_time: int = None,
    ):
        self.mover_region_id = mover_region_id
        self.vpc_id = vpc_id
        self.status = status
        self.private_ip = private_ip
        self.mover_id = mover_id
        self.ali_uid = ali_uid
        self.ecs_instance_id = ecs_instance_id
        self.service_status = service_status
        self.v_switch_id = v_switch_id
        self.scale = scale
        self.elastic_ip = elastic_ip
        self.updated_time = updated_time
        self.public_ip = public_ip
        self.note = note
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mover_region_id is not None:
            result['MoverRegionId'] = self.mover_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.elastic_ip is not None:
            result['ElasticIp'] = self.elastic_ip
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.note is not None:
            result['Note'] = self.note
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoverRegionId') is not None:
            self.mover_region_id = m.get('MoverRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('ElasticIp') is not None:
            self.elastic_ip = m.get('ElasticIp')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeMoversResponseBodyMovers(TeaModel):
    def __init__(
        self,
        gateway: List[DescribeMoversResponseBodyMoversGateway] = None,
    ):
        self.gateway = gateway

    def validate(self):
        if self.gateway:
            for k in self.gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateway'] = []
        if self.gateway is not None:
            for k in self.gateway:
                result['Gateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway = []
        if m.get('Gateway') is not None:
            for k in m.get('Gateway'):
                temp_model = DescribeMoversResponseBodyMoversGateway()
                self.gateway.append(temp_model.from_map(k))
        return self


class DescribeMoversResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        movers: DescribeMoversResponseBodyMovers = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.movers = movers

    def validate(self):
        if self.movers:
            self.movers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.movers is not None:
            result['Movers'] = self.movers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Movers') is not None:
            temp_model = DescribeMoversResponseBodyMovers()
            self.movers = temp_model.from_map(m['Movers'])
        return self


class DescribeMoversResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMoversResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMoversResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfflineClusterRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
    ):
        self.alias = alias

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class DescribeOfflineClusterResponseBodyVClustersVCluster(TeaModel):
    def __init__(
        self,
        vpc: str = None,
        v_switch: str = None,
        alias: str = None,
    ):
        self.vpc = vpc
        self.v_switch = v_switch
        self.alias = alias

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.v_switch is not None:
            result['VSwitch'] = self.v_switch
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('VSwitch') is not None:
            self.v_switch = m.get('VSwitch')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class DescribeOfflineClusterResponseBodyVClusters(TeaModel):
    def __init__(
        self,
        vcluster: List[DescribeOfflineClusterResponseBodyVClustersVCluster] = None,
    ):
        self.vcluster = vcluster

    def validate(self):
        if self.vcluster:
            for k in self.vcluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VCluster'] = []
        if self.vcluster is not None:
            for k in self.vcluster:
                result['VCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vcluster = []
        if m.get('VCluster') is not None:
            for k in m.get('VCluster'):
                temp_model = DescribeOfflineClusterResponseBodyVClustersVCluster()
                self.vcluster.append(temp_model.from_map(k))
        return self


class DescribeOfflineClusterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        offline: bool = None,
        success: bool = None,
        vclusters: DescribeOfflineClusterResponseBodyVClusters = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.offline = offline
        self.success = success
        self.vclusters = vclusters

    def validate(self):
        if self.vclusters:
            self.vclusters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.offline is not None:
            result['Offline'] = self.offline
        if self.success is not None:
            result['Success'] = self.success
        if self.vclusters is not None:
            result['VClusters'] = self.vclusters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Offline') is not None:
            self.offline = m.get('Offline')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VClusters') is not None:
            temp_model = DescribeOfflineClusterResponseBodyVClusters()
            self.vclusters = temp_model.from_map(m['VClusters'])
        return self


class DescribeOfflineClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOfflineClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOfflineClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRemotesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRemotesResponseBodyMoversGateway(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        remote_host: str = None,
        mount_point: str = None,
        mover_id: str = None,
        mount_type: str = None,
        remote_name: str = None,
        ali_uid: int = None,
        region_id: str = None,
        remote_type: str = None,
        password: str = None,
        updated_time: int = None,
        path: str = None,
        created_time: int = None,
    ):
        self.vpc_id = vpc_id
        self.remote_host = remote_host
        self.mount_point = mount_point
        self.mover_id = mover_id
        self.mount_type = mount_type
        self.remote_name = remote_name
        self.ali_uid = ali_uid
        self.region_id = region_id
        self.remote_type = remote_type
        self.password = password
        self.updated_time = updated_time
        self.path = path
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.remote_host is not None:
            result['RemoteHost'] = self.remote_host
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point
        if self.mover_id is not None:
            result['MoverId'] = self.mover_id
        if self.mount_type is not None:
            result['mountType'] = self.mount_type
        if self.remote_name is not None:
            result['RemoteName'] = self.remote_name
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remote_type is not None:
            result['RemoteType'] = self.remote_type
        if self.password is not None:
            result['Password'] = self.password
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.path is not None:
            result['Path'] = self.path
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RemoteHost') is not None:
            self.remote_host = m.get('RemoteHost')
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')
        if m.get('MoverId') is not None:
            self.mover_id = m.get('MoverId')
        if m.get('mountType') is not None:
            self.mount_type = m.get('mountType')
        if m.get('RemoteName') is not None:
            self.remote_name = m.get('RemoteName')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoteType') is not None:
            self.remote_type = m.get('RemoteType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeRemotesResponseBodyMovers(TeaModel):
    def __init__(
        self,
        gateway: List[DescribeRemotesResponseBodyMoversGateway] = None,
    ):
        self.gateway = gateway

    def validate(self):
        if self.gateway:
            for k in self.gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateway'] = []
        if self.gateway is not None:
            for k in self.gateway:
                result['Gateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway = []
        if m.get('Gateway') is not None:
            for k in m.get('Gateway'):
                temp_model = DescribeRemotesResponseBodyMoversGateway()
                self.gateway.append(temp_model.from_map(k))
        return self


class DescribeRemotesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        movers: DescribeRemotesResponseBodyMovers = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.movers = movers

    def validate(self):
        if self.movers:
            self.movers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.movers is not None:
            result['Movers'] = self.movers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Movers') is not None:
            temp_model = DescribeRemotesResponseBodyMovers()
            self.movers = temp_model.from_map(m['Movers'])
        return self


class DescribeRemotesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRemotesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRemotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBusinessStatusResponseBody(TeaModel):
    def __init__(
        self,
        in_debt_status: str = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        business_status: str = None,
        risk_control_status: str = None,
    ):
        self.in_debt_status = in_debt_status
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.business_status = business_status
        self.risk_control_status = risk_control_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_debt_status is not None:
            result['InDebtStatus'] = self.in_debt_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.risk_control_status is not None:
            result['RiskControlStatus'] = self.risk_control_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InDebtStatus') is not None:
            self.in_debt_status = m.get('InDebtStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('RiskControlStatus') is not None:
            self.risk_control_status = m.get('RiskControlStatus')
        return self


class DescribeUserBusinessStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserBusinessStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserBusinessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserOptionsResponseBodyOptions(TeaModel):
    def __init__(
        self,
        option: List[str] = None,
    ):
        self.option = option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option is not None:
            result['Option'] = self.option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            self.option = m.get('Option')
        return self


class DescribeUserOptionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        options: DescribeUserOptionsResponseBodyOptions = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.options is not None:
            result['Options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Options') is not None:
            temp_model = DescribeUserOptionsResponseBodyOptions()
            self.options = temp_model.from_map(m['Options'])
        return self


class DescribeUserOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserOptionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataAddressRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        private_ip: str = None,
        message: str = None,
        address_type: str = None,
        access_method: str = None,
        mgw_region_id: str = None,
        request_id: str = None,
        code: str = None,
        address: str = None,
        sub_address: str = None,
        access_key_secret: str = None,
        access_proxy: str = None,
        server_encryption: str = None,
        name: str = None,
        created_time: int = None,
        list_file_path: str = None,
        domain: str = None,
        success: bool = None,
        notes: str = None,
        ali_uid: int = None,
        appid: str = None,
        access_key_id: str = None,
        v_switch_id: str = None,
        elastic_ip: str = None,
        updated_time: int = None,
        detailed_status: str = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.private_ip = private_ip
        self.message = message
        self.address_type = address_type
        self.access_method = access_method
        self.mgw_region_id = mgw_region_id
        self.request_id = request_id
        self.code = code
        self.address = address
        self.sub_address = sub_address
        self.access_key_secret = access_key_secret
        self.access_proxy = access_proxy
        self.server_encryption = server_encryption
        self.name = name
        self.created_time = created_time
        self.list_file_path = list_file_path
        self.domain = domain
        self.success = success
        self.notes = notes
        self.ali_uid = ali_uid
        self.appid = appid
        self.access_key_id = access_key_id
        self.v_switch_id = v_switch_id
        self.elastic_ip = elastic_ip
        self.updated_time = updated_time
        self.detailed_status = detailed_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.message is not None:
            result['Message'] = self.message
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.access_method is not None:
            result['AccessMethod'] = self.access_method
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_proxy is not None:
            result['AccessProxy'] = self.access_proxy
        if self.server_encryption is not None:
            result['ServerEncryption'] = self.server_encryption
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.success is not None:
            result['Success'] = self.success
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.elastic_ip is not None:
            result['ElasticIp'] = self.elastic_ip
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('AccessMethod') is not None:
            self.access_method = m.get('AccessMethod')
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessProxy') is not None:
            self.access_proxy = m.get('AccessProxy')
        if m.get('ServerEncryption') is not None:
            self.server_encryption = m.get('ServerEncryption')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ElasticIp') is not None:
            self.elastic_ip = m.get('ElasticIp')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('DetailedStatus') is not None:
            self.detailed_status = m.get('DetailedStatus')
        return self


class GetDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportJobDetailedStatusRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        last_minutes: int = None,
    ):
        self.name = name
        self.last_minutes = last_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.last_minutes is not None:
            result['LastMinutes'] = self.last_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LastMinutes') is not None:
            self.last_minutes = m.get('LastMinutes')
        return self


class GetImportJobDetailedStatusResponseBodyJobSource(TeaModel):
    def __init__(
        self,
        status: str = None,
        domain: str = None,
        notes: str = None,
        address_type: str = None,
        appid: str = None,
        access_key_id: str = None,
        address: str = None,
        sub_address: str = None,
        detailed_status: str = None,
        name: str = None,
        created_time: int = None,
        list_file_path: str = None,
    ):
        self.status = status
        self.domain = domain
        self.notes = notes
        self.address_type = address_type
        self.appid = appid
        self.access_key_id = access_key_id
        self.address = address
        self.sub_address = sub_address
        self.detailed_status = detailed_status
        self.name = name
        self.created_time = created_time
        self.list_file_path = list_file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('DetailedStatus') is not None:
            self.detailed_status = m.get('DetailedStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        return self


class GetImportJobDetailedStatusResponseBodyJobDestination(TeaModel):
    def __init__(
        self,
        status: str = None,
        domain: str = None,
        notes: str = None,
        address_type: str = None,
        appid: str = None,
        access_key_id: str = None,
        address: str = None,
        sub_address: str = None,
        detailed_status: str = None,
        name: str = None,
        created_time: int = None,
        list_file_path: str = None,
    ):
        self.status = status
        self.domain = domain
        self.notes = notes
        self.address_type = address_type
        self.appid = appid
        self.access_key_id = access_key_id
        self.address = address
        self.sub_address = sub_address
        self.detailed_status = detailed_status
        self.name = name
        self.created_time = created_time
        self.list_file_path = list_file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.detailed_status is not None:
            result['DetailedStatus'] = self.detailed_status
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('DetailedStatus') is not None:
            self.detailed_status = m.get('DetailedStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        return self


class GetImportJobDetailedStatusResponseBodyJobSchedule(TeaModel):
    def __init__(
        self,
        finished_repeat_count: int = None,
        incremental_mode: bool = None,
        incremental_repeat_count: int = None,
        incremental_interval: int = None,
        run_immediate: bool = None,
    ):
        self.finished_repeat_count = finished_repeat_count
        self.incremental_mode = incremental_mode
        self.incremental_repeat_count = incremental_repeat_count
        self.incremental_interval = incremental_interval
        self.run_immediate = run_immediate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_repeat_count is not None:
            result['FinishedRepeatCount'] = self.finished_repeat_count
        if self.incremental_mode is not None:
            result['IncrementalMode'] = self.incremental_mode
        if self.incremental_repeat_count is not None:
            result['IncrementalRepeatCount'] = self.incremental_repeat_count
        if self.incremental_interval is not None:
            result['IncrementalInterval'] = self.incremental_interval
        if self.run_immediate is not None:
            result['RunImmediate'] = self.run_immediate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedRepeatCount') is not None:
            self.finished_repeat_count = m.get('FinishedRepeatCount')
        if m.get('IncrementalMode') is not None:
            self.incremental_mode = m.get('IncrementalMode')
        if m.get('IncrementalRepeatCount') is not None:
            self.incremental_repeat_count = m.get('IncrementalRepeatCount')
        if m.get('IncrementalInterval') is not None:
            self.incremental_interval = m.get('IncrementalInterval')
        if m.get('RunImmediate') is not None:
            self.run_immediate = m.get('RunImmediate')
        return self


class GetImportJobDetailedStatusResponseBodyJob(TeaModel):
    def __init__(
        self,
        status: str = None,
        enable_multi_versioning: bool = None,
        is_skip_exist_file: str = None,
        archive: bool = None,
        name: str = None,
        net_flow_limiter: str = None,
        exclude_list: List[str] = None,
        include_list: List[str] = None,
        source: GetImportJobDetailedStatusResponseBodyJobSource = None,
        destination: GetImportJobDetailedStatusResponseBodyJobDestination = None,
        schedule: GetImportJobDetailedStatusResponseBodyJobSchedule = None,
    ):
        self.status = status
        self.enable_multi_versioning = enable_multi_versioning
        self.is_skip_exist_file = is_skip_exist_file
        self.archive = archive
        self.name = name
        self.net_flow_limiter = net_flow_limiter
        self.exclude_list = exclude_list
        self.include_list = include_list
        self.source = source
        self.destination = destination
        self.schedule = schedule

    def validate(self):
        if self.source:
            self.source.validate()
        if self.destination:
            self.destination.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.enable_multi_versioning is not None:
            result['EnableMultiVersioning'] = self.enable_multi_versioning
        if self.is_skip_exist_file is not None:
            result['IsSkipExistFile'] = self.is_skip_exist_file
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.name is not None:
            result['Name'] = self.name
        if self.net_flow_limiter is not None:
            result['NetFlowLimiter'] = self.net_flow_limiter
        if self.exclude_list is not None:
            result['ExcludeList'] = self.exclude_list
        if self.include_list is not None:
            result['IncludeList'] = self.include_list
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EnableMultiVersioning') is not None:
            self.enable_multi_versioning = m.get('EnableMultiVersioning')
        if m.get('IsSkipExistFile') is not None:
            self.is_skip_exist_file = m.get('IsSkipExistFile')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetFlowLimiter') is not None:
            self.net_flow_limiter = m.get('NetFlowLimiter')
        if m.get('ExcludeList') is not None:
            self.exclude_list = m.get('ExcludeList')
        if m.get('IncludeList') is not None:
            self.include_list = m.get('IncludeList')
        if m.get('Source') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyJobSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Destination') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyJobDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Schedule') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyJobSchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        return self


class GetImportJobDetailedStatusResponseBodyStorageProgress(TeaModel):
    def __init__(
        self,
        progress: float = None,
        total: str = None,
        completed: str = None,
    ):
        self.progress = progress
        self.total = total
        self.completed = completed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.total is not None:
            result['Total'] = self.total
        if self.completed is not None:
            result['Completed'] = self.completed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        return self


class GetImportJobDetailedStatusResponseBodyObjectProgress(TeaModel):
    def __init__(
        self,
        progress: float = None,
        failed: int = None,
        total: int = None,
        completed: int = None,
    ):
        self.progress = progress
        self.failed = failed
        self.total = total
        self.completed = completed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.total is not None:
            result['Total'] = self.total
        if self.completed is not None:
            result['Completed'] = self.completed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        return self


class GetImportJobDetailedStatusResponseBody(TeaModel):
    def __init__(
        self,
        can_retry: bool = None,
        qps: str = None,
        request_id: str = None,
        success: bool = None,
        use_acceleration: bool = None,
        code: str = None,
        message: str = None,
        last_modified_time: int = None,
        netflow: str = None,
        job: GetImportJobDetailedStatusResponseBodyJob = None,
        storage_progress: GetImportJobDetailedStatusResponseBodyStorageProgress = None,
        object_progress: GetImportJobDetailedStatusResponseBodyObjectProgress = None,
    ):
        self.can_retry = can_retry
        self.qps = qps
        self.request_id = request_id
        self.success = success
        self.use_acceleration = use_acceleration
        self.code = code
        self.message = message
        self.last_modified_time = last_modified_time
        self.netflow = netflow
        self.job = job
        self.storage_progress = storage_progress
        self.object_progress = object_progress

    def validate(self):
        if self.job:
            self.job.validate()
        if self.storage_progress:
            self.storage_progress.validate()
        if self.object_progress:
            self.object_progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_retry is not None:
            result['CanRetry'] = self.can_retry
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.use_acceleration is not None:
            result['UseAcceleration'] = self.use_acceleration
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.netflow is not None:
            result['Netflow'] = self.netflow
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.storage_progress is not None:
            result['StorageProgress'] = self.storage_progress.to_map()
        if self.object_progress is not None:
            result['ObjectProgress'] = self.object_progress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanRetry') is not None:
            self.can_retry = m.get('CanRetry')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UseAcceleration') is not None:
            self.use_acceleration = m.get('UseAcceleration')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Netflow') is not None:
            self.netflow = m.get('Netflow')
        if m.get('Job') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('StorageProgress') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyStorageProgress()
            self.storage_progress = temp_model.from_map(m['StorageProgress'])
        if m.get('ObjectProgress') is not None:
            temp_model = GetImportJobDetailedStatusResponseBodyObjectProgress()
            self.object_progress = temp_model.from_map(m['ObjectProgress'])
        return self


class GetImportJobDetailedStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImportJobDetailedStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportJobDetailedStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportJobStatusRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetImportJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        can_retry: bool = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.status = status
        self.can_retry = can_retry
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.can_retry is not None:
            result['CanRetry'] = self.can_retry
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CanRetry') is not None:
            self.can_retry = m.get('CanRetry')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetImportJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImportJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportReportStatusRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        report_id: str = None,
    ):
        self.name = name
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetImportReportStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        import_file_list_path: str = None,
        export_url: str = None,
        success: bool = None,
        message: str = None,
        report_id: str = None,
        failed_file_list_path: str = None,
        request_id: str = None,
        description: str = None,
        completed_file_list_path: str = None,
        code: str = None,
        created_time: int = None,
    ):
        self.status = status
        self.import_file_list_path = import_file_list_path
        self.export_url = export_url
        self.success = success
        self.message = message
        self.report_id = report_id
        self.failed_file_list_path = failed_file_list_path
        self.request_id = request_id
        self.description = description
        self.completed_file_list_path = completed_file_list_path
        self.code = code
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.import_file_list_path is not None:
            result['ImportFileListPath'] = self.import_file_list_path
        if self.export_url is not None:
            result['ExportUrl'] = self.export_url
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.failed_file_list_path is not None:
            result['FailedFileListPath'] = self.failed_file_list_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.completed_file_list_path is not None:
            result['CompletedFileListPath'] = self.completed_file_list_path
        if self.code is not None:
            result['Code'] = self.code
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImportFileListPath') is not None:
            self.import_file_list_path = m.get('ImportFileListPath')
        if m.get('ExportUrl') is not None:
            self.export_url = m.get('ExportUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('FailedFileListPath') is not None:
            self.failed_file_list_path = m.get('FailedFileListPath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CompletedFileListPath') is not None:
            self.completed_file_list_path = m.get('CompletedFileListPath')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class GetImportReportStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImportReportStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportReportStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLightningCubeInstallerUrlRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
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


class GetLightningCubeInstallerUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        url: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.url = url
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.url is not None:
            result['Url'] = self.url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLightningCubeInstallerUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLightningCubeInstallerUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLightningCubeInstallerUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSlsTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_token: str = None,
        success: bool = None,
        expiration: str = None,
        code: str = None,
        access_key_secret: str = None,
        message: str = None,
        access_key_id: str = None,
    ):
        self.request_id = request_id
        self.security_token = security_token
        self.success = success
        self.expiration = expiration
        self.code = code
        self.access_key_secret = access_key_secret
        self.message = message
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.success is not None:
            result['Success'] = self.success
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.code is not None:
            result['Code'] = self.code
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.message is not None:
            result['Message'] = self.message
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class GetSlsTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSlsTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSlsTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportImportDataAddressTypeResponseBodySupportDataAddressTypeList(TeaModel):
    def __init__(
        self,
        data_address_type: List[str] = None,
    ):
        self.data_address_type = data_address_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_address_type is not None:
            result['dataAddressType'] = self.data_address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataAddressType') is not None:
            self.data_address_type = m.get('dataAddressType')
        return self


class GetSupportImportDataAddressTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        support_data_address_type_list: GetSupportImportDataAddressTypeResponseBodySupportDataAddressTypeList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.support_data_address_type_list = support_data_address_type_list

    def validate(self):
        if self.support_data_address_type_list:
            self.support_data_address_type_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.support_data_address_type_list is not None:
            result['SupportDataAddressTypeList'] = self.support_data_address_type_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SupportDataAddressTypeList') is not None:
            temp_model = GetSupportImportDataAddressTypeResponseBodySupportDataAddressTypeList()
            self.support_data_address_type_list = temp_model.from_map(m['SupportDataAddressTypeList'])
        return self


class GetSupportImportDataAddressTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSupportImportDataAddressTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSupportImportDataAddressTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderCallbackRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PayOrderCallbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        message: str = None,
        data: str = None,
        success: bool = None,
        synchro: bool = None,
    ):
        self.code = code
        self.request_id = request_id
        self.message = message
        self.data = data
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        if self.synchro is not None:
            result['synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')
        return self


class PayOrderCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PayOrderCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PayOrderCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class RefundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        success: bool = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.success = success
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.success is not None:
            result['success'] = self.success
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RefundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryDataAddressRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RetryDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RetryImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StartImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobRequest(TeaModel):
    def __init__(
        self,
        job_name: str = None,
    ):
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        return self


class StartJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StopImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobRequest(TeaModel):
    def __init__(
        self,
        job_name: str = None,
    ):
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        return self


class StopJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataAddressRequest(TeaModel):
    def __init__(
        self,
        mgw_region_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        name: str = None,
        address_type: str = None,
        domain: str = None,
        address: str = None,
        sub_address: str = None,
        appid: str = None,
        list_file_path: str = None,
        access_method: str = None,
        access_proxy: str = None,
        access_key_secret: str = None,
        access_key: str = None,
        server_encryption: str = None,
    ):
        self.mgw_region_id = mgw_region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.name = name
        self.address_type = address_type
        self.domain = domain
        self.address = address
        self.sub_address = sub_address
        self.appid = appid
        self.list_file_path = list_file_path
        self.access_method = access_method
        self.access_proxy = access_proxy
        self.access_key_secret = access_key_secret
        self.access_key = access_key
        self.server_encryption = server_encryption

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mgw_region_id is not None:
            result['MgwRegionId'] = self.mgw_region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.name is not None:
            result['Name'] = self.name
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.address is not None:
            result['Address'] = self.address
        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address
        if self.appid is not None:
            result['Appid'] = self.appid
        if self.list_file_path is not None:
            result['ListFilePath'] = self.list_file_path
        if self.access_method is not None:
            result['AccessMethod'] = self.access_method
        if self.access_proxy is not None:
            result['AccessProxy'] = self.access_proxy
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.server_encryption is not None:
            result['ServerEncryption'] = self.server_encryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MgwRegionId') is not None:
            self.mgw_region_id = m.get('MgwRegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')
        if m.get('Appid') is not None:
            self.appid = m.get('Appid')
        if m.get('ListFilePath') is not None:
            self.list_file_path = m.get('ListFilePath')
        if m.get('AccessMethod') is not None:
            self.access_method = m.get('AccessMethod')
        if m.get('AccessProxy') is not None:
            self.access_proxy = m.get('AccessProxy')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('ServerEncryption') is not None:
            self.server_encryption = m.get('ServerEncryption')
        return self


class UpdateDataAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDataAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDataAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImportJobRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        netflow_limiter: str = None,
    ):
        self.name = name
        self.netflow_limiter = netflow_limiter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.netflow_limiter is not None:
            result['NetflowLimiter'] = self.netflow_limiter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetflowLimiter') is not None:
            self.netflow_limiter = m.get('NetflowLimiter')
        return self


class UpdateImportJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        job_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.job_name = job_name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImportJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateImportJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateImportJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMigrationStatusRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        status: str = None,
    ):
        self.order_id = order_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateMigrationStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMigrationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMigrationStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMigrationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCssCreateOrderParamRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class VerifyCssCreateOrderParamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        message: str = None,
        data: bool = None,
        success: bool = None,
        synchro: bool = None,
    ):
        self.code = code
        self.request_id = request_id
        self.message = message
        self.data = data
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data
        if self.success is not None:
            result['success'] = self.success
        if self.synchro is not None:
            result['synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')
        return self


class VerifyCssCreateOrderParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyCssCreateOrderParamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyCssCreateOrderParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


