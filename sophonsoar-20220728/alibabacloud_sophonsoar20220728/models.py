# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BatchModifyInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        active: int = None,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # Specifies whether to start or stop the playbook.
        # 
        # *   **0**: stops the playbook.
        # *   **1**: starts the playbook.
        # 
        # This parameter is required.
        self.active = active
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The playbook UUID. If you want to specify multiple playbooks, separate the playbook UUIDs with commas (,).
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class BatchModifyInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchModifyInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchModifyInstanceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchModifyInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComparePlaybooksRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        new_playbook_release_id: int = None,
        old_playbook_release_id: int = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the second version.
        # 
        # >  You can call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation to query the IDs of versions. The system automatically generates IDs for new versions.
        # 
        # This parameter is required.
        self.new_playbook_release_id = new_playbook_release_id
        # The ID of the first version.
        # 
        # >  You can call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation to query the IDs of versions. The system automatically generates IDs for new versions.
        # 
        # This parameter is required.
        self.old_playbook_release_id = old_playbook_release_id
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_playbook_release_id is not None:
            result['NewPlaybookReleaseId'] = self.new_playbook_release_id
        if self.old_playbook_release_id is not None:
            result['OldPlaybookReleaseId'] = self.old_playbook_release_id
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewPlaybookReleaseId') is not None:
            self.new_playbook_release_id = m.get('NewPlaybookReleaseId')
        if m.get('OldPlaybookReleaseId') is not None:
            self.old_playbook_release_id = m.get('OldPlaybookReleaseId')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ComparePlaybooksResponseBodyCompareResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        new: bool = None,
        same: bool = None,
    ):
        # The description of the comparison result.
        self.description = description
        # Indicates whether the second version provides more information than the first version. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.new = new
        # Indicates whether the configurations of the two versions are the same. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.same = same

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.new is not None:
            result['New'] = self.new
        if self.same is not None:
            result['Same'] = self.same
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('New') is not None:
            self.new = m.get('New')
        if m.get('Same') is not None:
            self.same = m.get('Same')
        return self


class ComparePlaybooksResponseBody(TeaModel):
    def __init__(
        self,
        compare_result: ComparePlaybooksResponseBodyCompareResult = None,
        request_id: str = None,
    ):
        # The comparison result.
        self.compare_result = compare_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compare_result:
            self.compare_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_result is not None:
            result['CompareResult'] = self.compare_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareResult') is not None:
            temp_model = ComparePlaybooksResponseBodyCompareResult()
            self.compare_result = temp_model.from_map(m['CompareResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ComparePlaybooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ComparePlaybooksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ComparePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertPlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
        taskflow: str = None,
    ):
        # Language type for request and response messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for
        # View type. Values:
        # 
        # - 0: Current Alibaba Cloud account view.
        # - 1: View for all accounts under the enterprise.
        self.role_type = role_type
        # XML configuration information for playbook orchestration.
        # 
        # This parameter is required.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class ConvertPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        request_id: str = None,
    ):
        # The configurations.
        self.config = config
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request, and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConvertPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyPlaybookRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        lang: str = None,
        release_version: str = None,
        role_for: int = None,
        role_type: str = None,
        source_playbook_uuid: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.lang = lang
        self.release_version = release_version
        self.role_for = role_for
        self.role_type = role_type
        # This parameter is required.
        self.source_playbook_uuid = source_playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.source_playbook_uuid is not None:
            result['SourcePlaybookUuid'] = self.source_playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('SourcePlaybookUuid') is not None:
            self.source_playbook_uuid = m.get('SourcePlaybookUuid')
        return self


class CopyPlaybookResponseBodyData(TeaModel):
    def __init__(
        self,
        active: int = None,
        description: str = None,
        display_name: str = None,
        fail_num: int = None,
        fail_rate: float = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        history_md_5: int = None,
        input_params: str = None,
        last_runtime: int = None,
        logic_release_taskflow_md_5: str = None,
        output_params: str = None,
        own_type: str = None,
        permission: int = None,
        playbook_status: int = None,
        playbook_uuid: str = None,
        succ_num: int = None,
        tenant_id: str = None,
    ):
        self.active = active
        self.description = description
        self.display_name = display_name
        self.fail_num = fail_num
        self.fail_rate = fail_rate
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.history_md_5 = history_md_5
        self.input_params = input_params
        self.last_runtime = last_runtime
        self.logic_release_taskflow_md_5 = logic_release_taskflow_md_5
        self.output_params = output_params
        self.own_type = own_type
        self.permission = permission
        self.playbook_status = playbook_status
        self.playbook_uuid = playbook_uuid
        self.succ_num = succ_num
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.fail_num is not None:
            result['FailNum'] = self.fail_num
        if self.fail_rate is not None:
            result['FailRate'] = self.fail_rate
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.history_md_5 is not None:
            result['HistoryMd5'] = self.history_md_5
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime
        if self.logic_release_taskflow_md_5 is not None:
            result['LogicReleaseTaskflowMd5'] = self.logic_release_taskflow_md_5
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.playbook_status is not None:
            result['PlaybookStatus'] = self.playbook_status
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.succ_num is not None:
            result['SuccNum'] = self.succ_num
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')
        if m.get('FailRate') is not None:
            self.fail_rate = m.get('FailRate')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HistoryMd5') is not None:
            self.history_md_5 = m.get('HistoryMd5')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')
        if m.get('LogicReleaseTaskflowMd5') is not None:
            self.logic_release_taskflow_md_5 = m.get('LogicReleaseTaskflowMd5')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('PlaybookStatus') is not None:
            self.playbook_status = m.get('PlaybookStatus')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('SuccNum') is not None:
            self.succ_num = m.get('SuccNum')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CopyPlaybookResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CopyPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        data: CopyPlaybookResponseBodyData = None,
        page: CopyPlaybookResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CopyPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Page') is not None:
            temp_model = CopyPlaybookResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePlaybookRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        lang: str = None,
        taskflow_type: str = None,
    ):
        # Description of the playbook.
        self.description = description
        # Name of the playbook.
        # 
        # This parameter is required.
        self.display_name = display_name
        # Language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # Playbook TaskFlow type.
        # - **x6** : x6
        # - **bpmn**: bpmn
        self.taskflow_type = taskflow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.taskflow_type is not None:
            result['TaskflowType'] = self.taskflow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskflowType') is not None:
            self.taskflow_type = m.get('TaskflowType')
        return self


class CreatePlaybookResponseBodyData(TeaModel):
    def __init__(
        self,
        playbook_uuid: str = None,
    ):
        # UUID of the newly created playbook.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class CreatePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        data: CreatePlaybookResponseBodyData = None,
        request_id: str = None,
    ):
        # The result of the creation.
        self.data = data
        # The ID of this call request, a unique identifier generated by Alibaba Cloud for this request, which can be used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugPlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        record: str = None,
        taskflow: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The input parameters that you use to debug the playbook. You can define the parameters based on your business requirements.
        self.record = record
        # The XML configuration of the playbook.
        # 
        # >  You can call the [DescribePlaybook](~~DescribePlaybook~~) operation to query the XML configuration of the playbook.
        # 
        # This parameter is required.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.record is not None:
            result['Record'] = self.record
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class DebugPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        request_uuid: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The UUID of the debugging task. You can use the UUID to query the result and other details of the debugging task.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DebugPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DebugPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentAssetRequest(TeaModel):
    def __init__(
        self,
        asset_id: int = None,
        lang: str = None,
    ):
        # The ID of the asset.
        # 
        # >  You can call the [DescribeComponentAssets](~~DescribeComponentAssets~~) operation to query the ID.
        # 
        # This parameter is required.
        self.asset_id = asset_id
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteComponentAssetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteComponentAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteComponentAssetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DeletePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentAssetFormRequest(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        lang: str = None,
    ):
        # The component name.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentAssetFormResponseBody(TeaModel):
    def __init__(
        self,
        component_asset_form: str = None,
        request_id: str = None,
    ):
        # The metadata of the asset in the component. The value is a JSON array and contains the following fields:
        # 
        # *   **name**: the parameter name.
        # *   **defaultValue**: the default parameter value.
        # *   **description**: the parameter description.
        # *   **required**: indicates whether the parameter is required. Valid values: **true** and **false**.
        self.component_asset_form = component_asset_form
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_asset_form is not None:
            result['ComponentAssetForm'] = self.component_asset_form
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetForm') is not None:
            self.component_asset_form = m.get('ComponentAssetForm')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentAssetFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentAssetFormResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentAssetFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentAssetsRequest(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        lang: str = None,
    ):
        # The name of the component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentAssetsResponseBodyComponentAssets(TeaModel):
    def __init__(
        self,
        asset_uuid: str = None,
        componentname: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        params: str = None,
    ):
        # The UUID of the asset.
        self.asset_uuid = asset_uuid
        # The name of the component to which the asset belongs.
        self.componentname = componentname
        # The time when the asset was created. The time is in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the asset was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The UUID of the asset.
        self.id = id
        # The name of the asset.
        self.name = name
        # The configurations of the asset in the JSON string format. DescribeComponentAssetForm
        # 
        # >  For more information, see [DescribeComponentAssetForm](~~DescribeComponentAssetForm~~).
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_uuid is not None:
            result['AssetUuid'] = self.asset_uuid
        if self.componentname is not None:
            result['Componentname'] = self.componentname
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetUuid') is not None:
            self.asset_uuid = m.get('AssetUuid')
        if m.get('Componentname') is not None:
            self.componentname = m.get('Componentname')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class DescribeComponentAssetsResponseBody(TeaModel):
    def __init__(
        self,
        component_assets: List[DescribeComponentAssetsResponseBodyComponentAssets] = None,
        request_id: str = None,
    ):
        # The information about the assets.
        self.component_assets = component_assets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.component_assets:
            for k in self.component_assets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentAssets'] = []
        if self.component_assets is not None:
            for k in self.component_assets:
                result['ComponentAssets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_assets = []
        if m.get('ComponentAssets') is not None:
            for k in m.get('ComponentAssets'):
                temp_model = DescribeComponentAssetsResponseBodyComponentAssets()
                self.component_assets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentAssetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeComponentListResponseBody(TeaModel):
    def __init__(
        self,
        components: str = None,
        request_id: str = None,
    ):
        # The information about the components. The value is a JSON array.
        self.components = components
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components is not None:
            result['Components'] = self.components
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentPlaybookRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeComponentPlaybookResponseBodyPlaybooks(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        input_params: str = None,
    ):
        # The description of the predefined component.
        self.description = description
        # The name of the predefined component.
        self.display_name = display_name
        # The input parameter configuration of the playbook. The value is a JSON array.
        # 
        # >  For more information, see [DescribePlaybookInputOutput](~~DescribePlaybookInputOutput~~).
        self.input_params = input_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        return self


class DescribeComponentPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        playbooks: List[DescribeComponentPlaybookResponseBodyPlaybooks] = None,
        request_id: str = None,
    ):
        # The information about the predefined components.
        self.playbooks = playbooks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbooks:
            for k in self.playbooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k in self.playbooks:
                result['Playbooks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k in m.get('Playbooks'):
                temp_model = DescribeComponentPlaybookResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentsJsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeComponentsJsResponseBody(TeaModel):
    def __init__(
        self,
        components_js: str = None,
        request_id: str = None,
    ):
        # The configuration of the JavaScript file for the component.
        self.components_js = components_js
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components_js is not None:
            result['ComponentsJs'] = self.components_js
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentsJs') is not None:
            self.components_js = m.get('ComponentsJs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeComponentsJsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentsJsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentsJsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistinctReleasesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
        taskflow_md_5: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The MD5 value of the playbook XML configuration.
        self.taskflow_md_5 = taskflow_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribeDistinctReleasesResponseBodyRecords(TeaModel):
    def __init__(
        self,
        description: str = None,
        taskflow_md_5: str = None,
        taskflow_type: str = None,
    ):
        # The version description.
        self.description = description
        # The MD5 value of the version XML configuration.
        self.taskflow_md_5 = taskflow_md_5
        # The format of the playbook. Valid values:
        # 
        # *   **xml**: XML format.
        # *   **x6**: JSON format.
        self.taskflow_type = taskflow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        if self.taskflow_type is not None:
            result['TaskflowType'] = self.taskflow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        if m.get('TaskflowType') is not None:
            self.taskflow_type = m.get('TaskflowType')
        return self


class DescribeDistinctReleasesResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeDistinctReleasesResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The information about versions.
        self.records = records
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDistinctReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDistinctReleasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDistinctReleasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDistinctReleasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnumItemsRequest(TeaModel):
    def __init__(
        self,
        enum_type: str = None,
        lang: str = None,
    ):
        # The type of the enumeration item. Valid values:
        # 
        # *   **process**: scenarios
        # 
        # This parameter is required.
        self.enum_type = enum_type
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enum_type is not None:
            result['EnumType'] = self.enum_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnumType') is not None:
            self.enum_type = m.get('EnumType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeEnumItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the enumeration item.
        self.key = key
        # The value of the enumeration item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEnumItemsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeEnumItemsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The information about the enumeration item.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEnumItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnumItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEnumItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEnumItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExecutePlaybooksRequest(TeaModel):
    def __init__(
        self,
        input_mode: str = None,
        lang: str = None,
        param_type: str = None,
        playbook_name: str = None,
        uuid: str = None,
    ):
        # The entity type of the script input parameter. When you want to query multiple entity types, separate them with commas.
        # - **ip**: IP entity.
        # - **file**: file entity.
        # - **process**: process entity.
        # - **incident**: incident entity.
        self.input_mode = input_mode
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The input parameter type of the playbook.
        # 
        # *   **template-ip**\
        # *   **template-file**\
        # *   **template-process**\
        # *   **custom**\
        self.param_type = param_type
        # The playbook name. Fuzzy search is supported.
        self.playbook_name = playbook_name
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_mode is not None:
            result['InputMode'] = self.input_mode
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputMode') is not None:
            self.input_mode = m.get('InputMode')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeExecutePlaybooksResponseBodyPlaybookMetrics(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        param_config: str = None,
        param_type: str = None,
        uuid: str = None,
    ):
        # The playbook description.
        self.description = description
        # The playbook name.
        self.display_name = display_name
        # The configuration of the input parameter. The value is a JSON array.
        # 
        # >  For more information, see [DescribePlaybookInputOutput](~~DescribePlaybookInputOutput~~).
        self.param_config = param_config
        # The input parameter type of the playbook.
        # 
        # *   **template-ip**\
        # *   **template-file**\
        # *   **template-process**\
        # *   **custom**\
        self.param_type = param_type
        # The playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.param_config is not None:
            result['ParamConfig'] = self.param_config
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParamConfig') is not None:
            self.param_config = m.get('ParamConfig')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeExecutePlaybooksResponseBody(TeaModel):
    def __init__(
        self,
        playbook_metrics: List[DescribeExecutePlaybooksResponseBodyPlaybookMetrics] = None,
        request_id: str = None,
    ):
        # The playbook.
        self.playbook_metrics = playbook_metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_metrics:
            for k in self.playbook_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PlaybookMetrics'] = []
        if self.playbook_metrics is not None:
            for k in self.playbook_metrics:
                result['PlaybookMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.playbook_metrics = []
        if m.get('PlaybookMetrics') is not None:
            for k in m.get('PlaybookMetrics'):
                temp_model = DescribeExecutePlaybooksResponseBodyPlaybookMetrics()
                self.playbook_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExecutePlaybooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExecutePlaybooksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeExecutePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFieldRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        query_key: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The key of the global configuration. Valid values:
        # 
        # *   **soar_filed_tags**: queries the input template of the playbook.
        # 
        # This parameter is required.
        self.query_key = query_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        return self


class DescribeFieldResponseBody(TeaModel):
    def __init__(
        self,
        fields: str = None,
        name: str = None,
        request_id: str = None,
    ):
        # The configuration content.
        self.fields = fields
        # The name of the global configuration.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFieldResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupProductionsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        self.lang = lang
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeGroupProductionsResponseBodyDataProductionsPolicyList(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        type: str = None,
    ):
        self.policy_name = policy_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeGroupProductionsResponseBodyDataProductions(TeaModel):
    def __init__(
        self,
        code: str = None,
        default_domain: str = None,
        default_version: str = None,
        description: str = None,
        full_domains: List[str] = None,
        group: str = None,
        name: str = None,
        policy_list: List[DescribeGroupProductionsResponseBodyDataProductionsPolicyList] = None,
        ram_code: str = None,
        short_name: str = None,
        source: str = None,
        versions: List[str] = None,
    ):
        self.code = code
        self.default_domain = default_domain
        self.default_version = default_version
        self.description = description
        self.full_domains = full_domains
        self.group = group
        self.name = name
        self.policy_list = policy_list
        self.ram_code = ram_code
        self.short_name = short_name
        self.source = source
        self.versions = versions

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.full_domains is not None:
            result['FullDomains'] = self.full_domains
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['PolicyList'].append(k.to_map() if k else None)
        if self.ram_code is not None:
            result['RamCode'] = self.ram_code
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.source is not None:
            result['Source'] = self.source
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FullDomains') is not None:
            self.full_domains = m.get('FullDomains')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k in m.get('PolicyList'):
                temp_model = DescribeGroupProductionsResponseBodyDataProductionsPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('RamCode') is not None:
            self.ram_code = m.get('RamCode')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class DescribeGroupProductionsResponseBodyData(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        productions: List[DescribeGroupProductionsResponseBodyDataProductions] = None,
    ):
        self.group_name = group_name
        self.productions = productions

    def validate(self):
        if self.productions:
            for k in self.productions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        result['Productions'] = []
        if self.productions is not None:
            for k in self.productions:
                result['Productions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        self.productions = []
        if m.get('Productions') is not None:
            for k in m.get('Productions'):
                temp_model = DescribeGroupProductionsResponseBodyDataProductions()
                self.productions.append(temp_model.from_map(k))
        return self


class DescribeGroupProductionsResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGroupProductionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeGroupProductionsResponseBodyData] = None,
        page: DescribeGroupProductionsResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeGroupProductionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            temp_model = DescribeGroupProductionsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGroupProductionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGroupProductionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGroupProductionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLatestRecordSchemaRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        component_name: str = None,
        node_name: str = None,
        output_fields: List[str] = None,
    ):
        # The action name of the component.
        self.action_name = action_name
        # The name of the component.
        self.component_name = component_name
        # The name of the node.
        self.node_name = node_name
        # The output fields.
        self.output_fields = output_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.output_fields is not None:
            result['OutputFields'] = self.output_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OutputFields') is not None:
            self.output_fields = m.get('OutputFields')
        return self


class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema(TeaModel):
    def __init__(
        self,
        node_schema: List[DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema] = None,
    ):
        # The structure information.
        self.node_schema = node_schema

    def validate(self):
        if self.node_schema:
            for k in self.node_schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeSchema'] = []
        if self.node_schema is not None:
            for k in self.node_schema:
                result['NodeSchema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_schema = []
        if m.get('NodeSchema') is not None:
            for k in m.get('NodeSchema'):
                temp_model = DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema()
                self.node_schema.append(temp_model.from_map(k))
        return self


class DescribeLatestRecordSchemaResponseBody(TeaModel):
    def __init__(
        self,
        playbook_node_schema: DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema = None,
        request_id: str = None,
    ):
        # The output structure information of the playbook.
        self.playbook_node_schema = playbook_node_schema
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_node_schema:
            self.playbook_node_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_node_schema is not None:
            result['PlaybookNodeSchema'] = self.playbook_node_schema.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookNodeSchema') is not None:
            temp_model = DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema()
            self.playbook_node_schema = temp_model.from_map(m['PlaybookNodeSchema'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLatestRecordSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLatestRecordSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLatestRecordSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeParamTagsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeNodeParamTagsResponseBodyParamReferredPaths(TeaModel):
    def __init__(
        self,
        param_name: str = None,
        referred_path: List[str] = None,
    ):
        # The name of the upstream node.
        self.param_name = param_name
        # The paths.
        self.referred_path = referred_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.referred_path is not None:
            result['ReferredPath'] = self.referred_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ReferredPath') is not None:
            self.referred_path = m.get('ReferredPath')
        return self


class DescribeNodeParamTagsResponseBody(TeaModel):
    def __init__(
        self,
        param_referred_paths: List[DescribeNodeParamTagsResponseBodyParamReferredPaths] = None,
        request_id: str = None,
    ):
        # The configuration of the recommended path.
        self.param_referred_paths = param_referred_paths
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.param_referred_paths:
            for k in self.param_referred_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParamReferredPaths'] = []
        if self.param_referred_paths is not None:
            for k in self.param_referred_paths:
                result['ParamReferredPaths'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.param_referred_paths = []
        if m.get('ParamReferredPaths') is not None:
            for k in m.get('ParamReferredPaths'):
                temp_model = DescribeNodeParamTagsResponseBodyParamReferredPaths()
                self.param_referred_paths.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeParamTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeParamTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeParamTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeUsedInfosRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The node name of the component.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeNodeUsedInfosResponseBody(TeaModel):
    def __init__(
        self,
        node_used_infos: str = None,
        request_id: str = None,
    ):
        # The node reference information. The value is in the JSON format and contains the following fields:
        # 
        # *   **action**: the referencing action. This field contains the following information:
        # 
        #     *   **name**: the name of the referencing node.
        #     *   **inputParams**: the parameter settings of the referencing node.
        self.node_used_infos = node_used_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_used_infos is not None:
            result['NodeUsedInfos'] = self.node_used_infos
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeUsedInfos') is not None:
            self.node_used_infos = m.get('NodeUsedInfos')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeUsedInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeUsedInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeUsedInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotifyTemplateListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        self.lang = lang
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeNotifyTemplateListResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        event_id: str = None,
        params: str = None,
        subject: str = None,
        template_name: str = None,
    ):
        self.content = content
        self.event_id = event_id
        self.params = params
        self.subject = subject
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.params is not None:
            result['Params'] = self.params
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeNotifyTemplateListResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNotifyTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeNotifyTemplateListResponseBodyData] = None,
        page: DescribeNotifyTemplateListResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeNotifyTemplateListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            temp_model = DescribeNotifyTemplateListResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNotifyTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNotifyTemplateListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNotifyTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiInfoRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        lang: str = None,
        pop_code: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # This parameter is required.
        self.api_name = api_name
        # This parameter is required.
        self.api_version = api_version
        self.lang = lang
        # This parameter is required.
        self.pop_code = pop_code
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeOpenApiInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        input_params: str = None,
        output_params: str = None,
        response_demo: str = None,
        summary: str = None,
        title: str = None,
    ):
        self.description = description
        self.input_params = input_params
        self.output_params = output_params
        self.response_demo = response_demo
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.response_demo is not None:
            result['ResponseDemo'] = self.response_demo
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ResponseDemo') is not None:
            self.response_demo = m.get('ResponseDemo')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeOpenApiInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeOpenApiInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeOpenApiInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOpenApiInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpenApiInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOpenApiInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiListRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        lang: str = None,
        pop_code: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        self.api_name = api_name
        # This parameter is required.
        self.api_version = api_version
        self.lang = lang
        # This parameter is required.
        self.pop_code = pop_code
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeOpenApiListResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        directories: Any = None,
        version: str = None,
    ):
        self.code = code
        self.directories = directories
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.directories is not None:
            result['Directories'] = self.directories
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Directories') is not None:
            self.directories = m.get('Directories')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeOpenApiListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeOpenApiListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeOpenApiListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOpenApiListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpenApiListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOpenApiListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookRequest(TeaModel):
    def __init__(
        self,
        debug_flag: int = None,
        lang: str = None,
        playbook_uuid: str = None,
        taskflow_md_5: str = None,
    ):
        # The flag that indicates whether the playbook is of the debugging or published version. Valid values:
        # 
        # *   **1**: playbook of the debugging version
        # *   **0**: playbook of the published version
        self.debug_flag = debug_flag
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The MD5 hash value of the playbook.
        self.taskflow_md_5 = taskflow_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_flag is not None:
            result['DebugFlag'] = self.debug_flag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugFlag') is not None:
            self.debug_flag = m.get('DebugFlag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribePlaybookResponseBodyPlaybook(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        fail_exe_num: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        input_params: str = None,
        last_exe_time: int = None,
        online_active: bool = None,
        online_release_taskflow_md_5: str = None,
        own_type: str = None,
        playbook_uuid: str = None,
        success_exe_num: int = None,
        taskflow: str = None,
        taskflow_type: str = None,
    ):
        # The description of the playbook.
        self.description = description
        # The display name of the playbook.
        self.display_name = display_name
        # The number of times that the playbook failed to be run.
        self.fail_exe_num = fail_exe_num
        # The creation time of the playbook. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The modification time of the playbook. The value is a 13-digit timestamp.
        self.gmt_modified = gmt_modified
        # The input parameter configuration of the playbook. The value is a JSON array.
        # 
        # >  For more information, see [DescribePlaybookInputOutput](~~DescribePlaybookInputOutput~~).
        self.input_params = input_params
        # The time when the playbook was last run. The value is a 13-digit timestamp.
        self.last_exe_time = last_exe_time
        # The status of the playbook. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.online_active = online_active
        # The MD5 hash value in the latest published version of the playbook.
        self.online_release_taskflow_md_5 = online_release_taskflow_md_5
        # The type of the playbook. Valid values:
        # 
        # *   **preset**: predefined playbook
        # *   **user**: custom playbook
        self.own_type = own_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The number of times that the playbook was successfully run.
        self.success_exe_num = success_exe_num
        # The XML configuration of the playbook.
        self.taskflow = taskflow
        # The playbook configuration type.
        # *   **xml**: XML format.
        # *   **x6**: JSON format.
        self.taskflow_type = taskflow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.fail_exe_num is not None:
            result['FailExeNum'] = self.fail_exe_num
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.last_exe_time is not None:
            result['LastExeTime'] = self.last_exe_time
        if self.online_active is not None:
            result['OnlineActive'] = self.online_active
        if self.online_release_taskflow_md_5 is not None:
            result['OnlineReleaseTaskflowMd5'] = self.online_release_taskflow_md_5
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.success_exe_num is not None:
            result['SuccessExeNum'] = self.success_exe_num
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        if self.taskflow_type is not None:
            result['TaskflowType'] = self.taskflow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FailExeNum') is not None:
            self.fail_exe_num = m.get('FailExeNum')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('LastExeTime') is not None:
            self.last_exe_time = m.get('LastExeTime')
        if m.get('OnlineActive') is not None:
            self.online_active = m.get('OnlineActive')
        if m.get('OnlineReleaseTaskflowMd5') is not None:
            self.online_release_taskflow_md_5 = m.get('OnlineReleaseTaskflowMd5')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('SuccessExeNum') is not None:
            self.success_exe_num = m.get('SuccessExeNum')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        if m.get('TaskflowType') is not None:
            self.taskflow_type = m.get('TaskflowType')
        return self


class DescribePlaybookResponseBody(TeaModel):
    def __init__(
        self,
        playbook: DescribePlaybookResponseBodyPlaybook = None,
        request_id: str = None,
    ):
        # The configuration of the playbook.
        self.playbook = playbook
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook:
            self.playbook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook is not None:
            result['Playbook'] = self.playbook.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbook') is not None:
            temp_model = DescribePlaybookResponseBodyPlaybook()
            self.playbook = temp_model.from_map(m['Playbook'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookInputOutputRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookInputOutputResponseBodyConfig(TeaModel):
    def __init__(
        self,
        exe_config: str = None,
        input_params: str = None,
        output_params: str = None,
        param_type: str = None,
        playbook_uuid: str = None,
    ):
        # The execution method of the playbook is in JSONObject format.
        self.exe_config = exe_config
        # The input parameter configuration of the playbook. The value is a JSON array.
        self.input_params = input_params
        # The output parameter configuration. This parameter is unavailable and is always left empty.
        self.output_params = output_params
        # The input parameter type of the playbook. Valid values:
        # 
        # *   **template-ip**\
        # *   **template-file**\
        # *   **template-process**\
        # *   **custom**\
        self.param_type = param_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exe_config is not None:
            result['ExeConfig'] = self.exe_config
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExeConfig') is not None:
            self.exe_config = m.get('ExeConfig')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookInputOutputResponseBody(TeaModel):
    def __init__(
        self,
        config: DescribePlaybookInputOutputResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The configurations.
        self.config = config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribePlaybookInputOutputResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookInputOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookInputOutputResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookInputOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookMetricsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookMetricsResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        active: int = None,
        description: str = None,
        display_name: str = None,
        fail_num: int = None,
        gmt_create: int = None,
        history_md_5: int = None,
        last_runtime: int = None,
        own_type: str = None,
        playbook_uuid: str = None,
        succ_num: int = None,
    ):
        # The status of the playbook. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.active = active
        # The description of the playbook.
        self.description = description
        # The name of the playbook.
        self.display_name = display_name
        # The number of the tasks that are created for the playbook and failed to run.
        self.fail_num = fail_num
        # The time when the playbook was created. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The number of historical versions of the playbook.
        self.history_md_5 = history_md_5
        # The time when the playbook was last run. The value is a 13-digit timestamp.
        self.last_runtime = last_runtime
        # The type of the playbook. Valid values:
        # 
        # *   **preset**: predefined playbook
        # *   **user**: custom playbook
        self.own_type = own_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The number of the tasks that are created for the playbook and were successfully run.
        self.succ_num = succ_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.fail_num is not None:
            result['FailNum'] = self.fail_num
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.history_md_5 is not None:
            result['HistoryMd5'] = self.history_md_5
        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.succ_num is not None:
            result['SuccNum'] = self.succ_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HistoryMd5') is not None:
            self.history_md_5 = m.get('HistoryMd5')
        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('SuccNum') is not None:
            self.succ_num = m.get('SuccNum')
        return self


class DescribePlaybookMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metrics: DescribePlaybookMetricsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        # The details of the playbook.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = DescribePlaybookMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookNodesOutputRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the component node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        node_output: str = None,
    ):
        # The name of the component node.
        self.node_name = node_name
        # The historical output data of the component node. The value is in the JSON string format. If no data is found, the parameter is left empty.
        self.node_output = node_output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_output is not None:
            result['NodeOutput'] = self.node_output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')
        return self


class DescribePlaybookNodesOutputResponseBody(TeaModel):
    def __init__(
        self,
        playbook_nodes_output: DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput = None,
        request_id: str = None,
    ):
        # The output data of the component node.
        self.playbook_nodes_output = playbook_nodes_output
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_nodes_output:
            self.playbook_nodes_output.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_nodes_output is not None:
            result['PlaybookNodesOutput'] = self.playbook_nodes_output.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookNodesOutput') is not None:
            temp_model = DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput()
            self.playbook_nodes_output = temp_model.from_map(m['PlaybookNodesOutput'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookNodesOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookNodesOutputResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookNodesOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookNumberMetricsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribePlaybookNumberMetricsResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        start_up_num: int = None,
        total_num: int = None,
    ):
        # The number of enabled playbooks.
        self.start_up_num = start_up_num
        # The total number of playbooks.
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_up_num is not None:
            result['StartUpNum'] = self.start_up_num
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartUpNum') is not None:
            self.start_up_num = m.get('StartUpNum')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class DescribePlaybookNumberMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metrics: DescribePlaybookNumberMetricsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        # The statistics.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = DescribePlaybookNumberMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookNumberMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookNumberMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookNumberMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybookReleasesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The page number. Default value: 1. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. If you do not specify the PageSize parameter, 10 entries are returned by default.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybookReleasesResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePlaybookReleasesResponseBodyRecords(TeaModel):
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        taskflow_md_5: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to publish the version.
        self.creator = creator
        # The description of the layer version.
        self.description = description
        # The time when the version was created. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The time when the version was modified. The value is a 13-digit timestamp.
        self.gmt_modified = gmt_modified
        # The record ID.
        self.id = id
        # The MD5 value configured for the published version of the playbook.
        self.taskflow_md_5 = taskflow_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        return self


class DescribePlaybookReleasesResponseBody(TeaModel):
    def __init__(
        self,
        page: DescribePlaybookReleasesResponseBodyPage = None,
        records: List[DescribePlaybookReleasesResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page = page
        # The information about the playbook version.
        self.records = records
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribePlaybookReleasesResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribePlaybookReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybookReleasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybookReleasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybookReleasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlaybooksRequest(TeaModel):
    def __init__(
        self,
        active: int = None,
        end_millis: int = None,
        lang: str = None,
        name: str = None,
        order: str = None,
        own_type: str = None,
        page_number: int = None,
        page_size: int = None,
        param_types: str = None,
        playbook_uuid: str = None,
        playbook_uuids: str = None,
        sort: str = None,
        start_millis: int = None,
    ):
        # Activation status of the playbook. Values:
        # 
        # - **1**: Indicates the playbook is activated.
        # - **0**: Indicates the playbook is not activated.
        self.active = active
        # End time for the query, in 13-digit timestamp format.
        self.end_millis = end_millis
        # Specifies the language type for the request and response, default is **zh**. Values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The name of the playbook.
        self.name = name
        # The sorting logic, with a default value of **desc**. Values:
        # - **desc**: Descending order.
        # - **asc**: Ascending order.
        self.order = order
        # Type of the playbook. Values:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        self.own_type = own_type
        # Sets the page number from which to start displaying the query results. The default value is 1, indicating the first page.
        self.page_number = page_number
        # Specifies the maximum number of items to display per page in a paginated query. The default number of items per page is 20. If the PageSize parameter is empty, it will return 10 items by default.
        # > It is recommended that the PageSize value is not empty.
        self.page_size = page_size
        # The trigger method for the playbook, with a default value of **query all**. Values:
        # - **template-incident**: Security incident.
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-alert**: Security alert.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-host**: Host entity.
        # - **template-custom**: Custom.
        self.param_types = param_types
        # The UUID of the playbook.
        # > You can use the UUID to query specific playbook information.
        # > - Call the [DescribePlaybooks](~~DescribePlaybooks~~) API to obtain this parameter.
        self.playbook_uuid = playbook_uuid
        # UUID List of the playbook.
        # 
        # Note You can use the UUID list to query specific playbook information.
        # Call the DescribePlaybooks API to obtain this parameter.
        self.playbook_uuids = playbook_uuids
        # The sorting basis, with a default value of **1**. Values:
        # - **1**: Last modified time.
        # - **2**: Most recent execution time.
        self.sort = sort
        # Start time for the query, in 13-digit timestamp format.
        self.start_millis = start_millis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.param_types is not None:
            result['ParamTypes'] = self.param_types
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.playbook_uuids is not None:
            result['PlaybookUuids'] = self.playbook_uuids
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParamTypes') is not None:
            self.param_types = m.get('ParamTypes')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('PlaybookUuids') is not None:
            self.playbook_uuids = m.get('PlaybookUuids')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')
        return self


class DescribePlaybooksResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number in pagination queries.
        self.page_number = page_number
        # The number of items per page in pagination queries.
        self.page_size = page_size
        # The total number of items found.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePlaybooksResponseBodyPlaybooks(TeaModel):
    def __init__(
        self,
        active: int = None,
        display_name: str = None,
        gmt_create: int = None,
        gmt_modified: str = None,
        last_runtime: int = None,
        own_type: str = None,
        param_type: str = None,
        playbook_uuid: str = None,
    ):
        # The status indicator of the playbook. Values:
        # 
        # - **1**: Indicates the playbook is activated.
        # - **0**: Indicates the playbook is deactivated.
        self.active = active
        # The display name of the playbook.
        self.display_name = display_name
        # The creation time of the playbook, in 13-digit timestamp format.
        self.gmt_create = gmt_create
        # The modification time of the playbook.
        self.gmt_modified = gmt_modified
        # The last execution time of the playbook, in 13-digit timestamp format.
        self.last_runtime = last_runtime
        # The type of the playbook. Values:
        # 
        # - **preset**: Predefined playbook.
        # - **user**: Custom playbook.
        self.own_type = own_type
        # The trigger method for the playbook, with a default value of **query all**. Possible values are:
        # - **template-incident**: Security incident.
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-alert**: Security alert.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-host**: Host entity.
        self.param_type = param_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribePlaybooksResponseBody(TeaModel):
    def __init__(
        self,
        page: DescribePlaybooksResponseBodyPage = None,
        playbooks: List[DescribePlaybooksResponseBodyPlaybooks] = None,
        request_id: str = None,
    ):
        # Pagination query information.
        self.page = page
        # List of playbooks.
        self.playbooks = playbooks
        # The ID of the current request, generated by Alibaba Cloud as a unique identifier for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()
        if self.playbooks:
            for k in self.playbooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k in self.playbooks:
                result['Playbooks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribePlaybooksResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k in m.get('Playbooks'):
                temp_model = DescribePlaybooksResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlaybooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlaybooksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePlaybooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePopApiRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        env: str = None,
        pop_code: str = None,
    ):
        # The operation name of the Alibaba Cloud service.
        # 
        # This parameter is required.
        self.api_name = api_name
        # The version number of the API.
        # 
        # >  You can call the [DescribePopApiVersionList](~~DescribePopApiVersionList~~) operation to query the version number.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The environment in which the API operation parameter is used. Set the value to online.
        # 
        # This parameter is required.
        self.env = env
        # The POP code of the Alibaba Cloud service.
        # 
        # >  You can call the [DescribeApiList](~~DescribeApiList~~) operation to query the POP code.
        # 
        # This parameter is required.
        self.pop_code = pop_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.env is not None:
            result['Env'] = self.env
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        return self


class DescribePopApiResponseBodyOpenApiMetaList(TeaModel):
    def __init__(
        self,
        description: str = None,
        example_value: str = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        # The parameter description.
        self.description = description
        # The example value.
        self.example_value = example_value
        # The parameter name.
        self.name = name
        # Indicates whether the parameter is required.
        # 
        # *   true
        # *   false
        self.required = required
        # The data type of the parameter field. Valid values:
        # 
        # *   **string**\
        # *   **boolean**\
        # *   **integer**\
        # *   **long**\
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePopApiResponseBody(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        open_api_meta_list: List[DescribePopApiResponseBodyOpenApiMetaList] = None,
        pop_code: str = None,
        request_id: str = None,
        version: str = None,
    ):
        # The name of the API.
        self.api_name = api_name
        # The information about the API.
        self.open_api_meta_list = open_api_meta_list
        # The POP code of the Alibaba Cloud service.
        self.pop_code = pop_code
        # The request ID.
        self.request_id = request_id
        # The version of the API.
        self.version = version

    def validate(self):
        if self.open_api_meta_list:
            for k in self.open_api_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        result['OpenApiMetaList'] = []
        if self.open_api_meta_list is not None:
            for k in self.open_api_meta_list:
                result['OpenApiMetaList'].append(k.to_map() if k else None)
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        self.open_api_meta_list = []
        if m.get('OpenApiMetaList') is not None:
            for k in m.get('OpenApiMetaList'):
                temp_model = DescribePopApiResponseBodyOpenApiMetaList()
                self.open_api_meta_list.append(temp_model.from_map(k))
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePopApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePopApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePopApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePopApiItemListRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        env: str = None,
        lang: str = None,
        pop_code: str = None,
    ):
        # The API operation name of the Alibaba Cloud service. Fuzzy match is supported.
        self.api_name = api_name
        # The version number of the API.
        # 
        # >  You can call the [DescribePopApiVersionList](~~DescribePopApiVersionList~~) operation to query the version number.
        # 
        # This parameter is required.
        self.api_version = api_version
        # The environment in which the API operation parameters are used. Set the value to online.
        # 
        # This parameter is required.
        self.env = env
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The POP code of the Alibaba Cloud service.
        # 
        # >  You can call the [DescribeApiList](~~DescribeApiList~~) operation to query the POP code.
        # 
        # This parameter is required.
        self.pop_code = pop_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.env is not None:
            result['Env'] = self.env
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        return self


class DescribePopApiItemListResponseBody(TeaModel):
    def __init__(
        self,
        names: List[str] = None,
        pop_code: str = None,
        request_id: str = None,
        total: int = None,
        version: str = None,
    ):
        # The names of API operations.
        self.names = names
        # The POP code of the Alibaba Cloud service.
        self.pop_code = pop_code
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total
        # The version number of the API for the Alibaba Cloud service.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.pop_code is not None:
            result['PopCode'] = self.pop_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('PopCode') is not None:
            self.pop_code = m.get('PopCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePopApiItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePopApiItemListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePopApiItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        role_for: str = None,
        role_type: str = None,
    ):
        self.lang = lang
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeProcessStatisticsResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        ban_file_num: int = None,
        ban_ip_num: int = None,
        ban_process_num: int = None,
        task_num: int = None,
    ):
        self.ban_file_num = ban_file_num
        self.ban_ip_num = ban_ip_num
        self.ban_process_num = ban_process_num
        self.task_num = task_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ban_file_num is not None:
            result['BanFileNum'] = self.ban_file_num
        if self.ban_ip_num is not None:
            result['BanIpNum'] = self.ban_ip_num
        if self.ban_process_num is not None:
            result['BanProcessNum'] = self.ban_process_num
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BanFileNum') is not None:
            self.ban_file_num = m.get('BanFileNum')
        if m.get('BanIpNum') is not None:
            self.ban_ip_num = m.get('BanIpNum')
        if m.get('BanProcessNum') is not None:
            self.ban_process_num = m.get('BanProcessNum')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        return self


class DescribeProcessStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        metrics: DescribeProcessStatisticsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        self.metrics = metrics
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = DescribeProcessStatisticsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProcessStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProcessStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessTaskCountRequest(TeaModel):
    def __init__(
        self,
        entity_uuid_list: List[str] = None,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # Collection of entity UUIDs.
        # 
        # This parameter is required.
        self.entity_uuid_list = entity_uuid_list
        # Language type for request and response messages. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # User ID for administrators to switch to other member\\"s perspective.
        self.role_for = role_for
        # View type.
        # 
        # - **0**: Current Alibaba Cloud account view.
        # - **1**: View for all accounts under the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_uuid_list is not None:
            result['EntityUuidList'] = self.entity_uuid_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityUuidList') is not None:
            self.entity_uuid_list = m.get('EntityUuidList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeProcessTaskCountResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        entity_uuid: str = None,
    ):
        # Count.
        self.count = count
        # Entity UUID.
        self.entity_uuid = entity_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')
        return self


class DescribeProcessTaskCountResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeProcessTaskCountResponseBodyData] = None,
        request_id: str = None,
    ):
        # Transmitted data.
        self.data = data
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for this request, used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeProcessTaskCountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessTaskCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProcessTaskCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProcessTaskCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessTasksRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        event_uuid: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        param_content: str = None,
        process_action_end: int = None,
        process_action_start: int = None,
        process_remove_end: int = None,
        process_remove_start: int = None,
        process_strategy_uuid: str = None,
        scene_code: str = None,
        scope: str = None,
        source: str = None,
        task_id: str = None,
        task_status: str = None,
        trigger_source: str = None,
        yun_code: str = None,
    ):
        # The sort order. Valid values:
        # 
        # *   **desc** (default)
        # *   **asc**\
        self.direction = direction
        # The name of the handling entity.
        self.entity_name = entity_name
        # The type of the handling entity. Valid values:
        # 
        # *   **ip**\
        # *   **file**\
        # *   **process**\
        self.entity_type = entity_type
        self.entity_uuid = entity_uuid
        self.event_uuid = event_uuid
        # The field that you use to sort the result.
        # 
        # >  You can obtain the field from the response result.
        self.order_field = order_field
        # The page number. Default value: 1. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. If you do not specify the PageSize parameter, 10 entries are returned by default.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The handling entity, handling scenario, or handling parameter that is used for fuzzy match.
        self.param_content = param_content
        # The end of the time range for a handling task. The value is a 13-digit timestamp.
        self.process_action_end = process_action_end
        # The beginning of the time range for a handling task. The value is a 13-digit timestamp.
        self.process_action_start = process_action_start
        # The end of the time range for an unblocking task. The value is a 13-digit timestamp.
        self.process_remove_end = process_remove_end
        # The beginning of the time range for an unblocking task. The value is a 13-digit timestamp.
        self.process_remove_start = process_remove_start
        # The UUID of the handling policy.
        # 
        # >  You can call the [ListDisposeStrategy](https://help.aliyun.com/document_detail/2584440.html) operation to query the UUID of the handling policy.
        self.process_strategy_uuid = process_strategy_uuid
        # The scenario code of the handling task.
        # 
        # >  You can call the [DescribeEnumItems](~~DescribeEnumItems~~) operation to query the scenario code of the handling task. This parameter is available when you set **EnumType** to **process**.
        self.scene_code = scene_code
        # The ID of the Alibaba Cloud account that is specified in the handling task.
        self.scope = scope
        # The triggering source of the handling task. The value is a string array. Valid values:
        # 
        # *   **system**: triggered when you manually handle an event
        # *   **custom**: triggered by an event based on an automatic response rule
        # *   **custom_alert**: triggered by an alert based on an automatic response rule
        # *   **soar-manual**: triggered when you use SOAR to manually run a playbook
        # *   **soar-mdr**: triggered by Managed Security Service
        self.source = source
        # The unique identifier of the handling task.
        # 
        # >  This parameter is used to query a specific task. You can obtain the value from the response result.
        self.task_id = task_id
        # The status of the handling task. The value is a string. Valid values:
        # 
        # *   **11**: being handled
        # *   **21**: being blocked
        # *   **22**: being quarantined
        # *   **23**: completed
        # *   **24**: added to the whitelist
        # *   **20**: successful
        # *   **90**: failed
        # *   **91**: unblocking failed
        # *   **92**: restoring quarantined files failed
        self.task_status = task_status
        self.trigger_source = trigger_source
        # The cloud service that is associated with the handling task. The value is a string. Valid values:
        # 
        # *   **WAF**: Web Application Firewall (WAF)
        # *   **CFW**: Cloud Firewall
        # *   **Aegis**: Security Center
        self.yun_code = yun_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.param_content is not None:
            result['ParamContent'] = self.param_content
        if self.process_action_end is not None:
            result['ProcessActionEnd'] = self.process_action_end
        if self.process_action_start is not None:
            result['ProcessActionStart'] = self.process_action_start
        if self.process_remove_end is not None:
            result['ProcessRemoveEnd'] = self.process_remove_end
        if self.process_remove_start is not None:
            result['ProcessRemoveStart'] = self.process_remove_start
        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source
        if self.yun_code is not None:
            result['YunCode'] = self.yun_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParamContent') is not None:
            self.param_content = m.get('ParamContent')
        if m.get('ProcessActionEnd') is not None:
            self.process_action_end = m.get('ProcessActionEnd')
        if m.get('ProcessActionStart') is not None:
            self.process_action_start = m.get('ProcessActionStart')
        if m.get('ProcessRemoveEnd') is not None:
            self.process_remove_end = m.get('ProcessRemoveEnd')
        if m.get('ProcessRemoveStart') is not None:
            self.process_remove_start = m.get('ProcessRemoveStart')
        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')
        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')
        return self


class DescribeProcessTasksResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProcessTasksResponseBodyProcessTasks(TeaModel):
    def __init__(
        self,
        creator: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        err_code: str = None,
        err_msg: str = None,
        err_tip: str = None,
        event_uuid: str = None,
        gmt_create_millis: int = None,
        gmt_modified_millis: int = None,
        input_params: str = None,
        process_strategy_uuid: str = None,
        process_time: int = None,
        remove_time: int = None,
        req_uuid: str = None,
        scene_code: str = None,
        scene_name: str = None,
        scope: str = None,
        source: str = None,
        task_id: str = None,
        task_status: int = None,
        trigger_source: str = None,
        yun_code: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to submit the handling task.
        self.creator = creator
        # The name of the handling entity.
        self.entity_name = entity_name
        # The type of the handling entity.
        self.entity_type = entity_type
        self.entity_uuid = entity_uuid
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_msg = err_msg
        # The error tip returned if the call failed.
        self.err_tip = err_tip
        self.event_uuid = event_uuid
        # The creation time of the handling task. The value is a 13-digit timestamp.
        self.gmt_create_millis = gmt_create_millis
        # The modification time of the handling task. The value is a 13-digit timestamp.
        self.gmt_modified_millis = gmt_modified_millis
        # The input parameter of the handling task.
        self.input_params = input_params
        # The ID of the associated policy.
        self.process_strategy_uuid = process_strategy_uuid
        # The delivery time of the handling task. The value is a 13-digit timestamp.
        self.process_time = process_time
        # The unblocking time of the handling task. The value is a 13-digit timestamp.
        self.remove_time = remove_time
        self.req_uuid = req_uuid
        # The scenario code of the handling task.
        self.scene_code = scene_code
        # The scenario name of the handling task.
        self.scene_name = scene_name
        # The ID of the Alibaba Cloud account that is specified in the handling task.
        self.scope = scope
        # The submission source of the handling task.
        self.source = source
        # The unique identifier of the handling task.
        self.task_id = task_id
        # The status of the handling task.
        self.task_status = task_status
        self.trigger_source = trigger_source
        # The code of the cloud service that is associated with the handling task.
        self.yun_code = yun_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.err_tip is not None:
            result['ErrTip'] = self.err_tip
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.gmt_create_millis is not None:
            result['GmtCreateMillis'] = self.gmt_create_millis
        if self.gmt_modified_millis is not None:
            result['GmtModifiedMillis'] = self.gmt_modified_millis
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.remove_time is not None:
            result['RemoveTime'] = self.remove_time
        if self.req_uuid is not None:
            result['ReqUuid'] = self.req_uuid
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source
        if self.yun_code is not None:
            result['YunCode'] = self.yun_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ErrTip') is not None:
            self.err_tip = m.get('ErrTip')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('GmtCreateMillis') is not None:
            self.gmt_create_millis = m.get('GmtCreateMillis')
        if m.get('GmtModifiedMillis') is not None:
            self.gmt_modified_millis = m.get('GmtModifiedMillis')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('RemoveTime') is not None:
            self.remove_time = m.get('RemoveTime')
        if m.get('ReqUuid') is not None:
            self.req_uuid = m.get('ReqUuid')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')
        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')
        return self


class DescribeProcessTasksResponseBody(TeaModel):
    def __init__(
        self,
        page: DescribeProcessTasksResponseBodyPage = None,
        process_tasks: List[DescribeProcessTasksResponseBodyProcessTasks] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page = page
        # The handling tasks.
        self.process_tasks = process_tasks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()
        if self.process_tasks:
            for k in self.process_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        result['ProcessTasks'] = []
        if self.process_tasks is not None:
            for k in self.process_tasks:
                result['ProcessTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribeProcessTasksResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        self.process_tasks = []
        if m.get('ProcessTasks') is not None:
            for k in m.get('ProcessTasks'):
                temp_model = DescribeProcessTasksResponseBodyProcessTasks()
                self.process_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProcessTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProcessTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProcessTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordActionOutputListRequest(TeaModel):
    def __init__(
        self,
        action_uuid: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The UUID of the component action.
        # 
        # >  You can call the [DescribeSoarTaskAndActions](~~DescribeSoarTaskAndActions~~) operation to query the UUID.
        # 
        # This parameter is required.
        self.action_uuid = action_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The page number. Default value: 1. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. If you leave this parameter empty, 10 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSoarRecordActionOutputListResponseBody(TeaModel):
    def __init__(
        self,
        action_outputs: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The data that is returned when the component action is performed. The value is a JSON array.
        # 
        # >  The format of the output data is determined by the component that is configured when the playbook is written.
        self.action_outputs = action_outputs
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of pages returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_outputs is not None:
            result['ActionOutputs'] = self.action_outputs
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionOutputs') is not None:
            self.action_outputs = m.get('ActionOutputs')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSoarRecordActionOutputListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSoarRecordActionOutputListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordActionOutputListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordInOutputRequest(TeaModel):
    def __init__(
        self,
        action_uuid: str = None,
        lang: str = None,
    ):
        # The UUID of the component action.
        # 
        # >  You can call the [DescribeSoarTaskAndActions](~~DescribeSoarTaskAndActions~~) operation to query the UUIDs of component actions.
        # 
        # This parameter is required.
        self.action_uuid = action_uuid
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeSoarRecordInOutputResponseBody(TeaModel):
    def __init__(
        self,
        in_output_info: str = None,
        request_id: str = None,
    ):
        # The execution result of the component action.
        self.in_output_info = in_output_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_output_info is not None:
            result['InOutputInfo'] = self.in_output_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InOutputInfo') is not None:
            self.in_output_info = m.get('InOutputInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSoarRecordInOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSoarRecordInOutputResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordInOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarRecordsRequest(TeaModel):
    def __init__(
        self,
        end_millis: int = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_uuid: str = None,
        request_uuid: str = None,
        start_millis: int = None,
        task_status: str = None,
        taskflow_md_5: str = None,
        trigger_user: str = None,
    ):
        # The end time of the task execution, in 13-digit timestamp format.
        self.end_millis = end_millis
        # Set the language type for requests and received messages. The default is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Set which page to start displaying the query results from. The default value is 1, indicating the first page.
        self.page_number = page_number
        # Specify the maximum number of data entries per page when performing a paginated query. The default number of entries per page is 20. If the PageSize parameter is empty, it will return 10 entries by default.
        # > It is recommended not to leave the PageSize value empty.
        self.page_size = page_size
        # The UUID of the playbook.
        # > You can obtain this parameter by calling the [DescribePlaybooks](~~DescribePlaybooks~~) interface.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # UUID of the playbook task execution.
        # > You can obtain this parameter by calling the [DescribeSoarRecords](https://help.aliyun.com/document_detail/2627455.html) interface.
        self.request_uuid = request_uuid
        # The start time of the task execution, in 13-digit timestamp format.
        self.start_millis = start_millis
        # The status of the task execution. Values:
        # 
        # - **success**: Successful task.
        # - **failed**: Failed task.
        # - **inprogress**: Task in progress
        self.task_status = task_status
        # The MD5 value of the playbook configuration.
        self.taskflow_md_5 = taskflow_md_5
        # The Alibaba Cloud account ID that executed the playbook task.
        self.trigger_user = trigger_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarRecordsResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number in paginated queries.
        self.page_number = page_number
        # The number of items per page in paginated queries.
        self.page_size = page_size
        # The total number of queried items.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSoarRecordsResponseBodySoarExecuteRecords(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        error_msg: str = None,
        raw_event_req: str = None,
        request_uuid: str = None,
        result_message: str = None,
        start_time: int = None,
        status: str = None,
        task_name: str = None,
        task_type: str = None,
        taskflow_md_5: str = None,
        trigger_type: str = None,
        trigger_user: str = None,
    ):
        # The end time of the component execution, in 13-digit timestamp format.
        self.end_time = end_time
        # The error message of the playbook task. This field is empty when the task succeeds.
        self.error_msg = error_msg
        # The request parameters of the playbook task.
        self.raw_event_req = raw_event_req
        # The request ID of the playbook task, a unique ID for each task run.
        self.request_uuid = request_uuid
        # The return information of the playbook, defined by the user within the playbook.
        self.result_message = result_message
        # The start time of the task execution, in 13-digit timestamp format.
        self.start_time = start_time
        # The status of the playbook task. Values:
        # 
        # - **success**: Indicates successful execution.
        # - **fail**: Indicates failed execution.
        # - **running**: Indicates the task is running
        self.status = status
        # The name of the playbook task, which is the same as the playbook\\"s UUID.
        self.task_name = task_name
        # The type of the playbook task, with values:
        # 
        # - **general**: Represents a general playbook task.
        # - **standard**: Represents a component execution task.
        self.task_type = task_type
        # The MD5 value of the playbook configuration.
        self.taskflow_md_5 = taskflow_md_5
        # The type of the playbook task. Values:
        # 
        # - **debug**: Indicates a debugging task.
        # - **manual**: Indicates a manual task.
        # - **siem**: Indicates a task triggered by an event or alert.
        self.trigger_type = trigger_type
        # The Alibaba Cloud account ID that executes the playbook task.
        self.trigger_user = trigger_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.raw_event_req is not None:
            result['RawEventReq'] = self.raw_event_req
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RawEventReq') is not None:
            self.raw_event_req = m.get('RawEventReq')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page: DescribeSoarRecordsResponseBodyPage = None,
        request_id: str = None,
        soar_execute_records: List[DescribeSoarRecordsResponseBodySoarExecuteRecords] = None,
    ):
        # Information displayed on the page.
        # 
        # This parameter is required.
        self.page = page
        # The ID of the current request, generated by Alibaba Cloud as a unique identifier for the request, which can be used for troubleshooting and problem localization.
        self.request_id = request_id
        # Execution record result set.
        self.soar_execute_records = soar_execute_records

    def validate(self):
        if self.page:
            self.page.validate()
        if self.soar_execute_records:
            for k in self.soar_execute_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SoarExecuteRecords'] = []
        if self.soar_execute_records is not None:
            for k in self.soar_execute_records:
                result['SoarExecuteRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = DescribeSoarRecordsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.soar_execute_records = []
        if m.get('SoarExecuteRecords') is not None:
            for k in m.get('SoarExecuteRecords'):
                temp_model = DescribeSoarRecordsResponseBodySoarExecuteRecords()
                self.soar_execute_records.append(temp_model.from_map(k))
        return self


class DescribeSoarRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSoarRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSoarTaskAndActionsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        request_uuid: str = None,
    ):
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The playbook UUID.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DescribeSoarTaskAndActionsResponseBodyDetailsActions(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_uuid: str = None,
        asset_name: str = None,
        component: str = None,
        end_time: int = None,
        node_name: str = None,
        request_uuid: str = None,
        start_time: int = None,
        status: str = None,
        task_name: str = None,
        task_status: str = None,
        trigger_user: str = None,
    ):
        # The action name of the component.
        self.action = action
        # The UUID of the component execution record.
        self.action_uuid = action_uuid
        # The name of the asset that is used by the component.
        self.asset_name = asset_name
        # The component name.
        self.component = component
        # The end of the time range during which the component is run. The value is a 13-digit timestamp.
        self.end_time = end_time
        # The custom name of the node in the component.
        self.node_name = node_name
        # The request ID of the task. The value is unique.
        self.request_uuid = request_uuid
        # The beginning of the time range during which the component is run. The value is a 13-digit timestamp.
        self.start_time = start_time
        # The running result of the component. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        self.status = status
        # The name of the task. The value is the same as the playbook UUID.
        self.task_name = task_name
        # The status of the triggered component action.
        # 
        # >  This parameter is disabled and left empty.
        self.task_status = task_status
        # The ID of the Alibaba Cloud account that is used to execute the task.
        self.trigger_user = trigger_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.component is not None:
            result['Component'] = self.component
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarTaskAndActionsResponseBodyDetails(TeaModel):
    def __init__(
        self,
        actions: List[DescribeSoarTaskAndActionsResponseBodyDetailsActions] = None,
        end_time: int = None,
        error_msg: str = None,
        raw_event_req: str = None,
        request_uuid: str = None,
        result_level: str = None,
        result_message: str = None,
        start_time: int = None,
        status: str = None,
        task_flow_md_5: str = None,
        task_name: str = None,
        task_tenant_id: str = None,
        trigger_type: str = None,
        trigger_user: str = None,
    ):
        # The list of component actions during the running of the playbook.
        self.actions = actions
        # The end of the time range during which the playbook is run. The value is a 13-digit timestamp.
        self.end_time = end_time
        # The error message of the task. If the task is successful, this field is empty.
        self.error_msg = error_msg
        # The request parameters of the task.
        self.raw_event_req = raw_event_req
        # The request ID of the task. The value is unique.
        self.request_uuid = request_uuid
        # The flag of the task. For debugging tasks, the value is **DEBUG**. For other tasks, the parameter is left empty.
        self.result_level = result_level
        # The returned information about the playbook. You can define the value in the playbook.
        self.result_message = result_message
        # The beginning of the time range during which the playbook is run. The value is a 13-digit timestamp.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   **success**\
        # *   **fail**\
        # *   **running**\
        self.status = status
        # The MD5 value of the playbook.
        self.task_flow_md_5 = task_flow_md_5
        # The name of the task. The value is the same as the playbook UUID.
        self.task_name = task_name
        # The ID of the Alibaba Cloud account to which the task belongs.
        self.task_tenant_id = task_tenant_id
        # The task type. Valid values:
        # 
        # *   **debug**: a debugging task
        # *   **manual**: a manual task
        # *   **siem**: an event-triggered task
        self.trigger_type = trigger_type
        # The ID of the Alibaba Cloud account that triggers the task.
        self.trigger_user = trigger_user

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.raw_event_req is not None:
            result['RawEventReq'] = self.raw_event_req
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        if self.result_level is not None:
            result['ResultLevel'] = self.result_level
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_flow_md_5 is not None:
            result['TaskFlowMd5'] = self.task_flow_md_5
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_tenant_id is not None:
            result['TaskTenantId'] = self.task_tenant_id
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DescribeSoarTaskAndActionsResponseBodyDetailsActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RawEventReq') is not None:
            self.raw_event_req = m.get('RawEventReq')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        if m.get('ResultLevel') is not None:
            self.result_level = m.get('ResultLevel')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskFlowMd5') is not None:
            self.task_flow_md_5 = m.get('TaskFlowMd5')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskTenantId') is not None:
            self.task_tenant_id = m.get('TaskTenantId')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')
        return self


class DescribeSoarTaskAndActionsResponseBody(TeaModel):
    def __init__(
        self,
        details: DescribeSoarTaskAndActionsResponseBodyDetails = None,
        request_id: str = None,
    ):
        # The execution details of each task.
        self.details = details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = DescribeSoarTaskAndActionsResponseBodyDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSoarTaskAndActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSoarTaskAndActionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSoarTaskAndActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSophonCommandsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the command. Fuzzy match is supported.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSophonCommandsResponseBodyDataParamConfig(TeaModel):
    def __init__(
        self,
        check_field: str = None,
        field: str = None,
        necessary: bool = None,
        value: str = None,
    ):
        # The regular expression that is used to check the format of the parameter value. If the parameter is left empty, the check is not performed.
        self.check_field = check_field
        # The name of the parameter.
        self.field = field
        # Indicates whether the parameter is required. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.necessary = necessary
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_field is not None:
            result['CheckField'] = self.check_field
        if self.field is not None:
            result['Field'] = self.field
        if self.necessary is not None:
            result['Necessary'] = self.necessary
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckField') is not None:
            self.check_field = m.get('CheckField')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Necessary') is not None:
            self.necessary = m.get('Necessary')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeSophonCommandsResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        param_config: List[DescribeSophonCommandsResponseBodyDataParamConfig] = None,
    ):
        # The description of the command.
        self.description = description
        # The display name of the command.
        self.display_name = display_name
        # The name of the command.
        self.name = name
        # The parameter configurations.
        self.param_config = param_config

    def validate(self):
        if self.param_config:
            for k in self.param_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        result['ParamConfig'] = []
        if self.param_config is not None:
            for k in self.param_config:
                result['ParamConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.param_config = []
        if m.get('ParamConfig') is not None:
            for k in m.get('ParamConfig'):
                temp_model = DescribeSophonCommandsResponseBodyDataParamConfig()
                self.param_config.append(temp_model.from_map(k))
        return self


class DescribeSophonCommandsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeSophonCommandsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The commands.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeSophonCommandsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSophonCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSophonCommandsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSophonCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVendorApiListRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
        product_code: str = None,
        vendor_code: str = None,
    ):
        self.api_name = api_name
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size
        self.product_code = product_code
        self.vendor_code = vendor_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')
        return self


class DescribeVendorApiListResponseBodyApiList(TeaModel):
    def __init__(
        self,
        advance_config: str = None,
        api_name: str = None,
        api_version: str = None,
        method: str = None,
        need_advance_config: bool = None,
        need_page_info: bool = None,
        page_info: str = None,
        parameter: str = None,
        product_code: str = None,
        product_domain: str = None,
        product_name: str = None,
        protocol: str = None,
        vendor_code: str = None,
    ):
        self.advance_config = advance_config
        self.api_name = api_name
        self.api_version = api_version
        self.method = method
        self.need_advance_config = need_advance_config
        self.need_page_info = need_page_info
        self.page_info = page_info
        self.parameter = parameter
        self.product_code = product_code
        self.product_domain = product_domain
        self.product_name = product_name
        self.protocol = protocol
        self.vendor_code = vendor_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_config is not None:
            result['AdvanceConfig'] = self.advance_config
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.method is not None:
            result['Method'] = self.method
        if self.need_advance_config is not None:
            result['NeedAdvanceConfig'] = self.need_advance_config
        if self.need_page_info is not None:
            result['NeedPageInfo'] = self.need_page_info
        if self.page_info is not None:
            result['PageInfo'] = self.page_info
        if self.parameter is not None:
            result['Parameter'] = self.parameter
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_domain is not None:
            result['ProductDomain'] = self.product_domain
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceConfig') is not None:
            self.advance_config = m.get('AdvanceConfig')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('NeedAdvanceConfig') is not None:
            self.need_advance_config = m.get('NeedAdvanceConfig')
        if m.get('NeedPageInfo') is not None:
            self.need_page_info = m.get('NeedPageInfo')
        if m.get('PageInfo') is not None:
            self.page_info = m.get('PageInfo')
        if m.get('Parameter') is not None:
            self.parameter = m.get('Parameter')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDomain') is not None:
            self.product_domain = m.get('ProductDomain')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')
        return self


class DescribeVendorApiListResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVendorApiListResponseBody(TeaModel):
    def __init__(
        self,
        api_list: List[DescribeVendorApiListResponseBodyApiList] = None,
        page: DescribeVendorApiListResponseBodyPage = None,
        request_id: str = None,
    ):
        self.api_list = api_list
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.api_list:
            for k in self.api_list:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiList'] = []
        if self.api_list is not None:
            for k in self.api_list:
                result['ApiList'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k in m.get('ApiList'):
                temp_model = DescribeVendorApiListResponseBodyApiList()
                self.api_list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            temp_model = DescribeVendorApiListResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVendorApiListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVendorApiListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVendorApiListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescriberPython3ScriptLogsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        request_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID that is returned when the Python3 script is run.
        # 
        # >  You can call the [RunPython3Script](~~RunPython3Script~~) operation to query the UUID.
        # 
        # This parameter is required.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')
        return self


class DescriberPython3ScriptLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        run_result: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The operational logs of the Python3 script.
        self.run_result = run_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        return self


class DescriberPython3ScriptLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescriberPython3ScriptLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescriberPython3ScriptLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyComponentAssetRequest(TeaModel):
    def __init__(
        self,
        asset_config: str = None,
        lang: str = None,
    ):
        # The configuration of the asset. The value is a JSON object.
        # 
        # This parameter is required.
        self.asset_config = asset_config
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_config is not None:
            result['AssetConfig'] = self.asset_config
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetConfig') is not None:
            self.asset_config = m.get('AssetConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ModifyComponentAssetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyComponentAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyComponentAssetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyComponentAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        lang: str = None,
        playbook_uuid: str = None,
        taskflow: str = None,
    ):
        # The description of the playbook.
        self.description = description
        # The display name of the playbook.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The XML configuration of the playbook.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')
        return self


class ModifyPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookInputOutputRequest(TeaModel):
    def __init__(
        self,
        exe_config: str = None,
        input_params: str = None,
        lang: str = None,
        output_params: str = None,
        param_type: str = None,
        playbook_uuid: str = None,
    ):
        # The executed mode of a playbook. The value is a JSON array.
        self.exe_config = exe_config
        # The configuration of the input parameters. The value is a JSON array.
        # 
        # This parameter is required.
        self.input_params = input_params
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The configuration of the output parameters. This parameter is unavailable. Leave it empty.
        # 
        # This parameter is required.
        self.output_params = output_params
        # The input parameter type.
        # 
        # *   **template-ip**\
        # *   **template-file**\
        # *   **template-process**\
        # *   **custom**\
        self.param_type = param_type
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exe_config is not None:
            result['ExeConfig'] = self.exe_config
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExeConfig') is not None:
            self.exe_config = m.get('ExeConfig')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ModifyPlaybookInputOutputResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPlaybookInputOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPlaybookInputOutputResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookInputOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlaybookInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        active: int = None,
        lang: str = None,
        playbook_uuid: str = None,
    ):
        # The playbook status. Valid values:
        # 
        # *   **1**: starts the playbook.
        # *   **0**: stops the playbook.
        # 
        # This parameter is required.
        self.active = active
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class ModifyPlaybookInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPlaybookInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPlaybookInstanceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPlaybookInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishPlaybookRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        playbook_uuid: str = None,
    ):
        # The description of the released version.
        self.description = description
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class PublishPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTreeDataRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class QueryTreeDataResponseBody(TeaModel):
    def __init__(
        self,
        playbooks: str = None,
        request_id: str = None,
    ):
        # The returned information about the playbook. The value is a JSON string.
        self.playbooks = playbooks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbooks is not None:
            result['Playbooks'] = self.playbooks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbooks') is not None:
            self.playbooks = m.get('Playbooks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTreeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTreeDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTreeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenamePlaybookNodeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        new_node_name: str = None,
        old_node_name: str = None,
        playbook_uuid: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The new name of the node.
        # 
        # This parameter is required.
        self.new_node_name = new_node_name
        # The original name of the node.
        # 
        # This parameter is required.
        self.old_node_name = old_node_name
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the UUIDs of playbooks.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_node_name is not None:
            result['NewNodeName'] = self.new_node_name
        if self.old_node_name is not None:
            result['OldNodeName'] = self.old_node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewNodeName') is not None:
            self.new_node_name = m.get('NewNodeName')
        if m.get('OldNodeName') is not None:
            self.old_node_name = m.get('OldNodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class RenamePlaybookNodeResponseBody(TeaModel):
    def __init__(
        self,
        rename_result: str = None,
        request_id: str = None,
    ):
        # The returned new name of the node.
        self.rename_result = rename_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rename_result is not None:
            result['RenameResult'] = self.rename_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenameResult') is not None:
            self.rename_result = m.get('RenameResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenamePlaybookNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenamePlaybookNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenamePlaybookNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertPlaybookReleaseRequest(TeaModel):
    def __init__(
        self,
        is_publish: bool = None,
        play_release_id: int = None,
        playbook_uuid: str = None,
    ):
        # Specifies whether to directly publish the new playbook after the rollback.
        # 
        # *   **true** (default)
        # *   **false**\
        self.is_publish = is_publish
        # The version of the playbook that you want to publish.
        # 
        # >  You can call the [DescribePlaybookReleases](~~DescribePlaybookReleases~~) operation to query the playbook version.
        # 
        # This parameter is required.
        self.play_release_id = play_release_id
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_publish is not None:
            result['IsPublish'] = self.is_publish
        if self.play_release_id is not None:
            result['PlayReleaseId'] = self.play_release_id
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPublish') is not None:
            self.is_publish = m.get('IsPublish')
        if m.get('PlayReleaseId') is not None:
            self.play_release_id = m.get('PlayReleaseId')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class RevertPlaybookReleaseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevertPlaybookReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevertPlaybookReleaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertPlaybookReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunNotifyComponentWithEmailRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        asset_id: int = None,
        component_name: str = None,
        content: str = None,
        lang: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
        receivers: List[str] = None,
        role_for: int = None,
        role_type: str = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.action_name = action_name
        # This parameter is required.
        self.asset_id = asset_id
        # This parameter is required.
        self.component_name = component_name
        # This parameter is required.
        self.content = content
        self.lang = lang
        # This parameter is required.
        self.node_name = node_name
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # This parameter is required.
        self.receivers = receivers
        self.role_for = role_for
        self.role_type = role_type
        # This parameter is required.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.content is not None:
            result['Content'] = self.content
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class RunNotifyComponentWithEmailResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RunNotifyComponentWithEmailResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        page: RunNotifyComponentWithEmailResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Page') is not None:
            temp_model = RunNotifyComponentWithEmailResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunNotifyComponentWithEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunNotifyComponentWithEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunNotifyComponentWithEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunNotifyComponentWithMessageCenterRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        aliuid: str = None,
        asset_id: int = None,
        channel_type_list: List[str] = None,
        component_name: str = None,
        event_id: str = None,
        lang: str = None,
        node_name: str = None,
        params: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # This parameter is required.
        self.action_name = action_name
        # This parameter is required.
        self.aliuid = aliuid
        self.asset_id = asset_id
        self.channel_type_list = channel_type_list
        # This parameter is required.
        self.component_name = component_name
        # This parameter is required.
        self.event_id = event_id
        self.lang = lang
        # This parameter is required.
        self.node_name = node_name
        self.params = params
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        self.role_for = role_for
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.channel_type_list is not None:
            result['ChannelTypeList'] = self.channel_type_list
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.params is not None:
            result['Params'] = self.params
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('ChannelTypeList') is not None:
            self.channel_type_list = m.get('ChannelTypeList')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class RunNotifyComponentWithMessageCenterResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RunNotifyComponentWithMessageCenterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        page: RunNotifyComponentWithMessageCenterResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Page') is not None:
            temp_model = RunNotifyComponentWithMessageCenterResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunNotifyComponentWithMessageCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunNotifyComponentWithMessageCenterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunNotifyComponentWithMessageCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunNotifyComponentWithWebhookRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        asset_id: int = None,
        component_name: str = None,
        content: str = None,
        lang: str = None,
        msg_type: str = None,
        node_name: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
        role_type: str = None,
        secret: str = None,
        webhook: str = None,
    ):
        # This parameter is required.
        self.action_name = action_name
        self.asset_id = asset_id
        # This parameter is required.
        self.component_name = component_name
        # This parameter is required.
        self.content = content
        self.lang = lang
        # This parameter is required.
        self.msg_type = msg_type
        # This parameter is required.
        self.node_name = node_name
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        self.role_for = role_for
        self.role_type = role_type
        self.secret = secret
        # This parameter is required.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.content is not None:
            result['Content'] = self.content
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class RunNotifyComponentWithWebhookResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RunNotifyComponentWithWebhookResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        page: RunNotifyComponentWithWebhookResponseBodyPage = None,
        request_id: str = None,
    ):
        self.data = data
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Page') is not None:
            temp_model = RunNotifyComponentWithWebhookResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunNotifyComponentWithWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunNotifyComponentWithWebhookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunNotifyComponentWithWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPython3ScriptRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        params: str = None,
        playbook_uuid: str = None,
        python_script: str = None,
    ):
        # The name of the node in the playbook.
        self.node_name = node_name
        # The input parameters of the Python3 script.
        self.params = params
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the UUIDs of playbooks.
        self.playbook_uuid = playbook_uuid
        # The Python3 script.
        self.python_script = python_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.params is not None:
            result['Params'] = self.params
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.python_script is not None:
            result['PythonScript'] = self.python_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('PythonScript') is not None:
            self.python_script = m.get('PythonScript')
        return self


class RunPython3ScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        run_result: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The execution result of the Python3 script.
        self.run_result = run_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_result is not None:
            result['RunResult'] = self.run_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')
        return self


class RunPython3ScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunPython3ScriptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunPython3ScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerPlaybookRequest(TeaModel):
    def __init__(
        self,
        input_param: str = None,
        playbook_uuid: str = None,
    ):
        # The input parameters of the playbook.
        # 
        # This parameter is required.
        self.input_param = input_param
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_param is not None:
            result['InputParam'] = self.input_param
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputParam') is not None:
            self.input_param = m.get('InputParam')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class TriggerPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trigger_uuid: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The running UUID of the playbook. This parameter is used to query the running result of the playbook.
        self.trigger_uuid = trigger_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger_uuid is not None:
            result['TriggerUuid'] = self.trigger_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TriggerUuid') is not None:
            self.trigger_uuid = m.get('TriggerUuid')
        return self


class TriggerPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerProcessTaskRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        task_id: str = None,
    ):
        # The type of the action. Valid values:
        # 
        # *   **remove**: cancels blocking or isolation.
        # *   **retry**: submits the task again.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The ID of the handling task.
        # 
        # >  You can call the [DescribeProcessTasks](~~DescribeProcessTasks~~) operation to query the IDs of handling tasks.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TriggerProcessTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerProcessTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerProcessTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerProcessTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerSophonPlaybookRequest(TeaModel):
    def __init__(
        self,
        command_name: str = None,
        input_params: str = None,
        sophon_task_id: str = None,
        trigger_type: str = None,
        uuid: str = None,
    ):
        # The name of the command that you want to trigger.
        # 
        # >  You can call the [DescribeSophonCommands](~~DescribeSophonCommands~~) operation to query the command name.
        self.command_name = command_name
        # The input parameters of the command or playbook that you want to trigger.
        # 
        # This parameter is required.
        self.input_params = input_params
        # The custom ID. If you do not specify this parameter when the playbook is triggered, a random ID is generated for fault locating and troubleshooting.
        self.sophon_task_id = sophon_task_id
        # The task type. Valid values:
        # 
        # *   **command**\
        # *   **playbook**\
        self.trigger_type = trigger_type
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class TriggerSophonPlaybookResponseBodyData(TeaModel):
    def __init__(
        self,
        sophon_task_id: str = None,
    ):
        # The custom ID. If you do not specify this parameter when the playbook is triggered, a random ID is generated for fault locating and troubleshooting.
        self.sophon_task_id = sophon_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class TriggerSophonPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        data: TriggerSophonPlaybookResponseBodyData = None,
        request_id: str = None,
    ):
        # The details that is returned after the command or playbook is triggered.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TriggerSophonPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerSophonPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerSophonPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerSophonPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPlaybookRequest(TeaModel):
    def __init__(
        self,
        playbook_uuid: str = None,
        task_flow: str = None,
    ):
        # The playbook UUID.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the playbook UUID.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The XML configuration of the playbook.
        # 
        # This parameter is required.
        self.task_flow = task_flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.task_flow is not None:
            result['TaskFlow'] = self.task_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('TaskFlow') is not None:
            self.task_flow = m.get('TaskFlow')
        return self


class VerifyPlaybookResponseBodyCheckTaskInfos(TeaModel):
    def __init__(
        self,
        detail: str = None,
        node_name: str = None,
        risk_level: str = None,
    ):
        # The error message returned when the playbook does not pass the check.
        self.detail = detail
        # The name of the node in the playbook.
        self.node_name = node_name
        # The severity level of the verification information. Valid values:
        # 
        # *   warn: An issue may occur during playbook running.
        # *   error: The playbook cannot be compiled.
        # *   remind: The publishing and running of the playbook are not affected. We recommend that you optimize the playbook format.
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class VerifyPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        check_task_infos: List[VerifyPlaybookResponseBodyCheckTaskInfos] = None,
        request_id: str = None,
    ):
        # The result of the verification.
        self.check_task_infos = check_task_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_task_infos:
            for k in self.check_task_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckTaskInfos'] = []
        if self.check_task_infos is not None:
            for k in self.check_task_infos:
                result['CheckTaskInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_task_infos = []
        if m.get('CheckTaskInfos') is not None:
            for k in m.get('CheckTaskInfos'):
                temp_model = VerifyPlaybookResponseBodyCheckTaskInfos()
                self.check_task_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyPlaybookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPythonFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # The Python code snippet.
        # 
        # This parameter is required.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class VerifyPythonFileResponseBodySyntax(TeaModel):
    def __init__(
        self,
        end_column: int = None,
        end_line_number: int = None,
        message: str = None,
        severity: int = None,
        start_column: int = None,
        start_line_number: int = None,
    ):
        # The number that indicates the end column of the error code.
        self.end_column = end_column
        # The number that indicates the end line of the error code.
        self.end_line_number = end_line_number
        # The error message for the error code.
        self.message = message
        # The severity level of the error code. Valid values:
        # 
        # *   4: moderate
        # *   8: serious
        self.severity = severity
        # The number that indicates the start column of the error code.
        self.start_column = start_column
        # The number that indicates the start line of the error code.
        self.start_line_number = start_line_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_column is not None:
            result['EndColumn'] = self.end_column
        if self.end_line_number is not None:
            result['EndLineNumber'] = self.end_line_number
        if self.message is not None:
            result['Message'] = self.message
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_column is not None:
            result['StartColumn'] = self.start_column
        if self.start_line_number is not None:
            result['StartLineNumber'] = self.start_line_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')
        if m.get('EndLineNumber') is not None:
            self.end_line_number = m.get('EndLineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')
        if m.get('StartLineNumber') is not None:
            self.start_line_number = m.get('StartLineNumber')
        return self


class VerifyPythonFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        syntax: List[VerifyPythonFileResponseBodySyntax] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The verification result. If the parameter is left empty, the syntax of the code snippet is correct.
        self.syntax = syntax

    def validate(self):
        if self.syntax:
            for k in self.syntax:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Syntax'] = []
        if self.syntax is not None:
            for k in self.syntax:
                result['Syntax'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.syntax = []
        if m.get('Syntax') is not None:
            for k in m.get('Syntax'):
                temp_model = VerifyPythonFileResponseBodySyntax()
                self.syntax.append(temp_model.from_map(k))
        return self


class VerifyPythonFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyPythonFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyPythonFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


