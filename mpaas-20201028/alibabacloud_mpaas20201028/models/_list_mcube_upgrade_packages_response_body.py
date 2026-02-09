# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeUpgradePackagesResponseBody(DaraModel):
    def __init__(
        self,
        list_packages_result: main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_packages_result = list_packages_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_packages_result:
            self.list_packages_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_packages_result is not None:
            result['ListPackagesResult'] = self.list_packages_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListPackagesResult') is not None:
            temp_model = main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResult()
            self.list_packages_result = temp_model.from_map(m.get('ListPackagesResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeUpgradePackagesResponseBodyListPackagesResult(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        packages: List[main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.packages = packages
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.packages:
            for v1 in self.packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['Packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['Packages'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.packages = []
        if m.get('Packages') is not None:
            for k1 in m.get('Packages'):
                temp_model = main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages()
                self.packages.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages(DaraModel):
    def __init__(
        self,
        allow_create_task: bool = None,
        app_code: str = None,
        appstore_url: str = None,
        back_log: str = None,
        change_log: str = None,
        client_file_size: int = None,
        client_name: str = None,
        cp_id: str = None,
        creator: str = None,
        download_url: str = None,
        global_variables: str = None,
        gmt_create: str = None,
        gmt_create_str: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        id: int = None,
        inner_version: str = None,
        ios_symbol: str = None,
        is_enterprise: int = None,
        is_rc: int = None,
        is_release: int = None,
        max_version: str = None,
        md_5: str = None,
        modifier: str = None,
        need_check: int = None,
        oss_path: str = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version: str = None,
        publish_period: int = None,
        qrcode_url: str = None,
        release_type: str = None,
        release_window: str = None,
        scm_download_url: str = None,
        server_version: int = None,
        verification_code: str = None,
        verify_result: int = None,
        version_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.back_log = back_log
        self.change_log = change_log
        self.client_file_size = client_file_size
        self.client_name = client_name
        self.cp_id = cp_id
        self.creator = creator
        self.download_url = download_url
        self.global_variables = global_variables
        self.gmt_create = gmt_create
        self.gmt_create_str = gmt_create_str
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.id = id
        self.inner_version = inner_version
        self.ios_symbol = ios_symbol
        self.is_enterprise = is_enterprise
        self.is_rc = is_rc
        self.is_release = is_release
        self.max_version = max_version
        self.md_5 = md_5
        self.modifier = modifier
        self.need_check = need_check
        self.oss_path = oss_path
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_name = product_name
        self.product_version = product_version
        self.publish_period = publish_period
        self.qrcode_url = qrcode_url
        self.release_type = release_type
        self.release_window = release_window
        self.scm_download_url = scm_download_url
        self.server_version = server_version
        self.verification_code = verification_code
        self.verify_result = verify_result
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_create_task is not None:
            result['AllowCreateTask'] = self.allow_create_task

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url

        if self.back_log is not None:
            result['BackLog'] = self.back_log

        if self.change_log is not None:
            result['ChangeLog'] = self.change_log

        if self.client_file_size is not None:
            result['ClientFileSize'] = self.client_file_size

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        if self.cp_id is not None:
            result['CpId'] = self.cp_id

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.global_variables is not None:
            result['GlobalVariables'] = self.global_variables

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str

        if self.id is not None:
            result['Id'] = self.id

        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version

        if self.ios_symbol is not None:
            result['IosSymbol'] = self.ios_symbol

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.is_rc is not None:
            result['IsRc'] = self.is_rc

        if self.is_release is not None:
            result['IsRelease'] = self.is_release

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.need_check is not None:
            result['NeedCheck'] = self.need_check

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period

        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.release_window is not None:
            result['ReleaseWindow'] = self.release_window

        if self.scm_download_url is not None:
            result['ScmDownloadUrl'] = self.scm_download_url

        if self.server_version is not None:
            result['ServerVersion'] = self.server_version

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')

        if m.get('BackLog') is not None:
            self.back_log = m.get('BackLog')

        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')

        if m.get('ClientFileSize') is not None:
            self.client_file_size = m.get('ClientFileSize')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        if m.get('CpId') is not None:
            self.cp_id = m.get('CpId')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('GlobalVariables') is not None:
            self.global_variables = m.get('GlobalVariables')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')

        if m.get('IosSymbol') is not None:
            self.ios_symbol = m.get('IosSymbol')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')

        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')

        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('ReleaseWindow') is not None:
            self.release_window = m.get('ReleaseWindow')

        if m.get('ScmDownloadUrl') is not None:
            self.scm_download_url = m.get('ScmDownloadUrl')

        if m.get('ServerVersion') is not None:
            self.server_version = m.get('ServerVersion')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

