# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20200710 import models as main_models
from darabonba.model import DaraModel

class ListMcubeUpgradeTasksResponseBody(DaraModel):
    def __init__(
        self,
        list_task_result: main_models.ListMcubeUpgradeTasksResponseBodyListTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_task_result = list_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_task_result:
            self.list_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_task_result is not None:
            result['ListTaskResult'] = self.list_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListTaskResult') is not None:
            temp_model = main_models.ListMcubeUpgradeTasksResponseBodyListTaskResult()
            self.list_task_result = temp_model.from_map(m.get('ListTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeUpgradeTasksResponseBodyListTaskResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        task_info: List[main_models.ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo] = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            for v1 in self.task_info:
                 if v1:
                    v1.validate()

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

        result['TaskInfo'] = []
        if self.task_info is not None:
            for k1 in self.task_info:
                result['TaskInfo'].append(k1.to_map() if k1 else None)

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

        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k1 in m.get('TaskInfo'):
                temp_model = main_models.ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo()
                self.task_info.append(temp_model.from_map(k1))

        return self

class ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_num: int = None,
        history_force: int = None,
        id: int = None,
        is_enterprise: int = None,
        memo: str = None,
        modifier: str = None,
        package_info_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_num = grey_num
        self.history_force = history_force
        self.id = id
        self.is_enterprise = is_enterprise
        self.memo = memo
        self.modifier = modifier
        self.package_info_id = package_info_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.whitelist_ids = whitelist_ids

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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.history_force is not None:
            result['HistoryForce'] = self.history_force

        if self.id is not None:
            result['Id'] = self.id

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id

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

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')

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

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

