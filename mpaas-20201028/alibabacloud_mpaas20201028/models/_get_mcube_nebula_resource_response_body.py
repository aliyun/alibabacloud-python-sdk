# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetMcubeNebulaResourceResponseBody(DaraModel):
    def __init__(
        self,
        get_nebula_resource_result: main_models.GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_nebula_resource_result = get_nebula_resource_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_nebula_resource_result:
            self.get_nebula_resource_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_nebula_resource_result is not None:
            result['GetNebulaResourceResult'] = self.get_nebula_resource_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetNebulaResourceResult') is not None:
            temp_model = main_models.GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult()
            self.get_nebula_resource_result = temp_model.from_map(m.get('GetNebulaResourceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_resource_info: main_models.GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_resource_info = nebula_resource_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_resource_info:
            self.nebula_resource_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.nebula_resource_info is not None:
            result['NebulaResourceInfo'] = self.nebula_resource_info.to_map()

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

        if m.get('NebulaResourceInfo') is not None:
            temp_model = main_models.GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo()
            self.nebula_resource_info = temp_model.from_map(m.get('NebulaResourceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        creator: str = None,
        download_url: str = None,
        extend_info: str = None,
        extra_data: str = None,
        fallback_base_url: str = None,
        file_size: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        id: int = None,
        install_type: int = None,
        main_url: str = None,
        memo: str = None,
        meta_id: int = None,
        modifier: str = None,
        package_type: int = None,
        platform: str = None,
        publish_period: int = None,
        resource_type: str = None,
        status: int = None,
        vhost: str = None,
    ):
        self.app_code = app_code
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.creator = creator
        self.download_url = download_url
        self.extend_info = extend_info
        self.extra_data = extra_data
        self.fallback_base_url = fallback_base_url
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.id = id
        self.install_type = install_type
        self.main_url = main_url
        self.memo = memo
        self.meta_id = meta_id
        self.modifier = modifier
        self.package_type = package_type
        self.platform = platform
        self.publish_period = publish_period
        self.resource_type = resource_type
        self.status = status
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max

        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.fallback_base_url is not None:
            result['FallbackBaseUrl'] = self.fallback_base_url

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.h_5version is not None:
            result['H5Version'] = self.h_5version

        if self.id is not None:
            result['Id'] = self.id

        if self.install_type is not None:
            result['InstallType'] = self.install_type

        if self.main_url is not None:
            result['MainUrl'] = self.main_url

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.meta_id is not None:
            result['MetaId'] = self.meta_id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')

        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('FallbackBaseUrl') is not None:
            self.fallback_base_url = m.get('FallbackBaseUrl')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')

        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('MetaId') is not None:
            self.meta_id = m.get('MetaId')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        return self

