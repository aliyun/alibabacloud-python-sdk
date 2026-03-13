# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class CopyPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CopyPlaybookResponseBodyData = None,
        page: main_models.CopyPlaybookResponseBodyPage = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The pagination information.
        self.page = page
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CopyPlaybookResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Page') is not None:
            temp_model = main_models.CopyPlaybookResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CopyPlaybookResponseBodyPage(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CopyPlaybookResponseBodyData(DaraModel):
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
        # The status of the playbook. Valid values:
        # 
        # *   1: enabled.
        # *   0: disabled.
        self.active = active
        # The description of the playbook.
        self.description = description
        # The name of the new playbook.
        self.display_name = display_name
        # The number of playbook execution failures.
        self.fail_num = fail_num
        # The failure rate of playbook execution.
        self.fail_rate = fail_rate
        # The time when the playbook was created. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The time when the playbook was modified. The value is a 13-digit timestamp.
        self.gmt_modified = gmt_modified
        # The number of historical versions of the playbook.
        self.history_md_5 = history_md_5
        # The input parameters of the playbook.
        self.input_params = input_params
        # The time when the playbook was last run. The value is a 13-digit timestamp.
        self.last_runtime = last_runtime
        # The online version MD5 of the playbook.
        self.logic_release_taskflow_md_5 = logic_release_taskflow_md_5
        # The output parameters of the playbook.
        self.output_params = output_params
        # The type of the playbook. Valid values:
        # 
        # *   preset: predefined playbook.
        # *   user: custom playbook.
        self.own_type = own_type
        # The permission to operate the playbook. Valid values:
        # 
        # *   1: view.
        # *   2: edit.
        self.permission = permission
        # The status of the playbook.
        self.playbook_status = playbook_status
        # The UUID of the new playbook.
        self.playbook_uuid = playbook_uuid
        # The number of successful playbook executions.
        self.succ_num = succ_num
        # The ID of the user to which the playbook belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

