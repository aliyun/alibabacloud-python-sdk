# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeNebulaTaskRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
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
        res_ids: str = None,
        serial_version_uid: int = None,
        status: int = None,
        sync_mode: str = None,
        sync_result: str = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        tenant_id: str = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
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
        self.res_ids = res_ids
        self.serial_version_uid = serial_version_uid
        self.status = status
        self.sync_mode = sync_mode
        self.sync_result = sync_result
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.tenant_id = tenant_id
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_id is not None:
            result['AppId'] = self.app_id

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

        if self.res_ids is not None:
            result['ResIds'] = self.res_ids

        if self.serial_version_uid is not None:
            result['SerialVersionUID'] = self.serial_version_uid

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

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

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

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

        if m.get('ResIds') is not None:
            self.res_ids = m.get('ResIds')

        if m.get('SerialVersionUID') is not None:
            self.serial_version_uid = m.get('SerialVersionUID')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

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

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpgradeNoticeNum') is not None:
            self.upgrade_notice_num = m.get('UpgradeNoticeNum')

        if m.get('UpgradeProgress') is not None:
            self.upgrade_progress = m.get('UpgradeProgress')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

