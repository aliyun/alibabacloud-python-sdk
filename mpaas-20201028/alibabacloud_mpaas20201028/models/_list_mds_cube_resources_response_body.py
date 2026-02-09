# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMdsCubeResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.ListMdsCubeResourcesResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.ListMdsCubeResourcesResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMdsCubeResourcesResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.ListMdsCubeResourcesResponseBodyResultContentData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.ListMdsCubeResourcesResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMdsCubeResourcesResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        content: main_models.ListMdsCubeResourcesResponseBodyResultContentDataContent = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.ListMdsCubeResourcesResponseBodyResultContentDataContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMdsCubeResourcesResponseBodyResultContentDataContent(DaraModel):
    def __init__(
        self,
        current_max_android_version: str = None,
        current_max_ios_version: str = None,
        first_page: bool = None,
        first_result: int = None,
        last_page: bool = None,
        list: List[main_models.ListMdsCubeResourcesResponseBodyResultContentDataContentList] = None,
        next_page: int = None,
        page_no: int = None,
        page_size: int = None,
        pre_page: int = None,
        total_count: int = None,
    ):
        self.current_max_android_version = current_max_android_version
        self.current_max_ios_version = current_max_ios_version
        self.first_page = first_page
        self.first_result = first_result
        self.last_page = last_page
        self.list = list
        self.next_page = next_page
        self.page_no = page_no
        self.page_size = page_size
        self.pre_page = pre_page
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_max_android_version is not None:
            result['CurrentMaxAndroidVersion'] = self.current_max_android_version

        if self.current_max_ios_version is not None:
            result['CurrentMaxIosVersion'] = self.current_max_ios_version

        if self.first_page is not None:
            result['FirstPage'] = self.first_page

        if self.first_result is not None:
            result['FirstResult'] = self.first_result

        if self.last_page is not None:
            result['LastPage'] = self.last_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentMaxAndroidVersion') is not None:
            self.current_max_android_version = m.get('CurrentMaxAndroidVersion')

        if m.get('CurrentMaxIosVersion') is not None:
            self.current_max_ios_version = m.get('CurrentMaxIosVersion')

        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')

        if m.get('FirstResult') is not None:
            self.first_result = m.get('FirstResult')

        if m.get('LastPage') is not None:
            self.last_page = m.get('LastPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListMdsCubeResourcesResponseBodyResultContentDataContentList()
                self.list.append(temp_model.from_map(k1))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMdsCubeResourcesResponseBodyResultContentDataContentList(DaraModel):
    def __init__(
        self,
        android_max_version: str = None,
        android_min_version: str = None,
        app_code: str = None,
        bin_file_md_5: str = None,
        bin_private_file_url: str = None,
        bin_public_file_url: str = None,
        extend_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ios_max_version: str = None,
        ios_min_version: str = None,
        json_private_file_url: str = None,
        json_public_file_url: str = None,
        min_cube_sdk_version: str = None,
        mock_data_download_url: str = None,
        operator: str = None,
        platform: str = None,
        preview_picture_url: str = None,
        resource_status: int = None,
        status: int = None,
        template_id: str = None,
        template_resource_desc: str = None,
        template_resource_version: str = None,
    ):
        self.android_max_version = android_max_version
        self.android_min_version = android_min_version
        self.app_code = app_code
        self.bin_file_md_5 = bin_file_md_5
        self.bin_private_file_url = bin_private_file_url
        self.bin_public_file_url = bin_public_file_url
        self.extend_info = extend_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.ios_max_version = ios_max_version
        self.ios_min_version = ios_min_version
        self.json_private_file_url = json_private_file_url
        self.json_public_file_url = json_public_file_url
        self.min_cube_sdk_version = min_cube_sdk_version
        self.mock_data_download_url = mock_data_download_url
        self.operator = operator
        self.platform = platform
        self.preview_picture_url = preview_picture_url
        self.resource_status = resource_status
        self.status = status
        self.template_id = template_id
        self.template_resource_desc = template_resource_desc
        self.template_resource_version = template_resource_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_max_version is not None:
            result['AndroidMaxVersion'] = self.android_max_version

        if self.android_min_version is not None:
            result['AndroidMinVersion'] = self.android_min_version

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.bin_file_md_5 is not None:
            result['BinFileMd5'] = self.bin_file_md_5

        if self.bin_private_file_url is not None:
            result['BinPrivateFileUrl'] = self.bin_private_file_url

        if self.bin_public_file_url is not None:
            result['BinPublicFileUrl'] = self.bin_public_file_url

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.ios_max_version is not None:
            result['IosMaxVersion'] = self.ios_max_version

        if self.ios_min_version is not None:
            result['IosMinVersion'] = self.ios_min_version

        if self.json_private_file_url is not None:
            result['JsonPrivateFileUrl'] = self.json_private_file_url

        if self.json_public_file_url is not None:
            result['JsonPublicFileUrl'] = self.json_public_file_url

        if self.min_cube_sdk_version is not None:
            result['MinCubeSdkVersion'] = self.min_cube_sdk_version

        if self.mock_data_download_url is not None:
            result['MockDataDownloadUrl'] = self.mock_data_download_url

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.preview_picture_url is not None:
            result['PreviewPictureUrl'] = self.preview_picture_url

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_resource_desc is not None:
            result['TemplateResourceDesc'] = self.template_resource_desc

        if self.template_resource_version is not None:
            result['TemplateResourceVersion'] = self.template_resource_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidMaxVersion') is not None:
            self.android_max_version = m.get('AndroidMaxVersion')

        if m.get('AndroidMinVersion') is not None:
            self.android_min_version = m.get('AndroidMinVersion')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('BinFileMd5') is not None:
            self.bin_file_md_5 = m.get('BinFileMd5')

        if m.get('BinPrivateFileUrl') is not None:
            self.bin_private_file_url = m.get('BinPrivateFileUrl')

        if m.get('BinPublicFileUrl') is not None:
            self.bin_public_file_url = m.get('BinPublicFileUrl')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IosMaxVersion') is not None:
            self.ios_max_version = m.get('IosMaxVersion')

        if m.get('IosMinVersion') is not None:
            self.ios_min_version = m.get('IosMinVersion')

        if m.get('JsonPrivateFileUrl') is not None:
            self.json_private_file_url = m.get('JsonPrivateFileUrl')

        if m.get('JsonPublicFileUrl') is not None:
            self.json_public_file_url = m.get('JsonPublicFileUrl')

        if m.get('MinCubeSdkVersion') is not None:
            self.min_cube_sdk_version = m.get('MinCubeSdkVersion')

        if m.get('MockDataDownloadUrl') is not None:
            self.mock_data_download_url = m.get('MockDataDownloadUrl')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PreviewPictureUrl') is not None:
            self.preview_picture_url = m.get('PreviewPictureUrl')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateResourceDesc') is not None:
            self.template_resource_desc = m.get('TemplateResourceDesc')

        if m.get('TemplateResourceVersion') is not None:
            self.template_resource_version = m.get('TemplateResourceVersion')

        return self

