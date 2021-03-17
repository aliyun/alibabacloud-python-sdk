# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddHostsToGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_id: str = None,
        host_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_id = host_group_id
        self.host_ids = host_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        return self


class AddHostsToGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
        host_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_group_id = host_group_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class AddHostsToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AddHostsToGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AddHostsToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AddHostsToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHostsToGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddHostsToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersToGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AddUsersToGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.user_group_id = user_group_id
        self.user_id = user_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddUsersToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AddUsersToGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AddUsersToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AddUsersToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUsersToGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUsersToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        hosts: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class AttachHostAccountsToUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class AttachHostAccountsToUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_accounts: List[AttachHostAccountsToUserResponseBodyResultsHostAccounts] = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.host_accounts = host_accounts
        self.user_id = user_id
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class AttachHostAccountsToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostAccountsToUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachHostAccountsToUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        hosts: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class AttachHostAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        host_accounts: List[AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts] = None,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.user_group_id = user_group_id
        self.host_accounts = host_accounts
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class AttachHostAccountsToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostAccountsToUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachHostAccountsToUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        host_groups: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.host_groups = host_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        return self


class AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_name: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class AttachHostGroupAccountsToUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_account_names: List[AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames] = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.user_id = user_id
        self.code = code
        self.message = message
        self.host_group_id = host_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class AttachHostGroupAccountsToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostGroupAccountsToUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostGroupAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostGroupAccountsToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachHostGroupAccountsToUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostGroupAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        host_groups: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.host_groups = host_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_name: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_account_names: List[AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames] = None,
        user_group_id: str = None,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.user_group_id = user_group_id
        self.code = code
        self.message = message
        self.host_group_id = host_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class AttachHostGroupAccountsToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[AttachHostGroupAccountsToUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostGroupAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostGroupAccountsToUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachHostGroupAccountsToUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostGroupAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        authorized_security_groups: List[str] = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.authorized_security_groups = authorized_security_groups
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigInstanceSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConfigInstanceSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigInstanceSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        region_id: str = None,
        white_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.region_id = region_id
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigInstanceWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConfigInstanceWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigInstanceWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        active_address_type: str = None,
        host_name: str = None,
        source: str = None,
        ostype: str = None,
        comment: str = None,
        source_instance_id: str = None,
        instance_region_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_private_address = host_private_address
        self.host_public_address = host_public_address
        self.active_address_type = active_address_type
        self.host_name = host_name
        self.source = source
        self.ostype = ostype
        self.comment = comment
        self.source_instance_id = source_instance_id
        self.instance_region_id = instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.source is not None:
            result['Source'] = self.source
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        return self


class CreateHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
    ):
        self.request_id = request_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class CreateHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostAccountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_id: str = None,
        protocol_name: str = None,
        host_account_name: str = None,
        password: str = None,
        private_key: str = None,
        pass_phrase: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_id = host_id
        self.protocol_name = protocol_name
        self.host_account_name = host_account_name
        self.password = password
        self.private_key = private_key
        self.pass_phrase = pass_phrase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        return self


class CreateHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_account_id: str = None,
    ):
        self.request_id = request_id
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class CreateHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_name: str = None,
        comment: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_name = host_group_name
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class CreateHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        host_group_id: str = None,
        request_id: str = None,
    ):
        self.host_group_id = host_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        source: str = None,
        user_name: str = None,
        password: str = None,
        display_name: str = None,
        comment: str = None,
        email: str = None,
        mobile: str = None,
        source_user_id: str = None,
        mobile_country_code: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.source = source
        self.user_name = user_name
        self.password = password
        self.display_name = display_name
        self.comment = comment
        self.email = email
        self.mobile = mobile
        self.source_user_id = source_user_id
        self.mobile_country_code = mobile_country_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_id: str = None,
    ):
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_name: str = None,
        comment: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_name = user_group_name
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_group_id: str = None,
    ):
        self.request_id = request_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class DeleteHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostAccountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class DeleteHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class DeleteHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttributePorts(TeaModel):
    def __init__(
        self,
        standard_port: int = None,
        custom_port: int = None,
    ):
        self.standard_port = standard_port
        self.custom_port = custom_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.standard_port is not None:
            result['StandardPort'] = self.standard_port
        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardPort') is not None:
            self.standard_port = m.get('StandardPort')
        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        ports: List[DescribeInstanceAttributeResponseBodyInstanceAttributePorts] = None,
        authorized_security_groups: List[str] = None,
        description: str = None,
        private_export_ips: List[str] = None,
        private_white_list: List[str] = None,
        expire_time: int = None,
        eni_instance_id: str = None,
        modify_password_module: str = None,
        internet_endpoint: str = None,
        instance_id: str = None,
        security_group_ids: List[str] = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        public_export_ips: List[str] = None,
        start_time: int = None,
        public_white_list: List[str] = None,
        web_terminal_module: str = None,
        instance_status: str = None,
        license_code: str = None,
        public_ips: List[str] = None,
        public_network_access: bool = None,
        storage: int = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.ports = ports
        self.authorized_security_groups = authorized_security_groups
        self.description = description
        self.private_export_ips = private_export_ips
        self.private_white_list = private_white_list
        self.expire_time = expire_time
        self.eni_instance_id = eni_instance_id
        self.modify_password_module = modify_password_module
        self.internet_endpoint = internet_endpoint
        self.instance_id = instance_id
        self.security_group_ids = security_group_ids
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.public_export_ips = public_export_ips
        self.start_time = start_time
        self.public_white_list = public_white_list
        self.web_terminal_module = web_terminal_module
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_ips = public_ips
        self.public_network_access = public_network_access
        self.storage = storage

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.description is not None:
            result['Description'] = self.description
        if self.private_export_ips is not None:
            result['PrivateExportIps'] = self.private_export_ips
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        if self.modify_password_module is not None:
            result['ModifyPasswordModule'] = self.modify_password_module
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.public_export_ips is not None:
            result['PublicExportIps'] = self.public_export_ips
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.web_terminal_module is not None:
            result['WebTerminalModule'] = self.web_terminal_module
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.storage is not None:
            result['Storage'] = self.storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeInstanceAttributeResponseBodyInstanceAttributePorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PrivateExportIps') is not None:
            self.private_export_ips = m.get('PrivateExportIps')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        if m.get('ModifyPasswordModule') is not None:
            self.modify_password_module = m.get('ModifyPasswordModule')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('PublicExportIps') is not None:
            self.public_export_ips = m.get('PublicExportIps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('WebTerminalModule') is not None:
            self.web_terminal_module = m.get('WebTerminalModule')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_attribute: DescribeInstanceAttributeResponseBodyInstanceAttribute = None,
    ):
        self.request_id = request_id
        self.instance_attribute = instance_attribute

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        instance_status: str = None,
        resource_group_id: str = None,
        instance_id: List[str] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.instance_status = instance_status
        self.resource_group_id = resource_group_id
        self.instance_id = instance_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        image_version: str = None,
        plan_code: str = None,
        description: str = None,
        expire_time: int = None,
        legacy: bool = None,
        internet_endpoint: str = None,
        instance_id: str = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        instance_status: str = None,
        license_code: str = None,
        public_network_access: bool = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.image_version = image_version
        self.plan_code = plan_code
        self.description = description
        self.expire_time = expire_time
        self.legacy = legacy
        self.internet_endpoint = internet_endpoint
        self.instance_id = instance_id
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_network_access = public_network_access

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code
        if self.description is not None:
            result['Description'] = self.description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.legacy is not None:
            result['Legacy'] = self.legacy
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        accept_language: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        hosts: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class DetachHostAccountsFromUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class DetachHostAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_accounts: List[DetachHostAccountsFromUserResponseBodyResultsHostAccounts] = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.host_accounts = host_accounts
        self.user_id = user_id
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class DetachHostAccountsFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostAccountsFromUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostAccountsFromUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachHostAccountsFromUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        hosts: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        host_accounts: List[DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts] = None,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.user_group_id = user_group_id
        self.host_accounts = host_accounts
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class DetachHostAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostAccountsFromUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachHostAccountsFromUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        host_groups: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.host_groups = host_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_name: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_account_names: List[DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames] = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.user_id = user_id
        self.code = code
        self.message = message
        self.host_group_id = host_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class DetachHostGroupAccountsFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostGroupAccountsFromUserResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostGroupAccountsFromUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostGroupAccountsFromUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachHostGroupAccountsFromUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostGroupAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        host_groups: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.host_groups = host_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_account_name: str = None,
    ):
        self.code = code
        self.message = message
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        host_account_names: List[DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames] = None,
        user_group_id: str = None,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
    ):
        self.host_account_names = host_account_names
        self.user_group_id = user_group_id
        self.code = code
        self.message = message
        self.host_group_id = host_group_id

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[DetachHostGroupAccountsFromUserGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostGroupAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostGroupAccountsFromUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachHostGroupAccountsFromUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostGroupAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableInstancePublicAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableInstancePublicAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class GetHostResponseBodyHostProtocols(TeaModel):
    def __init__(
        self,
        protocol_name: str = None,
        host_finger_print: str = None,
        port: int = None,
    ):
        self.protocol_name = protocol_name
        self.host_finger_print = host_finger_print
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_finger_print is not None:
            result['HostFingerPrint'] = self.host_finger_print
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostFingerPrint') is not None:
            self.host_finger_print = m.get('HostFingerPrint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class GetHostResponseBodyHost(TeaModel):
    def __init__(
        self,
        comment: str = None,
        active_address_type: str = None,
        host_public_address: str = None,
        protocols: List[GetHostResponseBodyHostProtocols] = None,
        host_name: str = None,
        source: str = None,
        host_private_address: str = None,
        ostype: str = None,
        host_id: str = None,
        source_instance_state: str = None,
        source_instance_id: str = None,
    ):
        self.comment = comment
        self.active_address_type = active_address_type
        self.host_public_address = host_public_address
        self.protocols = protocols
        self.host_name = host_name
        self.source = source
        self.host_private_address = host_private_address
        self.ostype = ostype
        self.host_id = host_id
        self.source_instance_state = source_instance_state
        self.source_instance_id = source_instance_id

    def validate(self):
        if self.protocols:
            for k in self.protocols:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        result['Protocols'] = []
        if self.protocols is not None:
            for k in self.protocols:
                result['Protocols'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.source is not None:
            result['Source'] = self.source
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        self.protocols = []
        if m.get('Protocols') is not None:
            for k in m.get('Protocols'):
                temp_model = GetHostResponseBodyHostProtocols()
                self.protocols.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class GetHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host: GetHostResponseBodyHost = None,
    ):
        self.request_id = request_id
        self.host = host

    def validate(self):
        if self.host:
            self.host.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host is not None:
            result['Host'] = self.host.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Host') is not None:
            temp_model = GetHostResponseBodyHost()
            self.host = temp_model.from_map(m['Host'])
        return self


class GetHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostAccountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_account_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        return self


class GetHostAccountResponseBodyHostAccount(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
        host_account_name: str = None,
        host_account_id: str = None,
        host_id: str = None,
    ):
        self.has_password = has_password
        self.private_key_fingerprint = private_key_fingerprint
        self.protocol_name = protocol_name
        self.host_account_name = host_account_name
        self.host_account_id = host_account_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class GetHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_account: GetHostAccountResponseBodyHostAccount = None,
    ):
        self.request_id = request_id
        self.host_account = host_account

    def validate(self):
        if self.host_account:
            self.host_account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_account is not None:
            result['HostAccount'] = self.host_account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostAccount') is not None:
            temp_model = GetHostAccountResponseBodyHostAccount()
            self.host_account = temp_model.from_map(m['HostAccount'])
        return self


class GetHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class GetHostGroupResponseBodyHostGroup(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        self.comment = comment
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class GetHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_group: GetHostGroupResponseBodyHostGroup = None,
    ):
        self.request_id = request_id
        self.host_group = host_group

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_group is not None:
            result['HostGroup'] = self.host_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostGroup') is not None:
            temp_model = GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m['HostGroup'])
        return self


class GetHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        comment: str = None,
        email: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
        user_id: str = None,
        source: str = None,
        user_name: str = None,
        user_state: List[str] = None,
        source_user_id: str = None,
    ):
        self.display_name = display_name
        self.comment = comment
        self.email = email
        self.mobile = mobile
        self.mobile_country_code = mobile_country_code
        self.user_id = user_id
        self.source = source
        self.user_name = user_name
        self.user_state = user_state
        self.source_user_id = source_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        user: GetUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBodyUserGroup(TeaModel):
    def __init__(
        self,
        comment: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.comment = comment
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class GetUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_group: GetUserGroupResponseBodyUserGroup = None,
    ):
        self.request_id = request_id
        self.user_group = user_group

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroup') is not None:
            temp_model = GetUserGroupResponseBodyUserGroup()
            self.user_group = temp_model.from_map(m['UserGroup'])
        return self


class GetUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_account_name: str = None,
        protocol_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_id = host_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_account_name = host_account_name
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
        host_account_name: str = None,
        host_account_id: str = None,
        host_id: str = None,
    ):
        self.has_password = has_password
        self.private_key_fingerprint = private_key_fingerprint
        self.protocol_name = protocol_name
        self.host_account_name = host_account_name
        self.host_account_id = host_account_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListHostAccountsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_accounts: List[ListHostAccountsResponseBodyHostAccounts] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_accounts = host_accounts

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        return self


class ListHostAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostAccountsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        host_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_account_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.host_id = host_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class ListHostAccountsForUserResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        is_authorized: bool = None,
        protocol_name: str = None,
        host_account_name: str = None,
        host_account_id: str = None,
        host_id: str = None,
    ):
        self.is_authorized = is_authorized
        self.protocol_name = protocol_name
        self.host_account_name = host_account_name
        self.host_account_id = host_account_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListHostAccountsForUserResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_accounts: List[ListHostAccountsForUserResponseBodyHostAccounts] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_accounts = host_accounts

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        return self


class ListHostAccountsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostAccountsForUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        host_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_account_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.host_id = host_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_account_name = host_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        return self


class ListHostAccountsForUserGroupResponseBodyHostAccounts(TeaModel):
    def __init__(
        self,
        is_authorized: bool = None,
        protocol_name: str = None,
        host_account_name: str = None,
        host_account_id: str = None,
        host_id: str = None,
    ):
        self.is_authorized = is_authorized
        self.protocol_name = protocol_name
        self.host_account_name = host_account_name
        self.host_account_id = host_account_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListHostAccountsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_accounts: List[ListHostAccountsForUserGroupResponseBodyHostAccounts] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_accounts = host_accounts

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserGroupResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        return self


class ListHostAccountsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostAccountsForUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        host_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class ListHostGroupAccountNamesForUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_account_names: List[str] = None,
    ):
        self.request_id = request_id
        self.host_account_names = host_account_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        return self


class ListHostGroupAccountNamesForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostGroupAccountNamesForUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupAccountNamesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        host_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class ListHostGroupAccountNamesForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_account_names: List[str] = None,
    ):
        self.request_id = request_id
        self.host_account_names = host_account_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        return self


class ListHostGroupAccountNamesForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostGroupAccountNamesForUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupAccountNamesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_group_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        member_count: int = None,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        self.member_count = member_count
        self.comment = comment
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_groups: List[ListHostGroupsResponseBodyHostGroups] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_groups = host_groups

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        return self


class ListHostGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        mode: str = None,
        user_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_group_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.mode = mode
        self.user_id = user_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        self.comment = comment
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_groups: List[ListHostGroupsForUserResponseBodyHostGroups] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_groups = host_groups

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        return self


class ListHostGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostGroupsForUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        mode: str = None,
        user_group_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_group_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.mode = mode
        self.user_group_id = user_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserGroupResponseBodyHostGroups(TeaModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        self.comment = comment
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        host_groups: List[ListHostGroupsForUserGroupResponseBodyHostGroups] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.host_groups = host_groups

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserGroupResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        return self


class ListHostGroupsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostGroupsForUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        page_number: str = None,
        page_size: str = None,
        ostype: str = None,
        host_name: str = None,
        host_address: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
        host_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.ostype = ostype
        self.host_name = host_name
        self.host_address = host_address
        self.source = source
        self.source_instance_id = source_instance_id
        self.source_instance_state = source_instance_state
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        return self


class ListHostsResponseBodyHosts(TeaModel):
    def __init__(
        self,
        comment: str = None,
        active_address_type: str = None,
        host_public_address: str = None,
        host_name: str = None,
        host_account_count: int = None,
        source: str = None,
        host_private_address: str = None,
        ostype: str = None,
        host_id: str = None,
        source_instance_state: str = None,
        source_instance_id: str = None,
    ):
        self.comment = comment
        self.active_address_type = active_address_type
        self.host_public_address = host_public_address
        self.host_name = host_name
        self.host_account_count = host_account_count
        self.source = source
        self.host_private_address = host_private_address
        self.ostype = ostype
        self.host_id = host_id
        self.source_instance_state = source_instance_state
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.source is not None:
            result['Source'] = self.source
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class ListHostsResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsResponseBodyHosts] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.hosts = hosts
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        mode: str = None,
        user_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_address: str = None,
        host_name: str = None,
        ostype: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.mode = mode
        self.user_id = user_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_address = host_address
        self.host_name = host_name
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserResponseBodyHosts(TeaModel):
    def __init__(
        self,
        comment: str = None,
        active_address_type: str = None,
        host_public_address: str = None,
        host_name: str = None,
        host_private_address: str = None,
        ostype: str = None,
        host_id: str = None,
    ):
        self.comment = comment
        self.active_address_type = active_address_type
        self.host_public_address = host_public_address
        self.host_name = host_name
        self.host_private_address = host_private_address
        self.ostype = ostype
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListHostsForUserResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsForUserResponseBodyHosts] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.hosts = hosts
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostsForUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        mode: str = None,
        user_group_id: str = None,
        page_number: str = None,
        page_size: str = None,
        host_address: str = None,
        host_name: str = None,
        ostype: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.mode = mode
        self.user_group_id = user_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.host_address = host_address
        self.host_name = host_name
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserGroupResponseBodyHosts(TeaModel):
    def __init__(
        self,
        comment: str = None,
        active_address_type: str = None,
        host_public_address: str = None,
        host_name: str = None,
        host_private_address: str = None,
        ostype: str = None,
        host_id: str = None,
    ):
        self.comment = comment
        self.active_address_type = active_address_type
        self.host_public_address = host_public_address
        self.host_name = host_name
        self.host_private_address = host_private_address
        self.ostype = ostype
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListHostsForUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        hosts: List[ListHostsForUserGroupResponseBodyHosts] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.hosts = hosts
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserGroupResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostsForUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHostsForUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region_id = region_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        self.tag_count = tag_count
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        page_number: str = None,
        page_size: str = None,
        user_group_name: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(
        self,
        member_count: int = None,
        comment: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.member_count = member_count
        self.comment = comment
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        user_groups: List[ListUserGroupsResponseBodyUserGroups] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        page_number: str = None,
        page_size: str = None,
        user_name: str = None,
        display_name: str = None,
        source: str = None,
        mobile: str = None,
        user_state: str = None,
        source_user_id: str = None,
        user_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.user_name = user_name
        self.display_name = display_name
        self.source = source
        self.mobile = mobile
        self.user_state = user_state
        self.source_user_id = source_user_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.source is not None:
            result['Source'] = self.source
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.user_state is not None:
            result['UserState'] = self.user_state
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        comment: str = None,
        mobile_country_code: str = None,
        mobile: str = None,
        user_id: str = None,
        source: str = None,
        user_name: str = None,
        user_state: List[str] = None,
        source_user_id: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.comment = comment
        self.mobile_country_code = mobile_country_code
        self.mobile = mobile
        self.user_id = user_id
        self.source = source
        self.user_name = user_name
        self.user_state = user_state
        self.source_user_id = source_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        users: List[ListUsersResponseBodyUsers] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class LockUsersResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.user_id = user_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class LockUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[LockUsersResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = LockUsersResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class LockUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LockUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_id: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        ostype: str = None,
        host_name: str = None,
        comment: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_id = host_id
        self.host_private_address = host_private_address
        self.host_public_address = host_public_address
        self.ostype = ostype
        self.host_name = host_name
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class ModifyHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostAccountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_account_id: str = None,
        host_account_name: str = None,
        password: str = None,
        private_key: str = None,
        pass_phrase: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_account_id = host_account_id
        self.host_account_name = host_account_name
        self.password = password
        self.private_key = private_key
        self.pass_phrase = pass_phrase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        return self


class ModifyHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
        comment: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class ModifyHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsActiveAddressTypeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_ids: str = None,
        active_address_type: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_ids = host_ids
        self.active_address_type = active_address_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        return self


class ModifyHostsActiveAddressTypeResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ModifyHostsActiveAddressTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ModifyHostsActiveAddressTypeResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyHostsActiveAddressTypeResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyHostsActiveAddressTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHostsActiveAddressTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostsActiveAddressTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsPortRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_ids: str = None,
        protocol_name: str = None,
        port: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_ids = host_ids
        self.protocol_name = protocol_name
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyHostsPortResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ModifyHostsPortResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ModifyHostsPortResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyHostsPortResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyHostsPortResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHostsPortResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostsPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        description: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.description = description
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
        password: str = None,
        display_name: str = None,
        comment: str = None,
        email: str = None,
        mobile: str = None,
        mobile_country_code: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_id = user_id
        self.password = password
        self.display_name = display_name
        self.comment = comment
        self.email = email
        self.mobile = mobile
        self.mobile_country_code = mobile_country_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.password is not None:
            result['Password'] = self.password
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
        comment: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class ModifyUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        resource_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.resource_id = resource_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHostsFromGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_group_id: str = None,
        host_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_group_id = host_group_id
        self.host_ids = host_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        return self


class RemoveHostsFromGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        host_group_id: str = None,
        host_id: str = None,
    ):
        self.code = code
        self.message = message
        self.host_group_id = host_group_id
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class RemoveHostsFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[RemoveHostsFromGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveHostsFromGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class RemoveHostsFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveHostsFromGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveHostsFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersFromGroupRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_id: str = None,
        user_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_group_id = user_group_id
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RemoveUsersFromGroupResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.user_group_id = user_group_id
        self.user_id = user_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveUsersFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[RemoveUsersFromGroupResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveUsersFromGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class RemoveUsersFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUsersFromGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUsersFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetHostAccountCredentialRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        host_account_id: str = None,
        credential_type: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.host_account_id = host_account_id
        self.credential_type = credential_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        return self


class ResetHostAccountCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetHostAccountCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetHostAccountCredentialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetHostAccountCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        vswitch_id: str = None,
        region_id: str = None,
        instance_security_groups: List[str] = None,
        security_group_ids: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.vswitch_id = vswitch_id
        self.region_id = region_id
        self.instance_security_groups = instance_security_groups
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_security_groups is not None:
            result['InstanceSecurityGroups'] = self.instance_security_groups
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceSecurityGroups') is not None:
            self.instance_security_groups = m.get('InstanceSecurityGroups')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_ids: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class UnlockUsersResponseBodyResults(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.user_id = user_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UnlockUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[UnlockUsersResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = UnlockUsersResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class UnlockUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnlockUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


