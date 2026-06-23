# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20200710 import models as main_models
from darabonba.model import DaraModel

class ListMcubeUpgradePackagesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        list_packages_result: main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResult = None,
        page_size: int = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.list_packages_result = list_packages_result
        self.page_size = page_size
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.total_count = total_count

    def validate(self):
        if self.list_packages_result:
            self.list_packages_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.list_packages_result is not None:
            result['ListPackagesResult'] = self.list_packages_result.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('ListPackagesResult') is not None:
            temp_model = main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResult()
            self.list_packages_result = temp_model.from_map(m.get('ListPackagesResult'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMcubeUpgradePackagesResponseBodyListPackagesResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        packages: List[main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages] = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.packages = packages
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        result['Packages'] = []
        if self.packages is not None:
            for k1 in self.packages:
                result['Packages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        self.packages = []
        if m.get('Packages') is not None:
            for k1 in m.get('Packages'):
                temp_model = main_models.ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages()
                self.packages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages(DaraModel):
    def __init__(
        self,
        allow_create_task: bool = None,
        app_code: str = None,
        appstore_url: str = None,
        change_log: str = None,
        creator: str = None,
        download_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_enterprise: int = None,
        md_5: str = None,
        modifier: str = None,
        need_check: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_period: int = None,
        verification_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.change_log = change_log
        self.creator = creator
        self.download_url = download_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_enterprise = is_enterprise
        self.md_5 = md_5
        self.modifier = modifier
        self.need_check = need_check
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_period = publish_period
        self.verification_code = verification_code

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

        if self.change_log is not None:
            result['ChangeLog'] = self.change_log

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.need_check is not None:
            result['NeedCheck'] = self.need_check

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')

        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self

