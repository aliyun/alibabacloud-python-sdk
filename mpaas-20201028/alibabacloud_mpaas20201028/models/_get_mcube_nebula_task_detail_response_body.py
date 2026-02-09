# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetMcubeNebulaTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        get_mcube_nebula_task_detail_result: main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_mcube_nebula_task_detail_result = get_mcube_nebula_task_detail_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_mcube_nebula_task_detail_result:
            self.get_mcube_nebula_task_detail_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_mcube_nebula_task_detail_result is not None:
            result['GetMcubeNebulaTaskDetailResult'] = self.get_mcube_nebula_task_detail_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetMcubeNebulaTaskDetailResult') is not None:
            temp_model = main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult()
            self.get_mcube_nebula_task_detail_result = temp_model.from_map(m.get('GetMcubeNebulaTaskDetailResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_task_detail: main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_task_detail = nebula_task_detail
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_task_detail:
            self.nebula_task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.nebula_task_detail is not None:
            result['NebulaTaskDetail'] = self.nebula_task_detail.to_map()

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

        if m.get('NebulaTaskDetail') is not None:
            temp_model = main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail()
            self.nebula_task_detail = temp_model.from_map(m.get('NebulaTaskDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        atomic: int = None,
        base_info_id: int = None,
        biz_type: str = None,
        creator: str = None,
        cronexpress: int = None,
        download_url: str = None,
        extra_data: str = None,
        file_size: str = None,
        full_repair: int = None,
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
        issue_desc: str = None,
        memo: str = None,
        modifier: str = None,
        oss_path: str = None,
        package_id: int = None,
        percent: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_period: int = None,
        publish_type: int = None,
        quick_rollback: int = None,
        release_version: str = None,
        rule_json_list: List[main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList] = None,
        source_id: str = None,
        source_name: str = None,
        source_type: str = None,
        status: int = None,
        sync_result: str = None,
        sync_type: int = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.atomic = atomic
        self.base_info_id = base_info_id
        self.biz_type = biz_type
        self.creator = creator
        self.cronexpress = cronexpress
        self.download_url = download_url
        self.extra_data = extra_data
        self.file_size = file_size
        self.full_repair = full_repair
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
        self.issue_desc = issue_desc
        self.memo = memo
        self.modifier = modifier
        self.oss_path = oss_path
        self.package_id = package_id
        self.percent = percent
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_period = publish_period
        self.publish_type = publish_type
        self.quick_rollback = quick_rollback
        self.release_version = release_version
        self.rule_json_list = rule_json_list
        self.source_id = source_id
        self.source_name = source_name
        self.source_type = source_type
        self.status = status
        self.sync_result = sync_result
        self.sync_type = sync_type
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        if self.rule_json_list:
            for v1 in self.rule_json_list:
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

        if self.atomic is not None:
            result['Atomic'] = self.atomic

        if self.base_info_id is not None:
            result['BaseInfoId'] = self.base_info_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.cronexpress is not None:
            result['Cronexpress'] = self.cronexpress

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.full_repair is not None:
            result['FullRepair'] = self.full_repair

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

        if self.issue_desc is not None:
            result['IssueDesc'] = self.issue_desc

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

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

        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.quick_rollback is not None:
            result['QuickRollback'] = self.quick_rollback

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k1 in self.rule_json_list:
                result['RuleJsonList'].append(k1.to_map() if k1 else None)

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result

        if self.sync_type is not None:
            result['SyncType'] = self.sync_type

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Atomic') is not None:
            self.atomic = m.get('Atomic')

        if m.get('BaseInfoId') is not None:
            self.base_info_id = m.get('BaseInfoId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Cronexpress') is not None:
            self.cronexpress = m.get('Cronexpress')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FullRepair') is not None:
            self.full_repair = m.get('FullRepair')

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

        if m.get('IssueDesc') is not None:
            self.issue_desc = m.get('IssueDesc')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

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

        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('QuickRollback') is not None:
            self.quick_rollback = m.get('QuickRollback')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k1 in m.get('RuleJsonList'):
                temp_model = main_models.GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k1))

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')

        if m.get('SyncType') is not None:
            self.sync_type = m.get('SyncType')

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

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList(DaraModel):
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

