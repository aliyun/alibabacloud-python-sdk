# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class AddWorkspaceDocMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: AddWorkspaceDocMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = AddWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class AddWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class AddWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        role_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class AddWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class AddWorkspaceDocMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[AddWorkspaceDocMembersRequestMembers] = None,
        node_id: str = None,
        tenant_context: AddWorkspaceDocMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.node_id = node_id
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = AddWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        node_id: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.node_id = node_id
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddWorkspaceDocMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddWorkspaceDocMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class AddWorkspaceMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: AddWorkspaceMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = AddWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class AddWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class AddWorkspaceMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        role_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class AddWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class AddWorkspaceMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[AddWorkspaceMembersRequestMembers] = None,
        tenant_context: AddWorkspaceMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = AddWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceMembersResponseBody(TeaModel):
    def __init__(
        self,
        not_in_org_list: List[str] = None,
        request_id: str = None,
    ):
        self.not_in_org_list = not_in_org_list
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.not_in_org_list is not None:
            result['NotInOrgList'] = self.not_in_org_list
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotInOrgList') is not None:
            self.not_in_org_list = m.get('NotInOrgList')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddWorkspaceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddWorkspaceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSheetHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateSheetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: CreateSheetHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateSheetHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateSheetShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateSheetRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateSheetRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        tenant_context: CreateSheetRequestTenantContext = None,
        workbook_id: str = None,
    ):
        self.name = name
        self.tenant_context = tenant_context
        self.workbook_id = workbook_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            temp_model = CreateSheetRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        tenant_context_shrink: str = None,
        workbook_id: str = None,
    ):
        self.name = name
        self.tenant_context_shrink = tenant_context_shrink
        self.workbook_id = workbook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class CreateSheetResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        request_id: str = None,
        visibility: str = None,
    ):
        self.id = id
        self.name = name
        self.request_id = request_id
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.visibility is not None:
            result['visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')
        return self


class CreateSheetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSheetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSheetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateWorkspaceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: CreateWorkspaceHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateWorkspaceHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateWorkspaceShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateWorkspaceRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tenant_context: CreateWorkspaceRequestTenantContext = None,
    ):
        self.description = description
        self.name = name
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            temp_model = CreateWorkspaceRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        return self


class CreateWorkspaceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tenant_context_shrink: str = None,
    ):
        self.description = description
        self.name = name
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        request_id: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.name = name
        # requestId
        self.request_id = request_id
        self.url = url
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.url is not None:
            result['url'] = self.url
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceDocHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class CreateWorkspaceDocHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: CreateWorkspaceDocHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = CreateWorkspaceDocHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class CreateWorkspaceDocShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class CreateWorkspaceDocRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateWorkspaceDocRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        name: str = None,
        parent_node_id: str = None,
        template_id: str = None,
        template_type: str = None,
        tenant_context: CreateWorkspaceDocRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.doc_type = doc_type
        self.name = name
        self.parent_node_id = parent_node_id
        self.template_id = template_id
        self.template_type = template_type
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TenantContext') is not None:
            temp_model = CreateWorkspaceDocRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceDocShrinkRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        name: str = None,
        parent_node_id: str = None,
        template_id: str = None,
        template_type: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.doc_type = doc_type
        self.name = name
        self.parent_node_id = parent_node_id
        self.template_id = template_id
        self.template_type = template_type
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceDocResponseBody(TeaModel):
    def __init__(
        self,
        doc_key: str = None,
        node_id: str = None,
        request_id: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.doc_key = doc_key
        self.node_id = node_id
        # requestId
        self.request_id = request_id
        self.url = url
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_key is not None:
            result['docKey'] = self.doc_key
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.url is not None:
            result['url'] = self.url
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docKey') is not None:
            self.doc_key = m.get('docKey')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkspaceDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkspaceDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateWorkspaceDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class DeleteWorkspaceDocMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: DeleteWorkspaceDocMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = DeleteWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class DeleteWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class DeleteWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class DeleteWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteWorkspaceDocMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[DeleteWorkspaceDocMembersRequestMembers] = None,
        node_id: str = None,
        tenant_context: DeleteWorkspaceDocMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.node_id = node_id
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DeleteWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = DeleteWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        node_id: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.node_id = node_id
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteWorkspaceDocMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceDocMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class DeleteWorkspaceMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: DeleteWorkspaceMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = DeleteWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class DeleteWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class DeleteWorkspaceMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class DeleteWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteWorkspaceMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[DeleteWorkspaceMembersRequestMembers] = None,
        tenant_context: DeleteWorkspaceMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DeleteWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = DeleteWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteWorkspaceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteWorkspaceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class GetUserHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: GetUserHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = GetUserHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class GetUserShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class GetUserRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        tenant_context: GetUserRequestTenantContext = None,
        language: str = None,
    ):
        self.tenant_context = tenant_context
        self.language = language

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = GetUserRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class GetUserShrinkRequest(TeaModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        language: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class GetUserResponseBodyDeptOrderList(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
        order: int = None,
    ):
        self.dept_id = dept_id
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class GetUserResponseBodyLeaderInDept(TeaModel):
    def __init__(
        self,
        dept_id: int = None,
        leader: bool = None,
    ):
        self.dept_id = dept_id
        self.leader = leader

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dept_id is not None:
            result['deptId'] = self.dept_id
        if self.leader is not None:
            result['leader'] = self.leader
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')
        if m.get('leader') is not None:
            self.leader = m.get('leader')
        return self


class GetUserResponseBodyRoleList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        id: int = None,
        name: str = None,
    ):
        self.group_name = group_name
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetUserResponseBodyUnionEmpExtUnionEmpMapList(TeaModel):
    def __init__(
        self,
        crop_id: str = None,
        userid: str = None,
    ):
        self.crop_id = crop_id
        self.userid = userid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop_id is not None:
            result['cropId'] = self.crop_id
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cropId') is not None:
            self.crop_id = m.get('cropId')
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class GetUserResponseBodyUnionEmpExt(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        union_emp_map_list: List[GetUserResponseBodyUnionEmpExtUnionEmpMapList] = None,
        userid: str = None,
    ):
        self.corp_id = corp_id
        self.union_emp_map_list = union_emp_map_list
        self.userid = userid

    def validate(self):
        if self.union_emp_map_list:
            for k in self.union_emp_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corpId'] = self.corp_id
        result['unionEmpMapList'] = []
        if self.union_emp_map_list is not None:
            for k in self.union_emp_map_list:
                result['unionEmpMapList'].append(k.to_map() if k else None)
        if self.userid is not None:
            result['userid'] = self.userid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')
        self.union_emp_map_list = []
        if m.get('unionEmpMapList') is not None:
            for k in m.get('unionEmpMapList'):
                temp_model = GetUserResponseBodyUnionEmpExtUnionEmpMapList()
                self.union_emp_map_list.append(temp_model.from_map(k))
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin: bool = None,
        avatar: str = None,
        boss: bool = None,
        dept_id_list: List[int] = None,
        dept_order_list: List[GetUserResponseBodyDeptOrderList] = None,
        email: str = None,
        exclusive_account: bool = None,
        exclusive_account_corp_id: str = None,
        exclusive_account_corp_name: str = None,
        exclusive_account_type: str = None,
        extension: str = None,
        hide_mobile: bool = None,
        hired_date: int = None,
        job_number: str = None,
        leader_in_dept: List[GetUserResponseBodyLeaderInDept] = None,
        login_id: str = None,
        manager_userid: str = None,
        mobile: str = None,
        name: str = None,
        nickname: str = None,
        org_email: str = None,
        real_authed: bool = None,
        remark: str = None,
        request_id: str = None,
        role_list: List[GetUserResponseBodyRoleList] = None,
        senior: bool = None,
        state_code: str = None,
        telephone: str = None,
        title: str = None,
        union_emp_ext: GetUserResponseBodyUnionEmpExt = None,
        userid: str = None,
        work_place: str = None,
    ):
        self.active = active
        self.admin = admin
        self.avatar = avatar
        self.boss = boss
        self.dept_id_list = dept_id_list
        self.dept_order_list = dept_order_list
        self.email = email
        self.exclusive_account = exclusive_account
        self.exclusive_account_corp_id = exclusive_account_corp_id
        self.exclusive_account_corp_name = exclusive_account_corp_name
        self.exclusive_account_type = exclusive_account_type
        self.extension = extension
        self.hide_mobile = hide_mobile
        self.hired_date = hired_date
        self.job_number = job_number
        self.leader_in_dept = leader_in_dept
        self.login_id = login_id
        self.manager_userid = manager_userid
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.org_email = org_email
        self.real_authed = real_authed
        self.remark = remark
        self.request_id = request_id
        self.role_list = role_list
        self.senior = senior
        self.state_code = state_code
        self.telephone = telephone
        self.title = title
        self.union_emp_ext = union_emp_ext
        self.userid = userid
        self.work_place = work_place

    def validate(self):
        if self.dept_order_list:
            for k in self.dept_order_list:
                if k:
                    k.validate()
        if self.leader_in_dept:
            for k in self.leader_in_dept:
                if k:
                    k.validate()
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()
        if self.union_emp_ext:
            self.union_emp_ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.admin is not None:
            result['admin'] = self.admin
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.boss is not None:
            result['boss'] = self.boss
        if self.dept_id_list is not None:
            result['deptIdList'] = self.dept_id_list
        result['deptOrderList'] = []
        if self.dept_order_list is not None:
            for k in self.dept_order_list:
                result['deptOrderList'].append(k.to_map() if k else None)
        if self.email is not None:
            result['email'] = self.email
        if self.exclusive_account is not None:
            result['exclusiveAccount'] = self.exclusive_account
        if self.exclusive_account_corp_id is not None:
            result['exclusiveAccountCorpId'] = self.exclusive_account_corp_id
        if self.exclusive_account_corp_name is not None:
            result['exclusiveAccountCorpName'] = self.exclusive_account_corp_name
        if self.exclusive_account_type is not None:
            result['exclusiveAccountType'] = self.exclusive_account_type
        if self.extension is not None:
            result['extension'] = self.extension
        if self.hide_mobile is not None:
            result['hideMobile'] = self.hide_mobile
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.job_number is not None:
            result['jobNumber'] = self.job_number
        result['leaderInDept'] = []
        if self.leader_in_dept is not None:
            for k in self.leader_in_dept:
                result['leaderInDept'].append(k.to_map() if k else None)
        if self.login_id is not None:
            result['loginId'] = self.login_id
        if self.manager_userid is not None:
            result['managerUserid'] = self.manager_userid
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.nickname is not None:
            result['nickname'] = self.nickname
        if self.org_email is not None:
            result['orgEmail'] = self.org_email
        if self.real_authed is not None:
            result['realAuthed'] = self.real_authed
        if self.remark is not None:
            result['remark'] = self.remark
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['roleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['roleList'].append(k.to_map() if k else None)
        if self.senior is not None:
            result['senior'] = self.senior
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.telephone is not None:
            result['telephone'] = self.telephone
        if self.title is not None:
            result['title'] = self.title
        if self.union_emp_ext is not None:
            result['unionEmpExt'] = self.union_emp_ext.to_map()
        if self.userid is not None:
            result['userid'] = self.userid
        if self.work_place is not None:
            result['workPlace'] = self.work_place
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('admin') is not None:
            self.admin = m.get('admin')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('boss') is not None:
            self.boss = m.get('boss')
        if m.get('deptIdList') is not None:
            self.dept_id_list = m.get('deptIdList')
        self.dept_order_list = []
        if m.get('deptOrderList') is not None:
            for k in m.get('deptOrderList'):
                temp_model = GetUserResponseBodyDeptOrderList()
                self.dept_order_list.append(temp_model.from_map(k))
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('exclusiveAccount') is not None:
            self.exclusive_account = m.get('exclusiveAccount')
        if m.get('exclusiveAccountCorpId') is not None:
            self.exclusive_account_corp_id = m.get('exclusiveAccountCorpId')
        if m.get('exclusiveAccountCorpName') is not None:
            self.exclusive_account_corp_name = m.get('exclusiveAccountCorpName')
        if m.get('exclusiveAccountType') is not None:
            self.exclusive_account_type = m.get('exclusiveAccountType')
        if m.get('extension') is not None:
            self.extension = m.get('extension')
        if m.get('hideMobile') is not None:
            self.hide_mobile = m.get('hideMobile')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')
        self.leader_in_dept = []
        if m.get('leaderInDept') is not None:
            for k in m.get('leaderInDept'):
                temp_model = GetUserResponseBodyLeaderInDept()
                self.leader_in_dept.append(temp_model.from_map(k))
        if m.get('loginId') is not None:
            self.login_id = m.get('loginId')
        if m.get('managerUserid') is not None:
            self.manager_userid = m.get('managerUserid')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')
        if m.get('orgEmail') is not None:
            self.org_email = m.get('orgEmail')
        if m.get('realAuthed') is not None:
            self.real_authed = m.get('realAuthed')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.role_list = []
        if m.get('roleList') is not None:
            for k in m.get('roleList'):
                temp_model = GetUserResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('senior') is not None:
            self.senior = m.get('senior')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('unionEmpExt') is not None:
            temp_model = GetUserResponseBodyUnionEmpExt()
            self.union_emp_ext = temp_model.from_map(m['unionEmpExt'])
        if m.get('userid') is not None:
            self.userid = m.get('userid')
        if m.get('workPlace') is not None:
            self.work_place = m.get('workPlace')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRowsBeforeHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class InsertRowsBeforeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: InsertRowsBeforeHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = InsertRowsBeforeHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class InsertRowsBeforeShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class InsertRowsBeforeRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class InsertRowsBeforeRequest(TeaModel):
    def __init__(
        self,
        row: int = None,
        row_count: int = None,
        sheet_id: str = None,
        tenant_context: InsertRowsBeforeRequestTenantContext = None,
        workbook_id: str = None,
    ):
        self.row = row
        self.row_count = row_count
        self.sheet_id = sheet_id
        self.tenant_context = tenant_context
        self.workbook_id = workbook_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            temp_model = InsertRowsBeforeRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeShrinkRequest(TeaModel):
    def __init__(
        self,
        row: int = None,
        row_count: int = None,
        sheet_id: str = None,
        tenant_context_shrink: str = None,
        workbook_id: str = None,
    ):
        self.row = row
        self.row_count = row_count
        self.sheet_id = sheet_id
        self.tenant_context_shrink = tenant_context_shrink
        self.workbook_id = workbook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.sheet_id is not None:
            result['SheetId'] = self.sheet_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('SheetId') is not None:
            self.sheet_id = m.get('SheetId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')
        return self


class InsertRowsBeforeResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class InsertRowsBeforeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertRowsBeforeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InsertRowsBeforeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceDocMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateWorkspaceDocMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: UpdateWorkspaceDocMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateWorkspaceDocMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateWorkspaceDocMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateWorkspaceDocMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        role_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class UpdateWorkspaceDocMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateWorkspaceDocMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[UpdateWorkspaceDocMembersRequestMembers] = None,
        node_id: str = None,
        tenant_context: UpdateWorkspaceDocMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.node_id = node_id
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateWorkspaceDocMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            temp_model = UpdateWorkspaceDocMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceDocMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        node_id: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.node_id = node_id
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceDocMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateWorkspaceDocMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceDocMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateWorkspaceDocMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceMembersHeadersAccountContext(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        return self


class UpdateWorkspaceMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context: UpdateWorkspaceMembersHeadersAccountContext = None,
    ):
        self.common_headers = common_headers
        self.account_context = account_context

    def validate(self):
        if self.account_context:
            self.account_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context is not None:
            result['AccountContext'] = self.account_context.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            temp_model = UpdateWorkspaceMembersHeadersAccountContext()
            self.account_context = temp_model.from_map(m['AccountContext'])
        return self


class UpdateWorkspaceMembersShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        account_context_shrink: str = None,
    ):
        self.common_headers = common_headers
        self.account_context_shrink = account_context_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.account_context_shrink is not None:
            result['AccountContext'] = self.account_context_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('AccountContext') is not None:
            self.account_context_shrink = m.get('AccountContext')
        return self


class UpdateWorkspaceMembersRequestMembers(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        role_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class UpdateWorkspaceMembersRequestTenantContext(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateWorkspaceMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[UpdateWorkspaceMembersRequestMembers] = None,
        tenant_context: UpdateWorkspaceMembersRequestTenantContext = None,
        workspace_id: str = None,
    ):
        self.members = members
        self.tenant_context = tenant_context
        self.workspace_id = workspace_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateWorkspaceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('TenantContext') is not None:
            temp_model = UpdateWorkspaceMembersRequestTenantContext()
            self.tenant_context = temp_model.from_map(m['TenantContext'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        self.members_shrink = members_shrink
        self.tenant_context_shrink = tenant_context_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateWorkspaceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateWorkspaceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


