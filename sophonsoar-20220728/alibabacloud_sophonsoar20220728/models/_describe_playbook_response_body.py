# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookResponseBody(DaraModel):
    def __init__(
        self,
        playbook: main_models.DescribePlaybookResponseBodyPlaybook = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbook is not None:
            result['Playbook'] = self.playbook.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbook') is not None:
            temp_model = main_models.DescribePlaybookResponseBodyPlaybook()
            self.playbook = temp_model.from_map(m.get('Playbook'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookResponseBodyPlaybook(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

