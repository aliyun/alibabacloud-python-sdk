# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMcubeHotpatchTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        query_hotpatch_task_detail_result: main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_hotpatch_task_detail_result = query_hotpatch_task_detail_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_hotpatch_task_detail_result:
            self.query_hotpatch_task_detail_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_hotpatch_task_detail_result is not None:
            result['QueryHotpatchTaskDetailResult'] = self.query_hotpatch_task_detail_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryHotpatchTaskDetailResult') is not None:
            temp_model = main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResult()
            self.query_hotpatch_task_detail_result = temp_model.from_map(m.get('QueryHotpatchTaskDetailResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        hotpatch_task_detail: main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetail = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.hotpatch_task_detail = hotpatch_task_detail
        # Id of the request
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.hotpatch_task_detail:
            self.hotpatch_task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.hotpatch_task_detail is not None:
            result['HotpatchTaskDetail'] = self.hotpatch_task_detail.to_map()

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

        if m.get('HotpatchTaskDetail') is not None:
            temp_model = main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetail()
            self.hotpatch_task_detail = temp_model.from_map(m.get('HotpatchTaskDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetail(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        base_info_id: int = None,
        bundles: List[str] = None,
        creator: str = None,
        download_url: str = None,
        file_size: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        md_5: str = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_period: int = None,
        publish_type: int = None,
        quick_rollback: int = None,
        release_version: str = None,
        rule_json_list: List[main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailRuleJsonList] = None,
        source_name: str = None,
        task_status: int = None,
        task_version: int = None,
        whitelist: List[main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailWhitelist] = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.base_info_id = base_info_id
        self.bundles = bundles
        self.creator = creator
        self.download_url = download_url
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.md_5 = md_5
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_period = publish_period
        self.publish_type = publish_type
        self.quick_rollback = quick_rollback
        self.release_version = release_version
        self.rule_json_list = rule_json_list
        self.source_name = source_name
        self.task_status = task_status
        self.task_version = task_version
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

        if self.base_info_id is not None:
            result['BaseInfoId'] = self.base_info_id

        if self.bundles is not None:
            result['Bundles'] = self.bundles

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.id is not None:
            result['Id'] = self.id

        if self.md_5 is not None:
            result['Md5'] = self.md_5

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

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_version is not None:
            result['TaskVersion'] = self.task_version

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

        if m.get('BaseInfoId') is not None:
            self.base_info_id = m.get('BaseInfoId')

        if m.get('Bundles') is not None:
            self.bundles = m.get('Bundles')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

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
                temp_model = main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k1))

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')

        self.whitelist = []
        if m.get('Whitelist') is not None:
            for k1 in m.get('Whitelist'):
                temp_model = main_models.QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailWhitelist()
                self.whitelist.append(temp_model.from_map(k1))

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailWhitelist(DaraModel):
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

class QueryMcubeHotpatchTaskDetailResponseBodyQueryHotpatchTaskDetailResultHotpatchTaskDetailRuleJsonList(DaraModel):
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

