# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMdsUpgradeTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContent = None,
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
            temp_model = main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMdsUpgradeTaskDetailResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentData = None,
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
            temp_model = main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMdsUpgradeTaskDetailResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        content: main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent = None,
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
            temp_model = main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent()
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

class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        appstoreurl: str = None,
        channel_contains: str = None,
        channel_excludes: str = None,
        city_contains: str = None,
        city_excludes: str = None,
        creator: str = None,
        device_grey_num: int = None,
        device_percent: int = None,
        download_url: str = None,
        execution_order: int = None,
        gmt_create_str: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_notice: int = None,
        grey_num: int = None,
        grey_uv: int = None,
        id: int = None,
        inner_version: str = None,
        is_enterprise: int = None,
        is_official: int = None,
        is_push: int = None,
        is_rc: int = None,
        is_release: int = None,
        memo: str = None,
        mobile_model_contains: str = None,
        mobile_model_excludes: str = None,
        modifier: str = None,
        net_type: str = None,
        os_version: str = None,
        package_info_id: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        qrcode_url: str = None,
        release_type: str = None,
        rule_json_list: List[main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList] = None,
        silent_type: int = None,
        sync_mode: str = None,
        sync_result: str = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        upgrade_valid_time: int = None,
        whitelist: List[main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist] = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.appstoreurl = appstoreurl
        self.channel_contains = channel_contains
        self.channel_excludes = channel_excludes
        self.city_contains = city_contains
        self.city_excludes = city_excludes
        self.creator = creator
        self.device_grey_num = device_grey_num
        self.device_percent = device_percent
        self.download_url = download_url
        self.execution_order = execution_order
        self.gmt_create_str = gmt_create_str
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_notice = grey_notice
        self.grey_num = grey_num
        self.grey_uv = grey_uv
        self.id = id
        self.inner_version = inner_version
        self.is_enterprise = is_enterprise
        self.is_official = is_official
        self.is_push = is_push
        self.is_rc = is_rc
        self.is_release = is_release
        self.memo = memo
        self.mobile_model_contains = mobile_model_contains
        self.mobile_model_excludes = mobile_model_excludes
        self.modifier = modifier
        self.net_type = net_type
        self.os_version = os_version
        self.package_info_id = package_info_id
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.qrcode_url = qrcode_url
        self.release_type = release_type
        self.rule_json_list = rule_json_list
        self.silent_type = silent_type
        self.sync_mode = sync_mode
        self.sync_result = sync_result
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.upgrade_valid_time = upgrade_valid_time
        self.whitelist = whitelist
        self.whitelist_ids = whitelist_ids

    def validate(self):
        if self.rule_json_list:
            for v1 in self.rule_json_list:
                 if v1:
                    v1.validate()
        if self.whitelist:
            for v1 in self.whitelist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.appstoreurl is not None:
            result['Appstoreurl'] = self.appstoreurl

        if self.channel_contains is not None:
            result['ChannelContains'] = self.channel_contains

        if self.channel_excludes is not None:
            result['ChannelExcludes'] = self.channel_excludes

        if self.city_contains is not None:
            result['CityContains'] = self.city_contains

        if self.city_excludes is not None:
            result['CityExcludes'] = self.city_excludes

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.device_grey_num is not None:
            result['DeviceGreyNum'] = self.device_grey_num

        if self.device_percent is not None:
            result['DevicePercent'] = self.device_percent

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.execution_order is not None:
            result['ExecutionOrder'] = self.execution_order

        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_notice is not None:
            result['GreyNotice'] = self.grey_notice

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.grey_uv is not None:
            result['GreyUv'] = self.grey_uv

        if self.id is not None:
            result['Id'] = self.id

        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.is_official is not None:
            result['IsOfficial'] = self.is_official

        if self.is_push is not None:
            result['IsPush'] = self.is_push

        if self.is_rc is not None:
            result['IsRc'] = self.is_rc

        if self.is_release is not None:
            result['IsRelease'] = self.is_release

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.mobile_model_contains is not None:
            result['MobileModelContains'] = self.mobile_model_contains

        if self.mobile_model_excludes is not None:
            result['MobileModelExcludes'] = self.mobile_model_excludes

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.push_content is not None:
            result['PushContent'] = self.push_content

        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k1 in self.rule_json_list:
                result['RuleJsonList'].append(k1.to_map() if k1 else None)

        if self.silent_type is not None:
            result['SilentType'] = self.silent_type

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        if self.upgrade_valid_time is not None:
            result['UpgradeValidTime'] = self.upgrade_valid_time

        result['Whitelist'] = []
        if self.whitelist is not None:
            for k1 in self.whitelist:
                result['Whitelist'].append(k1.to_map() if k1 else None)

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Appstoreurl') is not None:
            self.appstoreurl = m.get('Appstoreurl')

        if m.get('ChannelContains') is not None:
            self.channel_contains = m.get('ChannelContains')

        if m.get('ChannelExcludes') is not None:
            self.channel_excludes = m.get('ChannelExcludes')

        if m.get('CityContains') is not None:
            self.city_contains = m.get('CityContains')

        if m.get('CityExcludes') is not None:
            self.city_excludes = m.get('CityExcludes')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeviceGreyNum') is not None:
            self.device_grey_num = m.get('DeviceGreyNum')

        if m.get('DevicePercent') is not None:
            self.device_percent = m.get('DevicePercent')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExecutionOrder') is not None:
            self.execution_order = m.get('ExecutionOrder')

        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNotice') is not None:
            self.grey_notice = m.get('GreyNotice')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('GreyUv') is not None:
            self.grey_uv = m.get('GreyUv')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')

        if m.get('IsPush') is not None:
            self.is_push = m.get('IsPush')

        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')

        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('MobileModelContains') is not None:
            self.mobile_model_contains = m.get('MobileModelContains')

        if m.get('MobileModelExcludes') is not None:
            self.mobile_model_excludes = m.get('MobileModelExcludes')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')

        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k1 in m.get('RuleJsonList'):
                temp_model = main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k1))

        if m.get('SilentType') is not None:
            self.silent_type = m.get('SilentType')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        if m.get('UpgradeValidTime') is not None:
            self.upgrade_valid_time = m.get('UpgradeValidTime')

        self.whitelist = []
        if m.get('Whitelist') is not None:
            for k1 in m.get('Whitelist'):
                temp_model = main_models.QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist()
                self.whitelist.append(temp_model.from_map(k1))

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        business: str = None,
        gmt_modified: str = None,
        id: int = None,
        id_type: str = None,
        platform: str = None,
        status: int = None,
        white_list_count: int = None,
        white_list_name: str = None,
    ):
        self.app_code = app_code
        self.business = business
        self.gmt_modified = gmt_modified
        self.id = id
        self.id_type = id_type
        self.platform = platform
        self.status = status
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.business is not None:
            result['Business'] = self.business

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.status is not None:
            result['Status'] = self.status

        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count

        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')

        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')

        return self

class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList(DaraModel):
    def __init__(
        self,
        operation: str = None,
        rule_element: str = None,
        rule_type: str = None,
        value: str = None,
    ):
        self.operation = operation
        self.rule_element = rule_element
        self.rule_type = rule_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['Operation'] = self.operation

        if self.rule_element is not None:
            result['RuleElement'] = self.rule_element

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('RuleElement') is not None:
            self.rule_element = m.get('RuleElement')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

