# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeHotpatchTasksResponseBody(DaraModel):
    def __init__(
        self,
        list_hotpatch_tasks_result: main_models.ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_hotpatch_tasks_result = list_hotpatch_tasks_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_hotpatch_tasks_result:
            self.list_hotpatch_tasks_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_hotpatch_tasks_result is not None:
            result['ListHotpatchTasksResult'] = self.list_hotpatch_tasks_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListHotpatchTasksResult') is not None:
            temp_model = main_models.ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResult()
            self.list_hotpatch_tasks_result = temp_model.from_map(m.get('ListHotpatchTasksResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        hotpatch_task_info: List[main_models.ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResultHotpatchTaskInfo] = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.hotpatch_task_info = hotpatch_task_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.hotpatch_task_info:
            for v1 in self.hotpatch_task_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        result['HotpatchTaskInfo'] = []
        if self.hotpatch_task_info is not None:
            for k1 in self.hotpatch_task_info:
                result['HotpatchTaskInfo'].append(k1.to_map() if k1 else None)

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

        self.hotpatch_task_info = []
        if m.get('HotpatchTaskInfo') is not None:
            for k1 in m.get('HotpatchTaskInfo'):
                temp_model = main_models.ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResultHotpatchTaskInfo()
                self.hotpatch_task_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMcubeHotpatchTasksResponseBodyListHotpatchTasksResultHotpatchTaskInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        release_version: str = None,
        res_ids: str = None,
        task_status: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.release_version = release_version
        self.res_ids = res_ids
        self.task_status = task_status
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

        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.id is not None:
            result['Id'] = self.id

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

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.res_ids is not None:
            result['ResIds'] = self.res_ids

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

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

        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResIds') is not None:
            self.res_ids = m.get('ResIds')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

