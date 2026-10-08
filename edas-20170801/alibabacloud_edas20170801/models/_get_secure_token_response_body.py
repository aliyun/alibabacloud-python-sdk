# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetSecureTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        secure_token: main_models.GetSecureTokenResponseBodySecureToken = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The message returned for the request.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned security token.
        self.secure_token = secure_token

    def validate(self):
        if self.secure_token:
            self.secure_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secure_token is not None:
            result['SecureToken'] = self.secure_token.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecureToken') is not None:
            temp_model = main_models.GetSecureTokenResponseBodySecureToken()
            self.secure_token = temp_model.from_map(m.get('SecureToken'))

        return self

class GetSecureTokenResponseBodySecureToken(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        address_server_host: str = None,
        belong_region: str = None,
        description: str = None,
        edas_id: str = None,
        id: int = None,
        mse_instance_id: str = None,
        mse_internet_address: str = None,
        mse_intranet_address: str = None,
        mse_registry_type: str = None,
        region_id: str = None,
        region_name: str = None,
        secret_key: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        # The AccessKey ID used in the namespace.
        self.access_key = access_key
        # The address of Address Server associated with the namespace.
        self.address_server_host = address_server_host
        # The ID of the region.
        self.belong_region = belong_region
        # The description of the namespace.
        self.description = description
        # The ID of the Alibaba Cloud account that activated Enterprise Distributed Application Service (EDAS).
        self.edas_id = edas_id
        # The ID of the security token.
        self.id = id
        # The ID of the MSE instance.
        self.mse_instance_id = mse_instance_id
        # The public endpoint of the MSE registry.
        self.mse_internet_address = mse_internet_address
        # The private endpoint of the MSE registry.
        self.mse_intranet_address = mse_intranet_address
        # The type of the Microservices Engine (MSE) registry.
        # 
        # - default: the shared registry of EDAS
        # 
        # - exclusive_mse: MSE Nacos registry
        self.mse_registry_type = mse_registry_type
        # The ID of the region where the namespace resides.
        self.region_id = region_id
        # The name of the region where the namespace resides.
        self.region_name = region_name
        # The AccessKey secret used in the namespace.
        self.secret_key = secret_key
        # The tenant ID of the namespace.
        self.tenant_id = tenant_id
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.address_server_host is not None:
            result['AddressServerHost'] = self.address_server_host

        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region

        if self.description is not None:
            result['Description'] = self.description

        if self.edas_id is not None:
            result['EdasId'] = self.edas_id

        if self.id is not None:
            result['Id'] = self.id

        if self.mse_instance_id is not None:
            result['MseInstanceId'] = self.mse_instance_id

        if self.mse_internet_address is not None:
            result['MseInternetAddress'] = self.mse_internet_address

        if self.mse_intranet_address is not None:
            result['MseIntranetAddress'] = self.mse_intranet_address

        if self.mse_registry_type is not None:
            result['MseRegistryType'] = self.mse_registry_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AddressServerHost') is not None:
            self.address_server_host = m.get('AddressServerHost')

        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EdasId') is not None:
            self.edas_id = m.get('EdasId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MseInstanceId') is not None:
            self.mse_instance_id = m.get('MseInstanceId')

        if m.get('MseInternetAddress') is not None:
            self.mse_internet_address = m.get('MseInternetAddress')

        if m.get('MseIntranetAddress') is not None:
            self.mse_intranet_address = m.get('MseIntranetAddress')

        if m.get('MseRegistryType') is not None:
            self.mse_registry_type = m.get('MseRegistryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

