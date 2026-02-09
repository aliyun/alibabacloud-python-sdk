# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeHotpatchResourcesResponseBody(DaraModel):
    def __init__(
        self,
        list_hotpatch_resource_result: main_models.ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_hotpatch_resource_result = list_hotpatch_resource_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_hotpatch_resource_result:
            self.list_hotpatch_resource_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_hotpatch_resource_result is not None:
            result['ListHotpatchResourceResult'] = self.list_hotpatch_resource_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListHotpatchResourceResult') is not None:
            temp_model = main_models.ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResult()
            self.list_hotpatch_resource_result = temp_model.from_map(m.get('ListHotpatchResourceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResult(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        hotpatch_resource_info: List[main_models.ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResultHotpatchResourceInfo] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.hotpatch_resource_info = hotpatch_resource_info
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.hotpatch_resource_info:
            for v1 in self.hotpatch_resource_info:
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

        result['HotpatchResourceInfo'] = []
        if self.hotpatch_resource_info is not None:
            for k1 in self.hotpatch_resource_info:
                result['HotpatchResourceInfo'].append(k1.to_map() if k1 else None)

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

        self.hotpatch_resource_info = []
        if m.get('HotpatchResourceInfo') is not None:
            for k1 in m.get('HotpatchResourceInfo'):
                temp_model = main_models.ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResultHotpatchResourceInfo()
                self.hotpatch_resource_info.append(temp_model.from_map(k1))

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

class ListMcubeHotpatchResourcesResponseBodyListHotpatchResourceResultHotpatchResourceInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        creator: str = None,
        download_url: str = None,
        file_size: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hotpatch_version: str = None,
        id: int = None,
        md_5: str = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_period: int = None,
        release_version: str = None,
        source_name: str = None,
    ):
        self.app_code = app_code
        self.creator = creator
        self.download_url = download_url
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hotpatch_version = hotpatch_version
        self.id = id
        self.md_5 = md_5
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_period = publish_period
        self.release_version = release_version
        self.source_name = source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.hotpatch_version is not None:
            result['HotpatchVersion'] = self.hotpatch_version

        if self.id is not None:
            result['Id'] = self.id

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HotpatchVersion') is not None:
            self.hotpatch_version = m.get('HotpatchVersion')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        return self

