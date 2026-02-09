# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMcubeMiniTaskResponseBody(DaraModel):
    def __init__(
        self,
        query_mini_task_result: main_models.QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_mini_task_result = query_mini_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_mini_task_result:
            self.query_mini_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_mini_task_result is not None:
            result['QueryMiniTaskResult'] = self.query_mini_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryMiniTaskResult') is not None:
            temp_model = main_models.QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult()
            self.query_mini_task_result = temp_model.from_map(m.get('QueryMiniTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult(DaraModel):
    def __init__(
        self,
        mini_task_info: main_models.QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_task_info = mini_task_info
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mini_task_info:
            self.mini_task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mini_task_info is not None:
            result['MiniTaskInfo'] = self.mini_task_info.to_map()

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniTaskInfo') is not None:
            temp_model = main_models.QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo()
            self.mini_task_info = temp_model.from_map(m.get('MiniTaskInfo'))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        memo: str = None,
        package_id: int = None,
        platform: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        status: str = None,
        task_status: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.memo = memo
        self.package_id = package_id
        self.platform = platform
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.status = status
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.status is not None:
            result['Status'] = self.status

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

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

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        return self

