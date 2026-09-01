# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentSkillMetaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataAgentSkillMetaResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request is abnormal.
        self.error_code = error_code
        # The error message returned when the call fails.
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
            temp_model = main_models.ListDataAgentSkillMetaResponseBodyData()
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

class ListDataAgentSkillMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListDataAgentSkillMetaResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The list of data content.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListDataAgentSkillMetaResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataAgentSkillMetaResponseBodyDataContent(DaraModel):
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
        # The name of the creator.
        self.creator_user_name = creator_user_name
        # The skill description.
        self.description = description
        # Indicates whether the skill is available. Valid values: true and false.
        self.enabled = enabled
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The skill parsing error message. This parameter is returned when the skill status is INVALID.
        self.parse_error = parse_error
        # The region.
        self.region = region
        # The source of the skill. Valid values:
        # 
        # - User: a skill uploaded by the user.
        # - Agent: a skill derived from Agent analysis.
        self.skill_from = skill_from
        # The skill ID.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name
        # The skill status. Valid values:
        # 
        # - INIT: not ready.
        # - ACTIVE: active.
        # - INVALID: invalid.
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

