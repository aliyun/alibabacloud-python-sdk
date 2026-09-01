# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateDataAgentSkillMetaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateDataAgentSkillMetaResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned when a system-level request failure occurs.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.                                 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateDataAgentSkillMetaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateDataAgentSkillMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_parent_uid: str = None,
        aliyun_uid: str = None,
        creator_user_name: str = None,
        description: str = None,
        enabled: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        parse_error: str = None,
        region: str = None,
        skill_from: str = None,
        skill_id: str = None,
        skill_name: str = None,
        skill_status: str = None,
        workspace_id: str = None,
    ):
        # The Alibaba Cloud account ID of the parent account.
        self.aliyun_parent_uid = aliyun_parent_uid
        # The Alibaba Cloud account ID.
        self.aliyun_uid = aliyun_uid
        # The creator name.
        self.creator_user_name = creator_user_name
        # The skill description.
        self.description = description
        # Indicates whether the skill is available. Valid values: true and false.
        self.enabled = enabled
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The skill parsing error message.
        # - When the skill status is INVALID, the parsing error message is returned.
        self.parse_error = parse_error
        # The region.
        self.region = region
        # The skill source.
        self.skill_from = skill_from
        # The skill ID.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name
        # The skill status. Valid values:
        # - INIT: Not ready.
        # - ACTIVE: Active.
        # - INVALID: Invalid.
        self.skill_status = skill_status
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_parent_uid is not None:
            result['AliyunParentUid'] = self.aliyun_parent_uid

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.creator_user_name is not None:
            result['CreatorUserName'] = self.creator_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.parse_error is not None:
            result['ParseError'] = self.parse_error

        if self.region is not None:
            result['Region'] = self.region

        if self.skill_from is not None:
            result['SkillFrom'] = self.skill_from

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_status is not None:
            result['SkillStatus'] = self.skill_status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunParentUid') is not None:
            self.aliyun_parent_uid = m.get('AliyunParentUid')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('CreatorUserName') is not None:
            self.creator_user_name = m.get('CreatorUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ParseError') is not None:
            self.parse_error = m.get('ParseError')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SkillFrom') is not None:
            self.skill_from = m.get('SkillFrom')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillStatus') is not None:
            self.skill_status = m.get('SkillStatus')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

