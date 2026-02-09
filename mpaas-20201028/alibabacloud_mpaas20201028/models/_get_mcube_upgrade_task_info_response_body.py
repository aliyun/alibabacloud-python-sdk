# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetMcubeUpgradeTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        get_task_result: main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_task_result = get_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_task_result:
            self.get_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_task_result is not None:
            result['GetTaskResult'] = self.get_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetTaskResult') is not None:
            temp_model = main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult()
            self.get_task_result = temp_model.from_map(m.get('GetTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        task_info: main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        appstore_url: str = None,
        creater: str = None,
        creator: str = None,
        download_url: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        history_force: int = None,
        id: int = None,
        is_enterprise: int = None,
        is_official: int = None,
        is_rc: int = None,
        is_release: int = None,
        memo: str = None,
        modifier: str = None,
        net_type: str = None,
        os_version: str = None,
        package_info_id: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        qrcode_url: str = None,
        rule_json_list: List[main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList] = None,
        silent_type: int = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        upgrade_valid_time: int = None,
        whitelist: List[main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist] = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.appstore_url = appstore_url
        self.creater = creater
        self.creator = creator
        self.download_url = download_url
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.history_force = history_force
        self.id = id
        self.is_enterprise = is_enterprise
        self.is_official = is_official
        self.is_rc = is_rc
        self.is_release = is_release
        self.memo = memo
        self.modifier = modifier
        self.net_type = net_type
        self.os_version = os_version
        self.package_info_id = package_info_id
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.qrcode_url = qrcode_url
        self.rule_json_list = rule_json_list
        self.silent_type = silent_type
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.upgrade_valid_time = upgrade_valid_time
        self.whitelist = whitelist
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

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

        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url

        if self.creater is not None:
            result['Creater'] = self.creater

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.history_force is not None:
            result['HistoryForce'] = self.history_force

        if self.id is not None:
            result['Id'] = self.id

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.is_official is not None:
            result['IsOfficial'] = self.is_official

        if self.is_rc is not None:
            result['IsRc'] = self.is_rc

        if self.is_release is not None:
            result['IsRelease'] = self.is_release

        if self.memo is not None:
            result['Memo'] = self.memo

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

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.push_content is not None:
            result['PushContent'] = self.push_content

        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url

        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k1 in self.rule_json_list:
                result['RuleJsonList'].append(k1.to_map() if k1 else None)

        if self.silent_type is not None:
            result['SilentType'] = self.silent_type

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')

        if m.get('Creater') is not None:
            self.creater = m.get('Creater')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')

        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')

        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

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

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')

        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')

        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k1 in m.get('RuleJsonList'):
                temp_model = main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k1))

        if m.get('SilentType') is not None:
            self.silent_type = m.get('SilentType')

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
                temp_model = main_models.GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist()
                self.whitelist.append(temp_model.from_map(k1))

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        id: int = None,
        id_type: str = None,
        platform: str = None,
        status: int = None,
        user_type: str = None,
        white_list_count: int = None,
        white_list_name: str = None,
        whitelist_type: str = None,
    ):
        self.app_code = app_code
        self.id = id
        self.id_type = id_type
        self.platform = platform
        self.status = status
        self.user_type = user_type
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name
        self.whitelist_type = whitelist_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.status is not None:
            result['Status'] = self.status

        if self.user_type is not None:
            result['UserType'] = self.user_type

        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count

        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name

        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')

        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')

        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')

        return self

class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList(DaraModel):
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

