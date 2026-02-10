# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyCloudVendorAccountAKResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModifyCloudVendorAccountAKResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the AccessKey pair that is added.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ModifyCloudVendorAccountAKResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyCloudVendorAccountAKResponseBodyData(DaraModel):
    def __init__(
        self,
        ak_type: str = None,
        auth_id: int = None,
        auth_modules: List[main_models.ModifyCloudVendorAccountAKResponseBodyDataAuthModules] = None,
        ctdr_cloud_user_id: str = None,
        message: str = None,
        secret_id: str = None,
        service_status: int = None,
        status: int = None,
        vendor: str = None,
        vendor_auth_alias: str = None,
    ):
        # The type of the account to which the AccessKey pair belongs. Valid values:
        # 
        # *   **primary**
        # *   **sub**
        self.ak_type = ak_type
        # The unique ID of the AccessKey pair.
        self.auth_id = auth_id
        # The modules that are associated with the AccessKey pair.
        self.auth_modules = auth_modules
        # Account ID. 
        # >The account ID of the cloud provider being connected.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The error message of the AccessKey pair.
        self.message = message
        # The AccessKey ID.
        # 
        # >  If AkType is set to **primary**, the value of SecretId is AccessKey ID of the third-party master account. If AkType is set to **sub**, the value of SecretId is the AccessKey ID of the third-party sub-account. This parameter value does not change for a **Microsoft Azure account**. For an Azure account, this parameter value is the **app ID** that is used for authentication.
        self.secret_id = secret_id
        # The service status of the AccessKey pair. Valid values:
        # 
        # *   **0**: being used.
        # *   **1**: exception occurred.
        # *   **2**: being validated.
        # *   **3**: validation timed out.
        self.service_status = service_status
        # The status of the AccessKey pair. Valid values:
        # 
        # *   **0**: enabled.
        # *   **1**: disabled.
        self.status = status
        # The type of the cloud asset. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud.
        # *   **HUAWEICLOUD**: Huawei Cloud.
        # *   **Azure**: Microsoft Azure.
        # *   **AWS**: Amazon Web Services (AWS).
        # *  **VOLCENGINE**: Volcengine 
        # *  **google**: Google Cloud 
        # *  **CHAITIN**: Chaitin Tech 
        # *  **FORTINET**: Fortinet 
        # *  **THREATBOOK**: ThreatBook
        self.vendor = vendor
        # The name of the AccessKey pair.
        # 
        # >  The account information of the third-party cloud servers.
        self.vendor_auth_alias = vendor_auth_alias

    def validate(self):
        if self.auth_modules:
            for v1 in self.auth_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak_type is not None:
            result['AkType'] = self.ak_type

        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        result['AuthModules'] = []
        if self.auth_modules is not None:
            for k1 in self.auth_modules:
                result['AuthModules'].append(k1.to_map() if k1 else None)

        if self.ctdr_cloud_user_id is not None:
            result['CtdrCloudUserId'] = self.ctdr_cloud_user_id

        if self.message is not None:
            result['Message'] = self.message

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.status is not None:
            result['Status'] = self.status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_auth_alias is not None:
            result['VendorAuthAlias'] = self.vendor_auth_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkType') is not None:
            self.ak_type = m.get('AkType')

        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        self.auth_modules = []
        if m.get('AuthModules') is not None:
            for k1 in m.get('AuthModules'):
                temp_model = main_models.ModifyCloudVendorAccountAKResponseBodyDataAuthModules()
                self.auth_modules.append(temp_model.from_map(k1))

        if m.get('CtdrCloudUserId') is not None:
            self.ctdr_cloud_user_id = m.get('CtdrCloudUserId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorAuthAlias') is not None:
            self.vendor_auth_alias = m.get('VendorAuthAlias')

        return self

class ModifyCloudVendorAccountAKResponseBodyDataAuthModules(DaraModel):
    def __init__(
        self,
        message: str = None,
        module: str = None,
        module_asset_type: str = None,
        module_disp: str = None,
        module_service_status: int = None,
        module_statement: str = None,
    ):
        # The error message of the module.
        self.message = message
        # The code of the module. Valid values:
        # 
        # *   **HOST**: host.
        # *   **CSPM**: configuration assessment.
        # *   **SIEM**: CTDR.
        # *   **TRIAL**: log audit.
        self.module = module
        # The type of the cloud asset that is associated with the module.
        self.module_asset_type = module_asset_type
        # The display name of the module.
        self.module_disp = module_disp
        # The service status of the module. Valid values:
        # 
        # *   **0**: being used.
        # *   **1**: exception occurred.
        # *   **2**: being validated.
        # *   **3**: validation timed out.
        self.module_service_status = module_service_status
        # The permission description of the module.
        self.module_statement = module_statement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.module is not None:
            result['Module'] = self.module

        if self.module_asset_type is not None:
            result['ModuleAssetType'] = self.module_asset_type

        if self.module_disp is not None:
            result['ModuleDisp'] = self.module_disp

        if self.module_service_status is not None:
            result['ModuleServiceStatus'] = self.module_service_status

        if self.module_statement is not None:
            result['ModuleStatement'] = self.module_statement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('ModuleAssetType') is not None:
            self.module_asset_type = m.get('ModuleAssetType')

        if m.get('ModuleDisp') is not None:
            self.module_disp = m.get('ModuleDisp')

        if m.get('ModuleServiceStatus') is not None:
            self.module_service_status = m.get('ModuleServiceStatus')

        if m.get('ModuleStatement') is not None:
            self.module_statement = m.get('ModuleStatement')

        return self

