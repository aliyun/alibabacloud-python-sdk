# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeNebulaTasksResponseBody(DaraModel):
    def __init__(
        self,
        list_mcube_nebula_task_result: main_models.ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mcube_nebula_task_result = list_mcube_nebula_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mcube_nebula_task_result:
            self.list_mcube_nebula_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_mcube_nebula_task_result is not None:
            result['ListMcubeNebulaTaskResult'] = self.list_mcube_nebula_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMcubeNebulaTaskResult') is not None:
            temp_model = main_models.ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult()
            self.list_mcube_nebula_task_result = temp_model.from_map(m.get('ListMcubeNebulaTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_task_info: List[main_models.ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo] = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_task_info = nebula_task_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_task_info:
            for v1 in self.nebula_task_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        result['NebulaTaskInfo'] = []
        if self.nebula_task_info is not None:
            for k1 in self.nebula_task_info:
                result['NebulaTaskInfo'].append(k1.to_map() if k1 else None)

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

        self.nebula_task_info = []
        if m.get('NebulaTaskInfo') is not None:
            for k1 in m.get('NebulaTaskInfo'):
                temp_model = main_models.ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo()
                self.nebula_task_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        biz_type: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_endtime_str: str = None,
        grey_num: int = None,
        grey_url: str = None,
        id: int = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        percent: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        release_version: str = None,
        status: int = None,
        sync_result: str = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.biz_type = biz_type
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_endtime_str = grey_endtime_str
        self.grey_num = grey_num
        self.grey_url = grey_url
        self.id = id
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.percent = percent
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.release_version = release_version
        self.status = status
        self.sync_result = sync_result
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
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

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_endtime_str is not None:
            result['GreyEndtimeStr'] = self.grey_endtime_str

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.grey_url is not None:
            result['GreyUrl'] = self.grey_url

        if self.id is not None:
            result['Id'] = self.id

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.percent is not None:
            result['Percent'] = self.percent

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

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_version is not None:
            result['TaskVersion'] = self.task_version

        if self.upgrade_notice_num is not None:
            result['UpgradeNoticeNum'] = self.upgrade_notice_num

        if self.upgrade_progress is not None:
            result['UpgradeProgress'] = self.upgrade_progress

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyEndtimeStr') is not None:
            self.grey_endtime_str = m.get('GreyEndtimeStr')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('GreyUrl') is not None:
            self.grey_url = m.get('GreyUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

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

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')

        if m.get('UpgradeNoticeNum') is not None:
            self.upgrade_notice_num = m.get('UpgradeNoticeNum')

        if m.get('UpgradeProgress') is not None:
            self.upgrade_progress = m.get('UpgradeProgress')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

