# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardSetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        standard_set_info: main_models.GetStandardSetResponseBodyStandardSetInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.standard_set_info = standard_set_info
        self.success = success

    def validate(self):
        if self.standard_set_info:
            self.standard_set_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.standard_set_info is not None:
            result['StandardSetInfo'] = self.standard_set_info.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StandardSetInfo') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfo()
            self.standard_set_info = temp_model.from_map(m.get('StandardSetInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStandardSetResponseBodyStandardSetInfo(DaraModel):
    def __init__(
        self,
        approval_config: main_models.GetStandardSetResponseBodyStandardSetInfoApprovalConfig = None,
        code: str = None,
        create_time: str = None,
        creator: main_models.GetStandardSetResponseBodyStandardSetInfoCreator = None,
        default_standard_template_id: int = None,
        description: str = None,
        directory_reference: main_models.GetStandardSetResponseBodyStandardSetInfoDirectoryReference = None,
        id: int = None,
        last_modifier: main_models.GetStandardSetResponseBodyStandardSetInfoLastModifier = None,
        maintainer_list: List[main_models.GetStandardSetResponseBodyStandardSetInfoMaintainerList] = None,
        member_group_list: List[main_models.GetStandardSetResponseBodyStandardSetInfoMemberGroupList] = None,
        member_list: List[main_models.GetStandardSetResponseBodyStandardSetInfoMemberList] = None,
        modify_time: str = None,
        name: str = None,
        offline_approval_config: main_models.GetStandardSetResponseBodyStandardSetInfoOfflineApprovalConfig = None,
        visibility_config: main_models.GetStandardSetResponseBodyStandardSetInfoVisibilityConfig = None,
    ):
        self.approval_config = approval_config
        self.code = code
        self.create_time = create_time
        self.creator = creator
        self.default_standard_template_id = default_standard_template_id
        self.description = description
        self.directory_reference = directory_reference
        self.id = id
        self.last_modifier = last_modifier
        self.maintainer_list = maintainer_list
        self.member_group_list = member_group_list
        self.member_list = member_list
        self.modify_time = modify_time
        self.name = name
        self.offline_approval_config = offline_approval_config
        self.visibility_config = visibility_config

    def validate(self):
        if self.approval_config:
            self.approval_config.validate()
        if self.creator:
            self.creator.validate()
        if self.directory_reference:
            self.directory_reference.validate()
        if self.last_modifier:
            self.last_modifier.validate()
        if self.maintainer_list:
            for v1 in self.maintainer_list:
                 if v1:
                    v1.validate()
        if self.member_group_list:
            for v1 in self.member_group_list:
                 if v1:
                    v1.validate()
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()
        if self.offline_approval_config:
            self.offline_approval_config.validate()
        if self.visibility_config:
            self.visibility_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_config is not None:
            result['ApprovalConfig'] = self.approval_config.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.default_standard_template_id is not None:
            result['DefaultStandardTemplateId'] = self.default_standard_template_id

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_reference is not None:
            result['DirectoryReference'] = self.directory_reference.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier.to_map()

        result['MaintainerList'] = []
        if self.maintainer_list is not None:
            for k1 in self.maintainer_list:
                result['MaintainerList'].append(k1.to_map() if k1 else None)

        result['MemberGroupList'] = []
        if self.member_group_list is not None:
            for k1 in self.member_group_list:
                result['MemberGroupList'].append(k1.to_map() if k1 else None)

        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.offline_approval_config is not None:
            result['OfflineApprovalConfig'] = self.offline_approval_config.to_map()

        if self.visibility_config is not None:
            result['VisibilityConfig'] = self.visibility_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalConfig') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoApprovalConfig()
            self.approval_config = temp_model.from_map(m.get('ApprovalConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('DefaultStandardTemplateId') is not None:
            self.default_standard_template_id = m.get('DefaultStandardTemplateId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryReference') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoDirectoryReference()
            self.directory_reference = temp_model.from_map(m.get('DirectoryReference'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoLastModifier()
            self.last_modifier = temp_model.from_map(m.get('LastModifier'))

        self.maintainer_list = []
        if m.get('MaintainerList') is not None:
            for k1 in m.get('MaintainerList'):
                temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoMaintainerList()
                self.maintainer_list.append(temp_model.from_map(k1))

        self.member_group_list = []
        if m.get('MemberGroupList') is not None:
            for k1 in m.get('MemberGroupList'):
                temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoMemberGroupList()
                self.member_group_list.append(temp_model.from_map(k1))

        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoMemberList()
                self.member_list.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineApprovalConfig') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoOfflineApprovalConfig()
            self.offline_approval_config = temp_model.from_map(m.get('OfflineApprovalConfig'))

        if m.get('VisibilityConfig') is not None:
            temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoVisibilityConfig()
            self.visibility_config = temp_model.from_map(m.get('VisibilityConfig'))

        return self

class GetStandardSetResponseBodyStandardSetInfoVisibilityConfig(DaraModel):
    def __init__(
        self,
        specified_user_list: List[main_models.GetStandardSetResponseBodyStandardSetInfoVisibilityConfigSpecifiedUserList] = None,
        type: str = None,
    ):
        self.specified_user_list = specified_user_list
        self.type = type

    def validate(self):
        if self.specified_user_list:
            for v1 in self.specified_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpecifiedUserList'] = []
        if self.specified_user_list is not None:
            for k1 in self.specified_user_list:
                result['SpecifiedUserList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specified_user_list = []
        if m.get('SpecifiedUserList') is not None:
            for k1 in m.get('SpecifiedUserList'):
                temp_model = main_models.GetStandardSetResponseBodyStandardSetInfoVisibilityConfigSpecifiedUserList()
                self.specified_user_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetStandardSetResponseBodyStandardSetInfoVisibilityConfigSpecifiedUserList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoOfflineApprovalConfig(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        enable_approval: bool = None,
        is_submit_in_batch: bool = None,
        template_id: int = None,
    ):
        self.approval_type = approval_type
        self.enable_approval = enable_approval
        self.is_submit_in_batch = is_submit_in_batch
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.enable_approval is not None:
            result['EnableApproval'] = self.enable_approval

        if self.is_submit_in_batch is not None:
            result['IsSubmitInBatch'] = self.is_submit_in_batch

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('EnableApproval') is not None:
            self.enable_approval = m.get('EnableApproval')

        if m.get('IsSubmitInBatch') is not None:
            self.is_submit_in_batch = m.get('IsSubmitInBatch')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class GetStandardSetResponseBodyStandardSetInfoMemberList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoMemberGroupList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoMaintainerList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoLastModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoDirectoryReference(DaraModel):
    def __init__(
        self,
        directory: str = None,
    ):
        self.directory = directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        return self

class GetStandardSetResponseBodyStandardSetInfoCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardSetResponseBodyStandardSetInfoApprovalConfig(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        enable_approval: bool = None,
        is_submit_in_batch: bool = None,
        template_id: int = None,
    ):
        self.approval_type = approval_type
        self.enable_approval = enable_approval
        self.is_submit_in_batch = is_submit_in_batch
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.enable_approval is not None:
            result['EnableApproval'] = self.enable_approval

        if self.is_submit_in_batch is not None:
            result['IsSubmitInBatch'] = self.is_submit_in_batch

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('EnableApproval') is not None:
            self.enable_approval = m.get('EnableApproval')

        if m.get('IsSubmitInBatch') is not None:
            self.is_submit_in_batch = m.get('IsSubmitInBatch')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

