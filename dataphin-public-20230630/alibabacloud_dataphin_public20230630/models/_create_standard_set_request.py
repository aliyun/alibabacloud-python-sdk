# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateStandardSetRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateStandardSetRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateStandardSetRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateStandardSetRequestCreateCommand(DaraModel):
    def __init__(
        self,
        approval_config: main_models.CreateStandardSetRequestCreateCommandApprovalConfig = None,
        code: str = None,
        default_standard_template_id: int = None,
        description: str = None,
        directory_reference: main_models.CreateStandardSetRequestCreateCommandDirectoryReference = None,
        maintainer_list: List[str] = None,
        member_group_list: List[str] = None,
        member_list: List[str] = None,
        name: str = None,
        offline_approval_config: main_models.CreateStandardSetRequestCreateCommandOfflineApprovalConfig = None,
        visibility_config: main_models.CreateStandardSetRequestCreateCommandVisibilityConfig = None,
    ):
        self.approval_config = approval_config
        # This parameter is required.
        self.code = code
        self.default_standard_template_id = default_standard_template_id
        self.description = description
        self.directory_reference = directory_reference
        self.maintainer_list = maintainer_list
        self.member_group_list = member_group_list
        self.member_list = member_list
        # This parameter is required.
        self.name = name
        self.offline_approval_config = offline_approval_config
        self.visibility_config = visibility_config

    def validate(self):
        if self.approval_config:
            self.approval_config.validate()
        if self.directory_reference:
            self.directory_reference.validate()
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

        if self.default_standard_template_id is not None:
            result['DefaultStandardTemplateId'] = self.default_standard_template_id

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_reference is not None:
            result['DirectoryReference'] = self.directory_reference.to_map()

        if self.maintainer_list is not None:
            result['MaintainerList'] = self.maintainer_list

        if self.member_group_list is not None:
            result['MemberGroupList'] = self.member_group_list

        if self.member_list is not None:
            result['MemberList'] = self.member_list

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
            temp_model = main_models.CreateStandardSetRequestCreateCommandApprovalConfig()
            self.approval_config = temp_model.from_map(m.get('ApprovalConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultStandardTemplateId') is not None:
            self.default_standard_template_id = m.get('DefaultStandardTemplateId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryReference') is not None:
            temp_model = main_models.CreateStandardSetRequestCreateCommandDirectoryReference()
            self.directory_reference = temp_model.from_map(m.get('DirectoryReference'))

        if m.get('MaintainerList') is not None:
            self.maintainer_list = m.get('MaintainerList')

        if m.get('MemberGroupList') is not None:
            self.member_group_list = m.get('MemberGroupList')

        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineApprovalConfig') is not None:
            temp_model = main_models.CreateStandardSetRequestCreateCommandOfflineApprovalConfig()
            self.offline_approval_config = temp_model.from_map(m.get('OfflineApprovalConfig'))

        if m.get('VisibilityConfig') is not None:
            temp_model = main_models.CreateStandardSetRequestCreateCommandVisibilityConfig()
            self.visibility_config = temp_model.from_map(m.get('VisibilityConfig'))

        return self

class CreateStandardSetRequestCreateCommandVisibilityConfig(DaraModel):
    def __init__(
        self,
        specified_user_list: List[str] = None,
        type: str = None,
    ):
        self.specified_user_list = specified_user_list
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.specified_user_list is not None:
            result['SpecifiedUserList'] = self.specified_user_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecifiedUserList') is not None:
            self.specified_user_list = m.get('SpecifiedUserList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateStandardSetRequestCreateCommandOfflineApprovalConfig(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        enable_approval: bool = None,
        is_submit_in_batch: bool = None,
        template_id: int = None,
    ):
        # This parameter is required.
        self.approval_type = approval_type
        # This parameter is required.
        self.enable_approval = enable_approval
        # This parameter is required.
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

class CreateStandardSetRequestCreateCommandDirectoryReference(DaraModel):
    def __init__(
        self,
        directory: str = None,
    ):
        # This parameter is required.
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

class CreateStandardSetRequestCreateCommandApprovalConfig(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        enable_approval: bool = None,
        is_submit_in_batch: bool = None,
        template_id: int = None,
    ):
        # This parameter is required.
        self.approval_type = approval_type
        # This parameter is required.
        self.enable_approval = enable_approval
        # This parameter is required.
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

