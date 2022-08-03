# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AttachPolicyRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class AttachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachPolicyResponseBody = None,
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
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelCreateCloudAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CancelCreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCreateCloudAccountResponseBody = None,
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
            temp_model = CancelCreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelPromoteResourceAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CancelPromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPromoteResourceAccountResponseBody = None,
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
            temp_model = CancelPromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        enable_consolidated_billing: bool = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.enable_consolidated_billing = enable_consolidated_billing
        self.parent_folder_id = parent_folder_id
        self.payer_account_id = payer_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_consolidated_billing is not None:
            result['EnableConsolidatedBilling'] = self.enable_consolidated_billing
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableConsolidatedBilling') is not None:
            self.enable_consolidated_billing = m.get('EnableConsolidatedBilling')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class CreateCloudAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.record_id = record_id
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCloudAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: CreateCloudAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        self.account = account
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateCloudAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCloudAccountResponseBody = None,
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
            temp_model = CreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parent_folder_id: str = None,
    ):
        self.name = name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBodyFolder(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        folder_id: str = None,
        name: str = None,
        parent_folder_id: str = None,
    ):
        self.create_date = create_date
        self.folder_id = folder_id
        self.name = name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder: CreateFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        self.folder = folder
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = CreateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFolderResponseBody = None,
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
            temp_model = CreateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
    ):
        self.description = description
        self.policy_document = policy_document
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class CreatePolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        self.create_date = create_date
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: CreatePolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = CreatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_document: str = None,
        policy_name: str = None,
        set_as_default: bool = None,
    ):
        self.policy_document = policy_document
        self.policy_name = policy_name
        self.set_as_default = set_as_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')
        return self


class CreatePolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        version_id: str = None,
    ):
        self.create_date = create_date
        self.is_default_version = is_default_version
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreatePolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: CreatePolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        self.policy_version = policy_version
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = CreatePolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyVersionResponseBody = None,
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
            temp_model = CreatePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceAccountRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        enable_consolidated_billing: bool = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
    ):
        self.display_name = display_name
        self.enable_consolidated_billing = enable_consolidated_billing
        self.parent_folder_id = parent_folder_id
        self.payer_account_id = payer_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.enable_consolidated_billing is not None:
            result['EnableConsolidatedBilling'] = self.enable_consolidated_billing
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EnableConsolidatedBilling') is not None:
            self.enable_consolidated_billing = m.get('EnableConsolidatedBilling')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class CreateResourceAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateResourceAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: CreateResourceAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        self.account = account
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateResourceAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceAccountResponseBody = None,
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
            temp_model = CreateResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        name: str = None,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class CreateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: CreateResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name
        self.region_statuses = region_statuses
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: CreateResourceGroupResponseBodyResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceGroupResponseBody = None,
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
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
    ):
        self.assume_role_policy_document = assume_role_policy_document
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateRoleResponseBodyRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoleResponseBody = None,
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        custom_suffix: str = None,
        description: str = None,
        service_name: str = None,
    ):
        self.custom_suffix = custom_suffix
        self.description = description
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_suffix is not None:
            result['CustomSuffix'] = self.custom_suffix
        if self.description is not None:
            result['Description'] = self.description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSuffix') is not None:
            self.custom_suffix = m.get('CustomSuffix')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceLinkedRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateServiceLinkedRoleResponseBodyRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateServiceLinkedRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class DeleteFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFolderResponseBody = None,
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
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInvalidCloudAccountRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteInvalidCloudAccountRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteInvalidCloudAccountRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInvalidCloudAccountRecordResponseBody = None,
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
            temp_model = DeleteInvalidCloudAccountRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeletePolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeletePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyVersionResponseBody = None,
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
            temp_model = DeletePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class DeleteResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: DeleteResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name
        self.region_statuses = region_statuses
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: DeleteResourceGroupResponseBodyResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceGroupResponseBody = None,
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
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoleResponseBody = None,
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
            temp_model = DeleteRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        deletion_task_id: str = None,
        request_id: str = None,
    ):
        self.deletion_task_id = deletion_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceLinkedRoleResponseBody = None,
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
            temp_model = DeleteServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestoryResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DestoryResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DestoryResourceDirectoryResponseBody = None,
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
            temp_model = DestoryResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DestroyResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DestroyResourceDirectoryResponseBody = None,
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
            temp_model = DestroyResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DetachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachPolicyResponseBody = None,
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
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSummaryRequest(TeaModel):
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
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetAccountSummaryResponseBodySummaryMap(TeaModel):
    def __init__(
        self,
        attached_policies_per_group_quota: int = None,
        attached_policies_per_role_quota: int = None,
        attached_policies_per_user_quota: int = None,
        attached_system_policies_per_group_quota: int = None,
        attached_system_policies_per_role_quota: int = None,
        attached_system_policies_per_user_quota: int = None,
        policies: int = None,
        policies_quota: int = None,
        policy_size_quota: int = None,
        resource_groups: int = None,
        resource_groups_quota: int = None,
        roles: int = None,
        roles_quota: int = None,
        versions_per_policy_quota: int = None,
    ):
        self.attached_policies_per_group_quota = attached_policies_per_group_quota
        self.attached_policies_per_role_quota = attached_policies_per_role_quota
        self.attached_policies_per_user_quota = attached_policies_per_user_quota
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota
        self.policies = policies
        self.policies_quota = policies_quota
        self.policy_size_quota = policy_size_quota
        self.resource_groups = resource_groups
        self.resource_groups_quota = resource_groups_quota
        self.roles = roles
        self.roles_quota = roles_quota
        self.versions_per_policy_quota = versions_per_policy_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups
        if self.resource_groups_quota is not None:
            result['ResourceGroupsQuota'] = self.resource_groups_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')
        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')
        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')
        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')
        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')
        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')
        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')
        if m.get('ResourceGroups') is not None:
            self.resource_groups = m.get('ResourceGroups')
        if m.get('ResourceGroupsQuota') is not None:
            self.resource_groups_quota = m.get('ResourceGroupsQuota')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')
        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')
        return self


class GetAccountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        summary_map: GetAccountSummaryResponseBodySummaryMap = None,
    ):
        self.request_id = request_id
        self.summary_map = summary_map

    def validate(self):
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SummaryMap') is not None:
            temp_model = GetAccountSummaryResponseBodySummaryMap()
            self.summary_map = temp_model.from_map(m['SummaryMap'])
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountSummaryResponseBody = None,
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
            temp_model = GetAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class GetFolderResponseBodyFolder(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        folder_id: str = None,
        name: str = None,
        parent_folder_id: str = None,
    ):
        self.create_date = create_date
        self.folder_id = folder_id
        self.name = name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class GetFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder: GetFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        self.folder = folder
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = GetFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFolderResponseBody = None,
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
            temp_model = GetFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        self.language = language
        self.policy_name = policy_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        self.attachment_count = attachment_count
        self.create_date = create_date
        self.default_version = default_version
        self.description = description
        self.policy_document = policy_document
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyResponseBody = None,
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
    ):
        self.create_date = create_date
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: GetPolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        self.policy_version = policy_version
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = GetPolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyVersionResponseBody = None,
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
            temp_model = GetPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        self.create_date = create_date
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.resource_directory_id = resource_directory_id
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class GetResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: GetResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        self.request_id = request_id
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = GetResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class GetResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceDirectoryResponseBody = None,
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
            temp_model = GetResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceDirectoryAccountRequest(TeaModel):
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
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetResourceDirectoryAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        identity_information: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.display_name = display_name
        self.folder_id = folder_id
        self.identity_information = identity_information
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResourceDirectoryAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: GetResourceDirectoryAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        self.account = account
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = GetResourceDirectoryAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceDirectoryAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceDirectoryAccountResponseBody = None,
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
            temp_model = GetResourceDirectoryAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: GetResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name
        self.region_statuses = region_statuses
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: GetResourceGroupResponseBodyResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceGroupResponseBody = None,
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
            temp_model = GetResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        role_name: str = None,
    ):
        self.language = language
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRoleResponseBodyRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: GetRoleResponseBodyRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.latest_deletion_task = latest_deletion_task
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = GetRoleResponseBodyRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: GetRoleResponseBodyRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = GetRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleResponseBody = None,
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
            temp_model = GetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleDeletionStatusRequest(TeaModel):
    def __init__(
        self,
        deletion_task_id: str = None,
    ):
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources(TeaModel):
    def __init__(
        self,
        resource: List[str] = None,
    ):
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages(TeaModel):
    def __init__(
        self,
        role_usage: List[GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage] = None,
    ):
        self.role_usage = role_usage

    def validate(self):
        if self.role_usage:
            for k in self.role_usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleUsage'] = []
        if self.role_usage is not None:
            for k in self.role_usage:
                result['RoleUsage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_usage = []
        if m.get('RoleUsage') is not None:
            for k in m.get('RoleUsage'):
                temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage()
                self.role_usage.append(temp_model.from_map(k))
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReason(TeaModel):
    def __init__(
        self,
        message: str = None,
        role_usages: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages = None,
    ):
        self.message = message
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            self.role_usages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.role_usages is not None:
            result['RoleUsages'] = self.role_usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RoleUsages') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages()
            self.role_usages = temp_model.from_map(m['RoleUsages'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBody(TeaModel):
    def __init__(
        self,
        reason: GetServiceLinkedRoleDeletionStatusResponseBodyReason = None,
        request_id: str = None,
        status: str = None,
    ):
        self.reason = reason
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceLinkedRoleDeletionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceLinkedRoleDeletionStatusResponseBody = None,
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
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleTemplateRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription(TeaModel):
    def __init__(
        self,
        description: str = None,
        language: str = None,
    ):
        self.description = description
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions(TeaModel):
    def __init__(
        self,
        role_description: List[GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription] = None,
    ):
        self.role_description = role_description

    def validate(self):
        if self.role_description:
            for k in self.role_description:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleDescription'] = []
        if self.role_description is not None:
            for k in self.role_description:
                result['RoleDescription'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_description = []
        if m.get('RoleDescription') is not None:
            for k in m.get('RoleDescription'):
                temp_model = GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptionsRoleDescription()
                self.role_description.append(temp_model.from_map(k))
        return self


class GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate(TeaModel):
    def __init__(
        self,
        multiple_roles_allowed: bool = None,
        role_descriptions: GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions = None,
        role_name_prefix: str = None,
        service_name: str = None,
        system_policy_name: str = None,
    ):
        self.multiple_roles_allowed = multiple_roles_allowed
        self.role_descriptions = role_descriptions
        self.role_name_prefix = role_name_prefix
        self.service_name = service_name
        self.system_policy_name = system_policy_name

    def validate(self):
        if self.role_descriptions:
            self.role_descriptions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multiple_roles_allowed is not None:
            result['MultipleRolesAllowed'] = self.multiple_roles_allowed
        if self.role_descriptions is not None:
            result['RoleDescriptions'] = self.role_descriptions.to_map()
        if self.role_name_prefix is not None:
            result['RoleNamePrefix'] = self.role_name_prefix
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.system_policy_name is not None:
            result['SystemPolicyName'] = self.system_policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultipleRolesAllowed') is not None:
            self.multiple_roles_allowed = m.get('MultipleRolesAllowed')
        if m.get('RoleDescriptions') is not None:
            temp_model = GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplateRoleDescriptions()
            self.role_descriptions = temp_model.from_map(m['RoleDescriptions'])
        if m.get('RoleNamePrefix') is not None:
            self.role_name_prefix = m.get('RoleNamePrefix')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SystemPolicyName') is not None:
            self.system_policy_name = m.get('SystemPolicyName')
        return self


class GetServiceLinkedRoleTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_linked_role_template: GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate = None,
    ):
        self.request_id = request_id
        self.service_linked_role_template = service_linked_role_template

    def validate(self):
        if self.service_linked_role_template:
            self.service_linked_role_template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_linked_role_template is not None:
            result['ServiceLinkedRoleTemplate'] = self.service_linked_role_template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceLinkedRoleTemplate') is not None:
            temp_model = GetServiceLinkedRoleTemplateResponseBodyServiceLinkedRoleTemplate()
            self.service_linked_role_template = temp_model.from_map(m['ServiceLinkedRoleTemplate'])
        return self


class GetServiceLinkedRoleTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceLinkedRoleTemplateResponseBody = None,
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
            temp_model = GetServiceLinkedRoleTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        self.create_date = create_date
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.resource_directory_id = resource_directory_id
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class InitResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: InitResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        self.request_id = request_id
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = InitResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class InitResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitResourceDirectoryResponseBody = None,
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
            temp_model = InitResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountRecordsForParentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parent_folder_id = parent_folder_id
        self.query_keyword = query_keyword

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
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        return self


class ListAccountRecordsForParentResponseBodyRecordsRecord(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.record_id = record_id
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountRecordsForParentResponseBodyRecords(TeaModel):
    def __init__(
        self,
        record: List[ListAccountRecordsForParentResponseBodyRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = ListAccountRecordsForParentResponseBodyRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class ListAccountRecordsForParentResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: ListAccountRecordsForParentResponseBodyRecords = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Records') is not None:
            temp_model = ListAccountRecordsForParentResponseBodyRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountRecordsForParentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountRecordsForParentResponseBody = None,
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
            temp_model = ListAccountRecordsForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListAccountsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accounts = accounts
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
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
        if m.get('Accounts') is not None:
            temp_model = ListAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsResponseBody = None,
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
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsForParentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parent_folder_id = parent_folder_id
        self.query_keyword = query_keyword

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
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        return self


class ListAccountsForParentResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsForParentResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsForParentResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsForParentResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListAccountsForParentResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accounts = accounts
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
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
        if m.get('Accounts') is not None:
            temp_model = ListAccountsForParentResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsForParentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsForParentResponseBody = None,
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
            temp_model = ListAccountsForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAncestorsRequest(TeaModel):
    def __init__(
        self,
        child_id: str = None,
    ):
        self.child_id = child_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_id is not None:
            result['ChildId'] = self.child_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')
        return self


class ListAncestorsResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        folder_id: str = None,
        name: str = None,
    ):
        self.create_date = create_date
        self.folder_id = folder_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAncestorsResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListAncestorsResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListAncestorsResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListAncestorsResponseBody(TeaModel):
    def __init__(
        self,
        folders: ListAncestorsResponseBodyFolders = None,
        request_id: str = None,
    ):
        self.folders = folders
        self.request_id = request_id

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListAncestorsResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAncestorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAncestorsResponseBody = None,
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
            temp_model = ListAncestorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoldersForParentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parent_folder_id = parent_folder_id
        self.query_keyword = query_keyword

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
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        return self


class ListFoldersForParentResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        folder_id: str = None,
        name: str = None,
    ):
        self.create_date = create_date
        self.folder_id = folder_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListFoldersForParentResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListFoldersForParentResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListFoldersForParentResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponseBody(TeaModel):
    def __init__(
        self,
        folders: ListFoldersForParentResponseBodyFolders = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.folders = folders
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
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
        if m.get('Folders') is not None:
            temp_model = ListFoldersForParentResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFoldersForParentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoldersForParentResponseBody = None,
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
            temp_model = ListFoldersForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParentsRequest(TeaModel):
    def __init__(
        self,
        child_id: str = None,
    ):
        self.child_id = child_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_id is not None:
            result['ChildId'] = self.child_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')
        return self


class ListParentsResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        folder_id: str = None,
        name: str = None,
    ):
        self.create_date = create_date
        self.folder_id = folder_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListParentsResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListParentsResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListParentsResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListParentsResponseBody(TeaModel):
    def __init__(
        self,
        folders: ListParentsResponseBodyFolders = None,
        request_id: str = None,
    ):
        self.folders = folders
        self.request_id = request_id

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListParentsResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListParentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParentsResponseBody = None,
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
            temp_model = ListParentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_type: str = None,
    ):
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        self.attachment_count = attachment_count
        self.create_date = create_date
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policies: ListPoliciesResponseBodyPolicies = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.policies = policies
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoliciesResponseBody = None,
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyAttachmentsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.language = language
        self.page_number = page_number
        self.page_size = page_size
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment(TeaModel):
    def __init__(
        self,
        attach_date: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        self.attach_date = attach_date
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachments(TeaModel):
    def __init__(
        self,
        policy_attachment: List[ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment] = None,
    ):
        self.policy_attachment = policy_attachment

    def validate(self):
        if self.policy_attachment:
            for k in self.policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyAttachment'] = []
        if self.policy_attachment is not None:
            for k in self.policy_attachment:
                result['PolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_attachment = []
        if m.get('PolicyAttachment') is not None:
            for k in m.get('PolicyAttachment'):
                temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment()
                self.policy_attachment.append(temp_model.from_map(k))
        return self


class ListPolicyAttachmentsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_attachments: ListPolicyAttachmentsResponseBodyPolicyAttachments = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.policy_attachments = policy_attachments
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policy_attachments:
            self.policy_attachments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_attachments is not None:
            result['PolicyAttachments'] = self.policy_attachments.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyAttachments') is not None:
            temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachments()
            self.policy_attachments = temp_model.from_map(m['PolicyAttachments'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyAttachmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyAttachmentsResponseBody = None,
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
            temp_model = ListPolicyAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyVersionsRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
    ):
        self.policy_name = policy_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        version_id: str = None,
    ):
        self.create_date = create_date
        self.is_default_version = is_default_version
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListPolicyVersionsResponseBodyPolicyVersions(TeaModel):
    def __init__(
        self,
        policy_version: List[ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion] = None,
    ):
        self.policy_version = policy_version

    def validate(self):
        if self.policy_version:
            for k in self.policy_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyVersion'] = []
        if self.policy_version is not None:
            for k in self.policy_version:
                result['PolicyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_version = []
        if m.get('PolicyVersion') is not None:
            for k in m.get('PolicyVersion'):
                temp_model = ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion()
                self.policy_version.append(temp_model.from_map(k))
        return self


class ListPolicyVersionsResponseBody(TeaModel):
    def __init__(
        self,
        policy_versions: ListPolicyVersionsResponseBodyPolicyVersions = None,
        request_id: str = None,
    ):
        self.policy_versions = policy_versions
        self.request_id = request_id

    def validate(self):
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersions') is not None:
            temp_model = ListPolicyVersionsResponseBodyPolicyVersions()
            self.policy_versions = temp_model.from_map(m['PolicyVersions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPolicyVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyVersionsResponseBody = None,
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
            temp_model = ListPolicyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceGroupsResponseBodyResourceGroups(TeaModel):
    def __init__(
        self,
        resource_group: List[ListResourceGroupsResponseBodyResourceGroupsResourceGroup] = None,
    ):
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_groups: ListResourceGroupsResponseBodyResourceGroups = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.resource_groups = resource_groups
        self.total_count = total_count

    def validate(self):
        if self.resource_groups:
            self.resource_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroups') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroups()
            self.resource_groups = temp_model.from_map(m['ResourceGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceGroupsResponseBody = None,
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
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.language = language
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRolesResponseBodyRolesRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class ListRolesResponseBodyRolesRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: ListRolesResponseBodyRolesRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.latest_deletion_task = latest_deletion_task
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = ListRolesResponseBodyRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListRolesResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role: List[ListRolesResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        roles: ListRolesResponseBodyRoles = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.roles = roles
        self.total_count = total_count

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Roles') is not None:
            temp_model = ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesResponseBody = None,
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesForServiceRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        service: str = None,
    ):
        self.language = language
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListRolesForServiceResponseBodyRolesRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class ListRolesForServiceResponseBodyRolesRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: ListRolesForServiceResponseBodyRolesRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.latest_deletion_task = latest_deletion_task
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = ListRolesForServiceResponseBodyRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListRolesForServiceResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role: List[ListRolesForServiceResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesForServiceResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesForServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        roles: ListRolesForServiceResponseBodyRoles = None,
    ):
        self.request_id = request_id
        self.roles = roles

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Roles') is not None:
            temp_model = ListRolesForServiceResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        return self


class ListRolesForServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesForServiceResponseBody = None,
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
            temp_model = ListRolesForServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrustedServiceStatusRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal(TeaModel):
    def __init__(
        self,
        enable_time: str = None,
        service_principal: str = None,
    ):
        self.enable_time = enable_time
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipals(TeaModel):
    def __init__(
        self,
        enabled_service_principal: List[ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal] = None,
    ):
        self.enabled_service_principal = enabled_service_principal

    def validate(self):
        if self.enabled_service_principal:
            for k in self.enabled_service_principal:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnabledServicePrincipal'] = []
        if self.enabled_service_principal is not None:
            for k in self.enabled_service_principal:
                result['EnabledServicePrincipal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enabled_service_principal = []
        if m.get('EnabledServicePrincipal') is not None:
            for k in m.get('EnabledServicePrincipal'):
                temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal()
                self.enabled_service_principal.append(temp_model.from_map(k))
        return self


class ListTrustedServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled_service_principals: ListTrustedServiceStatusResponseBodyEnabledServicePrincipals = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.enabled_service_principals = enabled_service_principals
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.enabled_service_principals:
            self.enabled_service_principals.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_service_principals is not None:
            result['EnabledServicePrincipals'] = self.enabled_service_principals.to_map()
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
        if m.get('EnabledServicePrincipals') is not None:
            temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipals()
            self.enabled_service_principals = temp_model.from_map(m['EnabledServicePrincipals'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTrustedServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrustedServiceStatusResponseBody = None,
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
            temp_model = ListTrustedServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        destination_folder_id: str = None,
    ):
        self.account_id = account_id
        self.destination_folder_id = destination_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.destination_folder_id is not None:
            result['DestinationFolderId'] = self.destination_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DestinationFolderId') is not None:
            self.destination_folder_id = m.get('DestinationFolderId')
        return self


class MoveAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class MoveAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveAccountResponseBody = None,
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
            temp_model = MoveAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
    ):
        self.account_id = account_id
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class PromoteResourceAccountResponseBody(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PromoteResourceAccountResponseBody = None,
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
            temp_model = PromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResourceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        self.account_id = account_id
        self.page_number = page_number
        self.page_size = page_size
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class QueryResourceResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        self.create_date = create_date
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class QueryResourceResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[QueryResourceResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = QueryResourceResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class QueryResourceResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: QueryResourceResponseBodyResources = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = QueryResourceResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResourceResponseBody = None,
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
            temp_model = QueryResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveCloudAccountRequest(TeaModel):
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
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class RemoveCloudAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class RemoveCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveCloudAccountResponseBody = None,
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
            temp_model = RemoveCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendCreateCloudAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendCreateCloudAccountEmailResponseBody(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendCreateCloudAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendCreateCloudAccountEmailResponseBody = None,
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
            temp_model = ResendCreateCloudAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendPromoteResourceAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendPromoteResourceAccountEmailResponseBody(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        request_id: str = None,
    ):
        self.record_id = record_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendPromoteResourceAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendPromoteResourceAccountEmailResponseBody = None,
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
            temp_model = ResendPromoteResourceAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetDefaultPolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class SetDefaultPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDefaultPolicyVersionResponseBody = None,
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
            temp_model = SetDefaultPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        name: str = None,
    ):
        self.folder_id = folder_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFolderResponseBody = None,
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
            temp_model = UpdateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        new_display_name: str = None,
        resource_group_id: str = None,
    ):
        self.account_id = account_id
        self.new_display_name = new_display_name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class UpdateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
    ):
        self.account_id = account_id
        self.create_date = create_date
        self.display_name = display_name
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: UpdateResourceGroupResponseBodyResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = UpdateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceGroupResponseBody = None,
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
            temp_model = UpdateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        new_assume_role_policy_document: str = None,
        new_description: str = None,
        new_max_session_duration: int = None,
        role_name: str = None,
    ):
        self.new_assume_role_policy_document = new_assume_role_policy_document
        self.new_description = new_description
        self.new_max_session_duration = new_max_session_duration
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: UpdateRoleResponseBodyRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = UpdateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRoleResponseBody = None,
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
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


