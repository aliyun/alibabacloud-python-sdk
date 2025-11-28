# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddBaaSAntChainBizChainRequest(TeaModel):
    def __init__(
        self,
        baa_sant_chain_chain_id: str = None,
        baa_sant_chain_consortium_id: str = None,
        ca_cert: str = None,
        ca_cert_password: str = None,
        client_cert: str = None,
        client_key: str = None,
        client_key_password: str = None,
        contract_template_id_list: str = None,
        name: str = None,
        node_name_list: str = None,
        region_id: str = None,
        remark: str = None,
        user_key: str = None,
        user_key_password: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.baa_sant_chain_chain_id = baa_sant_chain_chain_id
        # This parameter is required.
        self.baa_sant_chain_consortium_id = baa_sant_chain_consortium_id
        # This parameter is required.
        self.ca_cert = ca_cert
        # This parameter is required.
        self.ca_cert_password = ca_cert_password
        # This parameter is required.
        self.client_cert = client_cert
        # This parameter is required.
        self.client_key = client_key
        # This parameter is required.
        self.client_key_password = client_key_password
        self.contract_template_id_list = contract_template_id_list
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.node_name_list = node_name_list
        self.region_id = region_id
        self.remark = remark
        # This parameter is required.
        self.user_key = user_key
        # This parameter is required.
        self.user_key_password = user_key_password
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sant_chain_chain_id is not None:
            result['BaaSAntChainChainId'] = self.baa_sant_chain_chain_id
        if self.baa_sant_chain_consortium_id is not None:
            result['BaaSAntChainConsortiumId'] = self.baa_sant_chain_consortium_id
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert
        if self.ca_cert_password is not None:
            result['CaCertPassword'] = self.ca_cert_password
        if self.client_cert is not None:
            result['ClientCert'] = self.client_cert
        if self.client_key is not None:
            result['ClientKey'] = self.client_key
        if self.client_key_password is not None:
            result['ClientKeyPassword'] = self.client_key_password
        if self.contract_template_id_list is not None:
            result['ContractTemplateIdList'] = self.contract_template_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.node_name_list is not None:
            result['NodeNameList'] = self.node_name_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_key is not None:
            result['UserKey'] = self.user_key
        if self.user_key_password is not None:
            result['UserKeyPassword'] = self.user_key_password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSAntChainChainId') is not None:
            self.baa_sant_chain_chain_id = m.get('BaaSAntChainChainId')
        if m.get('BaaSAntChainConsortiumId') is not None:
            self.baa_sant_chain_consortium_id = m.get('BaaSAntChainConsortiumId')
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')
        if m.get('CaCertPassword') is not None:
            self.ca_cert_password = m.get('CaCertPassword')
        if m.get('ClientCert') is not None:
            self.client_cert = m.get('ClientCert')
        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')
        if m.get('ClientKeyPassword') is not None:
            self.client_key_password = m.get('ClientKeyPassword')
        if m.get('ContractTemplateIdList') is not None:
            self.contract_template_id_list = m.get('ContractTemplateIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeNameList') is not None:
            self.node_name_list = m.get('NodeNameList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserKey') is not None:
            self.user_key = m.get('UserKey')
        if m.get('UserKeyPassword') is not None:
            self.user_key_password = m.get('UserKeyPassword')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AddBaaSAntChainBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBaaSAntChainBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddBaaSAntChainBizChainResponseBody = None,
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
            temp_model = AddBaaSAntChainBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBaaSFabricBizChainRequest(TeaModel):
    def __init__(
        self,
        baa_sfabric_channel_id: str = None,
        baa_sfabric_consortium_id: str = None,
        baa_sfabric_organization_id: str = None,
        contract_template_id_list: str = None,
        name: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.baa_sfabric_channel_id = baa_sfabric_channel_id
        # This parameter is required.
        self.baa_sfabric_consortium_id = baa_sfabric_consortium_id
        # This parameter is required.
        self.baa_sfabric_organization_id = baa_sfabric_organization_id
        self.contract_template_id_list = contract_template_id_list
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_channel_id is not None:
            result['BaaSFabricChannelId'] = self.baa_sfabric_channel_id
        if self.baa_sfabric_consortium_id is not None:
            result['BaaSFabricConsortiumId'] = self.baa_sfabric_consortium_id
        if self.baa_sfabric_organization_id is not None:
            result['BaaSFabricOrganizationId'] = self.baa_sfabric_organization_id
        if self.contract_template_id_list is not None:
            result['ContractTemplateIdList'] = self.contract_template_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricChannelId') is not None:
            self.baa_sfabric_channel_id = m.get('BaaSFabricChannelId')
        if m.get('BaaSFabricConsortiumId') is not None:
            self.baa_sfabric_consortium_id = m.get('BaaSFabricConsortiumId')
        if m.get('BaaSFabricOrganizationId') is not None:
            self.baa_sfabric_organization_id = m.get('BaaSFabricOrganizationId')
        if m.get('ContractTemplateIdList') is not None:
            self.contract_template_id_list = m.get('ContractTemplateIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddBaaSFabricBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBaaSFabricBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddBaaSFabricBizChainResponseBody = None,
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
            temp_model = AddBaaSFabricBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBsnFabricBizChainRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        name: str = None,
        node_list: str = None,
        region_id: str = None,
        remark: str = None,
        user_code: str = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.node_list = node_list
        self.region_id = region_id
        self.remark = remark
        # This parameter is required.
        self.user_code = user_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.name is not None:
            result['Name'] = self.name
        if self.node_list is not None:
            result['NodeList'] = self.node_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_code is not None:
            result['UserCode'] = self.user_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserCode') is not None:
            self.user_code = m.get('UserCode')
        return self


class AddBsnFabricBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBsnFabricBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddBsnFabricBizChainResponseBody = None,
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
            temp_model = AddBsnFabricBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        product_key: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        self.authorized_count = authorized_count
        # This parameter is required.
        self.product_key = product_key
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDeviceGroupResponseBody = None,
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
            temp_model = AddDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMemberRequest(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        authorized_device_count: int = None,
        contactor: str = None,
        name: str = None,
        region_id: str = None,
        remark: str = None,
        telephony: str = None,
        uid: str = None,
    ):
        # This parameter is required.
        self.authorized_count = authorized_count
        self.authorized_device_count = authorized_device_count
        # This parameter is required.
        self.contactor = contactor
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.remark = remark
        # This parameter is required.
        self.telephony = telephony
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.authorized_device_count is not None:
            result['AuthorizedDeviceCount'] = self.authorized_device_count
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.telephony is not None:
            result['Telephony'] = self.telephony
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('AuthorizedDeviceCount') is not None:
            self.authorized_device_count = m.get('AuthorizedDeviceCount')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Telephony') is not None:
            self.telephony = m.get('Telephony')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class AddMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMemberResponseBody = None,
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
            temp_model = AddMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        alg_impl: str = None,
        alg_type: str = None,
        name: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        self.alg_impl = alg_impl
        # This parameter is required.
        self.alg_type = alg_type
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alg_impl is not None:
            result['AlgImpl'] = self.alg_impl
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgImpl') is not None:
            self.alg_impl = m.get('AlgImpl')
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddPrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddPrivacyRuleResponseBody = None,
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
            temp_model = AddPrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRouteRuleRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        chain_up_mode: str = None,
        contract_name: str = None,
        contract_template_id: str = None,
        device_group_id: str = None,
        invoke_type: str = None,
        privacy_rule_id: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        self.chain_up_mode = chain_up_mode
        self.contract_name = contract_name
        self.contract_template_id = contract_template_id
        self.device_group_id = device_group_id
        # This parameter is required.
        self.invoke_type = invoke_type
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.chain_up_mode is not None:
            result['ChainUpMode'] = self.chain_up_mode
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.contract_template_id is not None:
            result['ContractTemplateId'] = self.contract_template_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('ChainUpMode') is not None:
            self.chain_up_mode = m.get('ChainUpMode')
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('ContractTemplateId') is not None:
            self.contract_template_id = m.get('ContractTemplateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddRouteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRouteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRouteRuleResponseBody = None,
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
            temp_model = AddRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgreeMemberAccessRequest(TeaModel):
    def __init__(
        self,
        member_account_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_account_id = member_account_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_account_id is not None:
            result['MemberAccountId'] = self.member_account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberAccountId') is not None:
            self.member_account_id = m.get('MemberAccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AgreeMemberAccessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AgreeMemberAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AgreeMemberAccessResponseBody = None,
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
            temp_model = AgreeMemberAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeBaaSRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AuthorizeBaaSResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeBaaSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeBaaSResponseBody = None,
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
            temp_model = AuthorizeBaaSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeDeviceGroupBizChainRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id_list: str = None,
        device_group_id: str = None,
        region_id: str = None,
    ):
        self.biz_chain_id_list = biz_chain_id_list
        # This parameter is required.
        self.device_group_id = device_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id_list is not None:
            result['BizChainIdList'] = self.biz_chain_id_list
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainIdList') is not None:
            self.biz_chain_id_list = m.get('BizChainIdList')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AuthorizeDeviceGroupBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeDeviceGroupBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeDeviceGroupBizChainResponseBody = None,
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
            temp_model = AuthorizeDeviceGroupBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeMemberBizChainRequest(TeaModel):
    def __init__(
        self,
        biz_chain_info: str = None,
        member_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.biz_chain_info = biz_chain_info
        # This parameter is required.
        self.member_id = member_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_info is not None:
            result['BizChainInfo'] = self.biz_chain_info
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainInfo') is not None:
            self.biz_chain_info = m.get('BizChainInfo')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AuthorizeMemberBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeMemberBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeMemberBizChainResponseBody = None,
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
            temp_model = AuthorizeMemberBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        privacy_rule_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrivacyRuleResponseBody = None,
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
            temp_model = DeletePrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRouteRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        route_rule_id: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.route_rule_id = route_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_rule_id is not None:
            result['RouteRuleId'] = self.route_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteRuleId') is not None:
            self.route_rule_id = m.get('RouteRuleId')
        return self


class DeleteRouteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRouteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRouteRuleResponseBody = None,
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
            temp_model = DeleteRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeniedMemberAccessRequest(TeaModel):
    def __init__(
        self,
        member_account_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_account_id = member_account_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_account_id is not None:
            result['MemberAccountId'] = self.member_account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberAccountId') is not None:
            self.member_account_id = m.get('MemberAccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeniedMemberAccessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeniedMemberAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeniedMemberAccessResponseBody = None,
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
            temp_model = DeniedMemberAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_baa_s: bool = None,
        role_type: str = None,
    ):
        self.authorized_baa_s = authorized_baa_s
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_baa_s is not None:
            result['AuthorizedBaaS'] = self.authorized_baa_s
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedBaaS') is not None:
            self.authorized_baa_s = m.get('AuthorizedBaaS')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeAccountRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAccountRoleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeAccountRoleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccountRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountRoleResponseBody = None,
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
            temp_model = DescribeAccountRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdminInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAdminInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        access_date: int = None,
        access_status: str = None,
        authorized_count: int = None,
        authorized_device_count: int = None,
        contactor: str = None,
        member_id: str = None,
        name: str = None,
        remark: str = None,
        status: str = None,
        telephony: str = None,
        uid: str = None,
    ):
        self.access_date = access_date
        self.access_status = access_status
        self.authorized_count = authorized_count
        self.authorized_device_count = authorized_device_count
        self.contactor = contactor
        self.member_id = member_id
        self.name = name
        self.remark = remark
        self.status = status
        self.telephony = telephony
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_date is not None:
            result['AccessDate'] = self.access_date
        if self.access_status is not None:
            result['AccessStatus'] = self.access_status
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.authorized_device_count is not None:
            result['AuthorizedDeviceCount'] = self.authorized_device_count
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.telephony is not None:
            result['Telephony'] = self.telephony
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDate') is not None:
            self.access_date = m.get('AccessDate')
        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('AuthorizedDeviceCount') is not None:
            self.authorized_device_count = m.get('AuthorizedDeviceCount')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Telephony') is not None:
            self.telephony = m.get('Telephony')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeAdminInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAdminInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeAdminInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAdminInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdminInfoResponseBody = None,
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
            temp_model = DescribeAdminInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizChainStatInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBizChainStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_chain_name: str = None,
        used_count: int = None,
    ):
        self.biz_chain_name = biz_chain_name
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeBizChainStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeBizChainStatInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBizChainStatInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBizChainStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBizChainStatInfoResponseBody = None,
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
            temp_model = DescribeBizChainStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardApiInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDashboardApiInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        used_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeDashboardApiInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDashboardApiInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeDashboardApiInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardApiInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardApiInfoResponseBody = None,
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
            temp_model = DescribeDashboardApiInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardBaseInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDashboardBaseInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        api_invoke_count: int = None,
        biz_chain_count: int = None,
        device_count: int = None,
        member_count: int = None,
    ):
        self.api_invoke_count = api_invoke_count
        self.biz_chain_count = biz_chain_count
        self.device_count = device_count
        self.member_count = member_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoke_count is not None:
            result['ApiInvokeCount'] = self.api_invoke_count
        if self.biz_chain_count is not None:
            result['BizChainCount'] = self.biz_chain_count
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvokeCount') is not None:
            self.api_invoke_count = m.get('ApiInvokeCount')
        if m.get('BizChainCount') is not None:
            self.biz_chain_count = m.get('BizChainCount')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        return self


class DescribeDashboardBaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDashboardBaseInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeDashboardBaseInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardBaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardBaseInfoResponseBody = None,
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
            temp_model = DescribeDashboardBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDashboardDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        used_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeDashboardDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDashboardDeviceInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeDashboardDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardDeviceInfoResponseBody = None,
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
            temp_model = DescribeDashboardDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardMemberApiInfoRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.biz_chain_id = biz_chain_id
        # This parameter is required.
        self.end_time = end_time
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDashboardMemberApiInfoResponseBodyDataMemberInfoList(TeaModel):
    def __init__(
        self,
        api_invoke_count: int = None,
        time: int = None,
    ):
        self.api_invoke_count = api_invoke_count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoke_count is not None:
            result['ApiInvokeCount'] = self.api_invoke_count
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvokeCount') is not None:
            self.api_invoke_count = m.get('ApiInvokeCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeDashboardMemberApiInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        member_info_list: List[DescribeDashboardMemberApiInfoResponseBodyDataMemberInfoList] = None,
        member_name: str = None,
    ):
        self.member_info_list = member_info_list
        self.member_name = member_name

    def validate(self):
        if self.member_info_list:
            for k in self.member_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberInfoList'] = []
        if self.member_info_list is not None:
            for k in self.member_info_list:
                result['MemberInfoList'].append(k.to_map() if k else None)
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_info_list = []
        if m.get('MemberInfoList') is not None:
            for k in m.get('MemberInfoList'):
                temp_model = DescribeDashboardMemberApiInfoResponseBodyDataMemberInfoList()
                self.member_info_list.append(temp_model.from_map(k))
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        return self


class DescribeDashboardMemberApiInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeDashboardMemberApiInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDashboardMemberApiInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardMemberApiInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardMemberApiInfoResponseBody = None,
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
            temp_model = DescribeDashboardMemberApiInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardMemberDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDashboardMemberDeviceInfoResponseBodyDataMemberInfoList(TeaModel):
    def __init__(
        self,
        device_count: int = None,
        time: int = None,
    ):
        self.device_count = device_count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeDashboardMemberDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        member_info_list: List[DescribeDashboardMemberDeviceInfoResponseBodyDataMemberInfoList] = None,
        member_name: str = None,
    ):
        self.member_info_list = member_info_list
        self.member_name = member_name

    def validate(self):
        if self.member_info_list:
            for k in self.member_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberInfoList'] = []
        if self.member_info_list is not None:
            for k in self.member_info_list:
                result['MemberInfoList'].append(k.to_map() if k else None)
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_info_list = []
        if m.get('MemberInfoList') is not None:
            for k in m.get('MemberInfoList'):
                temp_model = DescribeDashboardMemberDeviceInfoResponseBodyDataMemberInfoList()
                self.member_info_list.append(temp_model.from_map(k))
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        return self


class DescribeDashboardMemberDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeDashboardMemberDeviceInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDashboardMemberDeviceInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDashboardMemberDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardMemberDeviceInfoResponseBody = None,
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
            temp_model = DescribeDashboardMemberDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        device_count: int = None,
        distributable_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.device_count = device_count
        self.distributable_count = distributable_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.distributable_count is not None:
            result['DistributableCount'] = self.distributable_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('DistributableCount') is not None:
            self.distributable_count = m.get('DistributableCount')
        return self


class DescribeDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDeviceInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeviceInfoResponseBody = None,
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
            temp_model = DescribeDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeStatInfoRequest(TeaModel):
    def __init__(
        self,
        edge_dn: str = None,
        edge_pk: str = None,
        region_id: str = None,
    ):
        self.edge_dn = edge_dn
        # This parameter is required.
        self.edge_pk = edge_pk
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_dn is not None:
            result['EdgeDn'] = self.edge_dn
        if self.edge_pk is not None:
            result['EdgePk'] = self.edge_pk
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeDn') is not None:
            self.edge_dn = m.get('EdgeDn')
        if m.get('EdgePk') is not None:
            self.edge_pk = m.get('EdgePk')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEdgeStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        total_device_license_count: int = None,
        used_device_license_count: int = None,
    ):
        self.total_device_license_count = total_device_license_count
        self.used_device_license_count = used_device_license_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_device_license_count is not None:
            result['TotalDeviceLicenseCount'] = self.total_device_license_count
        if self.used_device_license_count is not None:
            result['UsedDeviceLicenseCount'] = self.used_device_license_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDeviceLicenseCount') is not None:
            self.total_device_license_count = m.get('TotalDeviceLicenseCount')
        if m.get('UsedDeviceLicenseCount') is not None:
            self.used_device_license_count = m.get('UsedDeviceLicenseCount')
        return self


class DescribeEdgeStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeEdgeStatInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeEdgeStatInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEdgeStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdgeStatInfoResponseBody = None,
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
            temp_model = DescribeEdgeStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMemberBizChainStatInfoRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMemberBizChainStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_chain_name: str = None,
        used_count: int = None,
    ):
        self.biz_chain_name = biz_chain_name
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeMemberBizChainStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeMemberBizChainStatInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMemberBizChainStatInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMemberBizChainStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMemberBizChainStatInfoResponseBody = None,
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
            temp_model = DescribeMemberBizChainStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMemberStatInfoRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        region_id: str = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMemberStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        biz_chain_count: int = None,
        member_id: str = None,
        member_name: str = None,
        used_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.biz_chain_count = biz_chain_count
        self.member_id = member_id
        self.member_name = member_name
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.biz_chain_count is not None:
            result['BizChainCount'] = self.biz_chain_count
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('BizChainCount') is not None:
            self.biz_chain_count = m.get('BizChainCount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeMemberStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeMemberStatInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMemberStatInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMemberStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMemberStatInfoResponseBody = None,
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
            temp_model = DescribeMemberStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMemberTotalStatInfoRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMemberTotalStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        used_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeMemberTotalStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeMemberTotalStatInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeMemberTotalStatInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMemberTotalStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMemberTotalStatInfoResponseBody = None,
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
            temp_model = DescribeMemberTotalStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackgeInfoRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePackgeInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_trace: bool = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.enable_trace = enable_trace
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_trace is not None:
            result['EnableTrace'] = self.enable_trace
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTrace') is not None:
            self.enable_trace = m.get('EnableTrace')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePackgeInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePackgeInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribePackgeInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePackgeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackgeInfoResponseBody = None,
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
            temp_model = DescribePackgeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStatDeviceInfoResponseBodyDataBizChainList(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        biz_chain_name: str = None,
    ):
        self.authorized_count = authorized_count
        self.biz_chain_name = biz_chain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        return self


class DescribeStatDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_chain_list: List[DescribeStatDeviceInfoResponseBodyDataBizChainList] = None,
        distributable_count: int = None,
        total_authorized_count: int = None,
    ):
        self.biz_chain_list = biz_chain_list
        self.distributable_count = distributable_count
        self.total_authorized_count = total_authorized_count

    def validate(self):
        if self.biz_chain_list:
            for k in self.biz_chain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizChainList'] = []
        if self.biz_chain_list is not None:
            for k in self.biz_chain_list:
                result['BizChainList'].append(k.to_map() if k else None)
        if self.distributable_count is not None:
            result['DistributableCount'] = self.distributable_count
        if self.total_authorized_count is not None:
            result['TotalAuthorizedCount'] = self.total_authorized_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_chain_list = []
        if m.get('BizChainList') is not None:
            for k in m.get('BizChainList'):
                temp_model = DescribeStatDeviceInfoResponseBodyDataBizChainList()
                self.biz_chain_list.append(temp_model.from_map(k))
        if m.get('DistributableCount') is not None:
            self.distributable_count = m.get('DistributableCount')
        if m.get('TotalAuthorizedCount') is not None:
            self.total_authorized_count = m.get('TotalAuthorizedCount')
        return self


class DescribeStatDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeStatDeviceInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeStatDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStatDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStatDeviceInfoResponseBody = None,
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
            temp_model = DescribeStatDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatMemberDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStatMemberDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: str = None,
        biz_chain_count: str = None,
        member_id: str = None,
        member_name: str = None,
        used_count: str = None,
    ):
        self.authorized_count = authorized_count
        self.biz_chain_count = biz_chain_count
        self.member_id = member_id
        self.member_name = member_name
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.biz_chain_count is not None:
            result['BizChainCount'] = self.biz_chain_count
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('BizChainCount') is not None:
            self.biz_chain_count = m.get('BizChainCount')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeStatMemberDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeStatMemberDeviceInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeStatMemberDeviceInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStatMemberDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStatMemberDeviceInfoResponseBody = None,
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
            temp_model = DescribeStatMemberDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTotalStatInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTotalStatInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        total_count: int = None,
        used_count: int = None,
    ):
        self.authorized_count = authorized_count
        self.total_count = total_count
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        return self


class DescribeTotalStatInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTotalStatInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = DescribeTotalStatInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTotalStatInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTotalStatInfoResponseBody = None,
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
            temp_model = DescribeTotalStatInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDeviceResponseBody = None,
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
            temp_model = DisableDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.device_group_id = device_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDeviceGroupResponseBody = None,
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
            temp_model = DisableDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadPrivacyKeyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DownloadPrivacyKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DownloadPrivacyKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadPrivacyKeyResponseBody = None,
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
            temp_model = DownloadPrivacyKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDeviceResponseBody = None,
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
            temp_model = EnableDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.device_group_id = device_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDeviceGroupResponseBody = None,
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
            temp_model = EnableDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeMemberRequest(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_id = member_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class FreezeMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FreezeMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FreezeMemberResponseBody = None,
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
            temp_model = FreezeMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEdgeTotalDeviceCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEdgeTotalDeviceCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEdgeTotalDeviceCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEdgeTotalDeviceCountResponseBody = None,
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
            temp_model = GetEdgeTotalDeviceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllAdminRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllAdminResponseBodyData(TeaModel):
    def __init__(
        self,
        admin_id: str = None,
        name: str = None,
    ):
        self.admin_id = admin_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_id is not None:
            result['AdminId'] = self.admin_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminId') is not None:
            self.admin_id = m.get('AdminId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAllAdminResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllAdminResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllAdminResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllAdminResponseBody = None,
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
            temp_model = ListAllAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllBizChainRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllBizChainResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        name: str = None,
        used_onchain_count: int = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.used_onchain_count = used_onchain_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.used_onchain_count is not None:
            result['UsedOnchainCount'] = self.used_onchain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UsedOnchainCount') is not None:
            self.used_onchain_count = m.get('UsedOnchainCount')
        return self


class ListAllBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllBizChainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllBizChainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllBizChainResponseBody = None,
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
            temp_model = ListAllBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllBizChainContractRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllBizChainContractResponseBodyData(TeaModel):
    def __init__(
        self,
        contract_name: str = None,
        contract_template_id: str = None,
        invoke_type: str = None,
    ):
        self.contract_name = contract_name
        self.contract_template_id = contract_template_id
        self.invoke_type = invoke_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.contract_template_id is not None:
            result['ContractTemplateId'] = self.contract_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('ContractTemplateId') is not None:
            self.contract_template_id = m.get('ContractTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        return self


class ListAllBizChainContractResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllBizChainContractResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllBizChainContractResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllBizChainContractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllBizChainContractResponseBody = None,
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
            temp_model = ListAllBizChainContractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        name: str = None,
    ):
        self.device_group_id = device_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAllDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllDeviceGroupResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllDeviceGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllDeviceGroupResponseBody = None,
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
            temp_model = ListAllDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllMemberRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllMemberResponseBodyData(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        name: str = None,
    ):
        self.member_id = member_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAllMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllMemberResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllMemberResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllMemberResponseBody = None,
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
            temp_model = ListAllMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllPrivacyAlgorithmRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllPrivacyAlgorithmResponseBodyData(TeaModel):
    def __init__(
        self,
        alg_impl_list: List[str] = None,
        alg_type: str = None,
    ):
        self.alg_impl_list = alg_impl_list
        self.alg_type = alg_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alg_impl_list is not None:
            result['AlgImplList'] = self.alg_impl_list
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgImplList') is not None:
            self.alg_impl_list = m.get('AlgImplList')
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')
        return self


class ListAllPrivacyAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllPrivacyAlgorithmResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllPrivacyAlgorithmResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllPrivacyAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllPrivacyAlgorithmResponseBody = None,
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
            temp_model = ListAllPrivacyAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllPrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllPrivacyRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        privacy_rule_id: str = None,
    ):
        self.name = name
        self.privacy_rule_id = privacy_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        return self


class ListAllPrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllPrivacyRuleResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllPrivacyRuleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllPrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllPrivacyRuleResponseBody = None,
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
            temp_model = ListAllPrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllProductKeyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllProductKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        product_key: str = None,
    ):
        self.name = name
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListAllProductKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllProductKeyResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllProductKeyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllProductKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllProductKeyResponseBody = None,
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
            temp_model = ListAllProductKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllSystemContractRequest(TeaModel):
    def __init__(
        self,
        block_chain_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.block_chain_type = block_chain_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_chain_type is not None:
            result['BlockChainType'] = self.block_chain_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockChainType') is not None:
            self.block_chain_type = m.get('BlockChainType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllSystemContractResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        system_contract_id: str = None,
    ):
        self.name = name
        self.system_contract_id = system_contract_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.system_contract_id is not None:
            result['SystemContractId'] = self.system_contract_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemContractId') is not None:
            self.system_contract_id = m.get('SystemContractId')
        return self


class ListAllSystemContractResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAllSystemContractResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAllSystemContractResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAllSystemContractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllSystemContractResponseBody = None,
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
            temp_model = ListAllSystemContractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSAntChainRequest(TeaModel):
    def __init__(
        self,
        baa_sant_chain_consortium_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.baa_sant_chain_consortium_id = baa_sant_chain_consortium_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sant_chain_consortium_id is not None:
            result['BaaSAntChainConsortiumId'] = self.baa_sant_chain_consortium_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSAntChainConsortiumId') is not None:
            self.baa_sant_chain_consortium_id = m.get('BaaSAntChainConsortiumId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSAntChainResponseBodyData(TeaModel):
    def __init__(
        self,
        baa_sant_chain_chain_id: str = None,
        baa_sant_chain_chain_name: str = None,
    ):
        self.baa_sant_chain_chain_id = baa_sant_chain_chain_id
        self.baa_sant_chain_chain_name = baa_sant_chain_chain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sant_chain_chain_id is not None:
            result['BaaSAntChainChainId'] = self.baa_sant_chain_chain_id
        if self.baa_sant_chain_chain_name is not None:
            result['BaaSAntChainChainName'] = self.baa_sant_chain_chain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSAntChainChainId') is not None:
            self.baa_sant_chain_chain_id = m.get('BaaSAntChainChainId')
        if m.get('BaaSAntChainChainName') is not None:
            self.baa_sant_chain_chain_name = m.get('BaaSAntChainChainName')
        return self


class ListBaaSAntChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSAntChainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSAntChainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSAntChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSAntChainResponseBody = None,
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
            temp_model = ListBaaSAntChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSAntChainConsortiumResponseBodyData(TeaModel):
    def __init__(
        self,
        baa_sant_chain_consortium_id: str = None,
        baa_sant_chain_consortium_name: str = None,
    ):
        self.baa_sant_chain_consortium_id = baa_sant_chain_consortium_id
        self.baa_sant_chain_consortium_name = baa_sant_chain_consortium_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sant_chain_consortium_id is not None:
            result['BaaSAntChainConsortiumId'] = self.baa_sant_chain_consortium_id
        if self.baa_sant_chain_consortium_name is not None:
            result['BaaSAntChainConsortiumName'] = self.baa_sant_chain_consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSAntChainConsortiumId') is not None:
            self.baa_sant_chain_consortium_id = m.get('BaaSAntChainConsortiumId')
        if m.get('BaaSAntChainConsortiumName') is not None:
            self.baa_sant_chain_consortium_name = m.get('BaaSAntChainConsortiumName')
        return self


class ListBaaSAntChainConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSAntChainConsortiumResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSAntChainConsortiumResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSAntChainConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSAntChainConsortiumResponseBody = None,
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
            temp_model = ListBaaSAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSAntChainPeerRequest(TeaModel):
    def __init__(
        self,
        baa_sant_chain_chain_id: str = None,
        baa_sant_chain_consortium_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.baa_sant_chain_chain_id = baa_sant_chain_chain_id
        # This parameter is required.
        self.baa_sant_chain_consortium_id = baa_sant_chain_consortium_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sant_chain_chain_id is not None:
            result['BaaSAntChainChainId'] = self.baa_sant_chain_chain_id
        if self.baa_sant_chain_consortium_id is not None:
            result['BaaSAntChainConsortiumId'] = self.baa_sant_chain_consortium_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSAntChainChainId') is not None:
            self.baa_sant_chain_chain_id = m.get('BaaSAntChainChainId')
        if m.get('BaaSAntChainConsortiumId') is not None:
            self.baa_sant_chain_consortium_id = m.get('BaaSAntChainConsortiumId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSAntChainPeerResponseBodyData(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class ListBaaSAntChainPeerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSAntChainPeerResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSAntChainPeerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSAntChainPeerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSAntChainPeerResponseBody = None,
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
            temp_model = ListBaaSAntChainPeerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSFabricChannelRequest(TeaModel):
    def __init__(
        self,
        baa_sfabric_consortium_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.baa_sfabric_consortium_id = baa_sfabric_consortium_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_consortium_id is not None:
            result['BaaSFabricConsortiumId'] = self.baa_sfabric_consortium_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricConsortiumId') is not None:
            self.baa_sfabric_consortium_id = m.get('BaaSFabricConsortiumId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSFabricChannelResponseBodyData(TeaModel):
    def __init__(
        self,
        baa_sfabric_channel_id: str = None,
        baa_sfabric_channel_name: str = None,
    ):
        self.baa_sfabric_channel_id = baa_sfabric_channel_id
        self.baa_sfabric_channel_name = baa_sfabric_channel_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_channel_id is not None:
            result['BaaSFabricChannelId'] = self.baa_sfabric_channel_id
        if self.baa_sfabric_channel_name is not None:
            result['BaaSFabricChannelName'] = self.baa_sfabric_channel_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricChannelId') is not None:
            self.baa_sfabric_channel_id = m.get('BaaSFabricChannelId')
        if m.get('BaaSFabricChannelName') is not None:
            self.baa_sfabric_channel_name = m.get('BaaSFabricChannelName')
        return self


class ListBaaSFabricChannelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSFabricChannelResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSFabricChannelResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSFabricChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSFabricChannelResponseBody = None,
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
            temp_model = ListBaaSFabricChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSFabricConsortiumRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSFabricConsortiumResponseBodyData(TeaModel):
    def __init__(
        self,
        baa_sfabric_consortium_id: str = None,
        baa_sfabric_consortium_name: str = None,
    ):
        self.baa_sfabric_consortium_id = baa_sfabric_consortium_id
        self.baa_sfabric_consortium_name = baa_sfabric_consortium_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_consortium_id is not None:
            result['BaaSFabricConsortiumId'] = self.baa_sfabric_consortium_id
        if self.baa_sfabric_consortium_name is not None:
            result['BaaSFabricConsortiumName'] = self.baa_sfabric_consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricConsortiumId') is not None:
            self.baa_sfabric_consortium_id = m.get('BaaSFabricConsortiumId')
        if m.get('BaaSFabricConsortiumName') is not None:
            self.baa_sfabric_consortium_name = m.get('BaaSFabricConsortiumName')
        return self


class ListBaaSFabricConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSFabricConsortiumResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSFabricConsortiumResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSFabricConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSFabricConsortiumResponseBody = None,
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
            temp_model = ListBaaSFabricConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBaaSFabricOrganizationRequest(TeaModel):
    def __init__(
        self,
        baa_sfabric_channel_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.baa_sfabric_channel_id = baa_sfabric_channel_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_channel_id is not None:
            result['BaaSFabricChannelId'] = self.baa_sfabric_channel_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricChannelId') is not None:
            self.baa_sfabric_channel_id = m.get('BaaSFabricChannelId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBaaSFabricOrganizationResponseBodyData(TeaModel):
    def __init__(
        self,
        baa_sfabric_organization_id: str = None,
        baa_sfabric_organization_name: str = None,
    ):
        self.baa_sfabric_organization_id = baa_sfabric_organization_id
        self.baa_sfabric_organization_name = baa_sfabric_organization_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baa_sfabric_organization_id is not None:
            result['BaaSFabricOrganizationId'] = self.baa_sfabric_organization_id
        if self.baa_sfabric_organization_name is not None:
            result['BaaSFabricOrganizationName'] = self.baa_sfabric_organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaaSFabricOrganizationId') is not None:
            self.baa_sfabric_organization_id = m.get('BaaSFabricOrganizationId')
        if m.get('BaaSFabricOrganizationName') is not None:
            self.baa_sfabric_organization_name = m.get('BaaSFabricOrganizationName')
        return self


class ListBaaSFabricOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBaaSFabricOrganizationResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBaaSFabricOrganizationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBaaSFabricOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBaaSFabricOrganizationResponseBody = None,
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
            temp_model = ListBaaSFabricOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBizChainRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListBizChainResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        name: str = None,
        remark: str = None,
        type: str = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.name = name
        self.remark = remark
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBizChainResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListBizChainResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListBizChainResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListBizChainResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListBizChainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBizChainResponseBody = None,
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
            temp_model = ListBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBizChainDataRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        end_time: int = None,
        io_tdata_did: str = None,
        member_id: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        # This parameter is required.
        self.end_time = end_time
        self.io_tdata_did = io_tdata_did
        self.member_id = member_id
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.io_tdata_did is not None:
            result['IoTDataDID'] = self.io_tdata_did
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IoTDataDID') is not None:
            self.io_tdata_did = m.get('IoTDataDID')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBizChainDataResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_num: str = None,
        device_name: str = None,
        iot_data_did: str = None,
        member_name: str = None,
        product_key: str = None,
        timestamp: int = None,
        tx_hash: str = None,
    ):
        self.block_hash = block_hash
        self.block_num = block_num
        self.device_name = device_name
        self.iot_data_did = iot_data_did
        self.member_name = member_name
        self.product_key = product_key
        self.timestamp = timestamp
        self.tx_hash = tx_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_num is not None:
            result['BlockNum'] = self.block_num
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_data_did is not None:
            result['IotDataDID'] = self.iot_data_did
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['TxHash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockNum') is not None:
            self.block_num = m.get('BlockNum')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotDataDID') is not None:
            self.iot_data_did = m.get('IotDataDID')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TxHash') is not None:
            self.tx_hash = m.get('TxHash')
        return self


class ListBizChainDataResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListBizChainDataResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListBizChainDataResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBizChainDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListBizChainDataResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListBizChainDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBizChainDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBizChainDataResponseBody = None,
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
            temp_model = ListBizChainDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
    ):
        # This parameter is required.
        self.device_group_id = device_group_id
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListDeviceResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        last_onchain_time: str = None,
        name: str = None,
        status: str = None,
        used_onchain_count: int = None,
    ):
        self.device_id = device_id
        self.last_onchain_time = last_onchain_time
        self.name = name
        self.status = status
        self.used_onchain_count = used_onchain_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.last_onchain_time is not None:
            result['LastOnchainTime'] = self.last_onchain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.used_onchain_count is not None:
            result['UsedOnchainCount'] = self.used_onchain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('LastOnchainTime') is not None:
            self.last_onchain_time = m.get('LastOnchainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UsedOnchainCount') is not None:
            self.used_onchain_count = m.get('UsedOnchainCount')
        return self


class ListDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListDeviceResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListDeviceResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDeviceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceResponseBody = None,
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
            temp_model = ListDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
        status: str = None,
    ):
        self.member_name = member_name
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeviceGroupResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        current_user: bool = None,
        device_count: int = None,
        device_group_id: str = None,
        member_name: str = None,
        name: str = None,
        product_key: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.authorized_count = authorized_count
        self.current_user = current_user
        self.device_count = device_count
        self.device_group_id = device_group_id
        self.member_name = member_name
        self.name = name
        self.product_key = product_key
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.current_user is not None:
            result['CurrentUser'] = self.current_user
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.name is not None:
            result['Name'] = self.name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('CurrentUser') is not None:
            self.current_user = m.get('CurrentUser')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListDeviceGroupResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListDeviceGroupResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDeviceGroupResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceGroupResponseBody = None,
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
            temp_model = ListDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceGroupAuthorizedBizChainRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        region_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDeviceGroupAuthorizedBizChainResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized: bool = None,
        biz_chain_id: str = None,
        biz_chain_name: str = None,
        block_chain_type: str = None,
    ):
        self.authorized = authorized
        self.biz_chain_id = biz_chain_id
        self.biz_chain_name = biz_chain_name
        self.block_chain_type = block_chain_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.block_chain_type is not None:
            result['BlockChainType'] = self.block_chain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('BlockChainType') is not None:
            self.block_chain_type = m.get('BlockChainType')
        return self


class ListDeviceGroupAuthorizedBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListDeviceGroupAuthorizedBizChainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeviceGroupAuthorizedBizChainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeviceGroupAuthorizedBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceGroupAuthorizedBizChainResponseBody = None,
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
            temp_model = ListDeviceGroupAuthorizedBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeDeviceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        num: int = None,
        product_key: str = None,
        region_id: str = None,
        size: int = None,
    ):
        self.name = name
        # This parameter is required.
        self.num = num
        # This parameter is required.
        self.product_key = product_key
        self.region_id = region_id
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListEdgeDeviceResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        last_onchain_time: str = None,
        name: str = None,
        status: str = None,
        used_onchain_count: int = None,
    ):
        self.device_id = device_id
        self.last_onchain_time = last_onchain_time
        self.name = name
        self.status = status
        self.used_onchain_count = used_onchain_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.last_onchain_time is not None:
            result['LastOnchainTime'] = self.last_onchain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.used_onchain_count is not None:
            result['UsedOnchainCount'] = self.used_onchain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('LastOnchainTime') is not None:
            self.last_onchain_time = m.get('LastOnchainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UsedOnchainCount') is not None:
            self.used_onchain_count = m.get('UsedOnchainCount')
        return self


class ListEdgeDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListEdgeDeviceResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListEdgeDeviceResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEdgeDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEdgeDeviceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListEdgeDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEdgeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeDeviceResponseBody = None,
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
            temp_model = ListEdgeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEdgeDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
        status: str = None,
    ):
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListEdgeDeviceGroupResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        current_user: bool = None,
        device_count: int = None,
        device_group_id: str = None,
        edge_name: str = None,
        member_name: str = None,
        name: str = None,
        product_key: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.authorized_count = authorized_count
        self.current_user = current_user
        self.device_count = device_count
        self.device_group_id = device_group_id
        self.edge_name = edge_name
        self.member_name = member_name
        self.name = name
        self.product_key = product_key
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.current_user is not None:
            result['CurrentUser'] = self.current_user
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.edge_name is not None:
            result['EdgeName'] = self.edge_name
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.name is not None:
            result['Name'] = self.name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('CurrentUser') is not None:
            self.current_user = m.get('CurrentUser')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('EdgeName') is not None:
            self.edge_name = m.get('EdgeName')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListEdgeDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListEdgeDeviceGroupResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListEdgeDeviceGroupResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEdgeDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEdgeDeviceGroupResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListEdgeDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEdgeDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEdgeDeviceGroupResponseBody = None,
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
            temp_model = ListEdgeDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemberRequest(TeaModel):
    def __init__(
        self,
        contactor: str = None,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
        uid: str = None,
    ):
        self.contactor = contactor
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListMemberResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        admin_name: str = None,
        authorized_count: int = None,
        authorized_device_count: int = None,
        contactor: str = None,
        member_id: str = None,
        name: str = None,
        remark: str = None,
        status: str = None,
        telephony: str = None,
        uid: str = None,
    ):
        self.admin_name = admin_name
        self.authorized_count = authorized_count
        self.authorized_device_count = authorized_device_count
        self.contactor = contactor
        self.member_id = member_id
        self.name = name
        self.remark = remark
        self.status = status
        self.telephony = telephony
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.authorized_device_count is not None:
            result['AuthorizedDeviceCount'] = self.authorized_device_count
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.telephony is not None:
            result['Telephony'] = self.telephony
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('AuthorizedDeviceCount') is not None:
            self.authorized_device_count = m.get('AuthorizedDeviceCount')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Telephony') is not None:
            self.telephony = m.get('Telephony')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListMemberResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMemberResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMemberResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListMemberResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListMemberResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemberResponseBody = None,
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
            temp_model = ListMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemberAccessRecordRequest(TeaModel):
    def __init__(
        self,
        access_status: str = None,
        contactor: str = None,
        name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
        uid: str = None,
    ):
        self.access_status = access_status
        self.contactor = contactor
        self.name = name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_status is not None:
            result['AccessStatus'] = self.access_status
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListMemberAccessRecordResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        access_date: int = None,
        access_status: str = None,
        admin_name: str = None,
        authorized_count: int = None,
        authorized_device_count: int = None,
        contactor: str = None,
        member_id: str = None,
        member_response_date: int = None,
        name: str = None,
        remark: str = None,
        status: str = None,
        telephony: str = None,
        uid: str = None,
    ):
        self.access_date = access_date
        self.access_status = access_status
        self.admin_name = admin_name
        self.authorized_count = authorized_count
        self.authorized_device_count = authorized_device_count
        self.contactor = contactor
        self.member_id = member_id
        self.member_response_date = member_response_date
        self.name = name
        self.remark = remark
        self.status = status
        self.telephony = telephony
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_date is not None:
            result['AccessDate'] = self.access_date
        if self.access_status is not None:
            result['AccessStatus'] = self.access_status
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.authorized_device_count is not None:
            result['AuthorizedDeviceCount'] = self.authorized_device_count
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_response_date is not None:
            result['MemberResponseDate'] = self.member_response_date
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.telephony is not None:
            result['Telephony'] = self.telephony
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDate') is not None:
            self.access_date = m.get('AccessDate')
        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('AuthorizedDeviceCount') is not None:
            self.authorized_device_count = m.get('AuthorizedDeviceCount')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberResponseDate') is not None:
            self.member_response_date = m.get('MemberResponseDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Telephony') is not None:
            self.telephony = m.get('Telephony')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListMemberAccessRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListMemberAccessRecordResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListMemberAccessRecordResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMemberAccessRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListMemberAccessRecordResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListMemberAccessRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMemberAccessRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemberAccessRecordResponseBody = None,
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
            temp_model = ListMemberAccessRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMemberAuthorizedBizChainRequest(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_id = member_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMemberAuthorizedBizChainResponseBodyDataPeerList(TeaModel):
    def __init__(
        self,
        authorized: bool = None,
        peer_name: str = None,
    ):
        self.authorized = authorized
        self.peer_name = peer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.peer_name is not None:
            result['PeerName'] = self.peer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('PeerName') is not None:
            self.peer_name = m.get('PeerName')
        return self


class ListMemberAuthorizedBizChainResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized: bool = None,
        biz_chain_id: str = None,
        biz_chain_name: str = None,
        biz_chain_type: str = None,
        peer_list: List[ListMemberAuthorizedBizChainResponseBodyDataPeerList] = None,
    ):
        self.authorized = authorized
        self.biz_chain_id = biz_chain_id
        self.biz_chain_name = biz_chain_name
        self.biz_chain_type = biz_chain_type
        self.peer_list = peer_list

    def validate(self):
        if self.peer_list:
            for k in self.peer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.biz_chain_type is not None:
            result['BizChainType'] = self.biz_chain_type
        result['PeerList'] = []
        if self.peer_list is not None:
            for k in self.peer_list:
                result['PeerList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('BizChainType') is not None:
            self.biz_chain_type = m.get('BizChainType')
        self.peer_list = []
        if m.get('PeerList') is not None:
            for k in m.get('PeerList'):
                temp_model = ListMemberAuthorizedBizChainResponseBodyDataPeerList()
                self.peer_list.append(temp_model.from_map(k))
        return self


class ListMemberAuthorizedBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListMemberAuthorizedBizChainResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMemberAuthorizedBizChainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMemberAuthorizedBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMemberAuthorizedBizChainResponseBody = None,
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
            temp_model = ListMemberAuthorizedBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        num: int = None,
        region_id: str = None,
        size: int = None,
    ):
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListPrivacyRuleResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        alg_impl: str = None,
        alg_type: str = None,
        current_user: bool = None,
        member_name: str = None,
        name: str = None,
        privacy_rule_id: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.alg_impl = alg_impl
        self.alg_type = alg_type
        self.current_user = current_user
        self.member_name = member_name
        self.name = name
        self.privacy_rule_id = privacy_rule_id
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alg_impl is not None:
            result['AlgImpl'] = self.alg_impl
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type
        if self.current_user is not None:
            result['CurrentUser'] = self.current_user
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.name is not None:
            result['Name'] = self.name
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgImpl') is not None:
            self.alg_impl = m.get('AlgImpl')
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')
        if m.get('CurrentUser') is not None:
            self.current_user = m.get('CurrentUser')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPrivacyRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListPrivacyRuleResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListPrivacyRuleResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListPrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListPrivacyRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListPrivacyRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivacyRuleResponseBody = None,
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
            temp_model = ListPrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivacyRuleSharedMemberRequest(TeaModel):
    def __init__(
        self,
        privacy_rule_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPrivacyRuleSharedMemberResponseBodyDataMemberList(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_name: str = None,
        shared: str = None,
    ):
        self.member_id = member_id
        self.member_name = member_name
        self.shared = shared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.shared is not None:
            result['Shared'] = self.shared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Shared') is not None:
            self.shared = m.get('Shared')
        return self


class ListPrivacyRuleSharedMemberResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        biz_chain_name: str = None,
        member_list: List[ListPrivacyRuleSharedMemberResponseBodyDataMemberList] = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.biz_chain_name = biz_chain_name
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = ListPrivacyRuleSharedMemberResponseBodyDataMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class ListPrivacyRuleSharedMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPrivacyRuleSharedMemberResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPrivacyRuleSharedMemberResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPrivacyRuleSharedMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivacyRuleSharedMemberResponseBody = None,
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
            temp_model = ListPrivacyRuleSharedMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRouteRuleRequest(TeaModel):
    def __init__(
        self,
        biz_chain_name: str = None,
        chain_up_mode: str = None,
        device_group_name: str = None,
        num: int = None,
        region_id: str = None,
        size: int = None,
    ):
        self.biz_chain_name = biz_chain_name
        self.chain_up_mode = chain_up_mode
        self.device_group_name = device_group_name
        # This parameter is required.
        self.num = num
        self.region_id = region_id
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.chain_up_mode is not None:
            result['ChainUpMode'] = self.chain_up_mode
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.num is not None:
            result['Num'] = self.num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('ChainUpMode') is not None:
            self.chain_up_mode = m.get('ChainUpMode')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListRouteRuleResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        biz_chain_id: int = None,
        biz_chain_name: str = None,
        block_chain_type: str = None,
        chain_up_mode: str = None,
        contract_name: str = None,
        contract_template_id: str = None,
        device_group_id: str = None,
        device_group_name: str = None,
        invoke_type: str = None,
        privacy_rule_id: str = None,
        privacy_rule_name: str = None,
        remark: str = None,
        route_rule_id: str = None,
    ):
        self.biz_chain_id = biz_chain_id
        self.biz_chain_name = biz_chain_name
        self.block_chain_type = block_chain_type
        self.chain_up_mode = chain_up_mode
        self.contract_name = contract_name
        self.contract_template_id = contract_template_id
        self.device_group_id = device_group_id
        self.device_group_name = device_group_name
        self.invoke_type = invoke_type
        self.privacy_rule_id = privacy_rule_id
        self.privacy_rule_name = privacy_rule_name
        self.remark = remark
        self.route_rule_id = route_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.biz_chain_name is not None:
            result['BizChainName'] = self.biz_chain_name
        if self.block_chain_type is not None:
            result['BlockChainType'] = self.block_chain_type
        if self.chain_up_mode is not None:
            result['ChainUpMode'] = self.chain_up_mode
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.contract_template_id is not None:
            result['ContractTemplateId'] = self.contract_template_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.privacy_rule_name is not None:
            result['PrivacyRuleName'] = self.privacy_rule_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.route_rule_id is not None:
            result['RouteRuleId'] = self.route_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('BizChainName') is not None:
            self.biz_chain_name = m.get('BizChainName')
        if m.get('BlockChainType') is not None:
            self.block_chain_type = m.get('BlockChainType')
        if m.get('ChainUpMode') is not None:
            self.chain_up_mode = m.get('ChainUpMode')
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('ContractTemplateId') is not None:
            self.contract_template_id = m.get('ContractTemplateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('PrivacyRuleName') is not None:
            self.privacy_rule_name = m.get('PrivacyRuleName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RouteRuleId') is not None:
            self.route_rule_id = m.get('RouteRuleId')
        return self


class ListRouteRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        num: int = None,
        page_data: List[ListRouteRuleResponseBodyDataPageData] = None,
        size: int = None,
        total: int = None,
    ):
        self.num = num
        self.page_data = page_data
        self.size = size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListRouteRuleResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRouteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListRouteRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = ListRouteRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRouteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRouteRuleResponseBody = None,
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
            temp_model = ListRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBlockchainDataRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        contract_name: str = None,
        invoke_type: str = None,
        iot_data_did: str = None,
        region_id: str = None,
        transaction_id: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        self.contract_name = contract_name
        self.invoke_type = invoke_type
        # This parameter is required.
        self.iot_data_did = iot_data_did
        self.region_id = region_id
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.iot_data_did is not None:
            result['IotDataDID'] = self.iot_data_did
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('IotDataDID') is not None:
            self.iot_data_did = m.get('IotDataDID')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class QueryBlockchainDataResponseBodyData(TeaModel):
    def __init__(
        self,
        alg_type: str = None,
        plain_data: str = None,
        privacy_data: str = None,
        privacy_rule_id: str = None,
    ):
        self.alg_type = alg_type
        self.plain_data = plain_data
        self.privacy_data = privacy_data
        self.privacy_rule_id = privacy_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type
        if self.plain_data is not None:
            result['PlainData'] = self.plain_data
        if self.privacy_data is not None:
            result['PrivacyData'] = self.privacy_data
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')
        if m.get('PlainData') is not None:
            self.plain_data = m.get('PlainData')
        if m.get('PrivacyData') is not None:
            self.privacy_data = m.get('PrivacyData')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        return self


class QueryBlockchainDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryBlockchainDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = QueryBlockchainDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBlockchainDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBlockchainDataResponseBody = None,
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
            temp_model = QueryBlockchainDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBlockchainMetadataRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        contract_name: str = None,
        invoke_type: str = None,
        iot_data_did: str = None,
        region_id: str = None,
        transaction_id: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        self.contract_name = contract_name
        self.invoke_type = invoke_type
        # This parameter is required.
        self.iot_data_did = iot_data_did
        self.region_id = region_id
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.iot_data_did is not None:
            result['IotDataDID'] = self.iot_data_did
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('IotDataDID') is not None:
            self.iot_data_did = m.get('IotDataDID')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class QueryBlockchainMetadataResponseBodyData(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_number: str = None,
        iot_id: str = None,
        member_name: str = None,
        product_key: str = None,
        timestamp: int = None,
        tx_hash: str = None,
    ):
        self.block_hash = block_hash
        self.block_number = block_number
        self.iot_id = iot_id
        self.member_name = member_name
        self.product_key = product_key
        self.timestamp = timestamp
        self.tx_hash = tx_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_number is not None:
            result['BlockNumber'] = self.block_number
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['TxHash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockNumber') is not None:
            self.block_number = m.get('BlockNumber')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TxHash') is not None:
            self.tx_hash = m.get('TxHash')
        return self


class QueryBlockchainMetadataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryBlockchainMetadataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = QueryBlockchainMetadataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBlockchainMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBlockchainMetadataResponseBody = None,
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
            temp_model = QueryBlockchainMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SharePrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        member_id_list: str = None,
        privacy_rule_id: str = None,
        region_id: str = None,
    ):
        self.member_id_list = member_id_list
        # This parameter is required.
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id_list is not None:
            result['MemberIdList'] = self.member_id_list
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIdList') is not None:
            self.member_id_list = m.get('MemberIdList')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SharePrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SharePrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SharePrivacyRuleResponseBody = None,
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
            temp_model = SharePrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnFreezeMemberRequest(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_id = member_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UnFreezeMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnFreezeMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnFreezeMemberResponseBody = None,
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
            temp_model = UnFreezeMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizChainRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        name: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateBizChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBizChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBizChainResponseBody = None,
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
            temp_model = UpdateBizChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemberRequest(TeaModel):
    def __init__(
        self,
        authorized_count: int = None,
        authorized_device_count: int = None,
        contactor: str = None,
        member_id: str = None,
        name: str = None,
        region_id: str = None,
        remark: str = None,
        telephony: str = None,
        uid: str = None,
    ):
        # This parameter is required.
        self.authorized_count = authorized_count
        self.authorized_device_count = authorized_device_count
        # This parameter is required.
        self.contactor = contactor
        # This parameter is required.
        self.member_id = member_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.remark = remark
        # This parameter is required.
        self.telephony = telephony
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_count is not None:
            result['AuthorizedCount'] = self.authorized_count
        if self.authorized_device_count is not None:
            result['AuthorizedDeviceCount'] = self.authorized_device_count
        if self.contactor is not None:
            result['Contactor'] = self.contactor
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.telephony is not None:
            result['Telephony'] = self.telephony
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedCount') is not None:
            self.authorized_count = m.get('AuthorizedCount')
        if m.get('AuthorizedDeviceCount') is not None:
            self.authorized_device_count = m.get('AuthorizedDeviceCount')
        if m.get('Contactor') is not None:
            self.contactor = m.get('Contactor')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Telephony') is not None:
            self.telephony = m.get('Telephony')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class UpdateMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMemberResponseBody = None,
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
            temp_model = UpdateMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivacyRuleRequest(TeaModel):
    def __init__(
        self,
        alg_impl: str = None,
        alg_type: str = None,
        name: str = None,
        privacy_rule_id: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        self.alg_impl = alg_impl
        # This parameter is required.
        self.alg_type = alg_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alg_impl is not None:
            result['AlgImpl'] = self.alg_impl
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type
        if self.name is not None:
            result['Name'] = self.name
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgImpl') is not None:
            self.alg_impl = m.get('AlgImpl')
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdatePrivacyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePrivacyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePrivacyRuleResponseBody = None,
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
            temp_model = UpdatePrivacyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRouteRuleRequest(TeaModel):
    def __init__(
        self,
        biz_chain_id: str = None,
        contract_name: str = None,
        contract_template_id: str = None,
        invoke_type: str = None,
        privacy_rule_id: str = None,
        region_id: str = None,
        remark: str = None,
        route_rule_id: str = None,
    ):
        # This parameter is required.
        self.biz_chain_id = biz_chain_id
        self.contract_name = contract_name
        self.contract_template_id = contract_template_id
        # This parameter is required.
        self.invoke_type = invoke_type
        self.privacy_rule_id = privacy_rule_id
        self.region_id = region_id
        self.remark = remark
        # This parameter is required.
        self.route_rule_id = route_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_chain_id is not None:
            result['BizChainId'] = self.biz_chain_id
        if self.contract_name is not None:
            result['ContractName'] = self.contract_name
        if self.contract_template_id is not None:
            result['ContractTemplateId'] = self.contract_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.privacy_rule_id is not None:
            result['PrivacyRuleId'] = self.privacy_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.route_rule_id is not None:
            result['RouteRuleId'] = self.route_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizChainId') is not None:
            self.biz_chain_id = m.get('BizChainId')
        if m.get('ContractName') is not None:
            self.contract_name = m.get('ContractName')
        if m.get('ContractTemplateId') is not None:
            self.contract_template_id = m.get('ContractTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('PrivacyRuleId') is not None:
            self.privacy_rule_id = m.get('PrivacyRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RouteRuleId') is not None:
            self.route_rule_id = m.get('RouteRuleId')
        return self


class UpdateRouteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRouteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRouteRuleResponseBody = None,
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
            temp_model = UpdateRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadIoTDataToBlockchainRequest(TeaModel):
    def __init__(
        self,
        iot_auth_type: str = None,
        iot_data_did: str = None,
        iot_data_digest: str = None,
        iot_data_token: str = None,
        iot_id: str = None,
        iot_id_service_provider: str = None,
        iot_id_source: str = None,
        plain_data: str = None,
        privacy_data: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.iot_auth_type = iot_auth_type
        # This parameter is required.
        self.iot_data_did = iot_data_did
        # This parameter is required.
        self.iot_data_digest = iot_data_digest
        # This parameter is required.
        self.iot_data_token = iot_data_token
        # This parameter is required.
        self.iot_id = iot_id
        # This parameter is required.
        self.iot_id_service_provider = iot_id_service_provider
        # This parameter is required.
        self.iot_id_source = iot_id_source
        # This parameter is required.
        self.plain_data = plain_data
        # This parameter is required.
        self.privacy_data = privacy_data
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_auth_type is not None:
            result['IotAuthType'] = self.iot_auth_type
        if self.iot_data_did is not None:
            result['IotDataDID'] = self.iot_data_did
        if self.iot_data_digest is not None:
            result['IotDataDigest'] = self.iot_data_digest
        if self.iot_data_token is not None:
            result['IotDataToken'] = self.iot_data_token
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_id_service_provider is not None:
            result['IotIdServiceProvider'] = self.iot_id_service_provider
        if self.iot_id_source is not None:
            result['IotIdSource'] = self.iot_id_source
        if self.plain_data is not None:
            result['PlainData'] = self.plain_data
        if self.privacy_data is not None:
            result['PrivacyData'] = self.privacy_data
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotAuthType') is not None:
            self.iot_auth_type = m.get('IotAuthType')
        if m.get('IotDataDID') is not None:
            self.iot_data_did = m.get('IotDataDID')
        if m.get('IotDataDigest') is not None:
            self.iot_data_digest = m.get('IotDataDigest')
        if m.get('IotDataToken') is not None:
            self.iot_data_token = m.get('IotDataToken')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotIdServiceProvider') is not None:
            self.iot_id_service_provider = m.get('IotIdServiceProvider')
        if m.get('IotIdSource') is not None:
            self.iot_id_source = m.get('IotIdSource')
        if m.get('PlainData') is not None:
            self.plain_data = m.get('PlainData')
        if m.get('PrivacyData') is not None:
            self.privacy_data = m.get('PrivacyData')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UploadIoTDataToBlockchainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadIoTDataToBlockchainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadIoTDataToBlockchainResponseBody = None,
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
            temp_model = UploadIoTDataToBlockchainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


