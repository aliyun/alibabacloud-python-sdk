# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudVendorAccountAKListResponseBody(DaraModel):
    def __init__(
        self,
        cloud_vendor_account_aks: List[main_models.DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKs] = None,
        page_info: main_models.DescribeCloudVendorAccountAKListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the AccessKey pairs.
        self.cloud_vendor_account_aks = cloud_vendor_account_aks
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cloud_vendor_account_aks:
            for v1 in self.cloud_vendor_account_aks:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudVendorAccountAKs'] = []
        if self.cloud_vendor_account_aks is not None:
            for k1 in self.cloud_vendor_account_aks:
                result['CloudVendorAccountAKs'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_vendor_account_aks = []
        if m.get('CloudVendorAccountAKs') is not None:
            for k1 in m.get('CloudVendorAccountAKs'):
                temp_model = main_models.DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKs()
                self.cloud_vendor_account_aks.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCloudVendorAccountAKListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudVendorAccountAKListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKs(DaraModel):
    def __init__(
        self,
        ak_type: str = None,
        auth_id: int = None,
        auth_modules: List[main_models.DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKsAuthModules] = None,
        ctdr_cloud_user_id: str = None,
        extend_info: str = None,
        message: str = None,
        secret_id: str = None,
        service_status: int = None,
        status: int = None,
        vendor: str = None,
        vendor_auth_alias: str = None,
        vendor_uid: str = None,
        vendor_user_name: str = None,
    ):
        # The type of the account to which the AccessKey pair belongs. Valid values:
        # 
        # *   **primary**: a primary account
        # *   **sub**: a sub-account
        self.ak_type = ak_type
        # The unique ID of the AccessKey pair.
        self.auth_id = auth_id
        # The modules that are associated with the AccessKey pair.
        self.auth_modules = auth_modules
        # The Account ID.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The extended information of the module.
        self.extend_info = extend_info
        # The error message of the AccessKey pair.
        self.message = message
        # The AccessKey ID.
        self.secret_id = secret_id
        # The service status of the AccessKey pair. Valid values:
        # 
        # *   **0**: being used
        # *   **1**: exception occurred
        # *   **2**: being validated
        # *   **3**: validation timed out
        self.service_status = service_status
        # The status of the AccessKey pair. Valid values:
        # 
        # *   **0**: enabled
        # *   **1**: disabled
        self.status = status
        # The cloud service provider. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud
        # *   **HUAWEICLOUD**: Huawei Cloud
        # *   **Azure**: Microsoft Azure
        # *   **AWS**: Amazon Web Services (AWS)
        self.vendor = vendor
        # The name of the AccessKey pair.
        self.vendor_auth_alias = vendor_auth_alias
        # Account ID of the multi-cloud instance.
        self.vendor_uid = vendor_uid
        # Account name of the multi-cloud instance.
        self.vendor_user_name = vendor_user_name

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

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

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

        if self.vendor_uid is not None:
            result['VendorUid'] = self.vendor_uid

        if self.vendor_user_name is not None:
            result['VendorUserName'] = self.vendor_user_name

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
                temp_model = main_models.DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKsAuthModules()
                self.auth_modules.append(temp_model.from_map(k1))

        if m.get('CtdrCloudUserId') is not None:
            self.ctdr_cloud_user_id = m.get('CtdrCloudUserId')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

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

        if m.get('VendorUid') is not None:
            self.vendor_uid = m.get('VendorUid')

        if m.get('VendorUserName') is not None:
            self.vendor_user_name = m.get('VendorUserName')

        return self

class DescribeCloudVendorAccountAKListResponseBodyCloudVendorAccountAKsAuthModules(DaraModel):
    def __init__(
        self,
        message: str = None,
        module: str = None,
        module_asset_type: str = None,
        module_disp: str = None,
        module_service_status: int = None,
        module_statement: str = None,
        trail_message: str = None,
        trail_status: str = None,
    ):
        # The error message of the module.
        self.message = message
        # The code of the module. Valid values:
        # 
        # *   **HOST**: host
        # *   **CSPM**: configuration assessment
        # *   **SIEM**: CloudSiem
        # *   **TRIAL**: log audit
        self.module = module
        # The cloud asset that is associated with the module.
        self.module_asset_type = module_asset_type
        # The display name of the module.
        self.module_disp = module_disp
        # The service status of the module. Valid values:
        # 
        # *   **0**: being used
        # *   **1**: exception occurred
        # *   **2**: being validated
        # *   **3**: validation timed out
        self.module_service_status = module_service_status
        # The permission description of the module.
        self.module_statement = module_statement
        # The error message of the log audit service.
        self.trail_message = trail_message
        # The status of the log audit service. Valid values:
        # 
        # *   **init**: being initialized
        # *   **verify**: being validated
        # *   **enable**: enabled
        # *   **disable**: disabled
        # *   **error**: exception occurred
        # *   **timeout**: validation timed out
        self.trail_status = trail_status

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

        if self.trail_message is not None:
            result['TrailMessage'] = self.trail_message

        if self.trail_status is not None:
            result['TrailStatus'] = self.trail_status

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

        if m.get('TrailMessage') is not None:
            self.trail_message = m.get('TrailMessage')

        if m.get('TrailStatus') is not None:
            self.trail_status = m.get('TrailStatus')

        return self

